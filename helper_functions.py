import re

def clean_text(text):
    """
    Accepts a single text document and performs several regex
    substitutions in order to clean the document.
    Parameters
    ----------
    text: string
    Returns
    -------
    text: list of words
    """
    special_chars_regex = '[:?,.>$|!\'"]'
    white_spaces_regex = '[ ]{2,}'
    text = re.sub('[^a-zA-Z ]', " ", text)
    text = re.sub(special_chars_regex, " ", text)
    text = re.sub(white_spaces_regex, " ", text)
    text = text.split(" ")
    text = [word.lower() for word in text]
    return text


def match_patterns(instances, words, names=None):
    """
    Takes word list and return all words that match a given pattern

    Parameters
    ----------
    instances: list of instances of patterns (created automatically by Class)
    names: names of patterns to be matched, if not specified all patterns will be matched
    words: list of words
    Returns
    -------
    Prints name of pattern and it's matches
    returns: list of tuples with pattern name and matching words
    """
    matches = []
    for instance in instances:
        if names is None:
            matches.append((instance.pattern_name, instance.match(words)))
            print(instance.pattern_name, " matches: ", instance.match(words))
        elif instance.pattern_name in names:
            matches.append((instance.pattern_name, instance.match(words)))
            print(instance.pattern_name, " matches: ", instance.match(words))
    return matches

