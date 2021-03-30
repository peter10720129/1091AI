# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:53:36 2021

@author: ASUS
"""
import os


os.chdir('D:/peter/1092/bigdata/leetcode') 


print( os.getcwd() ) 


#%%%

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time



#%%%


import csv
from bs4 import BeautifulSoup

with open('output.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['rank', 'name', 'attend', 'nationality', 'web'])
  

    for i in range(1,11) :
    
        options = Options()
        options.add_argument("--disable-notifications")
         
        chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
        
        
        site = "https://leetcode.com/contest/globalranking/" + str(i) + "/" 
        
        chrome.get(site)
         
        
        soup = BeautifulSoup(chrome.page_source, "html.parser" )
        
        posts = soup.find_all("div", class_ = "ranking-row")
        
        
        leetcode = "https://leetcode.com"
    
    
      
        for post in posts:
            rank = post.find("div", class_ = "ranking col").text
            
            ids = post.find('a' , class_ ="user col clickable")
        
          
          
            name = post.find( "div" , class_ = "username user-color-legendary" )
            
            if name == None :
              name = post.find( "div" , class_ = "username" )
            
            name = name.text
         
            attend = post.find( "div", class_ = "info" ).text
              
            
            nationality = post.find( "span", class_="country-name" )
            
            if nationality != None : nationality = nationality.get("data-original-title") 
            
         
            web = ids.get('href')
            
            if web.find("https") == -1 :
                web = leetcode + web 
                
            writer.writerow([rank, name, attend, nationality, web ])
        






#%%

with open('weekly_233.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['rank', 'name', 'attend', 'nationality', 'web'])
  

    options = Options()
    options.add_argument("--disable-notifications")
     
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    
    
    site = "https://leetcode.com/contest/weekly-contest-233/ranking/"
    
    
    chrome.get(site)
    soup = BeautifulSoup(chrome.page_source, "html.parser" )

    
   
    
    posts = soup.find("tbody")
    

    trs = soup.find_all("tr")
    
    for tr in trs :
        tds = soup.find_all("td")
        i = 0 
        for td in tds :
          i += 1 
          print( str(i) + " " + td.text )        
 
