from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from .models import VideoCard
from django.http import request as req
#from video_card_api.api.models import *
from django.http import HttpResponse

import sys
import os


class Conv_VideoCard():
    Title = str
    GPUName = str
    GPUVariant = str
    Architecture = str
    ProcessSize = str
    Transistors = str
    DieSize = str
    ReleaseDate = str
    Generation = str
    Production = str
    BusInterface = str
    GPUClock = str
    MemoryClock = str
    MemorySize = str
    MemoryType = str
    MemoryBus = str
    Bandwidth = str
    PixelShaders = str
    VertexShaders = str
    TMUs = str
    ROPs = str
    PixelRate = str
    TextureRate = str
    SlotWidth = str
    TDP = str
    Outputs = str
    BoardNumber = str
    DirectX = str
    OpenGL = str
    OpenCL = str
    Vulkan = str
    PixelShader = str
    VertexShader = str
    LaunchPrice = str
    Foundry = str
    PowerConnectors = str
    VertexRate = str
    Length = str
    ShaderModel = str
    ShadingUnits = str
    ComputeUnits = str
    FP32performance = str
    BoostClock = str
    FP64performance = str
    FP16performance = str
    ShaderClock = str
    SMCount = str
    CUDA = str
    SMXCount = str
    SMMCount = str
    TensorCores = str
    RTCores = str

    def __init__(self,
                 Title='',
                 GPUName='',
                 GPUVariant='',
                 Architecture='',
                 ProcessSize='',
                 Transistors='',
                 DieSize='',
                 ReleaseDate='',
                 Generation='',
                 Production='',
                 BusInterface='',
                 GPUClock='',
                 MemoryClock='',
                 MemorySize='',
                 MemoryType='',
                 MemoryBus='',
                 Bandwidth='',
                 PixelShaders='',
                 VertexShaders='',
                 TMUs='',
                 ROPs='',
                 PixelRate='',
                 TextureRate='',
                 SlotWidth='',
                 TDP='',
                 Outputs='',
                 BoardNumber='',
                 DirectX='',
                 OpenGL='',
                 OpenCL='',
                 Vulkan='',
                 PixelShader='',
                 VertexShader='',
                 LaunchPrice='',
                 Foundry='',
                 PowerConnectors='',
                 VertexRate='',
                 Length='',
                 ShaderModel='',
                 ShadingUnits='',
                 ComputeUnits='',
                 FP32performance='',
                 BoostClock='',
                 FP64performance='',
                 FP16performance='',
                 ShaderClock='',
                 SMCount='',
                 CUDA='',
                 SMXCount='',
                 SMMCount='',
                 TensorCores='',
                 RTCores='',
                 ):
        self.Title = Title
        self.GPUName = GPUName
        self.GPUVariant = GPUVariant
        self.Architecture = Architecture
        self.ProcessSize = ProcessSize
        self.Transistors = Transistors
        self.DieSize = DieSize
        self.ReleaseDate = ReleaseDate
        self.Generation = Generation
        self.Production = Production
        self.BusInterface = BusInterface
        self.GPUClock = GPUClock
        self.MemoryClock = MemoryClock
        self.MemorySize = MemorySize
        self.MemoryType = MemoryType
        self.MemoryBus = MemoryBus
        self.Bandwidth = Bandwidth
        self.PixelShaders = PixelShaders
        self.VertexShaders = VertexShaders
        self.TMUs = TMUs
        self.ROPs = ROPs
        self.PixelRate = PixelRate
        self.TextureRate = TextureRate
        self.SlotWidth = SlotWidth
        self.TDP = TDP
        self.Outputs = Outputs
        self.BoardNumber = BoardNumber
        self.DirectX = DirectX
        self.OpenGL = OpenGL
        self.OpenCL = OpenCL
        self.Vulkan = Vulkan
        self.PixelShader = PixelShader
        self.VertexShader = VertexShader
        self.LaunchPrice = LaunchPrice
        self.Foundry = Foundry
        self.PowerConnectors = PowerConnectors
        self.VertexRate = VertexRate
        self.Length = Length
        self.ShaderModel = ShaderModel
        self.ShadingUnits = ShadingUnits
        self.ComputeUnits = ComputeUnits
        self.FP32performance = FP32performance
        self.BoostClock = BoostClock
        self.FP64performance = FP64performance
        self.FP16performance = FP16performance
        self.ShaderClock = ShaderClock
        self.SMCount = SMCount
        self.CUDA = CUDA
        self.SMXCount = SMXCount
        self.SMMCount = SMMCount
        self.TensorCores = TensorCores
        self.RTCores = RTCores

