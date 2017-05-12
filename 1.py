# -*- coding: utf-8
 
#импорт необходимых библиотек
import subprocess
import urllib
import urllib2
import cookielib
import re
import string
 
host = 'http://gbou-bpt.ru/'
user = 'student'
pasw = '2011'
 
#подготовка опенера с функцией обработки кукисов
CookieJar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar))
 
#запрос страницы авторизации
conn = urllib2.Request(host + '/component/user/')
page = opener.open(conn).read()
 
#получаем скрытые поля
params = re.findall(r'name="([^"]+)" value="([^"]+)"', page)
 
#Предварительная подготовка параметров для отправки POST-запроса
params.append( ('username', user) )
params.append( ('passwd', pasw) )
params.append( ('remember', 'yes') )
params.append( ('Submit', 'Войти') )
params.append( ('option', 'com_user') )
params.append( ('task', 'login') )
buf = {}
ident = ''
for param in params:
    buf[param[0]] = param[1]

# Отправляем подготовленные параметры
post = urllib.urlencode(buf)
conn = urllib2.Request(host + 'component/user/', post)
page = opener.open(conn).read()
#print(page)

# Считываем значение поля return, выполняющего роль тока
params = re.findall(r'name="([^"]+)" value="([^"]+)"', page)
buf = {}
buf[params[2][0]] = params[2][1]
#print(buf)

# Запрашиваем страницу с расписанием, сообщая токен
post = urllib.urlencode(buf)
conn = urllib2.Request(host + 'uheba/raspisanie/5-raspisanie.html', post)
page = opener.open(conn).read()
#print(page)

#Сохраняем файл
with open("requests_results.html", "w") as f:
    f.write(page)
subprocess.call('cp requests_results.html archive/`date +%Y-%m-%d`.html', shell=True)

subprocess.call('php index.php 2', shell=True)
subprocess.call('python 2.py 2', shell=True)
subprocess.call('php index.php 3', shell=True)
subprocess.call('python 2.py 3', shell=True)
