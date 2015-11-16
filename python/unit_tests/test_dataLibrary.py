from unittest import TestCase, main
from datalibrary import DataLibrary     # Normally one would never do this.


class TestDataLibrary(TestCase):
    data_library = DataLibrary()

    # Return a set() abbreviation patterns.
    # No dash: [First three letters]
    # Multi-dash: [First word + First letter after dash, (single, double, triple letter zen css code)]
    # Append dash '-' at the end of each abbreviation.
    # Do not abbreviate words less than or equal to 5 characters in length.
    #
    # The zen css code comes from concatenating the first letter of the string with the first letter after each dash.
    # e.g. 'border-top-width' --> 'btw-'
    #
    # Examples
    #               'color' --> set()
    #             'padding' --> {'pad-'}
    #          'margin-top' --> {'margin-t-', 'mt-'}
    # 'border-bottom-width' --> {'border-b-width', 'bbw-'}
    def test_get_abbreviated_property_names_short_word(self):
        property_names = ['top', 'color', 'cue', ]
        expected_abbreviation = set()
        for property_name in property_names:
            abbreviations = self.data_library.get_abbreviated_property_names(property_name=property_name)
            self.assertEqual(abbreviations,expected_abbreviation, msg=abbreviations)

    def test_get_abbreviated_property_names_single_word(self):
        property_names = ['padding', 'margin', 'background', ]
        expected_abbreviations = [{'pad-'}, {'mar-'}, {'bac-'}, ]
        for i, property_name in enumerate(property_names):
            abbreviations = self.data_library.get_abbreviated_property_names(property_name=property_name)
            self.assertEqual(abbreviations, expected_abbreviations[i], msg=abbreviations)

    def test_get_abbreviated_property_names_double_word(self):
        property_names = ['padding-top', 'margin-bottom', 'background-color', ]
        expected_abbreviations = [{'padding-t-', 'pt-'}, {'margin-b-', 'mb-'}, {'background-c-', 'bc-'}, ]
        for i, property_name in enumerate(property_names):
            abbreviations = self.data_library.get_abbreviated_property_names(property_name=property_name)
            self.assertEqual(abbreviations, expected_abbreviations[i], msg=abbreviations)

    def test_get_abbreviated_property_names_triple_word(self):
        property_names = ['border-bottom-width', 'page-break-inside', 'border-top-color', 'border-right-color', ]
        expected_abbreviations = [
            {'border-b-width-', 'bbw-'}, {'page-b-inside-', 'pbi-'}, {'border-t-color-', 'btc-'},
            {'border-r-color-', 'brc-'},
        ]
        for i, property_name in enumerate(property_names):
            abbreviations = self.data_library.get_abbreviated_property_names(property_name=property_name)
            self.assertEqual(abbreviations, expected_abbreviations[i], msg=abbreviations)

    def test_initialize_property_alias_dict(self):
        expected_dict = {
            'outline': {'out-'}, 'border-left-width': {'blw-', 'border-l-width-'},
            'counter-reset': {'cr-', 'counter-r-'}, 'counter-increment': {'counter-i-', 'ci-'},
            'cue-before': {'cb-', 'cue-b-'}, 'text-decoration': {'td-', 'text-d-'},
            'background-color': {'bc-', 'background-c-'}, 'richness': {'ric-'},
            'border-right-color': {'brc-', 'border-r-color-'},
            'quotes': {'quo-'}, 'top': set(), 'outline-color': {'outline-c-', 'oc-'},
            'border-top-color': {'btc-', 'border-t-color-'}, 'position': {'pos-'},
            'speak-punctuation': {'sp-', 'speak-p-'}, 'elevation': {'ele-'}, 'border-left': {'bl-', 'border-l-'},
            'margin': {'mar-'}, 'border-right-width': {'brw-', 'border-r-width-'},
            'background-image': {'background-i-', 'bi-'}, 'visibility': {'vis-'}, 'cue-after': {'ca-', 'cue-a-'},
            'text-align': {'ta-', 'text-a-'}, 'font-variant': {'font-v-', 'fv-'}, 'volume': {'vol-'},
            'table-layout': {'table-l-', 'tl-'}, 'border-top-width': {'btw-', 'border-t-width-'}, 'widows': {'wid-'},
            'white-space': {'ws-', 'white-s-'}, 'outline-style': {'os-', 'outline-s-'}, 'height': {'hei-'},
            'margin-right': {'mr-', 'margin-r-'}, 'list-style-type': {'list-s-type-', 'lst-'},
            'border-spacing': {'border-s-', 'bs-'}, 'border-style': {'border-s-', 'bs-'},
            'border-left-style': {'border-l-style-', 'bls-'}, 'pause-after': {'pause-a-', 'pa-'}, 'clip': set(),
            'empty-cells': {'empty-c-', 'ec-'}, 'text-indent': {'ti-', 'text-i-'}, 'border-width': {'bw-', 'border-w-'},
            'line-height': {'lh-', 'line-h-'}, 'margin-top': {'mt-', 'margin-t-'}, 'speak-numeral': {'sn-', 'speak-n-'},
            'background': {'bac-'}, 'border-bottom-style': {'bbs-', 'border-b-style-'}, 'azimuth': {'azi-'},
            'text-transform': {'text-t-', 'tt-'}, 'vertical-align': {'va-', 'vertical-a-'},
            'border-bottom-color': {'border-b-color-', 'bbc-'}, 'play-during': {'pd-', 'play-d-'}, 'cue': set(),
            'color': set(), 'pause': set(), 'border-bottom': {'bb-', 'border-b-'}, 'max-height': {'mh-', 'max-h-'},
            'list-style-image': {'lsi-', 'list-s-image-'}, 'padding-top': {'pt-', 'padding-t-'}, 'float': set(),
            'width': set(), 'page-break-inside': {'pbi-', 'page-b-inside-'}, 'word-spacing': {'ws-', 'word-s-'},
            'font-family': {'ff-', 'font-f-'}, 'border-top-style': {'border-t-style-', 'bts-'},
            'pause-before': {'pb-', 'pause-b-'}, 'bottom': {'bot-'}, 'cursor': {'cur-'}, 'min-width': {'mw-', 'min-w-'},
            'speak': set(), 'overflow': {'ove-'}, 'list-style': {'ls-', 'list-s-'},
            'margin-bottom': {'mb-', 'margin-b-'}, 'border-collapse': {'bc-', 'border-c-'},
            'border-left-color': {'border-l-color-', 'blc-'}, 'display': {'dis-'}, 'border-right': {'br-', 'border-r-'},
            'outline-width': {'ow-', 'outline-w-'}, 'border-color': {'bc-', 'border-c-'}, 'pitch': set(),
            'direction': {'dir-'}, 'border-bottom-width': {'bbw-', 'border-b-width-'}, 'clear': set(),
            'list-style-position': {'lsp-', 'list-s-position-'}, 'font-style': {'fs-', 'font-s-'},
            'padding-right': {'padding-r-', 'pr-'}, 'speech-rate': {'sr-', 'speech-r-'},
            'border-top': {'bt-', 'border-t-'}, 'font-size': {'fs-', 'font-s-'},
            'background-attachment': {'ba-', 'background-a-'}, 'min-height': {'mh-', 'min-h-'}, 'left': set(),
            'page-break-before': {'pbb-', 'page-b-before-'}, 'stress': {'str-'}, 'right': set(), 'font': set(),
            'padding-left': {'padding-l-', 'pl-'}, 'unicode-bidi': {'ub-', 'unicode-b-'},
            'padding-bottom': {'pb-', 'padding-b-'}, 'caption-side': {'caption-s-', 'cs-'}, 'content': {'con-'},
            'page-break-after': {'page-b-after-', 'pba-'}, 'border': {'bor-'}, 'z-index': {'z-i-', 'zi-'},
            'background-position': {'background-p-', 'bp-'}, 'font-weight': {'font-w-', 'fw-'},
            'voice-family': {'vf-', 'voice-f-'}, 'max-width': {'mw-', 'max-w-'}, 'letter-spacing': {'ls-', 'letter-s-'},
            'speak-header': {'speak-h-', 'sh-'}, 'pitch-range': {'pr-', 'pitch-r-'},
            'border-right-style': {'brs-', 'border-r-style-'}, 'padding': {'pad-'},
            'background-repeat': {'br-', 'background-r-'}, 'margin-left': {'margin-l-', 'ml-'}, 'orphans': {'orp-'}
        }
        initial_dict = self.data_library.initialize_property_alias_dict(property_names=self.data_library.property_names)
        self.assertEqual(initial_dict, expected_dict)

    def test_merge_dicts(self):
        dict1 = {
            'background': {'bg-', },
            'color': {'c-', },
            'font-size': {'fsize-', 'f-size-', },
            'font-weight': {'bold', 'bolder', 'lighter', 'fweight-', 'f-weight-', },
            'height': {'h-', },
            'margin': {'m-', },
        }
        dict2 = {
            'color': {'col-', },
            'margin': {'mar-', },
        }
        expected_dict = {
            'background': {'bg-', },
            'color': {'c-', 'col-'},
            'font-size': {'fsize-', 'f-size-', },
            'font-weight': {'bold', 'bolder', 'lighter', 'fweight-', 'f-weight-', },
            'height': {'h-', },
            'margin': {'m-', 'mar-', },
        }
        merged_dict = self.data_library.merge_dicts(dict1, dict2)
        self.assertEqual(merged_dict, expected_dict)

    def test_merge_dicts_invalid_key(self):
        dict1 = {'font-size': {'fsize-', 'f-size-', }, }
        dict2 = {'invalid_key': {'col-', }, }
        self.assertRaises(KeyError, self.data_library.merge_dicts, dict1, dict2)

    # Expects that dict1 will pass straight through since there is nothing to merge with it.
    def test_merge_dicts_empty_custom_dict(self):
        dict1 = {'font-size': {'fsize-', 'f-size-', }, }
        custom_dict = None
        merged_dict = self.data_library.merge_dicts(dict1, custom_dict)
        self.assertEqual(dict1, merged_dict)

    def test_get_clashing_aliases(self):
        expected_clashes = {
            'border-collapse': {'border-c-', 'bc-'}, 'border-style': {'bs-', 'border-s-'},
            'font-style': {'font-s-', 'fs-'}, 'background-repeat': {'br-'}, 'pitch-range': {'pr-'},
            'padding-bottom': {'pb-'}, 'min-width': {'mw-'}, 'border-right': {'br-'}, 'letter-spacing': {'ls-'},
            'border-spacing': {'bs-', 'border-s-'}, 'white-space': {'ws-'}, 'word-spacing': {'ws-'},
            'max-width': {'mw-'}, 'padding-right': {'pr-'}, 'background-color': {'bc-'}, 'max-height': {'mh-'},
            'border-color': {'border-c-', 'bc-'}, 'pause-before': {'pb-'}, 'min-height': {'mh-'}, 'list-style': {'ls-'},
            'font-size': {'font-s-', 'fs-'}
        }
        initial_dict = self.data_library.initialize_property_alias_dict(property_names=self.data_library.property_names)
        actual_clashes = self.data_library.get_clashing_aliases(property_dict=initial_dict)
        self.assertEqual(actual_clashes, expected_clashes)

    def test_remove_clashing_aliases(self):
        expected_clean_dict = {
            'border-left': {'bl-', 'border-l-'},
            'white-space': set(),
            'cursor': {'cur-'},
        }
        initial_dict = {
            'border-left': {'bl-', 'border-l-', 'clash1-', 'clash2-'},
            'white-space': {'clash2-'},
            'cursor': {'cur-', 'clash1-', },
        }
        expected_clashes = {
            'border-left': {'clash2-', 'clash1-'},
            'white-space': {'clash2-'},
            'cursor': {'clash1-'}
        }
        clash_dict = self.data_library.get_clashing_aliases(property_dict=initial_dict)
        self.assertEqual(clash_dict, expected_clashes, msg=clash_dict)  # Sanity check
        clean_dict = self.data_library.remove_clashing_aliases(initial_dict, clash_dict)
        self.assertEqual(clean_dict, expected_clean_dict)

    def test_build_property_alias_dict(self):
        self.maxDiff = None
        expected = {
            'border-top-style': {'border-t-style-', 'bts-'}, 'border-top-color': {'btc-', 'border-t-color-'},
            'outline-style': {'os-', 'outline-s-'}, 'azimuth': {'azi-'}, 'clear': set(), 'top': set(),
            'border-right-style': {'brs-', 'border-r-style-'}, 'caption-side': {'cs-', 'caption-s-'},
            'border-bottom': {'bb-', 'border-b-'}, 'cursor': {'cur-'},
            'font-weight': {'fweight-', 'lighter', 'fw-', 'bolder', 'f-weight-', 'font-w-', 'bold'},
            'left': set(), 'quotes': {'quo-'}, 'text-decoration': {'text-d-', 'td-'}, 'max-height': {'max-h-'},
            'outline-color': {'outline-c-', 'oc-'}, 'pitch': set(), 'bottom': {'bot-'}, 'pause': set(),
            'background-attachment': {'background-a-', 'ba-'}, 'overflow': {'ove-'},
            'border-left': {'border-l-', 'bl-'}, 'list-style-image': {'lsi-', 'list-s-image-'},
            'position': {'pos-'}, 'border-top': {'border-t-', 'bt-'}, 'height': {'hei-', 'h-'},
            'border-bottom-style': {'bbs-', 'border-b-style-'},
            'text-align': {'t-align-', 'talign-', 'ta-', 'text-a-'}, 'margin': {'mar-', 'm-'},
            'border-collapse': set(), 'cue': set(), 'speak-header': {'sh-', 'speak-h-'},
            'text-indent': {'text-i-', 'ti-'}, 'clip': set(), 'line-height': {'line-h-', 'lh-'},
            'pause-after': {'pa-', 'pause-a-'}, 'font-family': {'font-f-', 'ff-'},
            'border-left-style': {'border-l-style-', 'bls-'}, 'padding': {'p-', 'pad-'},
            'pause-before': {'pause-b-'}, 'border-left-width': {'blw-', 'border-l-width-'},
            'white-space': {'white-s-'}, 'width': {'w-'}, 'border-bottom-width': {'bbw-', 'border-b-width-'},
            'border-spacing': set(), 'cue-before': {'cue-b-', 'cb-'},
            'background-color': {'background-c-', 'bgc-', 'bg-c-', 'bg-color-'},
            'border-left-color': {'border-l-color-', 'blc-'}, 'min-width': {'min-w-'},
            'z-index': {'z-i-', 'zi-'}, 'voice-family': {'voice-f-', 'vf-'},
            'speech-rate': {'sr-', 'speech-r-'}, 'orphans': {'orp-'}, 'empty-cells': {'empty-c-', 'ec-'},
            'letter-spacing': {'letter-s-'}, 'counter-increment': {'ci-', 'counter-i-'}, 'content': {'con-'},
            'font': set(), 'background': {'bac-', 'bg-'}, 'visibility': {'vis-'},
            'text-transform': {'tt-', 'text-t-'}, 'padding-right': {'padding-r-'}, 'max-width': {'max-w-'},
            'font-variant': {'fv-', 'font-v-'}, 'margin-left': {'margin-l-', 'ml-'},
            'border-right-width': {'brw-', 'border-r-width-'}, 'cue-after': {'cue-a-', 'ca-'},
            'richness': {'ric-'}, 'padding-left': {'padding-l-', 'pl-'},
            'margin-top': {'m-top-', 'margin-t-', 'mt-'}, 'border-right-color': {'brc-', 'border-r-color-'},
            'border-top-width': {'border-t-width-', 'btw-'}, 'padding-bottom': {'padding-b-'},
            'border-right': {'border-r-'}, 'widows': {'wid-'}, 'border-style': set(), 'stress': {'str-'},
            'word-spacing': {'word-s-'}, 'background-repeat': {'background-r-'},
            'border-width': {'bw-', 'border-w-'}, 'volume': {'vol-'}, 'margin-right': {'mr-', 'margin-r-'},
            'unicode-bidi': {'unicode-b-', 'ub-'}, 'elevation': {'ele-'},
            'outline-width': {'ow-', 'outline-w-'}, 'min-height': {'min-h-'},
            'border-bottom-color': {'border-b-color-', 'bbc-'}, 'list-style': {'list-s-'},
            'background-image': {'bi-', 'background-i-'}, 'speak-numeral': {'sn-', 'speak-n-'},
            'vertical-align': {'va-', 'vertical-a-', 'v-align-', 'valign-'}, 'display': {'dis-'},
            'background-position': {'background-p-', 'bp-'}, 'page-break-inside': {'page-b-inside-', 'pbi-'},
            'page-break-after': {'page-b-after-', 'pba-'}, 'page-break-before': {'pbb-', 'page-b-before-'},
            'pitch-range': {'pitch-r-'}, 'right': set(), 'table-layout': {'tl-', 'table-l-'},
            'font-size': {'fsize-', 'f-size-'}, 'padding-top': {'pt-', 'padding-t-', 'p-top-'},
            'color': {'c-'}, 'counter-reset': {'cr-', 'counter-r-'}, 'border-color': set(),
            'font-style': set(), 'border': {'bor-'}, 'speak-punctuation': {'speak-p-', 'sp-'},
            'list-style-position': {'lsp-', 'list-s-position-'},
            'margin-bottom': {'margin-b-', 'mb-', 'm-bot-'}, 'outline': {'out-'}, 'speak': set(),
            'play-during': {'play-d-', 'pd-'}, 'direction': {'dir-'}, 'list-style-type': {'list-s-type-', 'lst-'},
            'float': set()
        }
        actual = self.data_library.build_property_alias_dict()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()