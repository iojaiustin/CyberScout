import requests
import re
import random
import telebot
import watchlist
import cyberscout
import threading
import os

BOT_TOKEN = "6333473690:AAEL-L2hH8zaaEf8DHLMkR_TlXl3US3FWWI"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, """	  
		Hello! 
		-Add keywords to your watchlist by using the '/add <keyword> command'. 
		-Perform a quick search based on a keyword using the '/check <keyword> command'.
		-You can track any softwares, technologies or credentials you are using. 
		-(Eg. 'Garmin' , 'john.doe@yahoo.com' , 'p@ssword123').
		-Use the '/about' command to learn more about how I work."""
	)

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

@bot.message_handler(commands=['check'])
def check(message):
	bot.reply_to(message, "Checking"+message.text.replace("/check","")+" now")
	content = ""

	urls = cyberscout.perform_search_cred(message.text.replace("/check",""))
	if urls:
		content += "' "+message.text.replace("/check","")+" 'has been seen here:\n"
		for url in urls:
			if ".onion" in url:
				content+="!CRITICAL!\n"
				content+="'"+message.text.replace("/check ","")+"' was found in a DarkWeb page:"
			content+=url
			content+="\n"

	if re.fullmatch(email_regex, message.text.replace("/check ","")):
		email = message.text.replace("/check ","")
		results = cyberscout.search_breach(email.split("@")[0])
		if len(results):
			if "Warning" not in content:
				content += "!Warning!\n"
			content+="Your email was found in database breach:\n"
			for account in results:
				content += account+"\n"

	
	

	if content:
		bot.reply_to(message, content)
	else:
		bot.reply_to(message, "Congratz!\nYou are all clear :)")

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

bot.infinity_polling()