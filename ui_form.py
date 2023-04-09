# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QCheckBox,
    QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Adofai2Taiko(object):
    def setupUi(self, Adofai2Taiko):
        if not Adofai2Taiko.objectName():
            Adofai2Taiko.setObjectName(u"Adofai2Taiko")
        Adofai2Taiko.resize(618, 463)
        self.centralwidget = QWidget(Adofai2Taiko)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 601, 91))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 581, 65))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.adofaiFile = QLineEdit(self.layoutWidget)
        self.adofaiFile.setObjectName(u"adofaiFile")
        self.adofaiFile.setReadOnly(True)

        self.horizontalLayout.addWidget(self.adofaiFile)

        self.adofaiFileButton = QToolButton(self.layoutWidget)
        self.adofaiFileButton.setObjectName(u"adofaiFileButton")

        self.horizontalLayout.addWidget(self.adofaiFileButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.musicFile = QLineEdit(self.layoutWidget)
        self.musicFile.setObjectName(u"musicFile")
        self.musicFile.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.musicFile)

        self.musicFileButton = QToolButton(self.layoutWidget)
        self.musicFileButton.setObjectName(u"musicFileButton")

        self.horizontalLayout_2.addWidget(self.musicFileButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(520, 410, 93, 29))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 110, 601, 191))
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(12, 21, 581, 168))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.song = QLineEdit(self.layoutWidget_2)
        self.song.setObjectName(u"song")

        self.horizontalLayout_3.addWidget(self.song)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.songOrg = QLineEdit(self.layoutWidget_2)
        self.songOrg.setObjectName(u"songOrg")

        self.horizontalLayout_4.addWidget(self.songOrg)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.artist = QLineEdit(self.layoutWidget_2)
        self.artist.setObjectName(u"artist")

        self.horizontalLayout_5.addWidget(self.artist)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.artistOrg = QLineEdit(self.layoutWidget_2)
        self.artistOrg.setObjectName(u"artistOrg")

        self.horizontalLayout_6.addWidget(self.artistOrg)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.creator = QLineEdit(self.layoutWidget_2)
        self.creator.setObjectName(u"creator")

        self.horizontalLayout_7.addWidget(self.creator)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.offset = QSpinBox(self.layoutWidget_2)
        self.offset.setObjectName(u"offset")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offset.sizePolicy().hasHeightForWidth())
        self.offset.setSizePolicy(sizePolicy)
        self.offset.setMinimum(-10000)
        self.offset.setMaximum(10000)
        self.offset.setValue(0)

        self.horizontalLayout_9.addWidget(self.offset)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.bpm = QDoubleSpinBox(self.layoutWidget_2)
        self.bpm.setObjectName(u"bpm")
        sizePolicy.setHeightForWidth(self.bpm.sizePolicy().hasHeightForWidth())
        self.bpm.setSizePolicy(sizePolicy)
        self.bpm.setMinimum(0.000000000000000)
        self.bpm.setMaximum(10000.000000000000000)

        self.horizontalLayout_8.addWidget(self.bpm)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_8)

        self.isChangeBPM = QCheckBox(self.layoutWidget_2)
        self.isChangeBPM.setObjectName(u"isChangeBPM")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.isChangeBPM.sizePolicy().hasHeightForWidth())
        self.isChangeBPM.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.isChangeBPM)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.volume = QSpinBox(self.layoutWidget_2)
        self.volume.setObjectName(u"volume")
        sizePolicy.setHeightForWidth(self.volume.sizePolicy().hasHeightForWidth())
        self.volume.setSizePolicy(sizePolicy)
        self.volume.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.volume.setMaximum(100)
        self.volume.setValue(100)

        self.horizontalLayout_13.addWidget(self.volume)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 310, 601, 91))
        self.layoutWidget_3 = QWidget(self.groupBox_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 20, 581, 61))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.layoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.withSpeed = QRadioButton(self.layoutWidget_3)
        self.buttonGroup = QButtonGroup(Adofai2Taiko)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.withSpeed)
        self.withSpeed.setObjectName(u"withSpeed")
        self.withSpeed.setChecked(True)

        self.horizontalLayout_11.addWidget(self.withSpeed)

        self.dong = QRadioButton(self.layoutWidget_3)
        self.buttonGroup.addButton(self.dong)
        self.dong.setObjectName(u"dong")

        self.horizontalLayout_11.addWidget(self.dong)

        self.ka = QRadioButton(self.layoutWidget_3)
        self.buttonGroup.addButton(self.ka)
        self.ka.setObjectName(u"ka")

        self.horizontalLayout_11.addWidget(self.ka)

        self.random = QRadioButton(self.layoutWidget_3)
        self.buttonGroup.addButton(self.random)
        self.random.setObjectName(u"random")

        self.horizontalLayout_11.addWidget(self.random)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.layoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.beginBar = QSpinBox(self.layoutWidget_3)
        self.beginBar.setObjectName(u"beginBar")
        sizePolicy.setHeightForWidth(self.beginBar.sizePolicy().hasHeightForWidth())
        self.beginBar.setSizePolicy(sizePolicy)
        self.beginBar.setValue(1)

        self.horizontalLayout_12.addWidget(self.beginBar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        Adofai2Taiko.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Adofai2Taiko)
        self.statusbar.setObjectName(u"statusbar")
        Adofai2Taiko.setStatusBar(self.statusbar)

        self.retranslateUi(Adofai2Taiko)

        QMetaObject.connectSlotsByName(Adofai2Taiko)
    # setupUi

    def retranslateUi(self, Adofai2Taiko):
        Adofai2Taiko.setWindowTitle(QCoreApplication.translate("Adofai2Taiko", u"Adofai2Taiko", None))
        self.groupBox.setTitle(QCoreApplication.translate("Adofai2Taiko", u"\u5bfc\u5165", None))
        self.label.setText(QCoreApplication.translate("Adofai2Taiko", u"ADOFAI\u8c31\u9762\u6587\u4ef6", None))
        self.adofaiFileButton.setText(QCoreApplication.translate("Adofai2Taiko", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Adofai2Taiko", u"\u97f3\u4e50\u6587\u4ef6", None))
        self.musicFileButton.setText(QCoreApplication.translate("Adofai2Taiko", u"...", None))
        self.generateButton.setText(QCoreApplication.translate("Adofai2Taiko", u"\u751f\u6210", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Adofai2Taiko", u"\u8c31\u9762\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Adofai2Taiko", u"\u6b4c\u66f2", None))
        self.label_4.setText(QCoreApplication.translate("Adofai2Taiko", u"\u6b4c\u66f2\u539f\u6587", None))
        self.label_5.setText(QCoreApplication.translate("Adofai2Taiko", u"\u4f5c\u66f2\u5bb6", None))
        self.label_6.setText(QCoreApplication.translate("Adofai2Taiko", u"\u4f5c\u66f2\u5bb6\u539f\u6587", None))
        self.label_7.setText(QCoreApplication.translate("Adofai2Taiko", u"\u8c31\u9762\u4f5c\u8005", None))
        self.label_9.setText(QCoreApplication.translate("Adofai2Taiko", u"\u504f\u79fb", None))
        self.label_8.setText(QCoreApplication.translate("Adofai2Taiko", u"BPM", None))
        self.isChangeBPM.setText(QCoreApplication.translate("Adofai2Taiko", u"\u662f\u5426\u4e3a\u53d8\u901f\u66f2\uff1f", None))
        self.label_12.setText(QCoreApplication.translate("Adofai2Taiko", u"\u97f3\u91cf", None))
        self.volume.setSuffix(QCoreApplication.translate("Adofai2Taiko", u"%", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Adofai2Taiko", u"\u5176\u4ed6\u8bbe\u7f6e", None))
        self.label_10.setText(QCoreApplication.translate("Adofai2Taiko", u"\u549a/\u5494\u8bbe\u7f6e", None))
        self.withSpeed.setText(QCoreApplication.translate("Adofai2Taiko", u"\u968f\u901f\u5ea6\u53d8\u5316", None))
        self.dong.setText(QCoreApplication.translate("Adofai2Taiko", u"\u549a", None))
        self.ka.setText(QCoreApplication.translate("Adofai2Taiko", u"\u5494", None))
        self.random.setText(QCoreApplication.translate("Adofai2Taiko", u"\u968f\u673a", None))
        self.label_11.setText(QCoreApplication.translate("Adofai2Taiko", u"\u8c31\u9762\u5f00\u59cb\u5c0f\u8282", None))
    # retranslateUi

