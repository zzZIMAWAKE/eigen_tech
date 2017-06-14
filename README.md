## Dependency setup:

Run
```shell
pip install -r requirements.txt
```

Once the requirements have been installed you'll need to run the following to install the pickle file required for english tokenizing via nltk
```shell
python setup.py
```

## Usage:

Use the following command to run the code:
```shell
python main.py
```

Use the following command to run any tests:
```shell
pytest
````

If you want to increase the number of most commonly occurring words that will be displayed increased the number assigned to the results_limit variable
If you wish to add custom files, add them to the inputs folder. Should you no longer want to run the existing files you should delete them, it will run through
ever file within the inputs folder, it will throw an exception if any of the files are not txt files.

## Documentation

_A brief description of the structure of this project and what I was aiming to achieve._

Each sentence from the file is stored in the sentence class, this is initiated with a word extractor service, described below.
The sentence class stores the text from the sentence, each word extracted by the word extractor service, the file the sentence
came from and stats about the sentence, which are currently the counts for each word in the sentence. It also provides a sentence contains
method which will return a boolean value as to whether the sentence contains a particular word.

The word extractor service is used as the method by which we want to extract words, in this case I chose to extract words like 'don't' as a single word
as opposed to the tokenizer's default setting of splitting those up to be 'do' and 'n't'. I thought this was more relevant to what this program tried
to achieve. By passing this service in to the sentence class it's really easy to add alternative word extraction classes and use those instead.

The text file handler service is used to provide tokenizable data to nltk from text files, new file handler services can be created for different file types
with the aim of allowing the handling of other filetypes in the future. For now if a non text file is provided an exception will be thrown to tell the user that
the file handler for that file type needs to be implemented.

The tokenized data service is used to tokenize the data provided by the file handler, it is initialized with a word extractor service and
a sentence tokenizer. The purpose of initialising it with a word extractor and sentence tokenizer was to ensure that only one word extractor
and one sentence tokenizer would be used throughout the entirety of one run, in this way it means we get consistent results across several files
preventing the user from tokenizer data from one file in one way, and another file in another way, meaning our results are meaningful and consistent.

The output services are self explanatory and just format our data in to outputs, either printing in the console or creating a csv.


