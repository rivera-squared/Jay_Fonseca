import pandas as pd
import spacy
import re
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('jay_fonseca.csv')
df['fecha']=pd.to_datetime(df['fecha'])
df['mes']=df['fecha'].apply(get_month)
df['año']=df['fecha'].apply(get_year)

nlp = spacy.load('es_core_news_md')

# extractive summary by word count
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
    #sents = sorted(sents[:10], key=lambda x: x[2])        
    # compile them into text
    summary_text = ""
    for sent in sents:
        summary_text += sent[0] + " "
        
    return summary_text        
 

# Funcion para saber cuan largo es el texto del articulo
def text_length(text):
    x=len(text)
    return x

df=df[(df['mes']=='December') & (df['año']==2022)] # Isolating for January 2023
df=df.dropna() # Droppping missing values
df['resumen']=df['texto'].apply(get_summary) # Creating column with the article text's summary

# Text preprocessing with the newly created column

df['resumen']=df['resumen'].apply(lower_text)
df['resumen']=df['resumen'].apply(remove_stopwords)

get_ngrams(df.resumen)
get_3ngrams(df.resumen)
ng2=get_2ngrams(df.resumen) # Get 2-ngrams
frases2=pd.DataFrame({'frase':np.array(ng2)[:,0],'frecuencia':np.array(ng2)[:,1]}) # Create a DF out of the 2 ngram
frases2['frecuencia']=frases2['frecuencia'].astype(int) # Convert to integer

ng3=get_3ngrams(df.resumen) # Get 2-ngrams
frases3=pd.DataFrame({'frase':np.array(ng3)[:,0],'frecuencia':np.array(ng3)[:,1]}) # Create a DF out of the 2 ngram
frases3['frecuencia']=frases2['frecuencia'].astype(int) # Convert to integer


# set plot style: grey grid in the background:
sns.set(style="darkgrid")

# load dataset
tips = sns.load_dataset("tips")

# Set the figure size
plt.figure(figsize=(15, 13))

# plot a bar chart
sns.barplot(
    x="frecuencia", 
    y="frase", 
    data=frases3, 
    estimator=sum, 
    ci=None, 
    color='#69b3a2');
plt.title('Frases (3 palabras) mas comunes durante enero 2023')
#plt.suptitle('www.jayfonseca.com')
plt.xlabel('')
plt.show()