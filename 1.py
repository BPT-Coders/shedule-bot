# -*- coding: utf-8 -*-
import requests

s = requests.Session()


url = "http://gbou-bpt.ru/component/user/"
payload = {'username':'student', 'passwd':'0000', 'Submit':'Войти', 'option':'com_user', 'task':'login', 'return':'L2NvbXBvbmVudC91c2VyLw==', 'bbc437ee34e2cc7ad72714c82004fc6c':'1'}
r = s.post(url, payload)
print(r.text)



#s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#r = s.get('http://gbou-bpt.ru/uheba/raspisanie/5-raspisanie.html')

#print(r.text)

#url = "http://gbou-bpt.ru/uheba/raspisanie/5-raspisanie.html"
#r = requests.get(url)

#with open("requests_results.html", "w") as f:
#    f.write(r.content)