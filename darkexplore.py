import requests
import re

def get_links(query):
    url = "https://ahmia.fi/search/?q="+query
    response = requests.get(url)
    regex = "\w+\.onion"
    found_links = re.findall(regex,response.text)[:70]
    links = []
    for link in found_links:
        if link not in links and "@" not in query:
            links.append(link)

    return links