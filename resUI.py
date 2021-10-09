# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resUI2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.group_setting = QGroupBox(self.centralwidget)
        self.group_setting.setObjectName(u"group_setting")
        self.group_setting.setEnabled(False)
        self.group_setting.setGeometry(QRect(9, 9, 781, 321))
        self.verticalLayoutWidget = QWidget(self.group_setting)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 501, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.input_input = QLineEdit(self.verticalLayoutWidget)
        self.input_input.setObjectName(u"input_input")

        self.horizontalLayout_2.addWidget(self.input_input)

        self.btn_openInput = QPushButton(self.verticalLayoutWidget)
        self.btn_openInput.setObjectName(u"btn_openInput")

        self.horizontalLayout_2.addWidget(self.btn_openInput)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.input_output = QLineEdit(self.verticalLayoutWidget)
        self.input_output.setObjectName(u"input_output")

        self.horizontalLayout_3.addWidget(self.input_output)

        self.btn_openOutput = QPushButton(self.verticalLayoutWidget)
        self.btn_openOutput.setObjectName(u"btn_openOutput")

        self.horizontalLayout_3.addWidget(self.btn_openOutput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayoutWidget_5 = QWidget(self.group_setting)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 130, 341, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.input_width = QLineEdit(self.horizontalLayoutWidget_5)
        self.input_width.setObjectName(u"input_width")

        self.horizontalLayout_5.addWidget(self.input_width)

        self.label_8 = QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.input_height = QLineEdit(self.horizontalLayoutWidget_5)
        self.input_height.setObjectName(u"input_height")

        self.horizontalLayout_4.addWidget(self.input_height)

        self.label_3 = QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayoutWidget_6 = QWidget(self.group_setting)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 170, 341, 41))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.input_maxWidth = QLineEdit(self.horizontalLayoutWidget_6)
        self.input_maxWidth.setObjectName(u"input_maxWidth")

        self.horizontalLayout_12.addWidget(self.input_maxWidth)

        self.label_15 = QLabel(self.horizontalLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.horizontalLayoutWidget_6)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.input_maxHeight = QLineEdit(self.horizontalLayoutWidget_6)
        self.input_maxHeight.setObjectName(u"input_maxHeight")

        self.horizontalLayout_13.addWidget(self.input_maxHeight)

        self.label_17 = QLabel(self.horizontalLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)

        self.horizontalLayoutWidget_7 = QWidget(self.group_setting)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 220, 311, 41))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.horizontalLayoutWidget_7)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_14.addWidget(self.label_18)

        self.input_jpgeQuality = QLineEdit(self.horizontalLayoutWidget_7)
        self.input_jpgeQuality.setObjectName(u"input_jpgeQuality")

        self.horizontalLayout_14.addWidget(self.input_jpgeQuality)

        self.label_19 = QLabel(self.horizontalLayoutWidget_7)
        self.label_19.setObjectName(u"label_19")
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setTextFormat(Qt.PlainText)

        self.horizontalLayout_14.addWidget(self.label_19)

        self.horizontalLayoutWidget_8 = QWidget(self.group_setting)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 270, 311, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.horizontalLayoutWidget_8)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.input_pngCompression = QLineEdit(self.horizontalLayoutWidget_8)
        self.input_pngCompression.setObjectName(u"input_pngCompression")

        self.horizontalLayout_15.addWidget(self.input_pngCompression)

        self.label_21 = QLabel(self.horizontalLayoutWidget_8)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_15.addWidget(self.label_21)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 360, 781, 192))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(650, 250, 120, 60))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u538b\u7f29 - \u652f\u6301JPGE\u3001JPG\u3001PNG\u3001TGA\u683c\u5f0f 作者：lookingai.com", None))
        self.group_setting.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u76ee\u5f55", None))
        self.btn_openInput.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.btn_openOutput.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5bbd\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u9ad8\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6\u9608\u503c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5ea6\u9608\u503c", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"JPGE\u8f93\u51fa\u8d28\u91cf", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0-100 \u8d8a\u5927\u8d28\u91cf\u8d8a\u597d", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"PNG\u8f93\u51fa\u8d28\u91cf ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0-10 \u8d8a\u5c0f\u8d28\u91cf\u8d8a\u597d ", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
    # retranslateUi

