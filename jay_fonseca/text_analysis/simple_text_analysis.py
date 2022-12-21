import pandas as pd

jf = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/Jay_Fonseca/main/jay_fonseca/jay_fonseca_completo.csv')
jf['fecha'] =  pd.to_datetime(jf['fecha'])
jf['dia'] = jf['fecha'].apply(get_day_of_week)
jf['mes'] = jf['fecha'].apply(get_month)
jf['semana'] = jf['fecha'].apply(get_week)
jf['año'] = jf['fecha'].apply(get_year)

# Grouped by categoria
jf.groupby('categoria')['titulo'].count().reset_index().sort_values(by = 'titulo', ascending = False)

jf.groupby(['categoria','año'])['titulo'].count().reset_index().sort_values(by = ['año','titulo'], ascending = False)


#Isolating for Category 'Salud'
salud = jf[jf['categoria'] == 'Salud']
# Text preprocessing 

stop_words.extend(['puerto','rico'])

salud['titulo_lower'] = salud['titulo'].apply(lower_text)
salud['titulo_lower'] = salud['titulo_lower'].apply(remove_stopwords)
salud['titulo_lower'] = salud['titulo_lower'].apply(remove_numbers)

years = list(salud.año.unique())

for year in years:
    x = salud[salud['año'] == year]
    print("Most common 2-ngram for {}: \n{}\n".format(year, get_2ngrams(x.titulo_lower)))
    
get_ngrams(salud.titulo_lower)
get_3ngrams(salud.titulo_lower)
