# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MailAutomate.ui'
#
# Created: Thu Aug 23 17:41:11 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.templateCtrlBar = QtWidgets.QWidget(self.page)
        self.templateCtrlBar.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.templateCtrlBar.setObjectName("templateCtrlBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.templateCtrlBar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_5 = QtWidgets.QToolButton(self.templateCtrlBar)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_3.addWidget(self.toolButton_5)
        self.toolButton_6 = QtWidgets.QToolButton(self.templateCtrlBar)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_3.addWidget(self.toolButton_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.templateCtrlBar)
        self.templateEditor = QtWidgets.QTextEdit(self.page)
        self.templateEditor.setObjectName("templateEditor")
        self.verticalLayout_3.addWidget(self.templateEditor)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.csvEditor = QtWidgets.QColumnView(self.page_2)
        self.csvEditor.setObjectName("csvEditor")
        self.verticalLayout_4.addWidget(self.csvEditor)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 16))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.csvDockView = QtWidgets.QDockWidget(MainWindow)
        self.csvDockView.setBaseSize(QtCore.QSize(45, 0))
        self.csvDockView.setStyleSheet("")
        self.csvDockView.setObjectName("csvDockView")
        self.csvDockContents = QtWidgets.QWidget()
        self.csvDockContents.setObjectName("csvDockContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.csvDockContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.csvList = QtWidgets.QListView(self.csvDockContents)
        self.csvList.setObjectName("csvList")
        self.verticalLayout.addWidget(self.csvList)
        self.csvListCtrlBar = QtWidgets.QWidget(self.csvDockContents)
        self.csvListCtrlBar.setObjectName("csvListCtrlBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.csvListCtrlBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton(self.csvListCtrlBar)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(self.csvListCtrlBar)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.csvListCtrlBar)
        self.csvDockView.setWidget(self.csvDockContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.csvDockView)
        self.templateDockView = QtWidgets.QDockWidget(MainWindow)
        self.templateDockView.setBaseSize(QtCore.QSize(45, 0))
        self.templateDockView.setStyleSheet("")
        self.templateDockView.setObjectName("templateDockView")
        self.templateDockContents = QtWidgets.QWidget()
        self.templateDockContents.setObjectName("templateDockContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.templateDockContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.templateList = QtWidgets.QListView(self.templateDockContents)
        self.templateList.setObjectName("templateList")
        self.verticalLayout_2.addWidget(self.templateList)
        self.templateListCtrlBar = QtWidgets.QWidget(self.templateDockContents)
        self.templateListCtrlBar.setObjectName("templateListCtrlBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.templateListCtrlBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.templateListCtrlBar)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.toolButton_4 = QtWidgets.QToolButton(self.templateListCtrlBar)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_2.addWidget(self.toolButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.templateListCtrlBar)
        self.templateDockView.setWidget(self.templateDockContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.templateDockView)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.toolButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.toolButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.toolButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.toolButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.toolButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))

