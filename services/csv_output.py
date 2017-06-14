import csv


class CsvOutput:
    """Formats data in to a CSV output"""
    def __init__(self, sentences, popular_words):
        self.sentences = sentences
        self.popular_words = popular_words

    def run(self):
        with open('output.csv', 'w') as csvfile:
            output_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            output_writer.writerow(['Word(#)', 'Documents', 'Sentences containing the word'])
            for word in self.popular_words:
                files = []
                output_sentences = []
                for sentence in self.sentences:
                    if sentence.contains_word(word[0]):
                        files.append(sentence.file)
                        output_sentences.append(sentence.text)
                output_writer.writerow([word[0], ' '.join(set(files)), output_sentences.pop()])
                for output_sentence in output_sentences:
                    output_writer.writerow(['', '', output_sentence])
