import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def add(query,user_id):
    file = open(user_id+".txt","a")
    file.write(query+"\n")
    file.close()