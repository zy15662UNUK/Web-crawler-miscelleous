# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:38:57 2017

@author: James
"""


def download_web_jpg(url):
    import random
    import urllib.request
    name=random.randrange(1,100)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
