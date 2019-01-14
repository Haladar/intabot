import schedule
import time


import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot(filter_users=False)
bot.login(username=args.u, password=args.p,proxy=args.proxy)



def real(userid):
	a=bot.get_user_followers(userid)
	# print(a)
	list_with_followers = []
	counter  = 0
	# f = open(file_with_followers,'r+').read().split("\n")
	for i in a :
		counter +=1
		list_with_followers.append(i)
	return list_with_followers

def prev(file_with_followers):
	list_with_followers = []
	counter  = 0
	f = open(file_with_followers,'r+').read().split("\n")
	for i in f :
		counter +=1
		list_with_followers.append(i)
	return list_with_followers
	# print("Overall names: {}".format(counter))
# userid = bot.get_user_id_from_username("allstores.uz")
userid = bot.get_user_id_from_username("cars._empire_uzb")
print(userid)
file_prev  = 'cars._empire_notified.txt'
	

def write_notified(list_with_notified_users,file_prev):
	f = open(file_prev,'a')
	for ids in list_with_notified_users:
		f.write(ids+"\n")

def ultimate(userid,file_prev):
	MESSAGE = "Thanks for joining our community.😊 Send me the destination point that you want to see in our posts👆"
	MESSAGE.encode("utf-8")
	file_with_real_followers = real(userid)
	# print(file_with_real_followers)
	file_with_notified_followers = prev(file_prev)

	welcomeMessageIds = []
	for follower in file_with_real_followers:
		if follower not in file_with_notified_followers:
			bot.send_message(MESSAGE, follower)
			welcomeMessageIds.append(follower)

	#here we  need to send welcome messages

	write_notified(welcomeMessageIds,file_prev)

	print(welcomeMessageIds)


schedule.every(5).minutes.do(ultimate,userid,file_prev)



while True:
	schedule.run_pending()
	time.sleep(1)


