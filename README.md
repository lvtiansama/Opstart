# Opstart v1.1

基于原神的整蛊程序


## 版本更新内容

本版本仅针对`win`版本，修复了bat文件指定错误的问题

## 重要通知

这个项目的初衷是为了娱乐，开发者承诺本程序不会对使用者的计算机造成危害。

## 声明

本项目为开源、离线的项目，开发者对本项目没有控制力。可能会有人恶意修改本项目，以达成非法目的，因此开发者不能保证衍生作品的安全性。

此项目完全离线运行，不会收集任何用户信息或获取用户输入数据。

## 程序原理说明


运行 main.py 后，程序会依次进行如下操作：

1.程序会依次在计算机'D:/','C:/','E:/','F:/','G:/','H:/'中寻找`YuanShen.exe`，并将其启动。

&emsp;**在多次测试下，倘若没有找到`yuanshen.exe`，将有较小的概率抛出报错，该报错由于存在玄学性，开发者无法将其解决**

2.多线程执行，每一秒钟执行一次：将windows系统音量调节至100%

3.播放`Opstart.wav`，循环十次


## 关于 Python 版本问题

开发者使用`Python 3.10.6`编译本项目，打包的可执行文件版本也打包了`Python 3.10.6`，理论上其他python版本也可以正常兼容。


## 使用说明

### 可执行文件版
下载`Opstart_v1.0_win.zip`后将其解压，你将获得以下内容
```
Opstart_v1.0_win
├───安装.bat
└───Opstart
    ├───opsetup.wav
    └───yuanshen.exe
```

运行`安装.bat`后将会把`Opstart`文件复制到本地`D:\`，并且在桌面创建快捷方式，运行桌面上的`原神.lnk`即可。

倘如计算机本地没有卷名为`D:\`的磁盘，快捷方式将无法正常运行，你可以尝试将`安装.bat`修改如下：
```
xcopy %~dp0Opstart C:\Opstart /E /I /Y
powershell -Command "$s=(New-Object -ComObject WScript.Shell).CreateShortcut('%userprofile%\Desktop\原神.lnk');$s.TargetPath='C:\Opstart\yuanshen.exe';$s.Save()"
```
**注意：请保证`opsetup.wav`位于与`yuanshen.exe`同目录下，否则后抛出错误**

### pyhton版
下载`Opstart_v1.0.zip`后将其解压

运行以下命令安装依赖
```
pip install -r requirements.txt
```

运行以下命令执行程序
```
python main.py
```

## 关于作者

`Github`**https://github.com/lvtiansama**

`CSDN`**https://blog.csdn.net/lvtiansama**

`哔哩哔哩`**https://space.bilibili.com/88004482**