# Form implementation generated from reading ui file '/Users/dcboy/Desktop/pml/main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
 
 
from PyQt6 import QtCore, QtGui, QtWidgets
 
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 345)
        MainWindow.setMinimumSize(QtCore.QSize(389, 345))
        MainWindow.setMaximumSize(QtCore.QSize(389, 345))
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 8, 371, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 211))
        self.groupBox.setObjectName("groupBox")
        self.selectVersionBox = QtWidgets.QComboBox(self.groupBox)
        self.selectVersionBox.setGeometry(QtCore.QRect(80, 31, 191, 41))
        self.selectVersionBox.setObjectName("selectVersionBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 60, 21))
        self.label.setObjectName("label")
        self.launchGameBtn = QtWidgets.QPushButton(self.groupBox)
        self.launchGameBtn.setGeometry(QtCore.QRect(190, 150, 141, 51))
        self.launchGameBtn.setObjectName("launchGameBtn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 341, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.selectInstallVersionBox = QtWidgets.QComboBox(self.groupBox_2)
        self.selectInstallVersionBox.setGeometry(QtCore.QRect(10, 40, 321, 41))
        self.selectInstallVersionBox.setObjectName("selectInstallVersionBox")
        self.installGameButton = QtWidgets.QPushButton(self.groupBox_2)
        self.installGameButton.setGeometry(QtCore.QRect(12, 90, 131, 32))
        self.installGameButton.setObjectName("installGameButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 341, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.userName = QtWidgets.QLineEdit(self.groupBox_3)
        self.userName.setGeometry(QtCore.QRect(90, 30, 241, 31))
        self.userName.setObjectName("userName")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 90, 341, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_3.setObjectName("label_3")
        self.mcDirText = QtWidgets.QLabel(self.groupBox_4)
        self.mcDirText.setGeometry(QtCore.QRect(50, 30, 281, 16))
        self.mcDirText.setObjectName("mcDirText")
        self.setMcDirButton = QtWidgets.QPushButton(self.groupBox_4)
        self.setMcDirButton.setGeometry(QtCore.QRect(12, 50, 321, 32))
        self.setMcDirButton.setObjectName("setMcDirButton")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 190, 201, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.styleBox = QtWidgets.QComboBox(self.groupBox_5)
        self.styleBox.setGeometry(QtCore.QRect(10, 30, 181, 32))
        self.styleBox.setObjectName("styleBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.stauts = QtWidgets.QLabel(self.centralwidget)
        self.stauts.setGeometry(QtCore.QRect(60, 310, 321, 31))
        self.stauts.setObjectName("stauts")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 41, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Launcher Main"))
        self.groupBox.setTitle(_translate("MainWindow", "启动"))
        self.label.setText(_translate("MainWindow", "选择版本"))
        self.launchGameBtn.setText(_translate("MainWindow", "启动游戏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主页面"))
        self.groupBox_2.setTitle(_translate("MainWindow", "安装版本"))
        self.installGameButton.setText(_translate("MainWindow", "安装"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "下载"))
        self.groupBox_3.setTitle(_translate("MainWindow", "用户"))
        self.label_2.setText(_translate("MainWindow", "用户名"))
        self.groupBox_4.setTitle(_translate("MainWindow", "MC文件夹"))
        self.label_3.setText(_translate("MainWindow", "当前"))
        self.mcDirText.setText(_translate("MainWindow", "NONE"))
        self.setMcDirButton.setText(_translate("MainWindow", "选择..."))
        self.groupBox_5.setTitle(_translate("MainWindow", "主题样式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "设置"))
        self.stauts.setText(_translate("MainWindow", "启动启动器"))
        self.label_4.setText(_translate("MainWindow", "状态:"))
 