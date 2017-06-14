from nltk.tokenize import WhitespaceTokenizer, word_tokenize


class WordExtractor:
    """Method to extract words from the document,
    this can be interchanged with an alternate method should the need arise"""
    def extract(self, text):
        words = WhitespaceTokenizer().tokenize(text)
        # Catch special cases where we don't tokenize words with apostrophes
        sanitised_words = []
        for word in words:
            word = word.lower()
            word = word.strip(',.;!?:')
            if '\'' not in word or word[-1:] == '\'' or word[-2:] == '\'s':
                word = word_tokenize(word)
                sanitised_words += word
                continue
            sanitised_words.append(word)
        return sanitised_words
