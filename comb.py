import requests

def search(keyword):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get('https://api.proxynova.com/comb?query='+keyword,headers=headers)
    content = response.text
    return content