def json(request):
    raw_parameters = request.GET
    parameters={}
    for p in raw_parameters:
        print(p)
        print(raw_parameters.get(p))
        parameters.update({p:raw_parameters.get(p)})

    print("проверка")
    print(parameters.keys())
    if parameters.__len__()==1 and \
            ('Title' in parameters.keys() or 'id' in parameters.keys()):
        print("1 parameter")
        VC = search_VC1(parameters)
        print("parameters")
        print(parameters)
        print(VC)
        for vc in VC:
            print(vc)
            data = vc.return_all()
        print(data)
        return JsonResponse(data)
    else:
        print("more parameters")
        Titles_VC = search_VC2(parameters)
        data={}
        data.update({"VideoCards":Titles_VC})
        return JsonResponse(data)

def search_VC1(parametrs):

    #ПОИСК ПО ОДНОМУ ПАРАМЕТРУ   id  ИЛИ  Title

    for p in parametrs:
        print("search"+p+parametrs.get(p))
        list_VC=search(p,parametrs.get(p))

    return list_VC


def search_VC2(parametrs):
    print("!\n!\nSEARCH")
    work_list_VC=[]
    first_list_VC=[]
    list_VC=[]
    first_search=True
    first_update=True
    for p in parametrs:
        print(p)
        print(parametrs.get(p))
        if first_search==True:
            first_search=False
            first_list_VC=search(p,parametrs.get(p))
            list_VC=first_list_VC

        elif first_update==True:
            first_update=False
            print("count 2nd search")
            print(search(p,parametrs.get(p)).__len__())
            list_VC=list_VC_update(first_list_VC,search(p,parametrs.get(p)))
        else:
            list_VC = list_VC_update(list_VC, search(p, parametrs.get(p)))
        print("COUNT")
        print(list_VC.__len__())
    print(list_VC)
    return_list=[]
    for vc in list_VC:
        return_list.append(vc.Title)
    return return_list

