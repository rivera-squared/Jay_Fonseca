import pandas as pd
import spacy
import re

nlp = spacy.load('es_core_news_md')

# extractive summary by word count
text = """This is an example text. We will use seven sentences and we will return 3. This blog is written by Yujian Tang. Yujian is the best software content creator. This is a software content blog focused on Python, your software career, and Machine Learning. Yujian's favorite ML subcategory is Natural Language Processing. This is the end of our example."""

def get_summary(text):
    
    # tokenize
    doc = nlp(text)
    # create dictionary
    word_dict = {}
    # loop through every sentence and give it a weight
    for word in doc:
        word = word.text.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    # create a list of tuple (sentence text, score, index)
    sents = []
    # score sentences
    sent_score = 0
    for index, sent in enumerate(doc.sents):
        for word in sent:
            word = word.text.lower()
            sent_score += word_dict[word]
        sents.append((sent.text.replace("\n", " "), sent_score/len(sent), index))
    
    
    # sort sentence by word occurrences
    sents = sorted(sents, key=lambda x: -x[1])
    # return top 3
    sents = sorted(sents[:3], key=lambda x: x[2])        
    # compile them into text
    summary_text = ""
    for sent in sents:
        summary_text += sent[0] + " "
        
    return summary_text        
 
get_summary(merged.iloc[10]['texto'])

# Funcion para saber cuan largo es el texto del articulo
def text_length(text):
    x=len(text)
    return x

merged['art_len']=merged['texto'].apply(text_length)


merged['resume']=merged['texto'].apply(get_summary)
merged.iloc[2]['texto'].strip()
merged.iloc[2]['resume'].strip()
