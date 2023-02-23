from scrapy import Selector
import requests
import pandas as pd

def get_autor(link):
    url = str(link)
    sel = Selector(text=requests.get(url).content)
    autor = ''.join(sel.xpath('//a[@class="url fn n"]/text()').extract())
    return autor

def get_texto(link):
    url = str(link)
    sel = Selector(text=requests.get(url).content)
    texto=' '.join(sel.xpath('//div[@class="entry-content readMoreContent moreView post"]/p/text()').extract())
    
    if texto == '':
        return "No texto disponible"
    else:
        return texto

def get_fuente_original(link):
    url = str(link)
    sel = Selector(text=requests.get(url).content)
    fuente_original = ''.join(sel.xpath('//div[@class="entry-content readMoreContent moreView post"]/p/a/text()').extract())
    
    if fuente_original == '':
        return "Jagual Media es Fuente Original"
    else:
        return fuente_original
    
    return fuente_original

def get_enlace_fuente_original(link):
    url = str(link)
    sel = Selector(text=requests.get(url).content)
    enlace_fuente_original = ''.join(sel.xpath('//div[@class="entry-content readMoreContent moreView post"]/p/a/@href').extract())
    
    if enlace_fuente_original == '':
        return "Jagual Media es Fuente Original"
    else:
        return enlace_fuente_original

def get_jay_fonseca(initial_page_number = 0, page_number=1):
    pages = list(range(initial_page_number,page_number,1))
    jf = []
    
    for page in pages:    
        texto=[]
        autor=[]
        fuente_original=[]
        enlace_original=[]
        
        url = 'https://jayfonseca.com/page/' + str(page)
        sel = Selector(text=requests.get(url).content)
        titulo = sel.xpath('//h2[@class="entry-title"]/a/text()').extract()
        fecha = sel.xpath('//li[@class="meta-date"]/text()').extract()
        link = sel.xpath('//h2[@class="entry-title"]/a/@href').extract()
    
        for enlace in link:
            texto.append(get_texto(enlace))
            autor.append(get_autor(enlace))
            fuente_original.append(get_fuente_original(enlace))
            enlace_original.append(get_enlace_fuente_original(enlace))
    
        
        x_df = pd.DataFrame({
            'fecha':fecha,
            'autor':autor,
            'titulo':titulo,
            'texto':texto,
            'enlace':link,
            "fuente_original":fuente_original,
            'enlace_original':enlace_original
            })
        
        jf.append(x_df)
    
    jf = pd.concat(jf)
    jf['fecha']=pd.to_datetime(jf['fecha'], dayfirst= True)
    jf=jf.sort_values(by='fecha', ascending=False)
    jf=jf.drop_duplicates(subset = 'enlace')
    print("Current page: {}".format(page))
    return jf