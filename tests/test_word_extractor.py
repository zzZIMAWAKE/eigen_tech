from services.word_extractor import WordExtractor
import unittest


class TestExtractWords(unittest.TestCase):
    def test_extract_words_from_sentence(self):
        sentence = 'This is a sentence, it isn\'t anything more, or anything less.!'
        expected_result = ['this', 'is', 'a', 'sentence', 'it', 'isn\'t', 'anything', 'more', 'or', 'anything', 'less']

        result = WordExtractor().extract(sentence)
        self.assertEqual(expected_result, result)
