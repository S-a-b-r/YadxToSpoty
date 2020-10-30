import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
url = 'https://music.yandex.ru/users/pofastygrisha/tracks'#url Странички с музыкой
uClient = uReq(url)
page_html = uClient.read()#Считываем html страницу
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("a",{"class" : "d-track__title"})#В переменной containers лежат объекты html, в которых содержатся названия песен
containers_groups = page_soup.findAll("span",{"class" : "d-track__artists"})#В переменной containers_groups лежат объекты html, в которых содержатся названия групп

list_titles = [] #Массив с названиями песен

#Заполняем массив
for i in range(len(containers)):
    list_titles.append(str(containers[i]))
    list_titles[i] = list_titles[i].split("<")[1]
    list_titles[i] = list_titles[i].split(">")[1]

list_groups = [] #Массив с названиями групп

#Заполняем массив
for i in range(len(containers_groups)):
    list_groups.append(str(containers_groups[i]))
    list_groups[i] = list_groups[i].split("<")[2]
    list_groups[i] = list_groups[i].split(">")[1]

#создаем фаил text.txt
f = open('text.txt', 'w')

#Заполняем фаил названиями песен с группами
for i in range(len(list_titles)):
    f.write(list_titles[i] +" - "+ list_groups[i] +'\n')

print("ready")

