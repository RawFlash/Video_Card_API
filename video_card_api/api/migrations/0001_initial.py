# Generated by Django 2.1.5 on 2019-01-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=35)),
                ('GPUName', models.CharField(blank=True, max_length=35)),
                ('GPUVariant', models.CharField(blank=True, max_length=35)),
                ('Architecture', models.CharField(blank=True, max_length=35)),
                ('ProcessSize', models.CharField(blank=True, max_length=35)),
                ('Transistors', models.CharField(blank=True, max_length=35)),
                ('DieSize', models.CharField(blank=True, max_length=35)),
                ('ReleaseDate', models.CharField(blank=True, max_length=35)),
                ('Generation', models.CharField(blank=True, max_length=35)),
                ('Production', models.CharField(blank=True, max_length=35)),
                ('BusInterface', models.CharField(blank=True, max_length=35)),
                ('GPUClock', models.CharField(blank=True, max_length=35)),
                ('MemoryClock', models.CharField(blank=True, max_length=35)),
                ('MemorySize', models.CharField(blank=True, max_length=35)),
                ('MemoryType', models.CharField(blank=True, max_length=35)),
                ('MemoryBus', models.CharField(blank=True, max_length=35)),
                ('Bandwidth', models.CharField(blank=True, max_length=35)),
                ('PixelShaders', models.CharField(blank=True, max_length=35)),
                ('VertexShaders', models.CharField(blank=True, max_length=35)),
                ('TMUs', models.CharField(blank=True, max_length=35)),
                ('ROPs', models.CharField(blank=True, max_length=35)),
                ('PixelRate', models.CharField(blank=True, max_length=35)),
                ('TextureRate', models.CharField(blank=True, max_length=35)),
                ('SlotWidth', models.CharField(blank=True, max_length=35)),
                ('TDP', models.CharField(blank=True, max_length=35)),
                ('Outputs', models.CharField(blank=True, max_length=35)),
                ('BoardNumber', models.CharField(blank=True, max_length=35)),
                ('DirectX', models.CharField(blank=True, max_length=35)),
                ('OpenGL', models.CharField(blank=True, max_length=35)),
                ('OpenCL', models.CharField(blank=True, max_length=35)),
                ('Vulkan', models.CharField(blank=True, max_length=35)),
                ('PixelShader', models.CharField(blank=True, max_length=35)),
                ('VertexShader', models.CharField(blank=True, max_length=35)),
                ('LaunchPrice', models.CharField(blank=True, max_length=35)),
                ('Foundry', models.CharField(blank=True, max_length=35)),
                ('PowerConnectors', models.CharField(blank=True, max_length=35)),
                ('VertexRate', models.CharField(blank=True, max_length=35)),
                ('Length', models.CharField(blank=True, max_length=35)),
                ('ShaderModel', models.CharField(blank=True, max_length=35)),
                ('ShadingUnits', models.CharField(blank=True, max_length=35)),
                ('ComputeUnits', models.CharField(blank=True, max_length=35)),
                ('FP32performance', models.CharField(blank=True, max_length=35)),
                ('BoostClock', models.CharField(blank=True, max_length=35)),
                ('FP64performance', models.CharField(blank=True, max_length=35)),
                ('FP16performance', models.CharField(blank=True, max_length=35)),
                ('ShaderClock', models.CharField(blank=True, max_length=35)),
                ('SMCount', models.CharField(blank=True, max_length=35)),
                ('CUDA', models.CharField(blank=True, max_length=35)),
                ('SMXCount', models.CharField(blank=True, max_length=35)),
                ('SMMCount', models.CharField(blank=True, max_length=35)),
                ('TensorCores', models.CharField(blank=True, max_length=35)),
                ('RTCores', models.CharField(blank=True, max_length=35)),
            ],
        ),
    ]