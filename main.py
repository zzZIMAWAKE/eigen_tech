import operator
import nltk
from services.word_extractor import WordExtractor
from services.csv_output import CsvOutput
from services.console_output import ConsoleOutput
from services.text_file_handler import TextFileHandler
from services.tokenized_data import TokenizedData

filenames = ['doc{}.txt'.format(i) for i in range(1, 7)]
results_limit = 5

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# Set up word extractor, file handlers and tokenized data storage class
word_extractor = WordExtractor()
text_file_handler = TextFileHandler()
tokenized_data = TokenizedData(sentence_tokenizer, word_extractor)

# Tokenize file data
for filename in filenames:
    if filename[-4:] == '.txt':
        tokenized_data.add_file(filename, text_file_handler)
    else:
        raise Exception('Please implement importer for this file type {}'.format(filename))

# Create counts for each word in the documents
word_counts = {}
for sentence in tokenized_data.sentences:
    for word, count in sentence.stats.items():
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += count

# Sort word counts
sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
most_popular_words = sorted_word_counts[:results_limit]

# Output to csv file: output.csv
csv_output = CsvOutput(tokenized_data.sentences, most_popular_words)
csv_output.run()

# Output to the console
# console_output = ConsoleOutput(sentences, selected_most_popular_words)
# console_output.run()

