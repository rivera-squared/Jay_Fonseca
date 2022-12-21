from scrapy import Selector
import requests
import pandas as pd

pages = list(range(1,405,1))
puerto_rico = []
for page in pages:    
    url = 'https://jayfonseca.com/category/puerto-rico/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Puerto Rico',
        'enlace':link})
    puerto_rico.append(x_df)

puerto_rico_df = pd.concat(puerto_rico)

# Noticias de Politica
pages = list(range(1,93,1))
politica = []
for page in pages:    
    url = 'https://jayfonseca.com/category/politica/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Politica',
        'enlace':link})
    politica.append(x_df)
    
politica_df = pd.concat(politica)    

pages = list(range(1,372,1))
gobierno = []
for page in pages:    
    url = 'https://jayfonseca.com/category/gobierno/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Gobierno',
        'enlace':link})
    gobierno.append(x_df)

    
gobierno_df = pd.concat(gobierno)

pages = list(range(1,32,1))
legislatura = []
for page in pages:    
    url = 'https://jayfonseca.com/category/legislatura/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Legislatura',
        'enlace':link})
    legislatura.append(x_df)
    
legislatura_df = pd.concat(legislatura)


pages = list(range(1,41,1))
tribunales = []
for page in pages:    
    url = 'https://jayfonseca.com/category/tribunales/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Tribunales',
        'enlace':link})
    tribunales.append(x_df)
    
tribunales_df = pd.concat(tribunales)


pages = list(range(1,12,1))
cultura = []
for page in pages:    
    url = 'https://jayfonseca.com/category/cultura/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Cultura',
        'enlace':link})
    cultura.append(x_df)
    
cultura_df = pd.concat(cultura)


pages = list(range(1,114,1))
salud = []
for page in pages:    
    url = 'https://jayfonseca.com/category/salud/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Salud',
        'enlace':link})
    salud.append(x_df)
    
salud_df = pd.concat(salud)

pages = list(range(1,69,1))
economia = []
for page in pages:    
    url = 'https://jayfonseca.com/category/economia/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Economia',
        'enlace':link})
    economia.append(x_df)
    
economia_df = pd.concat(economia)


pages = list(range(1,57,1))
educacion = []
for page in pages:    
    url = 'https://jayfonseca.com/category/educacion/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
       #'extracto':extracto,
        'categoria':'Educacion',
        'enlace':link})
    educacion.append(x_df)
    
educacion_df = pd.concat(educacion)



pages = list(range(1,54,1))
usa = []
for page in pages:    
    url = 'https://jayfonseca.com/category/estados-unidos/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Estados Unidos',
        'enlace':link})
    usa.append(x_df)
    
usa_df = pd.concat(usa)


pages = list(range(1,19,1))
internacional = []
for page in pages:    
    url = 'https://jayfonseca.com/category/internacional/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Internacional',
        'enlace':link})
    internacional.append(x_df)
    
internacional_df = pd.concat(internacional)
internacional_df['categoria']  = "Internacional"

pages = list(range(1,8,1))
ciencia = []
for page in pages:    
    url = 'https://jayfonseca.com/category/ciencia/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Ciencia',
        'enlace':link})
    ciencia.append(x_df)
    
ciencia_df = pd.concat(ciencia)
ciencia_df['categoria'] ='Ciencia'


pages = list(range(1,4,1))
deportes = []
for page in pages:    
    url = 'https://jayfonseca.com/category/deportes/page/' + str(page)
    sel = Selector(text=requests.get(url).content)
    titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
    link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
    extracto = sel.xpath('//div[@class="entry-excerpt"]/text()').extract()
    x_df = pd.DataFrame({
        'fecha':fecha,
        'titulo':titulo,
        #'extracto':extracto,
        'categoria':'Deportes',
        'enlace':link})
    deportes.append(x_df)
    
deportes_df = pd.concat(deportes)


jf = puerto_rico_df.append(politica_df)
jf = jf.append(gobierno_df)
jf = jf.append(legislatura_df)
jf = jf.append(tribunales_df)
jf = jf.append(cultura_df)
jf = jf.append(salud_df)
jf = jf.append(economia_df)
jf = jf.append(educacion_df)
jf = jf.append(usa_df)
jf = jf.append(internacional_df)
jf = jf.append(ciencia_df)
jf = jf.append(deportes_df)

jf['fecha'] = pd.to_datetime(jf['fecha'], dayfirst = True)
jf = jf.sort_values(by ='fecha', ascending = False)

jf.to_csv('jay_fonseca_completo.csv', index = False)





















