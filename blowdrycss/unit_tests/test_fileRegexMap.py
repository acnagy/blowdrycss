# builtins
from unittest import TestCase, main
from os import path
# custom
from filehandler import FileRegexMap


class TestFileRegexMap(TestCase):
    def test_is_valid_extension_true(self):
        file_paths = [path.join('test_aspx', 'test.aspx'), path.join('test_jinja', 'test.jinja2')]
        for _path in file_paths:
            file_regex_map = FileRegexMap(_path=_path)
            self.assertTrue(file_regex_map.is_valid_extension(), msg=_path)

    def test_is_valid_extension_whitespace(self):
        file_paths = [path.join('test_aspx', 'test.aspx  '), path.join('test_jinja', 'test.jinja2 ')]
        for _path in file_paths:
            file_regex_map = FileRegexMap(_path=_path)
            self.assertTrue(file_regex_map.is_valid_extension(), msg=_path)

    def test_is_valid_extension_false(self):
        wrong_extensions = ['.wrong', '.squirrel', '.incorrect']
        file_path = path.join('test_aspx', 'test.aspx')
        for wrong_extension in wrong_extensions:
            file_regex_map = FileRegexMap(_path=file_path)
            file_regex_map.extension = wrong_extension
            self.assertFalse(file_regex_map.is_valid_extension())

    def test_is_valid_extension_raises_OSError(self):
        file_paths = [path.join('test_files', 'test.wrong'), path.join('test_files', 'test.incorrect')]
        for _path in file_paths:
            self.assertRaises(OSError, FileRegexMap, _path)

    def test_regexes(self):
        expected_dicts = [
            {
                'sub_regex': r'<%.*?%>',
                'findall_regex': r'class="(.*?)"',
            },
            {
                'sub_regex': r'{.*?}?}',
                'findall_regex': r'class="(.*?)"',
            },
        ]
        file_paths = [path.join('test_aspx', 'test.aspx'), path.join('test_jinja', 'test.jinja2')]
        for i, _path in enumerate(file_paths):
            file_regex_map = FileRegexMap(_path=_path)
            actual_dict = file_regex_map.regex_dict
            self.assertEqual(actual_dict, expected_dicts[i], msg=_path)


if __name__ == '__main__':
    main()