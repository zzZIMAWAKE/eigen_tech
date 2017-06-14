import operator
import nltk
from models.sentence import Sentence
from services.word_extractor import WordExtractor
from services.csv_output import CsvOutput

# You need to execute nltk.download() first and download models -> punkt
#TODO: Loop through existing files as default, offer option to list filenames

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

extracted_sentences = []
sentences = []

# Tokenize sentences
for i in range(1, 7):
    file = "inputs/doc{}.txt".format(i)
    fp = open(file)
    data = fp.read()
    extracted_sentences += sentence_tokenizer.tokenize(data)
    for sentence in extracted_sentences:
        sentences.append(Sentence(sentence, file, WordExtractor()))
    fp.close()

word_counts = {}
for sentence in sentences:
    for word, count in sentence.stats.items():
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += count

# Sort word counts
sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
selected_most_popular_words = sorted_word_counts[:10]
# print(sorted_word_counts)
csv_output = CsvOutput(sentences, selected_most_popular_words)
csv_output.run()

# for sentence in sentences:
#     for selected_most_popular_word in selected_most_popular_words:
#         if re.compile(r'\b({0})\b'.format(selected_most_popular_word[0]), flags=re.IGNORECASE).search(sentence):
#             print('\n ------ \n')
#             print(selected_most_popular_word[0])
#             print('in the sentence:')
#             print(sentence)
#             print('\n ------ \n')

