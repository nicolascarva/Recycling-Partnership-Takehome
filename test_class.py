from main import Match

# 1. Accept either a string or a list of words as input text to be searched for pattern matches
# (if a string is passed, only words in the string that match the pattern should be caught)
# 2. Allow for registering an arbitrary number of pattern groups to search input text
# 3. Allow the user to specify a specific pattern group to search the text for matches
# 4. Allow the user to search input text with all registered patterns and return all matches by pattern group
t_string = 'Allow for registering #$ an arbitrary ^ number of pattern groups to search input text'
t_list = ['allow', 'for', 'registering', 'an', 'arbitrary', 'number', 'of', 'pattern', 'groups',
          'to', 'search', 'input', 'text']


class TestClass:
    def test_1a(self):
        """
        Test that string or list of words are accepted as input and the pattern matches
        """

        t_patterns = {'pat_1': ['ow', 'ing'], 'pat_2': ['ar']}
        input_1 = Match(t_string)
        input_2 = Match(t_list)
        input_1.add_patterns(t_patterns)
        input_2.add_patterns(t_patterns)

        assert input_1.match_patterns() == input_2.match_patterns() == {'pat_1': ['allow', 'registering'],
                                                                        'pat_2': ['arbitrary', 'search']}

    def test_two(self):
        """
        Test on more than one pattern
        """
        input_1 = Match('Allow for registering an arbitrary number of pattern groups to search input text')
        t_patterns = {'pat_1': ['or', 'ext'], 'pat_2': ['ow'], 'pat_3': ['an', 'er', 'ern']}
        input_1.add_patterns(t_patterns)

        assert input_1.match_patterns('pat_1') == {'pat_1': ['for', 'text']} \
               and input_1.match_patterns('pat_2') == {'pat_2': ['allow']} \
               and input_1.match_patterns('pat_3') == {'pat_3': ['registering', 'an', 'number', 'pattern']}

    def test_three(self):
        """
        Specify a specific pattern group for matching
        """
        input_1 = Match('Allow for registering an arbitrary number of pattern groups to search input text')
        t_patterns = {'pat_1': ['or', 'ext'], 'pat_2': ['ow'], 'pat_3': ['an', 'er', 'ern']}
        input_1.add_patterns(t_patterns)
        assert input_1.match_patterns(['pat_1', 'pat_3']) \
               == {'pat_1': ['for', 'text'], 'pat_3': ['registering', 'an', 'number', 'pattern']}

    def test_four(self):
        """
        Return all matches by pattern group
        """
        input_1 = Match('Allow for registering an arbitrary number of pattern groups to search input text')
        t_patterns = {'pat_1': ['or', 'ext'], 'pat_2': ['ow'], 'pat_3': ['an', 'er', 'ern'], 'pat_4': ['um']}
        input_1.add_patterns(t_patterns)

        assert input_1.match_patterns() \
               == {'pat_1': ['for', 'text'], 'pat_2': ['allow'], 'pat_3': ['registering', 'an', 'number', 'pattern'],
                   'pat_4': ['number']}
