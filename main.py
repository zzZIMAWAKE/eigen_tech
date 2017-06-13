import operator
import nltk
import string
from nltk.tokenize import WhitespaceTokenizer, word_tokenize

# You need to execute nltk.download() first and download models -> punkt
#TODO: Loop through existing files as default, offer option to list filenames

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
whitespace_tokenizer = WhitespaceTokenizer()
word_counts = {}
words = []
sentences = []
# Tokenize sentences
for i in range(1, 7):
    fp = open("inputs/doc{}.txt".format(i))
    data = fp.read()
    sentences += sentence_tokenizer.tokenize(data)
    fp.close()

# Tokenize words from sentences and strip unnecessary punctuation
for sentence in sentences:
    words += word_tokenize(sentence)

# Arrange words in to dictionary for counting occurrence
for word in words:
    word = word.lower()
    if word in string.punctuation:
        continue
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

# Sort word counts
sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
selected_most_popular_words = sorted_word_counts[:10]
print(sorted_word_counts)
# for sentence in sentences:
#     for selected_most_popular_word in selected_most_popular_words:
#         if selected_most_popular_word[0] in sentence:
#             print(selected_most_popular_word[0])
#             print(sentence)

