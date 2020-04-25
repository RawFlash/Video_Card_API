from django.shortcuts import render


# Create your views here.

#Метод занесения данных из .txt в базу Postgres
def main(request):


    return render(request,'test/Update_db.html',locals())
