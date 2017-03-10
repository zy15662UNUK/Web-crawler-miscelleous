# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:25:17 2017

@author: James
"""
'''
This is a help function for my crawler, which is to download and manipulate an online CSV file with its link.
'''
from urllib import request
def download_csv_stock_data_from_web(csv_url):
    response= request.urlopen(csv_url)#connect python to the internet and open the given link
    csv=response.read()#open a file and load that file into a variable called 'csv'
    csv_str=str(csv)#convert all the stuff in the file into string
    lines=csv_str.split('\\n')#spilt in to lines
    dest_url=r'sinopec.csv'# get a file name
    creatFile=open(dest_url,'w')#create or write a file named sinopec.csv
    for line in lines:
        creatFile.write(line+'\n')#write in line and take 
    creatFile.close()#remember to close the file after writting
    
 '''
to read the file downloaded, first open the file
text=open('sinopec.csv','r')
then read the file:
readout=text.read()
 '''       
    
    
