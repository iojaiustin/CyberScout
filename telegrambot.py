import requests
import re
import random
import telebot
import cyberscout
import threading
import argparse
import os
import logging

BOT_TOKEN = "API-KEY-HERE"

bot = telebot.TeleBot(BOT_TOKEN)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, """	  
		Hello! 
		-Perform a quick search based on a keyword using the '/trace <keyword> command'.
		-You can trace any credentials you are using. 
		-(Eg.  'john.doe@yahoo.com' , 'p@ssword123').
		"""
	)

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

@bot.message_handler(commands=['trace'])
def check(message):

	logging.info('Got a new request')
	bot.reply_to(message, "Checking"+message.text.replace("/trace","")+" now")
	content = ""

	urls = cyberscout.perform_search_cred(message.text.replace("/trace",""))
	if urls:
		content += "' "+message.text.replace("/trace","")+" 'has been seen here:\n"
		for url in urls:
			if ".onion" in url:
				content+="!CRITICAL!\n"
				content+="'"+message.text.replace("/trace ","")+"' was found in a DarkWeb page:"
			content+=url
			content+="\n"

	if re.fullmatch(email_regex, message.text.replace("/trace ","")):
		email = message.text.replace("/trace ","")
		results = cyberscout.search_breach(email.split("@")[0])
		if len(results):
			if "Warning" not in content:
				content += "!Warning!\n"
			content+="Your email was found in database breach:\n"
			for account in results:
				content += account+"\n"

	
	

	if content:
		bot.reply_to(message,content)
	else:
		bot.reply_to(message,"Congratz, you are all clear! For now...")

'''
@bot.message_handler(commands=['subscribe'])
def subscribe(message):
	bot.reply_to(message, "You subscribed! You can now use the '/add' command to add keywords to your watchlist.")
	print(str(message.from_user.id))
	file = open(str(message.from_user.id)+".txt","w")

	
@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
	bot.reply_to(message, "You unsubscribed! Stay safe until we meet again.")
	os.system("rm "+str(message.from_user.id)+".txt")


@bot.message_handler(commands=['add'])
def send_welcome(message):
	watchlist.add(str(message.text.replace("/add ","")), str(message.from_user.id))
	bot.reply_to(message, "Added" + message.text.replace("/add","") + " to your wacthlist!")
'''
bot.infinity_polling()
