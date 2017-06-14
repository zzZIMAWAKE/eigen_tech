class TextFileHandler:
    """Returns data that is compatible with nltk's tokenize method. We can set up several file handlers
    in this format to be able to handle several file types within the same batch."""
    def run(self, filename):
        file = "inputs/{}".format(filename)
        fp = open(file)
        data = fp.read()
        return data
