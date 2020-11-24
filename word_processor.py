
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    return(list(filter(lambda x: len(x) > 0, split(',;?. ', text.lower()))))


def words_longer_than(length, text):
    return(list(filter(lambda x: len(x) > length, split(',;?. ', text.lower()))))


def words_lengths_map(text):
    list_1 = ['x'*len(x) for x in convert_to_word_list(text)]
    return({len(x):list_1.count(x) for x in list_1})


def letters_count_map(text):
    return({chr(x):text.lower().count(chr(x)) for x in range(97, 123)})


def most_used_character(text):
    if any(x.isalpha() for x in text):
        return(max(letters_count_map(text), key=letters_count_map(text).get))

def get_alphabet_characters():
    return([chr(x) for x in range(97, 123)])