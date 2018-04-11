"""
The `utils` module presents a lot of functions to import and
transform data.
"""

import pickle

""" This table may be used many times during the program."""
puncts_table = {
    ".": "||period||",
    ",": "||comma||",
    "\"": "||quotation||",
    ";": "||semicolon||",
    "!": "||exclamation||",
    "?": "||question||",
    "(": "||left_parentheses||",
    ")": "||right_parentheses||",
    "--": "||dash||",
    "\n": "||return||"
}


def import_book(book_file, lowercase=True):
    """
    Reads a text file (and optionally converts to lowercase),
    returning a string with all the content.
    """
    try:
        with open(book_file, 'r') as book:
            text = book.read()
            text = text.lower()
            return text
    except (FileNotFoundError, PermissionError):
        message = 'There was a problem importing the book.\n'
        message += 'Please, check the path and permissions.'
        raise UserWarning(message)


def remove_puncts(text):
    """
    Using a dictionary with a conversion table, replaces puncts like
    ! by ||exclamation|| and , by ||comma||.
    """
    for key, value in puncts_table.items():
        text = text.replace(key, value)
    return text


def restore_puncts(text):
    """
    Replaces back tokens like ||comma|| by , - the inverse of
    `remove_puncts()` function.
    """
    for key, value in puncts_table.items():
        text = text.replace(value, key)
    return text


def create_list(text):
    """
    Receives a big string and returns a list with words.
    """
    return text.split()


def create_maps(text):
    """
    Receives a list of words and returns a tuple with 2 dicts:
     - a dict to translate words to numerical ids;
     - a dict to translate numerical ids to words;
    """
    word_to_num, num_to_word = {}, {}
    for num, word in enumerate(set(text)):
        num_to_word[num] = word
        word_to_num[word] = num
    return word_to_num, num_to_word


def save_object(obj, filename):
    """
    Uses `pickle` to save a given object to a file.
    """
    try:
        with open(filename, 'wb') as bkp:
            pickle.dump(obj, bkp)
    except (FileNotFoundError, PermissionError):
        message = 'There was a problem writing the pickle.\n'
        message += 'Please, check the path and permissions.'
        raise UserWarning(message)


def restore_object(filename):
    """
    Read a `pickle` file and returns the saved objects.
    """
    try:
        with open(filename, 'rb') as bkp:
            reading = pickle.load(bkp)
    except (FileNotFoundError, PermissionError):
        message = 'There was a problem reading the pickle.\n'
        message += 'Please, check the path and permissions.'
        raise UserWarning(message)
    return reading
