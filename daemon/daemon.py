# -*- coding: utf-8 -*-
import time
import vk_api
import mysql.connector
from mysql.connector import Error


###################################

def showUsers():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='bot',
                                       user='bot',
                                       password='0000')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            cursor.execute("set names utf8")
            cursor.execute("SELECT * FROM users")

            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        conn.close()

###############################################

def addUser(id, group):
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='bot',
                                       user='bot',
                                       password='0000')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            cursor.execute("set names utf8")

            query = "insert into users (`vkId`, `group`, `subscribe`) VALUES (%s,%s,%s)"
            args = (id, group, '0')
            cursor.execute(query, args)
            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            conn.commit()

    except Error as e:
        print(e)

    finally:
        conn.close()

######################################


vk = vk_api.VkApi(login = 'phone', password = 'pass')
vk.auth()

# Тело демона
while True:
    # obrabotka zayavok v drugi
	# Обрабатываем входящие заявки в друзья
    values = {'count': 1, 'out': 0}
    response = vk.method('friends.getRequests', values)
    for item in response['items']:
        print(item)
		# Подтверждаем каждую заявку
        vk.method('friends.add', {'user_id': item})
		# Записываем пользователя в БД
        addUser(str(item), 'test')
		# Отправляем пользователю сообщение с предложением получать расписание
        vk.method('messages.send', {'user_id': item,'message': 'do you need in the shedule? (answer + or - )'})


    #obrabotka soobschenii
	# Обработка входящих сообщений
    values = {'count': 1,'unread': 1}
    response = vk.method('messages.getDialogs', values)
    for item in response['items']:
        user_id = item[u'user_id']
        vk.method('messages.send', {'user_id': user_id,'message': 'lol'})
        print(item)
    time.sleep(1)

