# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:07:01 2017

@author: James
"""
import requests
from bs4 import BeautifulSoup

def web_crawler_link(maxpage,page):
     
    #page is the initial webpage,start point
    while page <= maxpage:
        url='https://www.t66y.com/thread0806.php?fid=16&search=&page='+str(page)#this is the url of the web, switch to certain page number
        source_code = requests.get(url)#get the source code of the page
        plain_text = source_code.text#only the text is necessary
        soup = BeautifulSoup(plain_text,'lxml')#Class BeauifulSoup is to search though and grab things in source text
        
        for link in soup.findAll('a', {'target':'_blank'}):#'a' means get link, {'class':'item-name'} means find link from title (item name), which is a class
            title = link.string
            
            href = 'https://www.t66y.com/'+ link.get('href')
            #print(title)
            #print(href)
            get_every_picture_link(href)
            
            
        page = page + 1
def get_every_picture_link(item_url):
    source_code = requests.get(item_url)#get the source code of the page
    plain_text = source_code.text#only the text is necessary
    soup = BeautifulSoup(plain_text,'lxml')
    for item_link in soup.findAll('input',{'type':'image'}):
        link = item_link.get('src')
        print(link)
        download_web_jpg(link)
def download_web_jpg(url):
    import random
    import urllib.request
    name=random.randrange(1,100)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)           
       
        
    
    