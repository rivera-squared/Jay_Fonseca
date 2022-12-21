import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import random

jf = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/Jay_Fonseca/main/jay_fonseca/jay_fonseca_completo.csv')
jf['fecha'] =  pd.to_datetime(jf['fecha'])
jf['dia'] = jf['fecha'].apply(get_day_of_week)
jf['mes'] = jf['fecha'].apply(get_month)
jf['semana'] = jf['fecha'].apply(get_week)
jf['año'] = jf['fecha'].apply(get_year)


#Isolating for Category 'Salud'
salud = jf[jf['categoria'] == 'Salud']

# Text preprocessing 

stop_words.extend(['puerto','rico','covid-19','covid'])

salud['titulo_lower'] = salud['titulo'].apply(lower_text)
salud['titulo_lower'] = salud['titulo_lower'].apply(remove_stopwords)
salud['titulo_lower'] = salud['titulo_lower'].apply(remove_numbers)


random.seed(42)

# Kmeans cluster analysis
vectorizer = TfidfVectorizer(
    max_df=0.5,
    min_df=5,
    )

X_tfidf = vectorizer.fit_transform(salud.titulo_lower)

kmeans = KMeans(
    n_clusters=10,
    max_iter=100,
    n_init=5,
).fit(X_tfidf)


salud_cluster = pd.DataFrame({
    'texto':salud.titulo_lower,
    'cluster':kmeans.labels_
    })

clusters = list(salud_cluster['cluster'].unique())

salud_clusters_bow = []
for cluster in clusters:
    x = salud_cluster[salud_cluster['cluster'] == cluster]
    x_ngram = get_ngrams(x['texto'])
    x_df = pd.DataFrame(x_ngram, columns =['frase','frecuencia'])
    x_df['cluster'] = cluster
    salud_clusters_bow.append(x_df)
    
salud_clusters_bow = pd.concat(salud_clusters_bow)
    
xx = salud[salud['titulo'].str.contains('Salud')]

