import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report


jf = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/Jay_Fonseca/main/jay_fonseca/jay_fonseca_completo.csv')
jf['fecha'] =  pd.to_datetime(jf['fecha'])
jf['dia'] = jf['fecha'].apply(get_day_of_week)
jf['mes'] = jf['fecha'].apply(get_month)
jf['semana'] = jf['fecha'].apply(get_week)
jf['año'] = jf['fecha'].apply(get_year)

jf['categoria'] = jf.categoria.astype('category')
jf['categoria_num'] = jf.categoria.cat.codes
jf['categoria'] = jf.categoria.astype('object')

stop_words.extend(['puerto','rico', 'aquí', 'resumen','noticias','calle', 'hoy', 'covid', 'covid-19',
                   'lunes','martes','miércoles','jueves','viernes','sábado','domingo', 'vea','escucha',
                   'enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre',
                   'dice'])


jf['titulo_lower'] = jf['titulo'].apply(lower_text)
jf['titulo_lower'] = jf['titulo_lower'].apply(remove_stopwords)
jf['titulo_lower'] = jf['titulo_lower'].apply(remove_numbers)

vectorizer = TfidfVectorizer(
    max_df=0.5,
    min_df=5,
    )

X = vectorizer.fit_transform(jf.titulo_lower)
y = jf['categoria_num']

categorias = jf.categoria.unique()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y)

clf = MultinomialNB(alpha = 1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred, target_names = categorias))


get_ngrams(jf.titulo_lower)
