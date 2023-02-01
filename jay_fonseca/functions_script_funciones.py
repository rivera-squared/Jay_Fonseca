import pandas as pd
import numpy as np
import spacy
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from spacytextblob.spacytextblob import SpacyTextBlob

# Script para funciones
#!pip install spacy download es_core_news_sm
#pip install spacy spacytextblob

nlp = spacy.load('es_core_news_md')
#nlp.add_pipe('spacytextblob')
stop_words = stopwords.words('spanish')


###############################################################################
# SECCIONES DE FUNCIONES
# Funcion para lemmatizar el texto
def preprocess(text):
    # Create Doc object
    doc = nlp(text, disable=['ner','parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas
                if lemma.isalpha() and lemma not in stop_words]
    return ' '.join(a_lemmas)
# Funcion para remover caracteres que no son alfa numéricos
def remove_punct(text):
    removed = re.sub(r"\W", ' ', text)
    return(removed)

# Funcion para remover numeros
def remove_numbers(text):
    removed = re.sub(r"\d", " ", text)
    return removed

# Funcion para encontrar personas en el documento
def persons(text):
    doc = nlp(text)
    ne = ', '.join([(ent.text) for ent in doc.ents
          if ent.label_ == "PER"])
    return(ne)
#Funcion para encontrar organizaciones en el documento
def orgs(text):
    doc = nlp(text)
    ne = ', '.join([(ent.text) for ent in doc.ents
          if ent.label_ == "ORG"])
    return(ne)
# Funcion para convertir todos los caracteres en minusculo
def lower_text(text):
    lowered = text.lower()
    return(lowered)    
#Funcion para obtener nombres propios
def get_proper_nouns(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'PROPN'])
    return pos
# Funcion para obtener nombres
def get_nouns(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'NOUN'])
    return pos

# Funcion para obtener verbos
def get_verbs(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'VERB'])
    return pos
# Funcion para obtener adjetivos
def get_adjectives(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'ADJ'])
    return pos
# Funcion para obtener advervios
def get_adverbs(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'ADV'])
    return pos

def tokenize_words(text):
    token = word_tokenize(text)
    return token


# Funcion para remover stop words y lowercase SIN LEMATIZAR

def remove_stopwords(text):
    tokens = word_tokenize(text)
    remove = [token for token in tokens if token not in stop_words]
    return ' '.join(remove)

def obtain_stopwords(text):
    tokens = word_tokenize(text)
    remove = [token for token in tokens if token in cw]
    return ' '.join(remove)


# Funcion para obtemer n-grams    
def get_ngrams(text, ngram_from=1, ngram_to=1, n=None, max_features=20000):
    
    vec = CountVectorizer(ngram_range = (ngram_from, ngram_to), 
                          max_features = max_features).fit(text)
    bag_of_words = vec.transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:20]

def get_2ngrams(text, ngram_from=2, ngram_to=2, n=None, max_features=20000):
    
    vec = CountVectorizer(ngram_range = (ngram_from, ngram_to), 
                          max_features = max_features).fit(text)
    bag_of_words = vec.transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:10]    

def get_3ngrams(text, ngram_from=3, ngram_to=3, n=None, max_features=20000):
    
    vec = CountVectorizer(ngram_range = (ngram_from, ngram_to), 
                          max_features = max_features).fit(text)
    bag_of_words = vec.transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:10]

def get_4ngrams(text, ngram_from=4, ngram_to=4, n=None, max_features=20000):
    
    vec = CountVectorizer(ngram_range = (ngram_from, ngram_to), 
                          max_features = max_features).fit(text)
    bag_of_words = vec.transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:10]

# Funcion para obtener los tfidf
def get_tfidf(text):
    vec = TfidfVectorizer()
    bag_of_words = vec.fit_transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:30]

def get_week(date):
    fecha = date.week
    return(fecha)

def get_day(date):
    fecha = date.day
    return fecha

def get_day_of_week(date):
    fecha = date.day_name()
    return fecha

def get_month(date):
    fecha = date.month_name()
    return fecha

def get_year(date):
    fecha = date.year
    return fecha

def get_polarity(text):
    doc = nlp(text)
    polarity = doc._.polarity
    return polarity