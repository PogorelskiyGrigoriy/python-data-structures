from unittest import TestCase
from words import Words

_words:list[str] = ['Apple', 'Application', 'Apricot', 'approach']

class TestWords(TestCase):
    def setUp(self):
        self.words = Words()
        for word in _words:
            self.words.add_word(word)
            
    def test_add_word(self):
        with self.assertRaises(ValueError):
            self.words.add_word('apple')
            
    def test_words_starts_with(self):
        self.assertEqual(self.words.words_starts_with('app'), ['Apple', 'Application', 'approach'])
        self.assertEqual(self.words.words_starts_with('appl'), ['Apple', 'Application'])
        self.assertEqual(self.words.words_starts_with('ap'), ['Apple', 'Application', 'approach', 'Apricot'])
        self.assertEqual(self.words.words_starts_with('a'), ['Apple', 'Application', 'approach', 'Apricot'])      
        self.assertEqual(self.words.words_starts_with('b'), [])