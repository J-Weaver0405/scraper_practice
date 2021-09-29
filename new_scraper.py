import csv 
from bs4 import BeautifulSoup
import requests
import os


"""
run interactively with python3 -i new_scraper.py to 
play around with the code
"""
from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'

html = requests.get(URL)
bs = BeautifulSoup(html.text, 'html.parser')
page_counter = 1

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')
for post in soup.findAll('tr', {'class': 'athing'}):
    print(post)