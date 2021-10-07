import re



class Match:


    def __init__(self, text):
        self.pattern_list= []
        if isinstance(text, list):
            text = " ".join(text)
        self.words = self.clean_text(text)

    def add_patterns(self, patterns):
        for pattern in patterns.items():
            self.pattern_list.append(self.Pattern(pattern))


    def match_patterns(self, pattern_names='all'):
        self.matches = {}

        if pattern_names == 'all':
            pat_test = [pat.pattern_name for pat in self.pattern_list]
        else:
            pat_test = [pat.pattern_name for pat in self.pattern_list if pat.pattern_name in pattern_names]

        for pat in self.pattern_list:
            if pat.pattern_name in pat_test:
                self.matches[pat.pattern_name] = []
                for word in self.words:
                    for ind_pat in pat.pattern_group:
                        if ind_pat in word and word not in self.matches[pat.pattern_name]:
                            self.matches[pat.pattern_name].append(word)
        print('Matches for ', pattern_names, ': ', self.matches )
        return self.matches




    class Pattern:
        """"Stores patterns as a class"""
        def __init__(self,  pattern):
            self.pattern_name = pattern[0]
            self.pattern_group = pattern[1]




    def clean_text(self, text):
        """
        Accepts a single text string and performs several regex
        substitutions in order to clean the document.
        Parameters
        ----------
        text: string
        Returns
        -------
        text: list of words
        """
        special_chars_regex = '[:?,.\>$|!\'"]'
        white_spaces_regex = '[ ]{2,}'
        text = re.sub('[^a-zA-Z ]', " ", text)
        text = re.sub(special_chars_regex, " ", text)
        text = re.sub(white_spaces_regex, " ", text)
        text = text.split(" ")
        text = [word.lower() for word in text]
        return text