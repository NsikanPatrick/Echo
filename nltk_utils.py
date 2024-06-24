import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

# Note that NLP concepts are tokenization, stemming, bag of words

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    sentence = ["Hello", "How", "Are", "You"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag = [0, 1, 0, 1, 0, 0, 0]
    """
    # What happened is that we pick each word from sentence array and check it in the
    # words array, we place 1 in the bag array at the same position were it is in the 
    # words array

    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[idx] = 1.0
            
    return bag
    
sentence = ["Hello", "How", "Are", "You"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bag = bag_of_words(sentence, words)

# print(bag)

# q = "How long does shipping take?"
# print(q)
# q = tokenize(q)
# print(q)

# ans = ["Shipping", "takes", "14", "days"]
# stemmed_words = [stem(a) for a in ans]
# print(stemmed_words)


