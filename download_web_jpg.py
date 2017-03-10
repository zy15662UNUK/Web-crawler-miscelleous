# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:38:57 2017

@author: James
"""
'''
This is a help function for my crawler, which is to download a picture from its link and give it a name generated from random number from (1,100) 
'''

def download_web_jpg(url):
    import random
    import urllib.request
    name=random.randrange(1,100)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
