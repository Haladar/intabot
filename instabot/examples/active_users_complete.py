import os
import sys
import argparse

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot



usrname= "delicious._empire"
pssword = "hayot1998d"

############
username="travel._empire"
#########3##3

bot = Bot()
bot.login(username=usrname, password=pssword)

def get_last_user_medias(username):
    user_id=bot.get_user_id_from_username(username)
    last_user_med=bot.get_last_user_medias(user_id,10)
    return last_user_med

def myID(username):
    return bot.get_user_id_from_username(username)



last_user_med=get_last_user_medias(username)
f=open('txts/likers/{}.txt'.format(username),'a')
counter=0
for i in last_user_med:
    list_of_likers=bot.get_media_likers(i)
    for j in list_of_likers:
        f.write(j+"\n")
        counter+=1
f.close()
print(last_user_med)
print("Overall written:{}".format(counter))


def find_active(dictionary,active_index):
    new_dictionary={}
    for ids,val in dictionary.items():
        if val>active_index:
            new_dictionary[str(ids)]=val
    return new_dictionary

def convert_to_ids_from_file(file):
    input_file=file
    file=open('txts/bot/likers/{}.txt'.format(input_file),'r').read().split('\n')
    final_list=[]
    for ids in file:
        #final_list.append(ids)
        final_list.append(ids)
    return final_list

def save_duplicates(new_list):
    duplicates={}
    for i in new_list:
        k=0
        for j in new_list:
            if j==i:
                k+=1
        duplicates[str(i)]=k
    return duplicates
def write_active_users_to_file(file,message):
    #file=input("enter the file name search from:  ")
    file1=convert_to_ids_from_file(file)
    duplicated=save_duplicates(file1)
    active=find_active(duplicated,2)
    #print(active)
    counter=0
    with open('txts/bot/active_likers/{}.txt'.format(file),'w') as fo:
        for key,val in active.items():
            counter+=1
            fo.write(key+'\n')
        # bots.send_message(message.chat.id, "Active users written: {}".format(counter))
        print("Active users written: {}".format(counter))


# username = str(input("enter the username:  "))
write_active_users_to_file(username,username)
print("Active liker are written to file")

####################    Follow script      ##############

bot = Bot(filter_users=False)

####INPUT OF THE TAEGET USERNAME#####
uname=username
print(uname)
#####################################
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")


args = parser.parse_args()

def convert_to_ids_from_file(file):

    files=open('txts/bot/active_likers/{}.txt'.format(file),'r').read().split('\n')
    final_list=[]
    for ids in files:
        #final_list.append(ids)
        final_list.append(ids)
    return final_list

users_to_follow=convert_to_ids_from_file(uname)

print(users_to_follow)

if not users_to_follow:
    exit()
else:
    print("Found %d users in file." % len(users_to_follow))

bot.login(username=args.u, password=args.p,proxy=args.proxy)

# bot.follow_users(users_to_follow)