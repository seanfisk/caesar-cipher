""":mod:`caesar.cipher` --- Implementation of the Caesar cipher"""

ASCII_LETTER_A_OFFSET = ord('A')

def caesar_char(char, key):
    """Caesar cipher for a single character.

    :param char: the character to encode or decode
    :type char: :class:`str`
    :param key: the amount of characters by which to shift
    :type key: :class:`int`
    :returns: the encoded or decoded char
    :rtype: :class:`str`
    """
    if char.isalpha():
        char = chr((ord(char.upper()) - ASCII_LETTER_A_OFFSET + key) % 26 +
                   ASCII_LETTER_A_OFFSET)
    return char

# based on: <http://code.activestate.com/recipes/577960-caesar-cipher/>
def caesar(text, key):
    """Encode or decode a Caesar cipher.

    :param text: the string to encode or decode
    :type text: :class:`str`
    :param key: the amount of characters by which to shift
    :type key: :class:`int`
    :returns: the encoded or decoded string
    :rtype: :class:`str`
    """
    result_list = []
    for char in text:
        result_list.append(caesar_char(char, key))
    return ''.join(result_list)
        
