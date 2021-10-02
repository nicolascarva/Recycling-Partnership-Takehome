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
    special_chars_regex = '[:?,.\>$|!\'"]'
    white_spaces_regex = '[ ]{2,}'
    text = re.sub('[^a-zA-Z ]', " ", text)
    text = re.sub(special_chars_regex, " ", text)
    text = re.sub(white_spaces_regex, " ", text)
    text = text.split(" ")
    text = [word.lower() for word in text]
    return text