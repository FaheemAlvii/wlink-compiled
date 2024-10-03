

def capitalize_all_words(text: str, seperator: str = ' ') -> str:
    """  Capitalizes every word in a string. str.capitalize only capitalizes the first word. """
    return seperator.join(map(str.capitalize, text.split(seperator)))  # noqa


def capitalize_first_word(text: str) -> str:
    """ Capitalizes the first word of a string. """
    return text.capitalize()