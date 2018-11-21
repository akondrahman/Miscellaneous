'''
Akond, n-gram model practice
'''

# from nltk.model.ngram import NgramModel
from source_ngram import NgramModel
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist, WittenBellProbDist
estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
grams = 3
lm = NgramModel(grams, brown.words(categories='news'), estimator)

# import nltk
# from nltk.util import ngrams
#
# def word_grams(words, min=1, max=4):
#     s = []
#     for n in range(min, max):
#         for ngram in ngrams(words, n):
#             s.append(' '.join(str(i) for i in ngram))
#     return s
#
# print word_grams('one two three four'.split(' '))
