# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 603)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 5, 11, 5)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboCamera = QtWidgets.QComboBox(self.groupBox_2)
        self.comboCamera.setMinimumSize(QtCore.QSize(150, 20))
        self.comboCamera.setObjectName("comboCamera")
        self.gridLayout.addWidget(self.comboCamera, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.splitter.setStretchFactor(1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(476, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.viewFinder = QCameraViewfinder(self.groupBox)
        self.viewFinder.setMinimumSize(QtCore.QSize(0, 0))
        self.viewFinder.setObjectName("viewFinder")
        self.gridLayout_2.addWidget(self.viewFinder, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_3.setMinimumSize(QtCore.QSize(476, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LabImage = QtWidgets.QLabel(self.groupBox_3)
        self.LabImage.setMinimumSize(QtCore.QSize(0, 0))
        self.LabImage.setAlignment(QtCore.Qt.AlignCenter)
        self.LabImage.setObjectName("LabImage")
        self.verticalLayout_2.addWidget(self.LabImage)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 963, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actStartCamera = QtWidgets.QAction(MainWindow)
        self.actStartCamera.setEnabled(False)
        self.actStartCamera.setObjectName("actStartCamera")
        self.actStopCamera = QtWidgets.QAction(MainWindow)
        self.actStopCamera.setEnabled(False)
        self.actStopCamera.setObjectName("actStopCamera")
        self.actCapture = QtWidgets.QAction(MainWindow)
        self.actCapture.setEnabled(False)
        self.actCapture.setObjectName("actCapture")
        self.actQuit = QtWidgets.QAction(MainWindow)
        self.actQuit.setObjectName("actQuit")
        self.mainToolBar.addAction(self.actStartCamera)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actStopCamera)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actCapture)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "camera"))
        self.label.setText(_translate("MainWindow", "摄像头设备"))
        self.groupBox.setTitle(_translate("MainWindow", "摄像头预览"))
        self.groupBox_3.setTitle(_translate("MainWindow", "抓取的图片"))
        self.LabImage.setText(_translate("MainWindow", "抓取的图片"))
        self.actStartCamera.setText(_translate("MainWindow", "开启摄像头"))
        self.actStartCamera.setToolTip(_translate("MainWindow", "开启摄像头"))
        self.actStopCamera.setText(_translate("MainWindow", "关闭摄像头"))
        self.actStopCamera.setToolTip(_translate("MainWindow", "关闭摄像头"))
        self.actCapture.setText(_translate("MainWindow", "拍照"))
        self.actCapture.setToolTip(_translate("MainWindow", "拍照"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出"))
#from QCameraViewfinder import QCameraViewfinder
# import res_rc
