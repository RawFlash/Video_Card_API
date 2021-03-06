# from django.db import models

from django.db import models


# from .views import Conv_VideoCard

class Conv_VC(models.Model):
    Id = str
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
    Manufacturer = str

    def __init__(self, Id, Title, GPUName, GPUVariant, Architecture, ProcessSize, Transistors, DieSize,
                 ReleaseDate, Generation, Production, BusInterface, GPUClock, MemoryClock,
                 MemorySize, MemoryType, MemoryBus, Bandwidth, PixelShaders, VertexShaders, TMUs,
                 ROPs, PixelRate, TextureRate, SlotWidth, TDP, Outputs, BoardNumber, DirectX,
                 OpenGL, OpenCL, Vulkan, PixelShader, VertexShader, LaunchPrice, Foundry,
                 PowerConnectors, VertexRate, Length, ShaderModel, ShadingUnits, ComputeUnits,
                 FP32performance, BoostClock, FP64performance, FP16performance, ShaderClock, SMCount,
                 CUDA, SMXCount, SMMCount, TensorCores, RTCores, Manufacturer):
        #super().__init__(*args, **kwargs)
        self.Id = Id
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
        self.Manufacturer = Manufacturer


class VideoCard(models.Model):
    objects1 = models.Manager()
    Title = models.CharField(max_length=35, blank=True)
    GPUName = models.CharField(max_length=35, blank=True)
    GPUVariant = models.CharField(max_length=35, blank=True)
    Architecture = models.CharField(max_length=35, blank=True)
    ProcessSize = models.CharField(max_length=35, blank=True)
    Transistors = models.CharField(max_length=35, blank=True)
    DieSize = models.CharField(max_length=35, blank=True)
    ReleaseDate = models.CharField(max_length=35, blank=True)
    Generation = models.CharField(max_length=35, blank=True)
    Production = models.CharField(max_length=35, blank=True)
    BusInterface = models.CharField(max_length=35, blank=True)
    GPUClock = models.CharField(max_length=35, blank=True)
    MemoryClock = models.CharField(max_length=35, blank=True)
    MemorySize = models.CharField(max_length=35, blank=True)
    MemoryType = models.CharField(max_length=35, blank=True)
    MemoryBus = models.CharField(max_length=35, blank=True)
    Bandwidth = models.CharField(max_length=35, blank=True)
    PixelShaders = models.CharField(max_length=35, blank=True)
    VertexShaders = models.CharField(max_length=35, blank=True)
    TMUs = models.CharField(max_length=35, blank=True)
    ROPs = models.CharField(max_length=35, blank=True)
    PixelRate = models.CharField(max_length=35, blank=True)
    TextureRate = models.CharField(max_length=35, blank=True)
    SlotWidth = models.CharField(max_length=35, blank=True)
    TDP = models.CharField(max_length=35, blank=True)
    Outputs = models.CharField(max_length=35, blank=True)
    BoardNumber = models.CharField(max_length=35, blank=True)
    DirectX = models.CharField(max_length=35, blank=True)
    OpenGL = models.CharField(max_length=35, blank=True)
    OpenCL = models.CharField(max_length=35, blank=True)
    Vulkan = models.CharField(max_length=35, blank=True)
    PixelShader = models.CharField(max_length=35, blank=True)
    VertexShader = models.CharField(max_length=35, blank=True)
    LaunchPrice = models.CharField(max_length=35, blank=True)
    Foundry = models.CharField(max_length=35, blank=True)
    PowerConnectors = models.CharField(max_length=35, blank=True)
    VertexRate = models.CharField(max_length=35, blank=True)
    Length = models.CharField(max_length=35, blank=True)
    ShaderModel = models.CharField(max_length=35, blank=True)
    ShadingUnits = models.CharField(max_length=35, blank=True)
    ComputeUnits = models.CharField(max_length=35, blank=True)
    FP32performance = models.CharField(max_length=35, blank=True)
    BoostClock = models.CharField(max_length=35, blank=True)
    FP64performance = models.CharField(max_length=35, blank=True)
    FP16performance = models.CharField(max_length=35, blank=True)
    ShaderClock = models.CharField(max_length=35, blank=True)
    SMCount = models.CharField(max_length=35, blank=True)
    CUDA = models.CharField(max_length=35, blank=True)
    SMXCount = models.CharField(max_length=35, blank=True)
    SMMCount = models.CharField(max_length=35, blank=True)
    TensorCores = models.CharField(max_length=35, blank=True)
    RTCores = models.CharField(max_length=35, blank=True)
    Manufacturer = models.CharField(max_length=35, blank=True)

    #ЛЮТАЯ ДИЧЬ
    #С конструктором json не работает
    #Без него не работает создание базы данных


    def __init__(self, CVC, *args, **kwargs):

        print(type(CVC))
        if CVC == Conv_VC:
            super().__init__(*args, **kwargs)
            self.Title = CVC.Title
            self.GPUName = CVC.GPUName
            self.GPUVariant = CVC.GPUVariant
            self.Architecture = CVC.Architecture
            self.ProcessSize = CVC.ProcessSize
            self.Transistors = CVC.Transistors
            self.DieSize = CVC.DieSize
            self.ReleaseDate = CVC.ReleaseDate
            self.Generation = CVC.Generation
            self.Production = CVC.Production
            self.BusInterface = CVC.BusInterface
            self.GPUClock = CVC.GPUClock
            self.MemoryClock = CVC.MemoryClock
            self.MemorySize = CVC.MemorySize
            self.MemoryType = CVC.MemoryType
            self.MemoryBus = CVC.MemoryBus
            self.Bandwidth = CVC.Bandwidth
            self.PixelShaders = CVC.PixelShaders
            self.VertexShaders = CVC.VertexShaders
            self.TMUs = CVC.TMUs
            self.ROPs = CVC.ROPs
            self.PixelRate = CVC.PixelRate
            self.TextureRate = CVC.TextureRate
            self.SlotWidth = CVC.SlotWidth
            self.TDP = CVC.TDP
            self.Outputs = CVC.Outputs
            self.BoardNumber = CVC.BoardNumber
            self.DirectX = CVC.DirectX
            self.OpenGL = CVC.OpenGL
            self.OpenCL = CVC.OpenCL
            self.Vulkan = CVC.Vulkan
            self.PixelShader = CVC.PixelShader
            self.VertexShader = CVC.VertexShader
            self.LaunchPrice = CVC.LaunchPrice
            self.Foundry = CVC.Foundry
            self.PowerConnectors = CVC.PowerConnectors
            self.VertexRate = CVC.VertexRate
            self.Length = CVC.Length
            self.ShaderModel = CVC.ShaderModel
            self.ShadingUnits = CVC.ShadingUnits
            self.ComputeUnits = CVC.ComputeUnits
            self.FP32performance = CVC.FP32performance
            self.BoostClock = CVC.BoostClock
            self.FP64performance = CVC.FP64performance
            self.FP16performance = CVC.FP16performance
            self.ShaderClock = CVC.ShaderClock
            self.SMCount = CVC.SMCount
            self.CUDA = CVC.CUDA
            self.SMXCount = CVC.SMXCount
            self.SMMCount = CVC.SMMCount
            self.TensorCores = CVC.TensorCores
            self.RTCores = CVC.RTCores
        else:
            super().__init__(*args, **kwargs)
            print("NONE")


    def create(self, CVC=Conv_VC):
        self.Title = CVC.Title
        self.GPUName = CVC.GPUName
        self.GPUVariant = CVC.GPUVariant
        self.Architecture = CVC.Architecture
        self.ProcessSize = CVC.ProcessSize
        self.Transistors = CVC.Transistors
        self.DieSize = CVC.DieSize
        self.ReleaseDate = CVC.ReleaseDate
        self.Generation = CVC.Generation
        self.Production = CVC.Production
        self.BusInterface = CVC.BusInterface
        self.GPUClock = CVC.GPUClock
        self.MemoryClock = CVC.MemoryClock
        self.MemorySize = CVC.MemorySize
        self.MemoryType = CVC.MemoryType
        self.MemoryBus = CVC.MemoryBus
        self.Bandwidth = CVC.Bandwidth
        self.PixelShaders = CVC.PixelShaders
        self.VertexShaders = CVC.VertexShaders
        self.TMUs = CVC.TMUs
        self.ROPs = CVC.ROPs
        self.PixelRate = CVC.PixelRate
        self.TextureRate = CVC.TextureRate
        self.SlotWidth = CVC.SlotWidth
        self.TDP = CVC.TDP
        self.Outputs = CVC.Outputs
        self.BoardNumber = CVC.BoardNumber
        self.DirectX = CVC.DirectX
        self.OpenGL = CVC.OpenGL
        self.OpenCL = CVC.OpenCL
        self.Vulkan = CVC.Vulkan
        self.PixelShader = CVC.PixelShader
        self.VertexShader = CVC.VertexShader
        self.LaunchPrice = CVC.LaunchPrice
        self.Foundry = CVC.Foundry
        self.PowerConnectors = CVC.PowerConnectors
        self.VertexRate = CVC.VertexRate
        self.Length = CVC.Length
        self.ShaderModel = CVC.ShaderModel
        self.ShadingUnits = CVC.ShadingUnits
        self.ComputeUnits = CVC.ComputeUnits
        self.FP32performance = CVC.FP32performance
        self.BoostClock = CVC.BoostClock
        self.FP64performance = CVC.FP64performance
        self.FP16performance = CVC.FP16performance
        self.ShaderClock = CVC.ShaderClock
        self.SMCount = CVC.SMCount
        self.CUDA = CVC.CUDA
        self.SMXCount = CVC.SMXCount
        self.SMMCount = CVC.SMMCount
        self.TensorCores = CVC.TensorCores
        self.RTCores = CVC.RTCores




