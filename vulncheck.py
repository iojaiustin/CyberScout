import requests
import re
import datetime
import newsdataapi

def get_vulns(keyword):
    response = requests.get("https://cxsecurity.com/cvemap/")
    if keyword in response.text:
        cves_found = response.text.split("<BR>")
        
        for element in cves_found:
            if keyword in element:
                cve = str(element)

        return cve
    
    else:
        print(keyword+" is  safe today!")

def get_link(content):
    vulnerability_details = content
    link = vulnerability_details[:vulnerability_details.index("title")]
    link = link.replace('<A href="','')
    link = link.replace('"','')
    return link

def get_description(content):
    return content.split('"')[3]

def get_cveid(content):
    return get_link(content).split('/')[4]


def check(list):
    result = ''
    if str(datetime.date.today()) in requests.get("https://cxsecurity.com/cvemap/").text:
        for element in list:
            content = get_vulns(element)
            if content:
                result += "A vulnerability was published today for '"+element+"':"+get_cveid(content)+"\n"
                result += get_description(content) + "\n"
                result += "More details here: "+get_link(content) + "\n"
            else:
                result += "Your technologies are safe today!\n"

    else:
        result += "No vulnerabilities reported for today!"
    
    return result

def check_news(keyword):
    api = newsdataapi.NewsDataApiClient(apikey="pub_31322e6d92c8d0cdc8bbf1a9a37aefcc76762")
    response = api.news_api(q="cybersecurity")
    content = ''
    for result in response['results']:
        if str(datetime.date.today()) in result['pubDate']:
            if keyword in result['title']:
                content += result['title']
                content += '\n'
                content += 'Check it here: ' + result['link']
    return content
