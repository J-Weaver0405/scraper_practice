import csv 
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import sqlite3




"""
run interactively with python3 -i new_scraper.py to 
play around with the code
"""


URL = 'https://news.ycombinator.com/'
html = requests.get(URL)
bs = BeautifulSoup(html.text, 'html.parser')

page_counter = 1
page_max = 2
posts = []


res = requests.get(URL)

soup = BeautifulSoup(res.content, 'html.parser')
titles = []
authors = []

for post in soup.findAll('tr', {'class': 'athing'}):
    title = post.find('a', {'class':'storylink'}).get_text()
    titles.append(title)
    
    for post in soup.findAll('td', {'class': 'subtext'}):
        author = post.find('a', {'class':'hnuser'})
        if author:
            print(author.get_text())
            authors.append(author.get_text())
            
    """
    Dataframe to SQL
    """
posts = zip(titles, authors)
df = pd.DataFrame(posts,columns=['story','author'])
df.to_csv('quote_list.csv')

conn = sqlite3.connect('Scraper.db')
c = conn.cursor()

df.to_sql('Hacker_news', conn, if_exists='replace',index = True)
conn.commit()

print(c.execute('select * from Hacker_news').fetchall())

