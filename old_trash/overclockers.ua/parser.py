import requests
from bs4 import BeautifulSoup

def Parsing_Main_Url1():

    #URL:   https://gtx-force.ru/sravnenie-vseh-videokart/

    s = requests.get('https://gtx-force.ru/sravnenie-vseh-videokart/')
    soup = BeautifulSoup(s.text, features="html.parser")

    urls=soup.find('table', {'class': 'easy-table easy-table-cuscosky'})\
        .findAll('a')

    write=open('urls.txt','w')

    for url in urls:
        new_url = str(url)
        new_url2 = new_url[10:new_url.find('">')]
        print(new_url2)
        write.write(new_url2+'\n')

    write.close()


def Parsing_Url1():

    # URL:   https://gtx-force.ru/sravnenie-vseh-videokart/..................

    urls = open('urls.txt','r').read().split('\n')
    main_url='https:/'

    for url in urls:
        if url!='':
            s=requests.get(main_url+url)
            print(main_url+url)
            soup = BeautifulSoup(s.text, features="html.parser")
            #print(soup)
            data = soup.find('table', {'class': 'easy-table easy-table-cuscosky'})

            print(data)


Parsing_Url1()





"""for i in range():
        s = requests.get("https://www.ivi.ru/watch/"+str(i)+"/description")
        soup = BeautifulSoup(s.text, features="html.parser")
        print("https://www.ivi.ru/watch/"+str(i)+"/description")

        if soup.find('section', {'class':'top-wrapper light'}) == None \
                and soup.find('span', {'class':'text_default'}) == None:

            tittle_raw = soup.find('div', {'class': 'title-block'}).find('h1').text
            year_raw = soup.find('div', {'class': 'properties'}).find('a', {'itemprop': 'datePublished'}).text
            categorys_raw = soup.find('div',{'class':'properties'}).find('span').findAll('a')
            actors_raw = soup.find('dd', {'itemprop': 'actor'}).findAll('a', {'itemprop': 'name'})
            rating_raw = soup.find('span',{'itemprop':'ratingValue'}).text

            if tittle_raw.startswith('Фильм') == True:
                tittle = tittle_raw[6:len(tittle_raw)]
            elif tittle_raw.startswith('Мульт') ==True:
                tittle = tittle_raw[11:len(tittle_raw)]
            else:tittle = "Null"

            year = int(year_raw)

            categorys = []

            for j in range(len(categorys_raw)):

                if len(str(categorys_raw[j].text).replace(' ','').replace('\n','')) >1:

                    now_category = str(categorys_raw[j].text).replace(' ','').replace('\n','')

                    for k in range(len(true_category)):

                        if now_category.startswith(true_category[k][0])==True:

                            new_category = true_category[k][1]

                        #now_category=new_category ??
                            categorys.append(new_category)

            actors = []

            for j in range(len(actors_raw)):

                if len(str(actors_raw[j].text).replace(' ', '').replace('\n', '')) > 1:

                    now_actor = str(actors_raw[j].text).replace('\n', '').strip()

                    actors.append(now_actor)

            rating = float(rating_raw.strip().replace(',','.'))

            film1 = MainModelClass.Film(tittle, year,categorys,actors,rating)

            print(str(film1.info()))

            ListFilm.append(film1)

        else: print("404")

return ListFilm"""