from helper_functions import clean_text
import weakref

# Create class for patterns

class Pattern:
    """"Stores patterns as a class"""
    instances = []
    def __init__(self, p_list, p_name = None):
        self.pattern_group = p_list
        # Only named patterns will be stored
        if p_name is not None:
            self.__class__.instances.append(weakref.proxy(self))
            self.pattern_name = p_name

    def match(self, my_words):
        self.pattern_words = []
        for word in my_words:
            for pat in self.pattern_group:
                if pat in word and word not in self.pattern_words:
                    self.pattern_words.append(word)
        return sorted(self.pattern_words)


class Words:
    """Stores words as a class"""

    def __init__(self, text):
        if type(text) is list:
            self.my_words = [word.lower() for word in text]
        else:
            self.my_words = clean_text(text)






