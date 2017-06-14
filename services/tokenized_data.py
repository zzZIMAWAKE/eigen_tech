from models.sentence import Sentence


class TokenizedData:
    """Runs our selected sentence tokenizer over our file data, also preps out sentence class with
    a word extractor, both of these can be interchanged to run different extractors / tokenizers"""
    def __init__(self, sentence_tokenizer, word_extractor):
        self.sentence_tokenizer = sentence_tokenizer
        self.word_extractor = word_extractor
        self.sentences = []

    def add_file(self, filename, file_handler):
        data = file_handler.run(filename)

        extracted_sentences = self.sentence_tokenizer.tokenize(data)
        for sentence in extracted_sentences:
            self.sentences.append(Sentence(sentence, filename, self.word_extractor))
