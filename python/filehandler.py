from os import path, walk, getcwd, makedirs
from glob import glob
from re import findall
from cssutils import parseString, ser
__author__ = 'chad nelson'
__project__ = 'blow dry css'


class FileFinder(object):
    """
    Designed to find all ``files_types`` specified within a particular ``project_directory``. All folders within the
    ``project_directory`` are searched.

    | **Parameters:**

        | **project_directory** (*str*) -- Full path to the project directory containing parsable files e.g.
          ``/home/usr/web_project``.

        | **file_types** (*str tuple*) -- A tuple containing file extensions of project files to be parsed. Extensions
          are in the wildcard form ``'*.<ext>'``.  Replace ``<ext>`` with the desired file extension.

    **Example:**

    >>> from os import getcwd, chdir, path
    >>> current_dir = getcwd()
    >>> chdir('..')
    >>> project_directory = path.join(current_dir + '\\examplesite')
    >>> chdir(current_dir)    # Change it back.
    >>> file_types = ('*.html', )
    >>> file_finder = FileFinder(
    >>>     project_directory=project_directory,
    >>>     file_types=file_types
    >>> )
    >>> files = file_finder.files

    """
    file_types = ('*.html', )

    def __init__(self, project_directory='', file_types=file_types):
        if path.isdir(project_directory):
            self.project_directory = project_directory
            self.file_types = file_types
            self.files = []
            print('Project Directory:', project_directory)
            print('\nFile Types:', self.file_types)

            self.set_files()
            print('\nProject Files Found:')
            self.print_collection(self.files)
        else:
            raise NotADirectoryError(project_directory + ' is not a directory.')

    @staticmethod
    def print_collection(collection):
        """
        Takes a list or tuple as input and prints each item.

        :type collection: list

        :param collection: A list of strings to be printed.
        :return: None

        """
        for item in collection:
            print(item)

    def set_files(self):
        """
        Get all files associated with defined ``file_types`` in ``project_directory``. For each ``file_type`` find
        the full path to each file in the project directory of the current ``file_type``.  Add the full path of each
        file found to the list ``self.files``.

        Reference:
        stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories#answer-954948

        :return: None

        """
        for directory, _, _ in walk(self.project_directory):
            for file_type in self.file_types:
                self.files.extend(glob(path.join(directory, file_type)))


