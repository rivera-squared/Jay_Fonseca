import pandas as pd

df=pd.read_csv('jay_fonseca.csv')
df.columns
df['fecha']=pd.to_datetime(df['fecha'])
df['mes']=df['fecha'].apply(get_month)
df['año']=df['fecha'].apply(get_year)

df=df.dropna(subset=['texto']) # Dropping missing values

# Text Preprocessing

stop_words = stopwords.words('spanish')
stop_words.extend(['puerto','rico','hoy','si','urrutia', 'según', 'explicó'])
df['texto']=df['texto'].apply(lower_text)
df['texto']=df['texto'].apply(remove_punct)
df['texto']=df['texto'].apply(remove_numbers)
df['texto']=df['texto'].apply(remove_stopwords)
df['resumen']=df['texto'].apply(get_summary)

df['resumen']=df['resumen'].apply(lower_text)
df['resumen']=df['resumen'].apply(remove_stopwords)

#df.to_csv('jay_fonseca_tmodeling.csv', index=False)

df=df[(df['año'] ==2022)]
df=df.sort_values(by=['fecha'])
meses = list(df.mes.unique())
list(df.autor.unique())
df.autor.value_counts()

autores = ['Jagual Media',
 'Cynthia López Cabán',
 'Jay Fonseca',
 'Katriana Vélez',
 'Hermes Ayala Guzmán', 
 'Yennifer Álvarez',
 'Ámbar Suárez Cubillé',
 'Milly Méndez']

x_autores=[]
for autor in autores:
    x=df[(df['autor']==autor)]
    ngram2 = get_2ngrams(x['resumen'])
    ngram3 = get_3ngrams(x['resumen'])
    x_df=pd.DataFrame({
        'autora':autor,
        '2frases':np.array(ngram2)[:,0],
        '2frases_freq':np.array(ngram2)[:,1],
        '3frases':np.array(ngram3)[:,0],
        '3frases_freq':np.array(ngram3)[:,1]
        })
    x_autores.append(x_df)
x_autores=pd.concat(x_autores)    

x_autores['2frases_freq']=x_autores['2frases_freq'].astype(int)
x_autores['3frases_freq']=x_autores['3frases_freq'].astype(int)

x_autores.dtypes

###############################################################################
# Graphic by authors
# define subplot grid
plt.figure(figsize=(17, 14))
plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(wspace=0.5)
plt.suptitle("Temas mas comunes por autores en \nwww.jayfonseca.com", fontsize=18, y=0.95)

for n, autor in enumerate(autores):
    ax=plt.subplot(4,2, n+1)
    
    x=x_autores[x_autores['autora']==autor]
    x=x.sort_values(by=['2frases_freq'])
    plt.barh(y = x['2frases'], width = x['2frases_freq']);
    ax.set_title(autor.upper())
    ax.set_xlabel("")
   
# Graphing 3-ngram    
plt.figure(figsize=(20, 17))
plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(wspace=0.5)
plt.suptitle("Temas mas comunes por autores en \nwww.jayfonseca.com", fontsize=18, y=0.95)

for n, autor in enumerate(autores):
    ax=plt.subplot(4,2, n+1)
    
    x=x_autores[x_autores['autora']==autor]
    x=x.sort_values(by=['3frases_freq'])
    plt.barh(y = x['3frases'], width = x['3frases_freq']);
    ax.set_title(autor.upper())
    ax.set_xlabel("")    
###############################################################################

###############################################################################
# Graphing by months
x_meses=[]
for mes in meses:
    x=df[(df['mes']==mes)]
    ngram2 = get_2ngrams(x['resumen'])
    ngram3 = get_3ngrams(x['resumen'])
    x_df=pd.DataFrame({
        'mes':mes,
        '2frases':np.array(ngram2)[:,0],
        '2frases_freq':np.array(ngram2)[:,1],
        '3frases':np.array(ngram3)[:,0],
        '3frases_freq':np.array(ngram3)[:,1]
        })
    x_meses.append(x_df)
x_meses=pd.concat(x_meses)    

x_meses['2frases_freq']=x_meses['2frases_freq'].astype(int)
x_meses['3frases_freq']=x_meses['3frases_freq'].astype(int)

# define subplot grid
plt.figure(figsize=(17, 14))
plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(wspace=0.5)
plt.suptitle("Temas mas comunes por mes en \nwww.jayfonseca.com", fontsize=18, y=0.95)

for n, mes in enumerate(meses):
    ax=plt.subplot(4,2, n+1)
    
    x=x_meses[x_meses['mes']==mes]
    x=x.sort_values(by=['2frases_freq'])
    plt.barh(y = x['2frases'], width = x['2frases_freq']);
    ax.set_title(mes.upper())
    ax.set_xlabel("")
   
# Graphing 3-ngram    
plt.figure(figsize=(20, 17))
plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(wspace=0.5)
plt.suptitle("Temas mas comunes por autores en \nwww.jayfonseca.com", fontsize=18, y=0.95)

for n, autor in enumerate(autores):
    ax=plt.subplot(4,2, n+1)
    
    x=x_autores[x_autores['autora']==autor]
    x=x.sort_values(by=['3frases_freq'])
    plt.barh(y = x['3frases'], width = x['3frases_freq']);
    ax.set_title(autor.upper())
    ax.set_xlabel("")    




















