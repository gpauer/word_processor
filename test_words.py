import unittest
import word_processor

class TestWords(unittest.TestCase):
    def test_convert_to_word_list(self):
        self.assertEqual(word_processor.convert_to_word_list('Hello., World. How? are  you??  doing.,? '), 
        ['hello', 'world', 'how', 'are', 'you', 'doing'])
        self.assertEqual(word_processor.convert_to_word_list('He llo., 123WORLD!!. How? are  you??  doing.,? '), 
        ['he', 'llo', '123world!!', 'how', 'are', 'you', 'doing'])
        self.assertEqual(word_processor.convert_to_word_list('.. .. ,,,,,   ,  ? ? ? ? '), 
        [])


    def test_words_longer_than(self):
        self.assertEqual(word_processor.words_longer_than(3, 'Hello   .,what do you want   to  do ..now?'),
        ['hello', 'what', 'want'])
        self.assertEqual(word_processor.words_longer_than(3, 'and or and maybe cuz i know,. it.?'),
        ['maybe', 'know'])


    def test_words_length_map(self):
        self.assertEqual(word_processor.words_lengths_map('Hello world how..... .,  ..are. you?,.'),
        {5:2, 3:3})
        self.assertEqual(word_processor.words_lengths_map('Hello world how..... .,  ..are. you am I 1 lol lmao?,.'),
        {5: 2, 3: 4, 2: 1, 1: 2, 4: 1})
        self.assertEqual(word_processor.words_lengths_map('Hello world how.....1 12 1 12 1 12 1 .,p aa bb cc abc abc qwrwedf  ..are. you?,.'),
        {5: 2, 3: 5, 1: 5, 2: 6, 7: 1})


    def test_letters_count_map(self):
        self.assertEqual(word_processor.letters_count_map('Hello world abc,.   abc xyz xyz,.?'),
        {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 
        'l': 3, 'm': 0, 'n': 0, 'o': 2, 'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 1, 'x': 2, 'y': 2, 'z': 2})

    
    def test_most_used_character(self):
        self.assertEqual(word_processor.most_used_character('Hello world abc,.   abc xyz xyz,.?'), 'l')
        self.assertEqual(word_processor.most_used_character('Hello world abcx,.   abc xyzx xyzx,.?'), 'x')
        self.assertEqual(word_processor.most_used_character('Hello world abc,.   aaaaaabc xyz xyz,.?'), 'a')
        self.assertEqual(word_processor.most_used_character('1234567890'), None)
        self.assertEqual(word_processor.most_used_character(''), None)


    def test_get_alphabet_letters(self):
        self.assertEqual(word_processor.get_alphabet_characters(), 
        ['a', 'b', 'c', 'd', 'e', 'f', 
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'])

if __name__ == '__main__':
    unittest.main()
    