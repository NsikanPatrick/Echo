import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

# Note that NLP concepts are tokenization, stemming, bag of words

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

q = "How long does shipping take?"
print(q)
q = tokenize(q)
print(q)

ans = ["Shipping", "takes", "14", "days"]
stemmed_words = [stem(a) for a in ans]
print(stemmed_words)


