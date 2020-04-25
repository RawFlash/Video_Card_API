# https://khashtamov.com/ru/postgresql-python-psycopg2/

import sys
import os
import psycopg2

def db(str):
    conn = psycopg2.connect(dbname='d94el3l37f2tku', user='dmmwocuvzyhiqo',
                            password='eaf0da154ee699b500f565fa6c4e7aa91cf5c550b2a20bfdae00f7b5106e1516',
                            host='ec2-174-129-33-176.compute-1.amazonaws.com')
    conn.autocommit = True
    cursor = conn.cursor()

    # cursor.execute('SELECT * FROM engine_airport WHERE city_code = %(city_code)s',
    #                   {'city_code': 'ALA'})

    # cursor.execute(
    """CREATE TABLE users (id SERIAL PRIMARY KEY,
    Title CHAR(64),
    GPUName CHAR(64),
    GPUVariant CHAR(64),
    Architecture CHAR(64),
    ProcessSize CHAR(64),
    Transistors CHAR(64),
    DieSize CHAR(64),
    ReleaseDate CHAR(64),
    Generation CHAR(64),
    Production CHAR(64),
    BusInterface CHAR(64),
    GPUClock CHAR(64),
    MemoryClock CHAR(64),
    MemorySize CHAR(64),
    MemoryType CHAR(64),
    MemoryBus CHAR(64),
    Bandwidth CHAR(64),
    PixelShaders CHAR(64),
    VertexShaders CHAR(64),
    TMUs CHAR(64),
               ROPs CHAR(64),
                  PixelRate CHAR(64),
                 TextureRate CHAR(64),
                  SlotWidth CHAR(64),
                  TDP CHAR(64),
                  Outputs CHAR(64),
                  BoardNumber CHAR(64),
                   DirectX CHAR(64),
                  OpenGL CHAR(64),
                 OpenCL CHAR(64),
                 Vulkan CHAR(64),
                 PixelShader CHAR(64),
                 VertexShader CHAR(64),
                 LaunchPrice CHAR(64),
                  Foundry CHAR(64),
                  PowerConnectors CHAR(64),
                 VertexRate CHAR(64),
                Length CHAR(64),
                ShaderModel CHAR(64),
                  ShadingUnits CHAR(64),
                  ComputeUnits CHAR(64),
                  FP32performance CHAR(64),
                  BoostClock CHAR(64),
                FP64performance CHAR(64),
                 FP16performance CHAR(64),
                 ShaderClock CHAR(64),
                  SMCount CHAR(64),
                 CUDA CHAR(64),
                 SMXCount CHAR(64),
                 SMMCount CHAR(64),
                 TensorCores CHAR(64),
                  RTCores CHAR(64),
                 Manufacturer CHAR(64));"""
    # )

    # cursor.execute("INSERT INTO users (login, password) VALUES ('abc', '123456');")

    #cursor.execute(
    #    "SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema','pg_catalog');")
    #records = cursor.fetchall()
    #print(records)

    #cursor.execute("SELECT * FROM users;")
    #records = cursor.fetchall()
    #print(records)

    cursor.execute(str)
    try:
        records = cursor.fetchall()
        print(records)
    except:
        None

    # cursor.fetchone() — возвращает 1 строку
    # cursor.fetchall() — возвращает список всех строк
    # cursor.fetchmany(size=5) — возвращает заданное количество строк

    cursor.close()
    conn.close()


def update_db():

    direct = ((sys.path[0]) + '\\parser\\video_card\\')
    files = os.listdir(direct)
    for file in files:
        ParametrsList = dict()
        print("Read file: " + file.title())
        read = open(direct + file, 'r').read().split('\n')
        Title = file[:-4]
        ParametrsList["Title"] = Title
        for i in list(range(0, len(read), 2)):
            if read[i] != '':
                ParametrsList[read[i]]=read[i+1]
        str0 = "INSERT INTO videocard ("
        str1=""
        str2=""
        i=0
        for par in ParametrsList.keys():
            if(i!=ParametrsList.keys().__len__()-1):
                str1 = str1 + par+", "
                str2 = str2 + "'" + ParametrsList.get(par, "N/A")+"', "
            else:
                str1 = str1 + par
                str2 = str2 + "'" + ParametrsList.get(par, "N/A")+"'"
            i = i + 1
            str1 = str1.replace("(float)","").replace("(double)","").replace("(half)","")
        db(str0+str1+") VALUES ("+str2+");")
        print("Query: "+str0+str1+") VALUES ("+str2+");")
        print("Add videocard "+ Title+"\n")



        #ЗАПРОС В БД ПО ПАРАМЕТРАМ
def request_db(par, val):
    db(
        "SELECT * FROM videocard WHERE "+par+" ='"+val+"';")




#db("SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema','pg_catalog');")

#db("DELETE FROM videocard")
#db("DROP TABLE users")
#update_db()


#НА HEROKU СВОЯ СИСТЕМА ОБРАБОТКИ ФАЙЛОВ, ЭТА ПАДАЛЬ УДАЛЯЕТ ФАЙЛЫ НЕОПИСАННЫЕ В ПРОЕКТЕ, ПОЭТОМУ НЕЛЬЗЯ ДЕЛАТЬ БАЗУ НА SQLITE
#ПЕРЕВЕЛ ВСЕ НА POSTGRESQL, НО МОДУЛИ ДЛЯ АВТОМАТИЧЕСКОГО ОБНВЛЕНИЯ Я ПИЛИТЬ НЕ ХОЧУ, ПОЭТОМУ ДАННЫЕ ЗАНОСЯТСЯ ТОЛЬКО С ЛОКАЛЬНОГО СЕРВЕРА
#ЭТОТ СКРИПТ ДЛЯ ПЕРЕНОСА ДАННЫХ ИЗ .TXT В БАЗУ НА POSTGRESQL НА СЕРВЕРЕ HEROKU