def search(par,val):
    #print("search "+par+" "+val)
    list_vc_r=[]
    if par =="id":
        print(par)
        print(val)
        list_vc= VideoCard.objects1.filter(id=val)
        print("list:")
        #print(list_vc)
        for vc in list_vc:
            print(vc.Title)
            print(vc.id)
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Title":
        list_vc= VideoCard.objects1.filter(Title=val)
        print("list:")
        print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="GPUName":
        list_vc= VideoCard.objects1.filter(GPUName=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="GPUVariant":
        list_vc= VideoCard.objects1.filter(GPUVariant=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Architecture":
        list_vc= VideoCard.objects1.filter(Architecture=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ProcessSize":
        list_vc= VideoCard.objects1.filter(ProcessSize=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Transistors":
        list_vc= VideoCard.objects1.filter(Transistors=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="DieSize":
        list_vc= VideoCard.objects1.filter(DieSize=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ReleaseDate":
        list_vc= VideoCard.objects1.filter(ReleaseDate=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Generation":
        list_vc= VideoCard.objects1.filter(Generation=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Production":
        list_vc= VideoCard.objects1.filter(Production=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="BusInterface":
        list_vc= VideoCard.objects1.filter(BusInterface=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="GPUClock":
        list_vc= VideoCard.objects1.filter(GPUClock=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="MemoryClock":
        list_vc= VideoCard.objects1.filter(MemoryClock=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="MemorySize":
        list_vc= VideoCard.objects1.filter(MemorySize=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="MemoryType":
        list_vc= VideoCard.objects1.filter(MemoryType=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="MemoryBus":
        list_vc= VideoCard.objects1.filter(MemoryBus=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Bandwidth":
        list_vc= VideoCard.objects1.filter(Bandwidth=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="PixelShaders":
        list_vc= VideoCard.objects1.filter(PixelShaders=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="VertexShaders":
        list_vc= VideoCard.objects1.filter(VertexShaders=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="TMUs":
        list_vc= VideoCard.objects1.filter(TMUs=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ROPs":
        list_vc= VideoCard.objects1.filter(ROPs=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="PixelRate":
        list_vc= VideoCard.objects1.filter(PixelRate=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="TextureRate":
        list_vc= VideoCard.objects1.filter(TextureRate=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="SlotWidth":
        list_vc= VideoCard.objects1.filter(SlotWidth=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="TDP":
        list_vc= VideoCard.objects1.filter(TDP=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Outputs":
        list_vc= VideoCard.objects1.filter(Outputs=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="BoardNumber":
        list_vc= VideoCard.objects1.filter(BoardNumber=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="DirectX":
        list_vc= VideoCard.objects1.filter(DirectX=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="OpenGL":
        list_vc= VideoCard.objects1.filter(OpenGL=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="OpenCL":
        list_vc= VideoCard.objects1.filter(OpenCL=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Vulkan":
        list_vc= VideoCard.objects1.filter(Vulkan=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="PixelShader":
        list_vc= VideoCard.objects1.filter(PixelShader=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="VertexShader":
        list_vc= VideoCard.objects1.filter(VertexShader=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="LaunchPrice":
        list_vc= VideoCard.objects1.filter(LaunchPrice=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Foundry":
        list_vc= VideoCard.objects1.filter(Foundry=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="PowerConnectors":
        list_vc= VideoCard.objects1.filter(PowerConnectors=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="VertexRate":
        list_vc= VideoCard.objects1.filter(VertexRate=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="Length":
        list_vc= VideoCard.objects1.filter(Length=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ShaderModel":
        list_vc= VideoCard.objects1.filter(ShaderModel=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ShadingUnits":
        list_vc= VideoCard.objects1.filter(ShadingUnits=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ComputeUnits":
        list_vc= VideoCard.objects1.filter(ComputeUnits=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="FP32performance":
        list_vc= VideoCard.objects1.filter(FP32performance=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="BoostClock":
        list_vc= VideoCard.objects1.filter(BoostClock=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="FP64performance":
        list_vc= VideoCard.objects1.filter(FP64performance=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="FP16performance":
        list_vc= VideoCard.objects1.filter(FP16performance=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="ShaderClock":
        list_vc= VideoCard.objects1.filter(ShaderClock=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="SMCount":
        list_vc= VideoCard.objects1.filter(SMCount=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="CUDA":
        list_vc= VideoCard.objects1.filter(CUDA=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="SMXCount":
        list_vc= VideoCard.objects1.filter(SMXCount=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="SMMCount":
        list_vc= VideoCard.objects1.filter(SMMCount=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="TensorCores":
        list_vc= VideoCard.objects1.filter(TensorCores=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    if par =="RTCores":
        list_vc= VideoCard.objects1.filter(RTCores=val)
        #print(list_vc)
        for vc in list_vc:
            list_vc_r.append(vc)
        #print(list_vc_r)
    return list_vc_r

def list_VC_update(first_list,second_list):
    list=[]
    for a in first_list:
        for b in second_list:
            if a==b:
                list.append(a)
    return list


def main(request):
    print('!!')
    return HttpResponse("Here's the text of the Web page.")

def test(request):
    try:
        vc =VideoCard.objects1.get(id=100).GPUName
        vc1=VideoCard.objects1.all()
        vc2 = VideoCard.objects1.filter(GPUName='Saturn')
        for i in vc2:
            print(i.MemorySize)
        print(str(vc2))
        print("!!!"+str(vc1))
        print(vc)
        print(VideoCard)
        print(str(vc))
        #print(VideoCard.)
        #vc = VideoCard.object.all()
        #print(vc)
    except:
        None
    return render(request, 'test.html')

def db(request):
    # print(sys.path)
    # print(BASE_DIR)
    direct = (str(sys.path[0]) + '\\update_db\\parser\\techpowerup.com\\video_card\\')
    # sys.path.append(direct)
    # print(direct)
    files = os.listdir(direct)
    # print(files)
    for file in files:
        print(file)
        read = open(direct+file, 'r').read().split('\n')
        #print(read)
        CVC = Conv_VideoCard()
        CVC.Title = file[:-4]
        for i in list(range(0, len(read), 2)):
            try:
                print(i)
                print(read[i])
                print(read[i + 1])
            except:
                None
            if read[i]!='':
                None
                if read[i+1] =='N/A':
                    CVC.__dict__.update({read[i]: ''})
                else:
                    CVC.__dict__.update({read[i]: read[i + 1]})

        VC = VideoCard.create(VideoCard,CVC)
        VC.save()

    return render(request, 'test.html')

def clean_db(request):
    VideoCard.objects1.all().delete()
    return redirect("http://127.0.0.1:8000/video_card_api/return/test")