#File : Sentiment_analysis.py

#import nltk
#import random
#from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize
#from nltk.corpus import movie_reviews
import pickle

#from sklearn.naive_bayes import MultinomialNB, BernoulliNB#, GaussianNB 

#from sklearn.linear_model import LogisticRegression, SGDClassifier
#from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode

###########################################################

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf
    
features = open('pickled_word_features.pickle', 'rb')
word_features = pickle.load(features)
features.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

naive_bayes = open('pickled_Naive_Bayes.pickle', 'rb')
NB_classifier = pickle.load(naive_bayes)
naive_bayes.close()

Multinomial = open('pickled_MNB_classifier.pickle', 'rb')
MNB_classifier = pickle.load(Multinomial)
Multinomial.close()

Bernoulli = open('pickled_BNB_classifier.pickle', 'rb')
BNB_classifier = pickle.load(Bernoulli)
Bernoulli.close()

Logistic = open('pickled_LogisticRegression_classifier.pickle', 'rb')
LogisticRegression_classifier = pickle.load(Logistic)
Logistic.close()

SGD = open('pickled_SGD_classifier.pickle', 'rb')
SGD_classifier = pickle.load(SGD)
SGD.close()

LinearSVC = open('pickled_LinearSVC_classifier.pickle', 'rb')
LinearSVC_classifier = pickle.load(LinearSVC)
LinearSVC.close()

NuSVC = open('pickled_NuSVC_classifier.pickle', 'rb')
NuSVC_classifier = pickle.load(NuSVC)
NuSVC.close()

voted_classifiers = VoteClassifier(NB_classifier,
                                   MNB_classifier,
                                   BNB_classifier,
                                   LogisticRegression_classifier,
                                   SGD_classifier,
                                   LinearSVC_classifier,
                                   NuSVC_classifier)



def sentiment(text):
    feats = find_features(text)
    return(voted_classifiers.classify(feats), voted_classifiers.confidence(feats))
          