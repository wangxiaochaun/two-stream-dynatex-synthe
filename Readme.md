# Two-Stream Convolution Networks for Dynamics Texture Synthesis
(tiny modification)

## 使用环境
- TensorFlow 1.11 (Anaconda virtual env)
- GTX 1080 for synthesizing 8 frames (or there will be memory OOM)
- Appearance-stream [tfmodel](https://drive.google.com/open?id=19KkFi92oWLzuOWnGo6Zsqe-2CCXFAoXZ)
- Dynamics-stream [tfmodel](https://drive.google.com/open?id=1DHnzoNO-iTgMUTbUOLrigEmpPHmn_mT1)
- [Dynamic textures](https://drive.google.com/open?id=0B5T9jWfa9iDySWJHZnpNZ2dHWUk)
- [Static textures](https://drive.google.com/open?id=11yMiPXiuYvLCyoLfQf_dEG6kuav8h6_3) (for dynamics style transfer)

## 使用方法
1. 下载Appearance和Dynamics的预训练模型；
2. 将Appearance和Dynamics预训练模型放在工程目录下的`./models`里
3. 下载Dynamic textures数据集，放在工程目录下的`./data`里

## 动态纹理合成
1. 对data里的每个子目录，里面有一张gif图和采样得到的12帧。将git图移出子目录。对剩余的图像，根据synthesizer的```__init__```中的```Optimizer.__init__```的第三个参数（默认是12），将多余图像也移出子目录。
    > 例如，我测试时用的GTX 1080,8G显存，只能跑8张图，就留8帧
2. 运行
```
python synthesize.py --type=dts --gpu=<NUMBER> --runid=<NAME>
--dynamics_target=data/dynamic_textures/<FOLDER>
--dynamics_model=models/<TFMODEL>
```
3. 示例：
```
python synthesize.py --type=dts --gpu=0 --runid="my_cool_fish" --dynamics_target=data/dynamic_textures/fish --dynamics_model=models/MSOEnet_ucf101train01_6e-4_allaug_exceptscale_randorder.tfmodel
```

## 注意
网络输出保存在'data/out/<RUNID>'中

使用'./useful_scripts/makegif.sh'可以创建gif图，具体地
    > 在useful_scripts里创建一个目录，把图像序列放进去；
    > 执行 ```python cropandconverttogifs.py```即可

## 进度
目前只测试了动态纹理合成部分，其余功能陆续更新中

## 原始链接
[Two-stream-dyntex-synh](https://github.com/ryersonvisionlab/two-stream-dyntex-synth)


