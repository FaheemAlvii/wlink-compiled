

def capitalize_all_words(text: str, seperator: str = ' ') -> str:
    """  Capitalizes every word in a string. str.capitalize only capitalizes the first word. """
    return seperator.join(map(str.capitalize, text.split(seperator)))


def capitalize_first_word(text: str) -> str:
    """ Capitalizes the first word of a string. """
    return text.capitalize()


if __name__ == '__main__':
    print(capitalize_all_words('a test for the function "capitalize_all_words."'))
    print(capitalize_first_word('a test for the function "capitalize_first_words."'))