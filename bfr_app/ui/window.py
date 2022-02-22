# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(550, 369)
        self.layoutWidget = QtWidgets.QWidget(Window)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 526, 344))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.dirEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.dirEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dirEdit.setMaxLength(30)
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setObjectName("dirEdit")
        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 2)
        self.loadFilesButton = QtWidgets.QPushButton(self.layoutWidget)
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.gridLayout.addWidget(self.loadFilesButton, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.srcFileList = QtWidgets.QListWidget(self.layoutWidget)
        self.srcFileList.setObjectName("srcFileList")
        self.verticalLayout.addWidget(self.srcFileList)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dstFileList = QtWidgets.QListWidget(self.layoutWidget)
        self.dstFileList.setObjectName("dstFileList")
        self.verticalLayout_2.addWidget(self.dstFileList)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 3)
        self.prefixEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.prefixEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.prefixEdit.setMaxLength(30)
        self.prefixEdit.setReadOnly(False)
        self.prefixEdit.setObjectName("prefixEdit")
        self.gridLayout.addWidget(self.prefixEdit, 4, 0, 1, 1)
        self.extensionLabel = QtWidgets.QLabel(self.layoutWidget)
        self.extensionLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.extensionLabel.setObjectName("extensionLabel")
        self.gridLayout.addWidget(self.extensionLabel, 4, 1, 1, 1)
        self.renameFilesButton = QtWidgets.QPushButton(self.layoutWidget)
        self.renameFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.renameFilesButton.setObjectName("renameFilesButton")
        self.gridLayout.addWidget(self.renameFilesButton, 4, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setMinimum(30)
        self.progressBar.setProperty("value", 29)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Form"))
        self.label.setText(_translate("Window", "Last Source Directory"))
        self.loadFilesButton.setText(_translate("Window", "&Load Files"))
        self.label_2.setText(_translate("Window", "Files to Rename"))
        self.label_3.setText(_translate("Window", "Renamed Files"))
        self.label_4.setText(_translate("Window", "Filename Prefix"))
        self.prefixEdit.setPlaceholderText(_translate("Window", "Rename your files to ..."))
        self.extensionLabel.setText(_translate("Window", "*.jpg"))
        self.renameFilesButton.setText(_translate("Window", "&Rename"))
