###############################################################################
# This Script an intermediary process to obtain text and authors from Jay's articles
###############################################################################
import pandas as pd

df=pd.read_csv('C:/Users/uronsda/Documents/edward/python/web-scraping/web_scraping_new/Alt_PR/jay_fonseca/jay_fonseca_completo.csv')

jf1=pd.read_csv('jay_fonseca.csv')
jf1=jf1.reset_index()
jf1=jf1.rename(columns={"index":'temp'})

jf1[jf1['temp']==4000]['titulo']

temps='923'
df_new=[]
for temp in temps:
    url = jf1[jf1['temp']==temp]['enlace'].iloc[0]
    url = 'https://jayfonseca.com/buscan-incentivar-con-mejor-pago-a-maestros-en-vieques-y-culebra/'
    sel = Selector(text=requests.get(url).content)
    texto=' '.join(sel.xpath('//div[@class="entry-content readMoreContent moreView post"]/p/text()').extract())
    autor=sel.xpath('//a[@class="url fn n"]/text()').extract()
    
    df_temp=pd.DataFrame({
        'texto':texto,
        'autor':autor,        
        'temp':temp
        })
    df_new.append(df_temp)
df_new=pd.concat(df_new)    

df=pd.read_csv('jay_texto_autor.csv')
df=df.append(df_new)

#df.to_csv('jay_texto_autor.csv',index=False)

merged=df.merge(jf1, how = 'left')

merged.columns

jf = merged[['fecha','titulo','autor','texto','enlace']]

jf=jf.dropna(subset=['enlace'])
jf.isna().sum()
jf.to_csv('jay_fonseca.csv',index=False)
