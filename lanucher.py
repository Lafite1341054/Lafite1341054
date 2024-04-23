import subprocess
import sys
from threading import Thread
from time import sleep
import time
import traceback
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from json import dumps, load, dump, loads
# 导入designer工具生成的login模块
from ui import Ui_MainWindow
import minecraft_launcher_lib
import ctypes
import inspect
from rich.console import Console
from qt_material import apply_stylesheet, list_themes
console = Console()
 
FLAG = True
LOCK = False
ILOCK = False
verlistpub = []
 
try:
    # def setTip(obj):
    # myWin.status.setText(obj)
 
    def startfile(filename):
        try:
            os.startfile(filename)
        except:
            subprocess.Popen(['open', filename])
 
    def _async_raise(tid, exctype):
        """raises the exception, performs cleanup if needed"""
        try:
            tid = ctypes.c_long(tid)
            if not inspect.isclass(exctype):
                exctype = type(exctype)
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                tid, ctypes.py_object(exctype))
            if res == 0:
                # pass
                raise ValueError("invalid thread id")
            elif res != 1:
                # """if it returns a number greater than one, you're in trouble,
                # and you should call it again with exc=NULL to revert the effect"""
                ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
                raise SystemError("PyThreadState_SetAsyncExc failed")
        except Exception as err:
            print(err)
 
    def info(*obj):
        localtime = time.localtime(time.time())
        stackinfo = traceback.extract_stack()
        who = stackinfo[1][2]
        line = stackinfo[1][1]
        # console.print("[black on green] I ", *obj)
        print(
            f"[{localtime[3]:0>2}:{localtime[4]:0>2}:{localtime[5]:0>2}] [{who:>20} |{line:>5} ] [INFO]", *obj)
 
    def warn(*obj):
        # console.log("[black on yellow] W ", *obj)
        localtime = time.localtime(time.time())
        stackinfo = traceback.extract_stack()
        who = stackinfo[1][2]
        line = stackinfo[1][1]
        # console.print("[black on green] I ", *obj)
        print(
            f"[{localtime[3]:0>2}:{localtime[4]:0>2}:{localtime[5]:0>2}] [{who:>20} |{line:>5} ] [WARN]", *obj)
 
    def error(*obj):
        # console.log("[black on red] E ", *obj)
        localtime = time.localtime(time.time())
        stackinfo = traceback.extract_stack()
        who = stackinfo[1][2]
        line = stackinfo[1][1]
        # console.print("[black on green] I ", *obj)
        print(
            f"[{localtime[3]:0>2}:{localtime[4]:0>2}:{localtime[5]:0>2}] [{who:>20} |{line:>5} ] [ERROR]", *obj)
 
    def readData():
        try:
            with open(".hj.json") as j:
                data = load(j)
                # data["mclist"] = minecraft_launcher_lib.utils.get_installed_versions(
                # data["mcdirs"])
                info("Read File Succ")
        except:
            warn("File Not Found ignore it")
            temp = {}
            temp["mcdirs"] = minecraft_launcher_lib.utils.get_minecraft_directory()
            temp["user"] = "Launcher"
            temp["theme"] = list_themes()[0]
            # temp["mclist"] = minecraft_launcher_lib.utils.get_installed_versions(
            # temp["mcdirs"])
            with open(".hj.json", 'w') as j:
                dump(temp, j)
            data = temp
        return data
 
    def reloadver():
        alllist = minecraft_launcher_lib.utils.get_version_list()
        ver = []
        for i in alllist:
            if(i["type"] == "snapshot"):
                ver.append(i["id"])
            elif(i["type"] == "release"):
                ver.append(i["id"])
            else:
                ver.append(i["id"])
 
        return ver
 
    info("Launcher is Launching")
 
    def stop_thread(thread):
        """终止线程"""
        _async_raise(thread.ident, SystemExit)
 
    class IoThread(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.data = ""
            self.counter = 0
 
        def run(self):
            info("Start IoThread")
            while(FLAG):
                if(self.counter == 1):
                    # print("Counter!")
                    self.data = readData()
                    # self.reloadver()
                    MyMainForm.apiSetConf(self, self.data)
                if(self.counter >= 6000):
                    self.counter = 0
                    # print("s")
                self.counter += 1
                sleep(0.1)
                # print(self.counter)
 
    class MyMainForm(QMainWindow, Ui_MainWindow):
        def __init__(self, Parent=None):
            global myWin
            global verlistpub
            global app
            super(MyMainForm, self).__init__(Parent)
            self.setupUi(self)
            self.mclist = []
            # self.setWindowFlags(Qt.FramelessWindowHint)  # Hide Board
            self.tabWidget.currentChanged.connect(self.tabchange)
            self.launchGameBtn.clicked.connect(self.launchGameFunc)
            self.conf = readData()
            if(not os.path.exists(self.conf["mcdirs"])):
                error("Folder Is NOT FOUND")
                warn("Not Found Ignore it")
                self.conf["mcdirs"] = minecraft_launcher_lib.utils.get_minecraft_directory()
                with open('./.hj.json', 'w') as f:
                    dump(self.conf, f)
 
            self.conf = readData()
            self.userName.setText(self.conf["user"])
            self.userName.editingFinished.connect(self.setUserText)
            self.label_4.setWordWrap(True)
            self.stauts.setWordWrap(True)
            self.stauts.setAlignment(QtCore.Qt.AlignTop)
            self.mcDirText.setText(self.conf["mcdirs"])
            self.setMcDirButton.clicked.connect(self.setMcDir)
            self.label_4.setAlignment(QtCore.Qt.AlignTop)
            # self.closeButton.clicked.connect(self.closeFunc)
            try:
                self.choiceVer = self.mclist[0]["id"]
            except:
                pass
            self.ttemp = reloadver()
            for i in self.ttemp:
                self.selectInstallVersionBox.addItem(i)
            self.installGameButton.clicked.connect(self.installGameFunc)
            self.selectVersionBox.activated[str].connect(self.setMcVersion)
            self.styleBox.activated[str].connect(self.changeThemes)
            self.selectInstallVersionBox.activated[str].connect(
                self.setinstallMcVersion)
            self.version = "1.1.1"
            self.choiceTheme = self.conf["theme"]
            for i in list_themes():
                self.styleBox.addItem(i)
            self.threadpool = []
            try:
                self.mclist = minecraft_launcher_lib.utils.get_installed_versions(
                    self.conf["mcdirs"])
            except:
                pass
            self.lock = False
            self.desc = ""
            self.progress = 0
            # self.ttemp = reloadver()
            self.current_max = 0
            for i in self.mclist:
                self.selectVersionBox.addItem(i["id"])
            # self.setsText("asdfasdflkahsdfkjahsdf")
            self.threadpool.append(IoThread())
            for index in range(len(self.threadpool)):
                self.threadpool[index].start()
            self.installchoiceVer = self.ttemp[0]
            # .stauts.setText("sadfasdf")
 
        # def mousePressEvent(self, event):
        #     if event.button() == Qt.LeftButton:
        #         self.m_flag = True
        #         self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
        #         event.accept()
        #         self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
 
        # def mouseMoveEvent(self, QMouseEvent):
        #     if Qt.LeftButton and self.m_flag:
        #         self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
        #         QMouseEvent.accept()
 
        # def mouseReleaseEvent(self, QMouseEvent):
        #     self.m_flag = False
        #     self.setCursor(QCursor(Qt.ArrowCursor))
            try:
                apply_stylesheet(app, theme=self.conf["theme"])
                info("Succ Load Theme!")
            except:
                error(
                    f"The Launcher is Not Supported This Theme:{self.conf['theme']}")
                self.conf["theme"] = list_themes()[0]
                info(f"Change Theme:{self.conf['theme']}")
                apply_stylesheet(app, theme=self.conf["theme"])
                with open("./.hj.json", 'w') as f:
                    dump(self.conf, f)
 
        def setMcDir(self):
            result = QFileDialog.getExistingDirectory(
                None, "选取我的世界目录", self.conf["mcdirs"])
            info("Dir:", result)
            if(result is None or result == ""):
                warn("The Folder is Not Found")
            else:
                self.conf["mcdirs"] = result
                with open("./.hj.json", 'w') as f:
                    dump(self.conf, f)
            self.conf = readData()
            self.mcDirText.setText(self.conf["mcdirs"])
 
        def tabchange(self):
            index = self.tabWidget.currentIndex()
            info(f"Tab is Changed! Tabindex:{index}")
            # if self.tabWidget.currentIndex()==0
            if index == 1:
                pass
                # self.ttemp = reloadver()
                # for i in self.ttemp:
                #     self.selectInstallVersionBox.addItem(i)
            elif index == 0:
                try:
                    self.mclist = minecraft_launcher_lib.utils.get_installed_versions(
                        self.conf["mcdirs"])
                except:
                    self.mclist = []
                try:
                    self.choiceVer = self.mclist[0]["id"]
                except:
                    pass
                self.selectVersionBox.clear()
                for i in self.mclist:
                    self.selectVersionBox.addItem(i["id"])
 
        def installGameFunc(self):
            global ILOCK
            if(not ILOCK):
                ILOCK = True
                self.setTipText("准备安装版本:{}".format(self.installchoiceVer))
                info("Start install Version:{}".format(self.installchoiceVer))
                installmc = InstallMc(
                    self.installchoiceVer, self.conf["mcdirs"])
                installmc.start()
                self.setTipText("安装中...")
 
            else:
                self.setTipText("安装正在运行，请等待安装结束")
                warn("It's installing!")
 
        def changeThemes(self, text):
            global app
            self.conf["theme"] = text
            info(f"Change Theme:{text}")
            apply_stylesheet(app, theme=self.conf["theme"])
            with open("./.hj.json", 'w') as f:
                dump(self.conf, f)
 
        def setTipText(self, text):
            self.stauts.setText(text)
 
        def setUserText(self):
            self.conf["user"] = "".join(self.userName.text().split(" "))
            with open(".hj.json", 'w') as j:
                dump(self.conf, j)
 
        def setinstallMcVersion(self, text):
            self.installchoiceVer = text
            # print(text)
 
        def setMcVersion(self, text):
            self.choiceVer = text
            # print(text)
 
        def launchGameFunc(self):
            global LOCK
            if(not LOCK):
                LOCK = True
                info("Run Mc")
                self.setTipText("游戏启动中...")
                mc = RunMc(
                    self.choiceVer, self.conf["mcdirs"], self.userName.text(), "8888-8888-8888")
                mc.start()
                self.setTipText("游戏已启动等待游戏窗口出现...")
                info(self.userName.text())
 
            else:
                self.setTipText("游戏正在运行，请等待游戏结束")
                warn("The Game is running but User want to Creat NEW game thread!")
                warn("New Thread is kill by USER")
 
        def closeEvent(self, event):
            global FLAG
            FLAG = False
            for index in range(len(self.threadpool)):
                stop_thread(self.threadpool[index])
 
        def apiSetConf(self, conf: dict):
            self.config = conf
 
    class InstallMc(Thread):
        def __init__(self, version, mcdir):
            Thread.__init__(self)
            self.version = version
            self.mcdir = mcdir
            self.desc = ""
            self.current_max = 0
            self.progress = 0
 
        def set_max(self, new_max: int):
            self.current_max = new_max
            info(f"{self.desc} Finish")
            info("Start New Task!")
 
        def set_status(self, status: str):
            self.desc = status
            info(f"Change Task To:{status}")
 
        def set_progress(self, progress: int):
            global myWin
            if self.current_max != 0:
                self.progress = progress
                myWin.stauts.setText(
                    f"下载中: 已下载:{progress} 未下载:{self.current_max-progress}")
                info(
                    f"{self.desc}: Progress:{progress} Total:{self.current_max}")
                # MyMainForm.setTipText(MyMainForm, "s")
 
        def run(self):
            global ILOCK, myWin
            callback = {
                "setStatus": self.set_status,
                "setProgress": self.set_progress,
                "setMax": self.set_max
            }
            try:
                minecraft_launcher_lib.install.install_minecraft_version(
                    self.version, self.mcdir, callback)
                info(f"Succ Install Version:{self.version}")
                ILOCK = False
                myWin.stauts.setText(f"成功安装版本:{self.version}")
            except:
                myWin.stauts.setText("安装异常,未知版本!")
 
    class RunMc(Thread):
        def __init__(self, version, mcdir, username, uuuid):
            Thread.__init__(self)
            self.version = version
            self.mcdir = mcdir
            self.username = username
            self.uuid = uuuid
            self.desc = ""
            self.current_max = 0
            self.progress = 0
 
        def set_max(self, new_max: int):
            self.current_max = new_max
            info("Download Finish")
            info("Start New Task!")
 
        def set_status(self, status: str):
            self.desc = status
            info(f"Change Task To:{status}")
 
        def set_progress(self, progress: int):
            if self.current_max != 0:
                self.progress = progress
                myWin.stauts.setText(
                    f"启动中: 已准备:{progress} 未准备:{self.current_max-progress}")
                info(
                    f"{self.desc}: Progress:{progress} Total:{self.current_max}")
 
        def run(self):
            global LOCK
            callback = {
                "setStatus": self.set_status,
                "setProgress": self.set_progress,
                "setMax": self.set_max
            }
            try:
                minecraft_launcher_lib.install.install_minecraft_version(
                    self.version, self.mcdir, callback)
                options = {
                    "username": self.username,
                    "uuid": self.uuid,
                    "token": self.uuid,
                    "-Dminecraft.launcher.brand": "Huaji Launcher",
                    "-Dminecraft.launcher.version": "1.1.1"
                    # "launcherName": "PMCL",  # The name of your launcher
                    # "launcherVersion": "1.1",  # The version of your launcher
                }
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                    self.version, self.mcdir, options)
                myWin.stauts.setText("成功生成启动命令")
                # 最终，你可以直接启动Minecraft了
                subprocess.call(minecraft_command)
                info("Run Minecraft Command with:{}".format(minecraft_command))
                info("Mc is Run!")
                info("----------Log With Mc-----------")
                myWin.stauts.setText("等待游戏窗口出现...")
                subprocess.call(
                    minecraft_command)
                LOCK = False
                myWin.stauts.setText("游戏已退出")
            except:
                myWin.stauts.setText("安装异常,未知版本!")
 
    if __name__ == "__main__":
 
        # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
        app = QApplication(sys.argv)
        # 初始化
        myWin = MyMainForm()
        # 将窗口控件显示在屏幕上
        myWin.show()
        # 程序运行，sys.exit方法确保程序完整退出。
        sys.exit(app.exec_())
except SystemExit:
    pass
except:
    error("Launcher Error:")
    error("Looking For Trace Back:")
    console.print_exception(show_locals=True)
 