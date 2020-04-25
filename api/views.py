from django.http.response import JsonResponse
import psycopg2
from django.http import HttpResponse
from api import  models as model

import sys
import os



def json(request):
    raw_parameters = request.GET
    parameters={}

    #Создаю лист с параметрами
    for p in raw_parameters:
        parameters.update({p:raw_parameters.get(p)})

    #Если это один параметр и это имя или айди, то я ищу одну карту
    if parameters.__len__()==1 and \
            ('title' in parameters.keys() or 'id' in parameters.keys()):
        print("Count parameters: 1")

        #raw_VC это сырые данные из базы, их надо отформатировать по модели
        raw_VC = search_VC1(parameters)
        VC = model.rawVC_to_ConvVC(raw_VC[0])
        data = model.return_all(VC)
        for v in data.values():
            v = str(v).rstrip()
        #print(data.items())
        return JsonResponse(data)
    #Иначе ищу несколько видеокарт с помощью фильров, поэтапно отсеивая параметры и видеокарты
    else:
        Titles_VC = search_VC2(parameters)
        data={}
        data.update({"VideoCards":Titles_VC})
        return JsonResponse(data)


#ПОИСК ПО ОДНОМУ ПАРАМЕТРУ   id  ИЛИ  Title
def search_VC1(parametrs):
    VC=""
    for p in parametrs:
        VC=db("SELECT * FROM videocard WHERE "+p+" ='"+parametrs.get(p)+"';")
    return VC


#Поиск по нескольким параметрам
def search_VC2(parametrs):
    list_VC=[]
    first_search=True
    for p in parametrs:
        if first_search==True:
            first_search=False
            list_VC=request_db(p,parametrs.get(p))
        else:
            list_VC = list_VC_update(list_VC, request_db(p,parametrs.get(p)))
    return_list=[]
    for vc in list_VC:
        return_list.append(model.rawVC_to_ConvVC(vc).Title.rstrip())
    return return_list


def db(str):
    conn = psycopg2.connect(dbname='d94el3l37f2tku', user='dmmwocuvzyhiqo',
                            password='eaf0da154ee699b500f565fa6c4e7aa91cf5c550b2a20bfdae00f7b5106e1516',
                            host='ec2-174-129-33-176.compute-1.amazonaws.com')
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(str)
    try:
        records = cursor.fetchall()
        return records
    except:
        None

    cursor.close()
    conn.close()

def request_db(par, val):
    return db("SELECT * FROM videocard WHERE "+par+" ='"+val+"';")



def list_VC_update(first_list,second_list):
    list=[]
    for a in first_list:
        for b in second_list:
            if a==b:
                list.append(a)
    return list

def full(request):
    full_db_raw = db('SELECT * FROM videocard')
    video_cards=[]
    for note in full_db_raw:
        video_cards.append(model.return_all(model.rawVC_to_ConvVC(note)))
    for video_card in video_cards:
        for v in video_card.values():
            v = str(v).rstrip()

    return JsonResponse(video_cards,safe=False)