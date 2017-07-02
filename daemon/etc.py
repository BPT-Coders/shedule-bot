# -*- coding: utf-8 -*-
import time
import vk_api

def firstMess(userId, userMess):
    #print("user`s message:")
    #userMess = input()
    print(userMess)
    if userMess == '+rasp':
        print("ok")
        write_msg(userId, u'ok')
        askGroup(userId)
    else:
        write_msg(userId, u'idi v')
        firstMess(userId, userMess)
        
def askGroup(userId):
    print("enter your group:")
    write_msg(userId, u'enter your group:')
    t = ["3-4TP", "5-6DP", "7-8DP"]
    #group = input()
    if (t.count(group) > 0):
        write_msg(userId, u'yes')
    else:
        write_msg(userId, u'no')
        askGroup(userId)

vk = vk_api.VkApi(login = 'phone', password = 'pass')
#vk_api.VkApi(token = 'a02d...e83fd') #Авторизоваться как сообщество
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            firstMess(item[u'user_id'], item[u'body'])
            #write_msg(item[u'user_id'],u'Hello')
    time.sleep(1)
