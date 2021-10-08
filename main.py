import re


def clean_text(text):
    """
    Accepts a single text string and performs several regex
    substitutions in order to clean the document.
    Parameters
    ----------
    text: text (string)
    :return: list of words
    """
    special_chars_regex = r'[:?,.>$|!"\']/'
    white_spaces_regex = '[ ]{2,}'
    text = re.sub('[^a-zA-Z ]', " ", text)
    text = re.sub(special_chars_regex, " ", text)
    text = re.sub(white_spaces_regex, " ", text)
    text = text.split(" ")
    text = [word.lower() for word in text]
    return text


class Match:
    """"This class creates an object with the text that will be searched through. The add_patterns method is used
    to add patterns for searching. The match_patterns method will search through the named patterns (all if none is
    specified). The change_text method updates the text to be searched (this could also be done by instantiating
    a new object"""
    def __init__(self, text):
        self.pattern_list = []  # Keeps track of patterns in object
        if isinstance(text, list):  # Change list to text
            text = " ".join(text)
        self.words = clean_text(text)  # Text to be searched and cleaned
        self.matches = {}

    def add_patterns(self, patterns):
        """
        Adds pattern groups to be used for searching to the Match object.
        -------------
        :patterns: One or more pattern groups in dictionary form with the name as key and list of
        patterns as value {pattern_name1: pattern_group1}
        :return: Appends pattern to object for searching.
        """
        for pattern in patterns.items():
            self.pattern_list.append(self.Pattern(pattern))

    def match_patterns(self, pattern_names='all'):
        """
        Match text in self.words to the patterns specified. If no patterns are specified all
        patterns and its matches will be returned.
        -----------
        :pattern_names: List of pattern names (if empty, defaults to all patterns).
        :return: Matches in dictionary form {pattern_name: list_of_matched_words}.
        """
        self.matches = {}

        if pattern_names == 'all':
            pat_test = [pat.pattern_name for pat in self.pattern_list]
        else:
            pat_test = pattern_names

        for pat in self.pattern_list:
            if pat.pattern_name in pat_test:
                self.matches[pat.pattern_name] = []
                for word in self.words:
                    for ind_pat in pat.pattern_group:
                        if ind_pat in word and word not in self.matches[pat.pattern_name]:
                            self.matches[pat.pattern_name].append(word)
        print('Matches for ', pattern_names, ': ', self.matches)
        return self.matches

    def change_text(self, new_text):
        """
        Allows for changing the text to be searched through in the object.
        ------------
        :new_text: new text to be searched (string or list).
        :return: overwrites self.words (text to be searched).
        """
        if isinstance(new_text, list):  # Change list to text
            new_text = " ".join(new_text)
        self.words = clean_text(new_text)

    class Pattern:
        """"
        Stores patterns as a class with pattern name and group as attributes
        """
        def __init__(self,  pattern):
            self.pattern_name = pattern[0]
            self.pattern_group = pattern[1]
