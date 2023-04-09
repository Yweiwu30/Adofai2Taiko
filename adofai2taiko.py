import sys
import json
import re
import time
import shutil
import os
import zipfile
import random
import traceback
from fractions import Fraction

from PySide6.QtWidgets import *
from PySide6.QtGui import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Adofai2Taiko

class Adofai2Taiko(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Adofai2Taiko()
        self.ui.setupUi(self)
        self.al = {}
        self.adofaiFile = ""
        self.musicFile = ""
        self.outputPath = ""
        self.isChangeBPM = False
        self.taikoMode = 0
        self.ui.adofaiFileButton.clicked.connect(self.selectAdofaiChart)
        self.ui.musicFileButton.clicked.connect(self.selectMusic)
        self.ui.isChangeBPM.clicked.connect(self.setChangeBPM)
        self.ui.generateButton.clicked.connect(self.startConvert)
        self.taikoModeGroup = QButtonGroup(self)
        self.taikoModeGroup.addButton(self.ui.withSpeed, 0)
        self.taikoModeGroup.addButton(self.ui.dong, 1)
        self.taikoModeGroup.addButton(self.ui.ka, 2)
        self.taikoModeGroup.addButton(self.ui.random, 3)
        self.taikoModeGroup.buttonClicked.connect(self.setTaikoMode)

    def setChangeBPM(self):
        self.isChangeBPM = self.ui.isChangeBPM.isChecked()

    def setTaikoMode(self, item):
        self.taikoMode = item

    def selectAdofaiChart(self):
        file_path = QFileDialog.getOpenFileName(
            caption="选择ADOFAI谱面文件", filter="(*.adofai)")
        if file_path[0]:
            self.adofaiFile = file_path[0]
            self.ui.adofaiFile.setText(self.adofaiFile)
            self.readChart(self.adofaiFile)

    def selectMusic(self):
        file_path = QFileDialog.getOpenFileName(
            caption="选择音乐文件", filter="(*.ogg)")
        if file_path[0]:
            self.musicFile = file_path[0]
            self.ui.musicFile.setText(self.musicFile)

    def readChart(self, name):
        with open(name, "r", encoding="utf-8") as f:
            ff = f.read()
            if ff.startswith(u'\ufeff'):
                ff = ff.encode('utf8')[3:].decode('utf8')
            self.al = json.loads(re.sub(r"\"\s*,\s*\}", "\" }", ff))
        self.ui.song.setText(self.al["settings"]["song"])
        self.ui.songOrg.setText(self.al["settings"]["song"])
        self.ui.artist.setText(self.al["settings"]["artist"])
        self.ui.artistOrg.setText(self.al["settings"]["artist"])
        self.ui.creator.setText(self.al["settings"]["author"])
        self.ui.bpm.setValue(self.al["settings"]["bpm"])
        self.ui.offset.setValue(self.al["settings"]["offset"])
        self.ui.volume.setValue(self.al["settings"]["volume"])

    def adofaiConverter(self):
        angle_dict = {"R": 0, "E": 45, "U": 90, "Q": 135, "L": 180, "Z": 225, "D": 270, "C": 315, "J": 30, "T": 60, "G": 120, "H": 150, "N": 210,
                      "F": 240, "B": 300, "M": 330, "p": 15, "o": 75, "q": 105, "W": 165, "x": 195, "V": 255, "Y": 285, "A": 345, "!": 999}

        if "pathData" in list(self.al.keys()): # 转换旧版谱面至新版
            angle = []
            for i in range(len(self.al["pathData"])):
                if self.al["pathData"][i] in list(angle_dict.keys()):
                    angle.append(angle_dict[self.al["pathData"][i]])
                elif self.al["pathData"][i] == "5":
                    angle.append(angle[-1]+72)
                elif self.al["pathData"][i] == "7":
                    angle.append(angle[-1]+(360/7))
                else:
                    angle.append(0)
        else:
            angle = self.al["angleData"]
        dt = {"bpm": self.ui.bpm.value(),
              "angle": angle,
              "speed": {},
              "rotate": [],
              "pause": {},
              "tri": {}
              }
        lb = self.ui.bpm.value()
        for i in self.al["actions"]:
            if i["eventType"] == "SetSpeed":
                if "speedType" in i:
                    if i["speedType"] == "Multiplier":
                        dt["speed"].update({i["floor"]-1: i["bpmMultiplier"]*lb})
                        lb *= i["bpmMultiplier"]
                    else:
                        dt["speed"].update({i["floor"]-1: i["beatsPerMinute"]})
                        lb = i["beatsPerMinute"]

                else:
                    dt["speed"].update({i["floor"]-1: i["beatsPerMinute"]})
                    lb = i["beatsPerMinute"]
            elif i["eventType"] == "Twirl":
                dt["rotate"].append(i["floor"]-1)
            elif i["eventType"] == "Pause":
                dt["pause"].update({i["floor"]-1: i["duration"]})
            elif i["eventType"] == "MultiPlanet":
                if i["planets"] == "ThreePlanets":
                    dt["tri"].update({i["floor"]-1: 3})
                else:
                    dt["tri"].update({i["floor"]-1: 2})
        bt, br = Fraction(0, 1), self.ui.beginBar.value()*4-1
        beat = []
        rt = False
        bc = 2
        tm = Fraction(1, 1)
        lb, nb = dt["bpm"], dt["bpm"]
        msc = 0
        timed = [{"beat": [0, 0, 1], "bpm": dt["bpm"]}]
        tt = {0: 1 if 0 in list(dt["speed"]) and dt["speed"]
              [0] < dt["bpm"] else 0}  # 0=red 1=blue
        for i in range(0, len(dt["angle"])):
            l, n = dt["angle"][i-1] if i != 0 else 0, dt["angle"][i]
            if l == 999:
                l = (dt["angle"][i-2]-180) % 360
            if n != 999:
                da = Fraction((180+l-n-(60*(bc-2))) % 360)
                if rt:
                    da = Fraction((180-l+n-(60*(bc-2))) % 360)
                if da == 0:
                    da += 360
                if i in list(dt["pause"].keys()):
                    da += Fraction(str(dt["pause"][i]*180))
                bt += Fraction(da, 180*tm)
                if bt >= 1.0:
                    br += int(bt//1)
                    bt -= bt//1
                frac = str(bt).split("/")
                beat.append((br, int(frac[0]), int(
                    frac[1]) if len(frac) == 2 else 1))
            else:
                msc += 1
            if i in list(dt["speed"]):
                if (dt["speed"][i] / lb) % 2 == 0.0 or 2 % (dt["speed"][i] / lb) == 0.0 or self.isChangeBPM == False:
                    tm = Fraction(
                        Fraction(str(dt["speed"][i])), Fraction(str(nb)))
                else:
                    sp = dt["speed"][i]
                    tm = Fraction(1, 1)
                    while sp > 300.0:
                        sp /= 2
                        tm *= 2
                    timed.append({"beat": beat[-1], "bpm": sp})
                    nb = sp
                if self.taikoMode == 0:
                    if dt["speed"][i] < lb and list(tt.values())[-1] == 0:
                        tt.update({i-msc: 1})
                    elif dt["speed"][i] > lb and list(tt.values())[-1] == 1:
                        tt.update({i-msc: 0})
                elif self.taikoMode == 1:
                    tt.update({i-msc: 0})
                elif self.taikoMode == 2:
                    tt.update({i-msc: 1})
                elif self.taikoMode == 3:
                    tt.update({i-msc: random.randint(0,1)})
                lb = dt["speed"][i]
            if i in dt["rotate"]:
                rt = not rt
            if i in list(dt["tri"].keys()):
                bc = dt["tri"][i]
        return beat, tt, timed

    def toMalody(self, beat, tt, timed):
        note = [{"beat": [0, 0, 1], "sound": os.path.split(self.musicFile)[-1], "vol": self.ui.volume.value(),
                 "offset": self.ui.offset.value(), "type": 1}]
        style = 0
        for i in range(len(beat)):
            if i in list(tt.keys()):
                if tt[i] == 1:
                    style = 2
                else:
                    style = 0
            note.append({"beat": list(beat[i]), "column": 0, "style": style})
        cht = {"meta": {"$ver": 0, "creator": self.ui.creator.text(), "background": "", "version": "", "id": 0, "mode": 5, "time": int(time.time()),
                        "song": {"title": self.ui.song.text(), "artist": self.ui.artist.text(), "id": 0, "titleorg": self.ui.songOrg.text()},
                        "mode_ext": {"bar_begin": 0}},
               "time": timed,
               "effect": [],
               "note": note
               }
        return json.dumps(cht, indent=2)

    def writeChart(self, data):
        file_path = QFileDialog.getSaveFileName(caption="选择文件", filter="(*.mcz)")
        if file_path[0]:
            self.outputPath = file_path[0]
            try:
                with open(os.path.splitext(self.outputPath)[0]+".mc", "w", encoding="utf-8") as f:
                    f.write(data)
                shutil.copyfile(self.musicFile, os.path.join(os.path.split(self.outputPath)[0], os.path.split(self.musicFile)[-1]))
                output = zipfile.ZipFile(self.outputPath, mode="w")
                output.write(os.path.splitext(self.outputPath)[0]+".mc")
                output.write(os.path.join(os.path.split(self.outputPath)[0], os.path.split(self.musicFile)[-1]))
                output.close()
                os.remove(os.path.splitext(self.outputPath)[0]+".mc")
                os.remove(os.path.join(os.path.split(self.outputPath)[0], os.path.split(self.musicFile)[-1]))
                QMessageBox.information(self,"完成","转换成功")
            except OSError:
                QMessageBox.critical(self,"错误","文件保存失败，请检查源文件是否存在，剩余存储空间是否足够")
            except:
                QMessageBox.critical(self,"错误","文件保存失败，以下是错误信息：\n"+traceback.format_exc())

    def startConvert(self):
        if self.adofaiFile == "":
            QMessageBox.information(self,"提示","请选择ADOFAI谱面文件")
        elif self.musicFile == "":
            QMessageBox.information(self,"提示","请选择音乐文件")
        else:
            try:
                beat, tt, timed = self.adofaiConverter()
                data = self.toMalody(beat, tt, timed)
                self.writeChart(data)
            except:
                QMessageBox.critical(self,"错误","谱面转换失败，以下是错误信息：\n"+traceback.format_exc())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Adofai2Taiko()
    window.show()
    sys.exit(app.exec())