def return_all(self):
    data = {}
    data.update({'Id': str(self.Id).rstrip()})
    data.update({'Title': str(self.Title).rstrip()})
    data.update({'GPUName': str(self.GPUName).rstrip()})
    data.update({'GPUVariant': str(self.GPUVariant).rstrip()})
    data.update({'Architecture': str(self.Architecture).rstrip()})
    data.update({'ProcessSize': str(self.ProcessSize).rstrip()})
    data.update({'Transistors': str(self.Transistors).rstrip()})
    data.update({'DieSize': str(self.DieSize).rstrip()})
    data.update({'ReleaseDate': str(self.ReleaseDate).rstrip()})
    data.update({'Generation': str(self.Generation).rstrip()})
    data.update({'Production': str(self.Production).rstrip()})
    data.update({'BusInterface': str(self.BusInterface).rstrip()})
    data.update({'GPUClock': str(self.GPUClock).rstrip()})
    data.update({'MemoryClock': str(self.MemoryClock).rstrip()})
    data.update({'MemorySize': str(self.MemorySize).rstrip()})
    data.update({'MemoryType': str(self.MemoryType).rstrip()})
    data.update({'MemoryBus': str(self.MemoryBus).rstrip()})
    data.update({'Bandwidth': str(self.Bandwidth).rstrip()})
    data.update({'PixelShaders': str(self.PixelShaders).rstrip()})
    data.update({'VertexShaders': str(self.VertexShaders).rstrip()})
    data.update({'TMUs': str(self.TMUs).rstrip()})
    data.update({'ROPs': str(self.ROPs).rstrip()})
    data.update({'PixelRate': str(self.PixelRate).rstrip()})
    data.update({'TextureRate': str(self.TextureRate).rstrip()})
    data.update({'SlotWidth': str(self.SlotWidth).rstrip()})
    data.update({'TDP': str(self.TDP).rstrip()})
    data.update({'Outputs': str(self.Outputs).rstrip()})
    data.update({'BoardNumber': str(self.BoardNumber).rstrip()})
    data.update({'DirectX': str(self.DirectX).rstrip()})
    data.update({'OpenGL': str(self.OpenGL).rstrip()})
    data.update({'OpenCL': str(self.OpenCL).rstrip()})
    data.update({'Vulkan': str(self.Vulkan).rstrip()})
    data.update({'PixelShader': str(self.PixelShader).rstrip()})
    data.update({'VertexShader': str(self.VertexShader).rstrip()})
    data.update({'LaunchPrice': str(self.LaunchPrice).rstrip()})
    data.update({'Foundry': str(self.Foundry).rstrip()})
    data.update({'PowerConnectors': str(self.PowerConnectors).rstrip()})
    data.update({'VertexRate': str(self.VertexRate).rstrip()})
    data.update({'Length': str(self.Length).rstrip()})
    data.update({'ShaderModel': str(self.ShaderModel).rstrip()})
    data.update({'ShadingUnits': str(self.ShadingUnits).rstrip()})
    data.update({'ComputeUnits': str(self.ComputeUnits).rstrip()})
    data.update({'FP32performance': str(self.FP32performance).rstrip()})
    data.update({'BoostClock': str(self.BoostClock).rstrip()})
    data.update({'FP64performance': str(self.FP64performance).rstrip()})
    data.update({'FP16performance': str(self.FP16performance).rstrip()})
    data.update({'ShaderClock': str(self.ShaderClock).rstrip()})
    data.update({'SMCount': str(self.SMCount).rstrip()})
    data.update({'CUDA': str(self.CUDA).rstrip()})
    data.update({'SMXCount': str(self.SMXCount).rstrip()})
    data.update({'SMMCount': str(self.SMMCount).rstrip()})
    data.update({'TensorCores': str(self.TensorCores).rstrip()})
    data.update({'RTCores': str(self.RTCores).rstrip()})
    data.update({'Manufacturer': str(self.Manufacturer).rstrip()})
    return data



