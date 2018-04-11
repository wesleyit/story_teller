"""
These are the unit tests for `utils` module.
"""

import pickle

import story_teller.utils as u


def test_import_book():
    """
    Reads a text file (and optionally converts to lowercase),
    returning a string with all the content.
    """
    passwd = u.import_book('/etc/passwd', lowercase=True)
    assert type(passwd) == str
    assert passwd.islower()
    assert passwd.find('root') >= 0


def test_remove_puncts():
    """
    Using a dictionary with a conversion table, replaces puncts like
    ! by ||exclamation|| and , by ||comma||.
    """
    before = 'Hey, Joe! Where are you?'
    converted = u.remove_puncts(before)
    answer = 'Hey||comma|| Joe||exclamation|| Where are you||question||'
    assert converted == answer


def test_restore_puncts():
    """
    Replaces back tokens like ||comma|| by , - the inverse of
    `remove_puncts()` function.
    """
    before = 'Hey||comma|| Joe||exclamation|| Where are you||question||'
    converted = u.restore_puncts(before)
    answer = 'Hey, Joe! Where are you?'
    assert converted == answer


def test_create_list():
    """
    Receives a big string and returns a list with words.
    """
    text = 'The dead horse is a lifeless animal.'
    converted = u.create_list(text)
    answer = ['The', 'dead', 'horse', 'is', 'a', 'lifeless', 'animal.']
    assert converted == answer
    assert len(converted) == 7


def test_create_maps():
    """
    Receives a list of words and returns a tuple with 2 dicts:
     - a dict to translate words to numerical ids;
     - a dict to translate numerical ids to words;
    """
    text = ['I', 'like', 'you', 'more', 'than', 'I', 'like', 'me']
    word_to_num, num_to_word = u.create_maps(text)
    like_num = word_to_num['like']
    assert num_to_word[like_num] == 'like'


def test_save_object():
    """
    Uses `pickle` to save a given object to a file.
    """
    bkp_file = '/tmp/save_test.p'
    text = 'Michael Jackson'
    reading = None
    u.save_object(text, bkp_file)
    try:
        with open(bkp_file, 'rb') as bkp:
            reading = pickle.load(bkp)
    except (FileNotFoundError, PermissionError):
        message = 'There was a problem saving the pickle.\n'
        message += 'Please, check the path and permissions.'
        raise UserWarning(message)
    assert reading == text


def test_restore_object():
    """
    Read a `pickle` file and returns the saved objects.
    """
    bkp_file = '/tmp/save_test.p'
    text = 'Michael Jackson'
    try:
        with open(bkp_file, 'wb') as bkp:
            reading = pickle.dump(text, bkp)
    except (FileNotFoundError, PermissionError):
        message = 'There was a problem saving the pickle.\n'
        message += 'Please, check the path and permissions.'
        raise UserWarning(message)
    reading = u.restore_object(bkp_file)
    assert reading == text
