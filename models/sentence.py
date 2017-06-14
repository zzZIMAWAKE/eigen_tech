import string
import re


class Sentence:
    """Uses our chosen word extractor to extract words from the sentence text,
    stores stats on word counts for later access"""
    def __init__(self, text, file, word_extractor):
        self.text = text
        self.file = file
        self.words = word_extractor.extract(self.text)
        self.stats = self._extract_stats()

    def _extract_stats(self):
        stats = {}
        for word in self.words:
            if word in ['\'d', '\'t', '\s', 's', 'd', 't'] or word in string.punctuation:
                continue

            if not re.search('[a-zA-Z0-9]', word):
                continue

            if word not in stats:
                stats[word] = 0
            stats[word] += 1

        return stats

    def contains_word(self, word):
        return True if word in self.words else False

