import requests
import re
import random
import telebot
import watchlist
import cyberscout
import os

BOT_TOKEN = "6333473690:AAEL-L2hH8zaaEf8DHLMkR_TlXl3US3FWWI"
bot = telebot.TeleBot(BOT_TOKEN)
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def send_notification(userId,message):
    url = "https://api.telegram.org/bot6333473690:AAEL-L2hH8zaaEf8DHLMkR_TlXl3US3FWWI/sendMessage"
    payload = '{"chat_id": "'+userId+'", "text": "'+message+'", "disable_notification": false}'
    headers = {'content-type': 'application/json'}
    r = requests.post(url,data=payload,headers=headers)

def notify():
    for file in os.listdir("users"):
        userId = file.replace(".txt","")


def check(query):
    content = ""

    urls = cyberscout.perform_search_cred(query)
    if urls:
        content += "' "+query+" 'has been seen here:\n"
        for url in urls:
            if ".onion" in url:
                content+="!CRITICAL!\n"
                content+="'"+query+"' was found in a DarkWeb page:"
            content+=url
            content+="\n"

    if re.fullmatch(email_regex, query):
        email = query
        results = cyberscout.search_breach(email.split("@")[0])
        if len(results):
            if "Warning" not in content:
                content += "!Warning!\n"
            content+="Your email was found in database breach:\n"
            for account in results:
                content += account+"\n"
				
    return content


print(check("cc100best"))