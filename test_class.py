from classes import Pattern, Words
from helper_functions import match_patterns

# 1. Accept either a string or a list of words as input text to be searched for pattern matches
# (if a string is passed, only words in the string that match the pattern should be caught)
# 2. Allow for registering an arbitrary number of pattern groups to search input text
# 3. Allow the user to specify a specific pattern group to search the text for matches
# 4. Allow the user to search input text with all registered patterns and return all matches by pattern group



class TestClass:
    def test_1a(self):
        # Test that string or list of words are accepted as input and the pattern matches
        t_string = 'Allow for registering an arbitrary number of pattern groups to search input text'
        t_list = ['allow', 'for', 'registering', 'an', 'arbitrary', 'number', 'of', 'pattern', 'groups', 'to', 'search',
                  'input', 'text']
        t_pattern = Pattern(['ow', 'ing'])
        input_1 = Words(t_string)
        input_2 = Words(t_list)
        assert t_pattern.match(input_1.my_words) == t_pattern.match(input_2.my_words) == ['allow', 'registering']


    def test_two(self):
        # Test on more than one pattern
        input = Words('Allow for registering an arbitrary number of pattern groups to search input text')
        t_pat_1 = Pattern(['or', 'ext'])
        t_pat_2 = Pattern(['ow'])
        t_pat_3 = Pattern(['an', 'er', 'ern'])
        assert t_pat_1.match(input.my_words) == ['for', 'text'] and t_pat_2.match(input.my_words) == ['allow'] \
               and t_pat_3.match((input.my_words)) == ['an', 'number', 'pattern', 'registering']


    def test_three(self):
        t_pat_1 = Pattern(['or', 'ext'], 'pat_1')
        t_pat_2 = Pattern(['ow'], 'pat_2')
        t_pat_3 = Pattern(['an', 'er', 'ern'], 'pat_3')
        input = Words('Allow for registering an arbitrary number of pattern groups to search input text')
        assert match_patterns(Pattern.instances, input.my_words, names=['pat_1', 'pat_3']) \
               == [('pat_1', ['for', 'text']), ('pat_3', ['an', 'number', 'pattern', 'registering'])]

    def test_four(self):
        Pattern.instances = []
        t_pat_1 = Pattern(['or', 'ext'], 'pat_1')
        t_pat_2 = Pattern(['ow'], 'pat_2')
        t_pat_3 = Pattern(['an', 'er', 'ern'], 'pat_3')
        t_pat_4 = Pattern(['an', 'in']) # Since this pattern doesn't have a name, it won't be saved
        input = Words('Allow for registering an arbitrary number of pattern groups to search input text')
        assert match_patterns(Pattern.instances, input.my_words) \
               == [('pat_1', ['for', 'text']), ('pat_2', ['allow']), ('pat_3', ['an', 'number', 'pattern', 'registering'])]

