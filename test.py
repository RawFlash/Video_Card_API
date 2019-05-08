#"""
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


str1='a'
str2 = get_key(locals(),'a')



get_key(locals(),'a')
print(str1.__getattribute__)
print(str2)
print(dir(str1))
print(locals())
#"""

"""
def format1(file):
    for str1 in file:
        str1 = str1[0:str1.index('=')]
        print(str1)

def format2(file):
    for str1 in file:
        str1="data.update({'"+str1+"':self."+str1+"})"
        print(str1.replace(' ',''))

def format3(file):
    for str1 in file:
        str1='''    if par =="'''+str1+'''":
        list_vc= VideoCard.objects1.filter('''+str1+'''=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)'''
        print(str1)

def format4(file):
    for str1 in file:
        print(str1.replace(' ',''))


file = open("test.txt",'r').read().split("\n")
format3(file)
"""