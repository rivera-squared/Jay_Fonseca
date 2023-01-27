import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from yellowbrick.cluster import KElbowVisualizer

jf = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/Jay_Fonseca/main/jay_fonseca/jay_fonseca_completo.csv')
jf['fecha'] =  pd.to_datetime(jf['fecha'])
jf['dia'] = jf['fecha'].apply(get_day_of_week)
jf['mes'] = jf['fecha'].apply(get_month)
jf['semana'] = jf['fecha'].apply(get_week)
jf['año'] = jf['fecha'].apply(get_year)


#Isolating for Category 'Salud'
salud = jf[jf['categoria'] == 'Salud']

# Text preprocessing 
stop_words = stopwords.words('spanish')
stop_words.extend(['puerto','rico','covid-19','covid','reportan','reporta'])

salud['titulo_lower'] = salud['titulo'].apply(lower_text)
salud['titulo_lower'] = salud['titulo_lower'].apply(remove_stopwords)
salud['titulo_lower'] = salud['titulo_lower'].apply(remove_numbers)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(salud.titulo_lower)

# Evaluating clusters
model = KMeans(random_state = 0, n_init = 20)
visualizer = KElbowVisualizer(model, k = (2,12))
visualizer.fit(X)
visualizer.show()

# Choose the number of cluster based on the results of elbow method
kmeans = KMeans(n_clusters = 5, random_state = 0, n_init=20).fit(X)
kmeans.score(X)

# Creating column based on the clusters
salud['cluster'] = kmeans.labels_

# Quick stats on cluster
salud.groupby('cluster')['titulo_lower'].count()

# Most common  2 ngrams per cluster
clusters = list(range(0,4,1))
for cluster in clusters:
    x = salud[salud['cluster']==cluster]
    print("\n\n2-ngram mas comunes para cluster: {} \n".format(cluster))
    print(get_2ngrams(x.titulo_lower))

jf.groupby('categoria')['fecha'].count()
jf['categoria'].unique()

# Isolating for Category "Gobierno"

gobierno = jf[(jf['categoria'] == "Gobierno") & (jf['año'] == 2022)]

stop_words = stopwords.words('spanish')

gobierno['titulo_lower'] = gobierno['titulo'].apply(lower_text)
gobierno['titulo_lower'] = gobierno['titulo_lower'].apply(remove_stopwords)
gobierno['titulo_lower'] = gobierno['titulo_lower'].apply(remove_numbers)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(gobierno.titulo_lower)

# Evaluating clusters
model = KMeans(random_state = 0, n_init = 20)
visualizer = KElbowVisualizer(model, k = (2,20))
visualizer.fit(X)
visualizer.show()

# Choose the number of cluster based on the results of elbow method
kmeans = KMeans(n_clusters = 14, random_state = 0, n_init=20).fit(X)
kmeans.score(X)

gobierno['cluster'] = kmeans.labels_

gobierno.groupby('cluster')['fecha'].count()

# Most common  2 ngrams per cluster
clusters = list(range(0,14,1))
for cluster in clusters:
    x = gobierno[gobierno['cluster']==cluster]
    print("\n\n2-ngram mas comunes para cluster: {} \n".format(cluster))
    print(get_2ngrams(x.titulo_lower))


gobierno_bow = []
clusters = list(range(0,14,1))
for cluster in clusters:
    x = gobierno[gobierno['cluster'] == cluster]
    x_ng = get_2ngrams(x.titulo_lower)
    x_df = pd.DataFrame(x_ng, columns=['frase','frecuencia'])
    x_df['cluster'] = cluster
    gobierno_bow.append(x_df)
    
gobierno_bow = pd.concat(gobierno_bow)    


plt.barh(gobierno_bow['frecuencia'], gobierno_bow['frase'])
plt.show()










