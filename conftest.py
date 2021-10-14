import pytest
from new_scraper import *

# add test fixtures for scraper

@pytest.fixture
def page_request(): 
    URL = 'https://news.ycombinator.com/'
    res = requests.get(URL)
    return res
    
@pytest.fixture
def title_request(): 
    title = post.find('a', {'class':'storylink'}).get_text()
    res = titles.append(title)
    return res
    
@pytest.fixture
def author_names():
    author = post.find('a', {'class':'hnuser'})
    res = author.get_text()