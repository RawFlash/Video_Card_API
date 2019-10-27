from django.http import HttpResponse
from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
import sys
import os

def main2(request):

    return render(request,'test/test.html',locals())

def bots(request):

    http_proxy = "http://10.10.1.10:3128"
    https_proxy = "https://10.10.1.11:1080"
    ftp_proxy = "ftp://10.10.1.10:3128"

    proxyDict = {
        "http": http_proxy,
        "https": https_proxy,
        "ftp": ftp_proxy
    }

    s = requests.get("https://video-card-api.herokuapp.com/test", proxies = proxyDict)
    i=0
    while i<5:

        i=i+1
        s = requests.get("https://video-card-api.herokuapp.com/test", proxies=proxyDict)

    return HttpResponse("Боты сработали")

    # print('!!')
    #return HttpResponse("Тестовая страница)")