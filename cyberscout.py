import re
import json
import darkparse
import vulncheck
import darkexplore
import requests
import comb
from cybernews.cybernews import CyberNews
from googlesearch import search
from bs4 import BeautifulSoup

content = ""
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def perform_search_cred(query):
    urls = []
    results = search(query,"pastebin.com")
    if results:
        for link in results:
            urls.append(link)

    results = search(query,"doxbin.com")
    if results:
        for link in results:
            urls.append(link)

  
    dark_results = darkexplore.get_links(query)
    if dark_results:
        for link in dark_results:
            if "zerdg.onion" not in str(link):
                urls.append(str(link))

    return urls



def search_breach(query):
    results = []
    response = comb.search(query)
    if '{"count":0' not in response:
        res = json.loads(response)
        for link in res['lines']:
            if str(link) not in results:
                results.append(link)

    return results

'''
def search_software():
    response = requests.get("https://cyware.com/category/cyber-security-news-articles")
    content = response.text
    
    #soup = BeautifulSoup(content,"lxml")
    #articles = soup.find_all("h1",class_="cy-card__title m-0 cursor-pointer pb-3")
    #print(articles)
    
    #content = content.split('>')
    #for article in content:
    #    print(article)
'''