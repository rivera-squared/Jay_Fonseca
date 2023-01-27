import pandas as pd

salud=pd.read_csv('jf_salud.csv')
salud.columns


nlp = spacy.load('es_core_news_md')
stop_words = stopwords.words('spanish')


salud['titulo']=salud['titulo'].apply(lower_text)
salud['titulo']=salud['titulo'].apply(remove_stopwords)

cw=get_ngrams(salud['titulo'])
cw=list(np.array(cw)[:,0])
# Quiero tratar dejar las palabras mas comunes (despues de extraer los stopwords regulares)
# La idea es disminuir las palabras disponibles para poder reintentar el algoritmo
# NB para clasificar topics

salud['palabras_comunes']=salud['titulo'].apply(obtain_stopwords)
obtain_stopwords("Yo quiero ser enfático... no hay ni covid, ni flu")

#from sklearn.preprocessing import MultiLabelBinarizer
onehot_enc = MultiLabelBinarizer()
onehot_enc.fit(salud.palabras_comunes)

#from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(salud.palabras_comunes, salud.salud_label, test_size=0.25, random_state=None, stratify=salud.salud_label)

#from sklearn.naive_bayes import BernoulliNB

bnbc = BernoulliNB(binarize=None)
bnbc.fit(onehot_enc.transform(X_train), y_train)

score = bnbc.score(onehot_enc.transform(X_test), y_test)
print(score)
y_pred=bnbc.predict(onehot_enc.transform(X_test))

#from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

new_text=['gobernador',
          'gobernador salud',
          'salud reporta muerte puerto rico tras',
          'empresa']

bnbc.predict_proba(onehot_enc.transform(new_text))
