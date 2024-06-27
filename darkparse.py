import requests
import re
import darkexplore
import itertools

def get_tor_session(urls):
    session = requests.session()
    session.proxies = {'http':'socks5h//127.0.01:9050','https':'socks5h://127.0.0.1:9050'}
    
    #response = session.get()

'''
def validate():
    pattern1 = r"(\d{4})(-?)(\d{4})(\2\d{4}){2}"
    pattern2 = r"((\d)(?!\2{3})){16}"

    for elt in tests:
        if re.match( pattern1, elt):
            print("example has dashes in correct place")
            elt = elt.replace("-", "")
            if re.match(pattern2, elt):
                print("...and has the right numbers.")
'''