class FileConverter(object):
    """ Converts text files to strings.

    On initialization checks the existence of ``file_path``.

    **Example:**

    >>> from os import getcwd, chdir, path
    >>> # Valid file_path
    >>> current_dir = getcwd()
    >>> chdir('..')
    >>> file_path = path.join(current_dir + '\\examplesite\\index.html')
    >>> chdir(current_dir)    # Change it back.
    >>> file_converter = FileConverter(file_path=file_path)
    >>> file_string = file_converter.get_file_as_string()
    >>> #
    >>> # Invalid file_path
    >>> file_converter = FileConverter(file_path='/not/valid/file.html')
    FileNotFoundError: file_path /not/valid/file.html does not exist.

    """
    def __init__(self, file_path=''):
        if path.isfile(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError('file_path ' + file_path + ' does not exist.')

    def get_file_as_string(self):
        """ Convert the file to a string and return it.

        :return: (*str*) Return the file as a string.

        **Example:**

        >>> from os import getcwd, chdir, path
        >>> current_dir = getcwd()
        >>> chdir('..')
        >>> file_path = path.join(current_dir + '\\examplesite\\index.html')
        >>> chdir(current_dir)    # Change it back.
        >>> file_converter = FileConverter(file_path=file_path)
        >>> file_string = file_converter.get_file_as_string()
        """
        with open(self.file_path, 'r') as file:
            file_as_string = file.read().replace('\n', '')
        return file_as_string


class CSSFile(object):
    """ A tool for writing and minifying CSS files.

    *Reference:*
    stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary#answer-14364249

    | **Parameters:**

    | **css_directory** (*str*) -- File directory where the .css and .min.css output files are stored.

    | **file_name** (*str*) -- The name of the CSS output file. Default is 'blowdry'. The output file
      is named blowdry.css or blowdry.min.css.

    | *Note:* ``file_name`` does not include extension because ``write_css()`` and ``minify()`` append the extension.

    **Example:**

    >>> from os import getcwd, chdir, path
    >>> current_dir = getcwd()
    >>> chdir('..')
    >>> project_directory = path.join(current_dir + '\\examplesite')
    >>> css_directory = path.join(project_directory + '\\css')
    >>> chdir(current_dir)    # Change it back.
    >>> css_text = '.margin-top-50px { margin-top: 3.125em }'
    >>> css_file = CSSFile(
    >>>     file_directory=css_directory, file_name='blowdry'
    >>> )
    >>> css_file.write_css(css_text=css_text)
    >>> css_file.minify(css_text=css_text)

    """
    def __init__(self, file_directory=getcwd(), file_name='blowdry'):
        self.file_directory = file_directory
        self.file_name = file_name
        try:                                        # Python 2.7 Compliant
            makedirs(file_directory)                # Make 'css' directory
        except OSError:
            if not path.isdir(file_directory):      # Verify directory existences
                raise OSError(file_directory + ' is not a directory, and could not be created.')

    def file_path(self, extension=''):
        """ Joins the ``file_directory``, ``file_name``, and ``extension``. Returns the full ``file_path``.

        - Transform extension to lowercase.
        - Only allow '.', '0-9', and 'a-z' characters.

        :type extension: str

        :param extension: A file extension including the ``.``, for example, ``.css`` or ``.min.css``
        :return: (*str*) -- Returns the full ``file_path``.

        """
        extension = extension.lower()
        if len(findall(r"([.0-9a-z])", extension)) == len(extension):
            return path.join(self.file_directory, self.file_name + extension)
        else:
            raise ValueError(
                'Extension: ' + extension + ' contains invalid characters. Only ".", "0-9", and "a-z" are allowed.'
            )

    def write_css(self, css_text=''):
        """ Output a human readable version of the css file in utf-8 format.

        **Notes:**

        - The file is human readable. It is not intended to be human editable as the file is auto-generated.
        - Pre-existing files with the same name are overwritten.

        :type css_text: str

        :param css_text: Text containing the CSS to be written to the file.
        :return: None

        **Example:**

        >>> css_text = '.margin-top-50px { margin-top: 3.125em }'
        >>> css_file = CSSFile()
        >>> css_file.write_css(css_text=css_text)

        """
        parse_string = parseString(css_text)
        ser.prefs.useDefaults()                # Enables Default / Verbose Mode
        with open(self.file_path(extension='.css'), 'w') as css_file:
            css_file.write(parse_string.cssText.decode('utf-8'))

    def minify(self, css_text=''):
        """ Output a minified version of the css file in utf-8 format.

        **Definition:**

        The term minify "in the context of CSS means removing all unnecessary characters,
        such as spaces, new lines, comments without affecting the functionality of the source code."

        *Source:* https://www.jetbrains.com/phpstorm/help/minifying-css.html

        **Purpose:**

        | The purpose of minification is to increase web page load speed.
        | Reducing the size of the CSS file reduces
          the time spent downloading the CSS file and waiting for the page to load.

        **Notes:**

        - The file is minified and not human readable.
        - Pre-existing files with the same name are overwritten.
        - Uses the cssutils minification tool.

        :type css_text: str

        :param css_text: Text containing the CSS to be written to the file.
        :return: None

        **Example:**

        >>> css_text = '.margin-top-50px { margin-top: 3.125em }'
        >>> css_file = CSSFile()
        >>> css_file.minify(css_text=css_text)

        """
        parse_string = parseString(css_text)
        ser.prefs.useMinified()                 # Enables Minification
        with open(self.file_path(extension='.min.css'), 'w') as css_file:
            css_file.write(parse_string.cssText.decode('utf-8'))


class GenericFile(object):
    """ A tool for writing extension-independent files.

    **Reference:**
    stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary#answer-14364249

    | **Parameters:**

    | **file_directory** (*str*) -- File directory where the output files are saved / overwritten.

    | **file_name** (*str*) -- The name of the output file. Default is 'blowdry'. The output file
      is named blowdry + extension.

    | *Note:* ``file_name`` does not include extension because ``write_file()`` appends the extension.

    **Example:**

    >>> from os import getcwd, chdir, path
    >>> file_directory = path.join(getcwd())
    >>> css_text = '.margin-top-50px { margin-top: 3.125em }'
    >>> markdown_file = GenericFile(
    >>>     file_directory=file_directory, file_name='blowdry'
    >>> )
    >>> text = '# blowdrycss'
    >>> markdown_file.write_file(text=text, extension='.md')

    """
    def __init__(self, file_directory=getcwd(), file_name=''):
        self.file_directory = file_directory
        self.file_name = file_name
        try:                                        # Python 2.7 Compliant
            makedirs(file_directory)                # Make 'html' directory
        except OSError:
            if not path.isdir(file_directory):      # Verify directory existences
                raise OSError(file_directory + ' is not a directory, and could not be created.')

    # TODO: Move to utilities.py and split into two parts "extension_is_valid()" and "join_file_path()".
    # have "join_file_path" set an internal class member "full_file_path".
    def file_path(self, extension=''):
        """ Joins the ``file_directory``, ``file_name``, and ``extension``. Returns the full ``file_path``.

        - Transform extension to lowercase.
        - Only allow '.', '0-9', and 'a-z' characters.

        :type extension: str

        :param extension: A file extension including the ``.``, for example, ``.md``, ``.html``, and ``.rst``
        :return: (*str*) -- Returns the full ``file_path``.

        """
        extension = extension.lower()
        if len(findall(r"([.0-9a-z])", extension)) == len(extension):
            return path.join(self.file_directory, self.file_name + extension)
        else:
            raise ValueError(
                'Extension: ' + extension + ' contains invalid characters. Only ".", "0-9", and "a-z" are allowed.'
            )

    # TODO: Consider using the extension as an input to __init__().
    def write_file(self, text='', extension=''):
        """ Output a human readable version of the file in utf-8 format.

        Converts string to bytearray so that no new lines are added to the file.
        Note: Overwrites any pre-existing files with the same name.

        :type text: str
        :type extension: str

        :param text: The text to be written to the file.
        :param extension: The extension of the file.
        :return: None

        """
        with open(self.file_path(extension=extension), 'wb') as _file:
            _file.write(bytearray(text, 'utf-8'))
