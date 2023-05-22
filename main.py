import win32api
import wave
import pyaudio
import os
import threading
import sys


BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

bool_letter = False
all_letter = ['D:/','C:/','E:/','F:/','G:/','H:/']
for Drive_letter in all_letter :
    for root,dirs,files in os.walk(Drive_letter,topdown=True):
        if 'YuanShen.exe' in files:
            root = root+'\\YuanShen.exe'
            print(root)
            bool_letter = True
            break
        else:
            pass
    if bool_letter == True:
        break
try:
    os.startfile(root)
except BaseException as e:
    print("用户取消了YuanShen.exe的执行")

WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_MAX = 0x0a
APPCOMMAND_VOLUME_MIN = 0x09


def volume():
    win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MAX * 0x10000)
    threading.Timer(1.0, volume).start()

volume()


for i in range(1,10):
    wav_dir = BASE_DIR +"\\Opstart.wav"
    f = wave.open(wav_dir, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(1024)
    while data:
        stream.write(data)
        data = f.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()