#Конвертирование видеокарты с сырыми данными, тоесть нельзя обратиться к полю по названию
def rawVC_to_ConvVC(rawVC):
    newConv_VC = Conv_VC(
        rawVC[0],
        rawVC[1],
        rawVC[2],
        rawVC[3],
        rawVC[4],
        rawVC[5],
        rawVC[6],
        rawVC[7],
        rawVC[8],
        rawVC[9],
        rawVC[10],
        rawVC[11],
        rawVC[12],
        rawVC[13],
        rawVC[14],
        rawVC[15],
        rawVC[16],
        rawVC[17],
        rawVC[18],
        rawVC[19],
        rawVC[20],
        rawVC[21],
        rawVC[22],
        rawVC[23],
        rawVC[24],
        rawVC[25],
        rawVC[26],
        rawVC[27],
        rawVC[28],
        rawVC[29],
        rawVC[30],
        rawVC[31],
        rawVC[32],
        rawVC[33],
        rawVC[34],
        rawVC[35],
        rawVC[36],
        rawVC[37],
        rawVC[38],
        rawVC[39],
        rawVC[40],
        rawVC[41],
        rawVC[42],
        rawVC[43],
        rawVC[44],
        rawVC[45],
        rawVC[46],
        rawVC[47],
        rawVC[48],
        rawVC[49],
        rawVC[50],
        rawVC[51],
        rawVC[52],
        rawVC[53]
    )
    return newConv_VC
