import numpy as np
import nltk

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Define a function to tokenize a sentence
def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)

# Define a function to stem a word
def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())

# Define a function to convert a sentence into a bag of words representation
def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
 
    # Stem all the words in the sentence
    sentence_words = [stem(word) for word in tokenized_sentence]

    # Create an array of zeros with length equal to the number of words in the vocabulary
    bag = np.zeros(len(words), dtype=np.float32)
    
    # Iterate through each word in the vocabulary
    for idx, w in enumerate(words):
        # If the word exists in the sentence, set the corresponding value in the bag to 1
        if w in sentence_words: 
            bag[idx] = 1

    return bag


