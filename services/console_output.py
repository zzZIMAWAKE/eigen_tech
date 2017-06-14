
class ConsoleOutput:
    """Console output is only recommended for very small results"""
    def __init__(self, sentences, popular_words):
        self.sentences = sentences
        self.popular_words = popular_words

    def run(self):
        print('The most popular words are: ')
        print('----------------------------')
        files = []
        for word in self.popular_words:
            print('\n ------ \n')
            print(word[0])
            print('in the sentences:')
            for sentence in self.sentences:
                if sentence.contains_word(word[0]):
                    files.append(sentence.file)
                    print(sentence.text)
            print('located in files: ' + ' '.join(set(files)))
