# -*- coding: utf-8
import time
import vk_api
import sys

f = open('group.html', 'r')
message = f.read()
print(message)

vk = vk_api.VkApi(login = 'myLog', password = 'myPass')
#vk_api.VkApi(token = 'a02d...e83fd') #Авторизоваться как сообщество
vk.auth()
# Будем писать Мне
user_id = '411312344'
s = message
vk.method('messages.send', {'user_id':user_id,'message':s})

if sys.argv[1] == '2':
	# 2 кKypc
	user_id = '143453697' #Lipat
	s = message
	vk.method('messages.send', {'user_id':user_id,'message':s})
if sys.argv[1] == '3':
	user_id = '208803376' #Kibirev
	s = message
	vk.method('messages.send', {'user_id':user_id,'message':s})
        user_id = '157023917' #Burba
        s = message
        vk.method('messages.send', {'user_id':user_id,'message':s})


