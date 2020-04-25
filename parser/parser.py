'''
Парсер должен проходить по всем видеокартам на сайте
http://www.techpowerup.com/gpu-specs/

V1
Первоначально все ссылки делились по фирмам и годам, ссылки хранились в текстовых файлах
Сначала данные структурируются и записываются в текстовые файлы, откуда они считывались и записывались в базу
Текстовые файлы неудобны для хранения большого количества информации
Решил заменить на Json файл
'''

import requests
from bs4 import BeautifulSoup
import sys
import os
from datetime import  datetime


#Импортирует стандартную модель видеокарт
from api.models import VideoCard

def Parsing_Url_Videocard_Main():

#Достает из файла "MANUFACTURER" cписок всех производителей видеокарт
#Используется для перебора URL


    url_firm=open("MANUFACTURER.txt","r").read().split("\n")

    #Парсит все урлы с картами всех производителей начиная с 1986 г
    #Проверяет, если в год ничего не выпускалось, не парсит страницу
    #+парсит по годам
    #тк сайт не может вывести больше 100 урлов карт за раз

    #URL:   http://www.techpowerup.com/gpu-specs/

    for firm in url_firm:

        #Создает список из URL для парсинга из названия фирмы и года
        #С 1986 по наш год



        year = 1986

        now = datetime.now()

        url_year_read = list

        while year!=now.year+1:
            url_year_read.append(r"https://www.techpowerup.com/gpu-specs/?mfgr="+firm+r"&released="+str(year)+r"&sort=name")
            year+=1

        """
        #Директория для выбора файла для парсинга
        #В этих файла URLы типа
        # https://www.techpowerup.com/gpu-specs/?mfgr=NVIDIA&released=2019&sort=name

        dop_dir=r'urls_firm+year\''

        #Лист со всеми URLми производителя

        url_year_read=open(dop_dir[0:-1]+'urls_'+firm+'+year.txt','r').read().split('\n')
        """

        #Перебор по этим URLам

        for url_year in url_year_read:

            #Если он не пустой
            #Последняя строка в .txt пустая

            if url_year!='':

                #Запрос на сайт по URL

                s = requests.get(url_year)

                #Парсер страницы

                soup = BeautifulSoup(s.text, features="html.parser")

                #Проверка, если не существует видеокарт данного года от данного производителя
                #Предохранение от стрельбы в колено
                #Если на сайте есть надпись об отсутствии видеокарт, то переходим к следующей итерации
                #Если все нормально, продолжаем работать со списком видеокарт

                try:

                    if soup.find('table', {'class': 'processors'}).find('td',{'colspan':8}) == False:
                        None

                except:

                    continue

                else:

                    #Вытаскивает данные из списка названий видеокарт

                    data = soup.find('table', {'class': 'processors'}).findAll('a')

                    #Цикл с методом парсинга данных со страницы с видеокартой

                    for i in data:

                        #а - строковое представление URL

                        a = str(i)

                        #Создает нормальный URL для запроса страницы карты
                        #Из данных спарсенных из таблицы видеокарт

                        url = 'http://www.techpowerup.com' + a[9:a.find('">')]

                        #print(url)

                        Parsing_Url_Videocard(url,firm)

    '''#url_year_read=open("nvidia+year_urls.txt",'r').read().split('\n')

    for url_year in url_year_read:
        s = requests.get(url_year)
        soup = BeautifulSoup(s.text, features="html.parser")

        data = soup.find('table',{'class':'processors'}).findAll('a')

        for i in data:
            a=str(i)
            url='http://www.techpowerup.com'+a[9:a.find('">')]
            print(url)

            Parsing_Url_Videocard(url)



        #print(data)
    #s = requests.get('https://gtx-force.ru/sravnenie-vseh-videokart/')
    #soup = BeautifulSoup(s.text, features="html.parser")'''

def Parsing_Url_Videocard(url, firm):

    #Входит URL конкретной видеокарты и фирма


    #Создает название видеокарты из ссылки

    title_card_=url.replace('.com','tt')
    title_card=title_card_[35:title_card_.find('.c')]

    #print(title_card)



    '''
    #Создает текстовый файл с данными о видеокарте
    write = open("video_card/" + title_card+'.txt', 'w')
    '''

    #Запрос на сервер по URL конкретной видеокарты
    s=requests.get(url)

    #Парсит HTML
    soup=BeautifulSoup(s.text,features='html.parser')

    #Все таблицы с данными о видеокарте
    data=soup.find('div',{'class':"sectioncontainer"}).findAll('dl',{'class':'clearfix'})

    #Лист с свойствами видеокарты
    parametrs = list

    #Лист с значениям свойств видеокарты
    values = list

    for i in data:
        #Форматирование всех данных к нормальному виду
        parametr=str(i.dt.text).replace(' ','').replace('\n','').replace('\t','')
        value = str(i.dd.text).replace(' ', ' ').replace('\n', '').replace('\t', '').replace('²','^2')

        #Вывод параметра
        #Вывод значения
        print(parametr)
        print(value)

        '''
        #Запись всех данных в файл с видеокартой
        write.write(parametr+'\n')
        write.write(value+'\n')
        '''

        parametrs.append(parametr)
        values.append(value)

    parametrs.append("firm")
    values.append(firm)
    #Сохранение в джейсон доделать



# ХЗ че за метод
#Вроде для вывода всех данных

def Print_parametrs():
    #print(sys.path)
    direct =(str(sys.path[0])+'\\video_card')
    #sys.path.append(direct)
    print(direct)
    files = os.listdir(direct)
    print(files)
    parametrs=[]
    for file in files:
        #director=(r'\video_card\'')[0:-1]
        #print(director)
        path=r'\\'
        read = open(direct+path+file, 'r').read().split('\n')
        #print(read)
        #read=open(director+str(file),'r').read().split('\n')
        i=0
        for i in list(range(0,len(read),2)):
            if read[i].find('(')!=-1:
                serch_str = read[i][read[i].find('('):read[i].find(')') + 1]
                read[i]=read[i].replace(serch_str,'')

            print(read[i])
            if read[i] in parametrs:
                None
            elif read[i]=='' or read[i]=='\n':
                None
            else:
                parametrs.append(read[i])
    print("!!!!!!!!")

    write=open('parametrs.txt','w')

    for p in parametrs:
        print(p)
        write.write(p+'\n')
    write.close()


#Метод для определения максимальной длины значения всех параметров
#Делал чтоб определить какой тип данных использовать в БД
def Max_length():
    #print(sys.path)
    direct =(str(sys.path[0])+'\\video_card')
    #sys.path.append(direct)
    print(direct)
    files = os.listdir(direct)
    print(files)
    for file in files:

        path=r'\\'
        read = open(direct+path+file, 'r').read().split('\n')

        max_length=''
        for i in list(range(1,len(read),2)):
            print(read[i])
            if len(read[i]) >len(max_length):
                max_length=read[i]

    print("!!MAX_LENGTH!!"+max_length)
    print(len(max_length))

#Тестовая функция
def test ():
    print("Work")

#def UpdateDB():
    #VideoCard.



#Max_length()

#Print_parametrs()

#Parsing_Url_Videocard_Main()

#Parsing_Url_Videocard("http://www.techpowerup.com/gpu-specs/geforce-mx230.c3350")