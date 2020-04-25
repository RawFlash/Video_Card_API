from django.http import HttpResponse
from django.shortcuts import render


url = 'https://video-card-api.herokuapp.com/test'




def main(request):
    return render(request,'index.html')



""" Эксперементы с ТОР и ботами
import random
import http.client
#import tor.tor
import time
import socks
import socket



user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

def bots(request):

    print(request)

    http_proxy = "http://194.62.145.248:8080"
    https_proxy = "https://194.62.145.248:8080"
    ftp_proxy = "10.10.1.10:3128"

    proxiesD = {
        "http": "http://194.62.145.248:8080",
        "https": "https://194.62.145.248:8080"
    }

    socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    socket.socket = socks.socksocket

    print('!!')
    for i in range(1, 10):
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}

        s= requests.get(urltestip,headers = headers) #,proxies=proxiesD)
        t = random.randint(0,3)
        print('request: Number:'+ str(i) +', break:'+ str(t)+
              str(s.content) )
        time.sleep(t)


    return HttpResponse("Боты сработали")

def Torbots(request):


    session = requests.session()


    r = session.get(url)
    print(r.text)

    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9150'
    session.proxies['https'] = 'socks5h://localhost:9150'

    for i in range(1, 10):
        r = session.get(url)
        #print(r.text)
        #t = random.randint(0, 3)
        #print('request: Number:' + str(i) + ', break:' + str(t))
        print('request: Number:' + str(i) + ', break: 10' + str(session.proxies))
        time.sleep(10)

    '''
    print(request)

    http_proxy = "http://194.62.145.248:8080"
    https_proxy = "https://194.62.145.248:8080"
    ftp_proxy = "10.10.1.10:3128"

    proxiesD = {
        "http": "http://194.62.145.248:8080",
        "https": "https://194.62.145.248:8080"
    }

    print('!!')
    for i in range(1, 10):
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}

        s = requests.get(url, headers=headers)  # ,proxies=proxiesD)
        t = random.randint(0, 3)
        print('request: Number:' + str(i) + ', break:' + str(t))
        time.sleep(t)
        '''

    return HttpResponse("ТОРБоты сработали")




    #return HttpResponse("Тестовая страница)")
urltestip = 'https://2ip.ru'
urltestnormip = 'http://httpbin.org/ip'
еще код для норм вывода
r = session.get('http://httpbin.org/ip')
        print(r.text)


"""