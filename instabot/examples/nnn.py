import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot
try:
    input = raw_input
except NameError:
    pass

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)


def info(ids=None):
	#gives all info about id after being converted from username
	if  not ids:
		uname=input("enter username:  ")
		#information=open("{}.txt".format(uname),'w')
		user_id=bot.convert_to_user_id(uname)
		info=bot.get_user_info(user_id)
		
	else:
		info=bot.get_user_info(ids)
	return info



def email(mass=False,list_of_ids=None):
	#if by default then 1 output
	#if no then like a list
	#needs to be revides->useless 1 option
	if mass==False and list_of_ids==None:
		infos=info(ids=False)
		for key, val in infos.items():
			if key=="public_email":
				data="{}:{}".format(key,val)
				return data
	else:

		list_of_emails=[]
		for i in list_of_ids:
			infos=info(ids=i)
			for key, val in infos.items():
				if key=='username':
					uname=val
			for key, val in infos.items():
				if key=="public_email":
					data="{} : {}".format(uname,val)
					list_of_emails.append(data)
		return list_of_emails


def menu(list_):
	#give is a choice to get 1 all info or only emails
	#Needs to be more developed->phones,cities,country,is_business etc
	answer=int(input("Enter 1 to see all data:  \nEnter 2 to see only email:  \n"))
	if answer==1:
		pivot=info()
		print(pivot)
	elif answer==2:
		mail=email(mass=True,list_of_ids=list_)
		return mail


def filereader(txtfile):
	#makes ids from txt file 
	fileobj= open(txtfile,'r').read().split('\n')
	ids=[]
	for i in fileobj:
		ids.append(i)
	return ids

a=filereader('gymshark.txt')
all_emails=menu(a)
print(a)
with open("all_emails.txt",'w') as file:
	for item in all_emails:
		file.write(item+"\n")


#beauty_email=email()
#print(beauty_email)