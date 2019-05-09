# from django.db import models

from django.db import models


# from .views import Conv_VideoCard

class Conv_VideoCard(models.Model):
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

    def __init__(self, Title='', GPUName='', GPUVariant='', Architecture='', ProcessSize='', Transistors='', DieSize='',
                 ReleaseDate='', Generation='', Production='', BusInterface='', GPUClock='', MemoryClock='',
                 MemorySize='', MemoryType='', MemoryBus='', Bandwidth='', PixelShaders='', VertexShaders='', TMUs='',
                 ROPs='', PixelRate='', TextureRate='', SlotWidth='', TDP='', Outputs='', BoardNumber='', DirectX='',
                 OpenGL='', OpenCL='', Vulkan='', PixelShader='', VertexShader='', LaunchPrice='', Foundry='',
                 PowerConnectors='', VertexRate='', Length='', ShaderModel='', ShadingUnits='', ComputeUnits='',
                 FP32performance='', BoostClock='', FP64performance='', FP16performance='', ShaderClock='', SMCount='',
                 CUDA='', SMXCount='', SMMCount='', TensorCores='', RTCores='', *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    '''def __init__(self, CVC, *args, **kwargs):

        print(type(CVC))
        if CVC == Conv_VideoCard:
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
            #self.Title="DICH"
        
        '''

    def create(self, CVC=Conv_VideoCard):
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
        data.update({'Title': self.Title})
        data.update({'GPUName': self.GPUName})
        data.update({'GPUVariant': self.GPUVariant})
        data.update({'Architecture': self.Architecture})
        data.update({'ProcessSize': self.ProcessSize})
        data.update({'Transistors': self.Transistors})
        data.update({'DieSize': self.DieSize})
        data.update({'ReleaseDate': self.ReleaseDate})
        data.update({'Generation': self.Generation})
        data.update({'Production': self.Production})
        data.update({'BusInterface': self.BusInterface})
        data.update({'GPUClock': self.GPUClock})
        data.update({'MemoryClock': self.MemoryClock})
        data.update({'MemorySize': self.MemorySize})
        data.update({'MemoryType': self.MemoryType})
        data.update({'MemoryBus': self.MemoryBus})
        data.update({'Bandwidth': self.Bandwidth})
        data.update({'PixelShaders': self.PixelShaders})
        data.update({'VertexShaders': self.VertexShaders})
        data.update({'TMUs': self.TMUs})
        data.update({'ROPs': self.ROPs})
        data.update({'PixelRate': self.PixelRate})
        data.update({'TextureRate': self.TextureRate})
        data.update({'SlotWidth': self.SlotWidth})
        data.update({'TDP': self.TDP})
        data.update({'Outputs': self.Outputs})
        data.update({'BoardNumber': self.BoardNumber})
        data.update({'DirectX': self.DirectX})
        data.update({'OpenGL': self.OpenGL})
        data.update({'OpenCL': self.OpenCL})
        data.update({'Vulkan': self.Vulkan})
        data.update({'PixelShader': self.PixelShader})
        data.update({'VertexShader': self.VertexShader})
        data.update({'LaunchPrice': self.LaunchPrice})
        data.update({'Foundry': self.Foundry})
        data.update({'PowerConnectors': self.PowerConnectors})
        data.update({'VertexRate': self.VertexRate})
        data.update({'Length': self.Length})
        data.update({'ShaderModel': self.ShaderModel})
        data.update({'ShadingUnits': self.ShadingUnits})
        data.update({'ComputeUnits': self.ComputeUnits})
        data.update({'FP32performance': self.FP32performance})
        data.update({'BoostClock': self.BoostClock})
        data.update({'FP64performance': self.FP64performance})
        data.update({'FP16performance': self.FP16performance})
        data.update({'ShaderClock': self.ShaderClock})
        data.update({'SMCount': self.SMCount})
        data.update({'CUDA': self.CUDA})
        data.update({'SMXCount': self.SMXCount})
        data.update({'SMMCount': self.SMMCount})
        data.update({'TensorCores': self.TensorCores})
        data.update({'RTCores': self.RTCores})
        return data
