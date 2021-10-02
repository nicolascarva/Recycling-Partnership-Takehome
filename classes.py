from helper_functions import clean_text


# Create class for patterns

class Pattern:
    """"Stores patterns as a class"""

    def __init__(self, p_list):
        self.pattern_group = p_list
        self.pattern_words = []

    def match(self, my_words):
        for word in my_words:
            for pat in self.pattern_group:
                if pat in word:
                    self.pattern_words.append(word)


class Words:
    """Stores words as a class"""

    def __init__(self, text_string):
        self.my_words = clean_text(text_string)





