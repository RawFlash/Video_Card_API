from django.http import HttpResponse
from django.shortcuts import render

def main2(request):

    return render(request,'test/test.html',locals())
    # print('!!')
    #return HttpResponse("Тестовая страница)")