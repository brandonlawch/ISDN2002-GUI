# -*- coding: utf-8 -*-
################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import files_rc
from app_modules import *
from ui_functions import PyToggle

class Validator(QtGui.QValidator):
    def validate(self, string, pos):
        return QtGui.QValidator.Acceptable, string.lower(), pos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.validator = Validator(MainWindow)
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
# "/* CHECKBOX */\n"
# "QCheckBox::indicator {\n"
# "    border: 3px solid rgb(52, 59, 72);\n"
# "	width: 15px;\n"
# "	height: 15px;\n"
# "	border-radius: 10px;\n"
# "    background: rgb(44, 49, 60);\n"
# "}\n"
# "QCheckBox::indicator:hover {\n"
# "    border: 3px solid rgb(58, 66, 81);\n"
# "}\n"
# "QCheckBox::indicator:checked {\n"
# "    background: 3px solid rgb(52, 59, 72);\n"
# "	border: 3px solid rgb(52, 59, 72);	\n"
# "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
# "}\n"
# "\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-settings.png);\n" 
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\ncolor: rgb(115, 230, 223);"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(180, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(0)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        ########################################################################
        #                                                                      #
        ## START    -------------- PAGE_HOME DEFINITION ----------------      ##
        #                                                                      #
        ## 001                                                                ##
        ########################################################################
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        ##########
        self.label_002 = QLabel(self.page_home)
        self.label_002.setObjectName(u"label_002")
        font003 = QFont()
        font003.setFamily(u"Roboto Thin")
        font003.setPointSize(30)
        self.label_002.setFont(font003)
        self.label_002.setStyleSheet(u"")
        self.verticalLayout_10.addWidget(self.label_002, alignment=Qt.AlignCenter)
        ##########
        self.pushButton_confirm = QPushButton(self.page_home)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setMinimumSize(QSize(130, 80))
        self.pushButton_confirm.setFixedWidth(550)
        font001 = QFont()
        font001.setFamily(u"Segoe UI")
        font001.setPointSize(15)
        self.pushButton_confirm.setFont(font001)
        self.pushButton_confirm.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon001 = QIcon()
        icon001.addFile(u":/16x16/icons/16x16/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_confirm.setIcon(icon001)
        self.pushButton_confirm.clicked.connect(MainWindow.homePageButtons)
        self.verticalLayout_10.addWidget(self.pushButton_confirm, alignment=Qt.AlignCenter)
        ##########
        self.pushButton_undo = QPushButton(self.page_home)
        self.pushButton_undo.setObjectName(u"pushButton_undo")
        self.pushButton_undo.setMinimumSize(QSize(130, 80))
        self.pushButton_undo.setFixedWidth(550)
        self.pushButton_undo.setFont(font001)
        self.pushButton_undo.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon002 = QIcon()
        icon002.addFile(u":/16x16/icons/16x16/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_undo.setIcon(icon002)
        self.pushButton_undo.clicked.connect(MainWindow.homePageButtons)
        self.verticalLayout_10.addWidget(self.pushButton_undo, alignment=Qt.AlignCenter)
        ##########
        self.pushButton_restore = QPushButton(self.page_home)
        self.pushButton_restore.setObjectName(u"pushButton_restore")
        self.pushButton_restore.setMinimumSize(QSize(130, 80))
        self.pushButton_restore.setFixedWidth(550)
        self.pushButton_restore.setFont(font001)
        self.pushButton_restore.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon003 = QIcon()
        icon003.addFile(u":/16x16/icons/16x16/cil-history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_restore.setIcon(icon003)
        self.pushButton_restore.clicked.connect(MainWindow.homePageButtons)
        self.verticalLayout_10.addWidget(self.pushButton_restore, alignment=Qt.AlignCenter)
        ##########
        self.horizontalLayout_002 = QHBoxLayout()
        self.horizontalLayout_002.setSpacing(0)
        self.horizontalLayout_002.setObjectName(u"horizontalLayout_002")
        ##########
        font004 = QFont()
        font004.setFamily(u"Roboto Thin")
        font004.setPointSize(15)
        self.label_005 = QLabel(self.page_home)
        self.label_005.setObjectName(u"label_005")
        self.label_005.setFont(font004)
        self.label_005.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.horizontalLayout_002.addWidget(self.label_005)
        ##########
        self.comboBox = QComboBox(self.page_home)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox.lineEdit().setReadOnly(True)
        self.comboBox.setFixedWidth(200)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(12)
        self.comboBox.setFont(font8)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.horizontalLayout_002.addWidget(self.comboBox)
        ##########
        self.label_006 = QLabel(self.page_home)
        self.label_006.setObjectName(u"label_006")
        self.label_006.setAlignment(Qt.AlignCenter | Qt.AlignLeft)
        self.label_006.setFixedWidth(180)
        self.horizontalLayout_002.addWidget(self.label_006)
        self.verticalLayout_10.addLayout(self.horizontalLayout_002, alignment=Qt.AlignCenter)
        ##########
        self.horizontalLayout_001 = QHBoxLayout()
        self.horizontalLayout_001.setSpacing(0)
        self.horizontalLayout_001.setObjectName(u"horizontalLayout_001")
        ##########
        font002 = QFont()
        font002.setFamily(u"Roboto Thin")
        font002.setPointSize(15)
        self.label_003 = QLabel(self.page_home)
        self.label_003.setObjectName(u"label_003")
        self.label_003.setFont(font002)
        self.label_003.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.horizontalLayout_001.addWidget(self.label_003)
        ##########
        self.toggle = PyToggle()
        self.toggle.setObjectName(u"toggle")
        self.toggle.stateChanged.connect(MainWindow.switchMode)
        self.horizontalLayout_001.addWidget(self.toggle)
        ##########
        self.label_004 = QLabel(self.page_home)
        self.label_004.setObjectName(u"label_004")
        self.label_004.setFont(font002)
        self.horizontalLayout_001.addWidget(self.label_004)
        
        self.verticalLayout_10.addLayout(self.horizontalLayout_001, alignment=Qt.AlignCenter)
        ##########
        self.label_001 = QLabel(self.page_home)
        self.label_001.setObjectName(u"label_001")
        font003 = QFont()
        font003.setFamily(u"Segoe UI")
        font003.setPointSize(15)
        self.label_001.setFont(font003)
        self.label_001.setAlignment(Qt.AlignCenter)
        self.verticalLayout_10.addWidget(self.label_001)
        ##########
        self.stackedWidget.addWidget(self.page_home)

        self.label_002.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("MainWindow", u"   Confirm Settings", None))
        self.pushButton_undo.setText(QCoreApplication.translate("MainWindow", u"   Undo Changes", None))
        self.pushButton_restore.setText(QCoreApplication.translate("MainWindow", u"   Restore Defaults", None))
        self.label_001.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_003.setText(QCoreApplication.translate("MainWindow", u"Preset Mode     ", None))
        self.label_004.setText(QCoreApplication.translate("MainWindow", u"     Freedom Mode", None))
        self.label_005.setText(QCoreApplication.translate("MainWindow", u"Excercise Intensity: ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Relaxing", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Moderate", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Intense", None))
        ########################################################################
        #                                                                      #
        ## END    --------------- PAGE_HOME DEFINITION -----------------      ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START  -------------- PAGE_LEFTHAND DEFINITION ----------------    ##
        #                                                                      #
        ## 1001                                                               ##
        ########################################################################
        self.page_leftHand = QWidget()
        self.page_leftHand.setObjectName(u"page_leftHand")
        self.gridLayout_1001 = QGridLayout(self.page_leftHand)
        self.gridLayout_1001.setObjectName(u"gridLayout_1001")
        self.gridLayout_1001.setRowStretch(0, 2)
        self.gridLayout_1001.setRowStretch(1, 1)
        self.gridLayout_1001.setRowStretch(2, 1)
        self.gridLayout_1001.setRowStretch(3, 6)
        self.gridLayout_1001.setColumnStretch(0, 5)
        self.gridLayout_1001.setColumnStretch(1, 2)
        self.gridLayout_1001.setColumnStretch(2, 4)
        ##########
        self.label_1003 = QLabel(self.page_leftHand)
        self.label_1003.setObjectName(u"label_1003")
        font1001 = QFont()
        font1001.setFamily(u"Roboto Thin")
        font1001.setPointSize(30)
        self.label_1003.setFont(font1001)
        self.label_1003.setStyleSheet(u"")
        self.gridLayout_1001.addWidget(self.label_1003, 0, 0, 1, 3)
        ##########
        font1002 = QFont()
        font1002.setFamily(u"Roboto Thin")
        font1002.setPointSize(15)
        self.label_1001 = QLabel(self.page_leftHand)
        self.label_1001.setObjectName(u"label_1001")
        self.label_1001.setFont(font1002)
        self.label_1001.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_1001.addWidget(self.label_1001, 1, 0, 1, 1)
        ##########
        font1003 = QFont()
        font1003.setFamily(u"Roboto Thin")
        font1003.setPointSize(13)
        self.lineEdit_1001 = QLineEdit(self.page_leftHand)
        self.lineEdit_1001.setObjectName(u"lineEdit_1001")
        self.lineEdit_1001.setReadOnly(True)
        self.lineEdit_1001.setFont(font1003)
        self.lineEdit_1001.setMaxLength(1)
        self.lineEdit_1001.setValidator(self.validator)
        self.lineEdit_1001.setMinimumSize(QSize(0, 30))
        self.lineEdit_1001.setMaximumWidth(220)
        self.lineEdit_1001.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_1001.addWidget(self.lineEdit_1001, 1, 1, 1, 2)
        ##########
        self.label_1002 = QLabel(self.page_leftHand)
        self.label_1002.setObjectName(u"label_1002")
        self.label_1002.setFont(font1002)
        self.label_1002.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_1001.addWidget(self.label_1002, 2, 0, 1, 1)
        ##########
        self.lineEdit_1002 = QLineEdit(self.page_leftHand)
        self.lineEdit_1002.setObjectName(u"lineEdit_1002")
        self.lineEdit_1002.setReadOnly(True)
        self.lineEdit_1002.setFont(font1003)
        self.lineEdit_1002.setMaxLength(1)
        self.lineEdit_1002.setValidator(self.validator)
        self.lineEdit_1002.setMinimumSize(QSize(0, 30))
        self.lineEdit_1002.setMaximumWidth(220)
        self.lineEdit_1002.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_1001.addWidget(self.lineEdit_1002, 2, 1, 1, 2)
        ##########
        self.stackedWidget.addWidget(self.page_leftHand)

        self.label_1003.setText(QCoreApplication.translate("MainWindow", u"Left Hand Keymappings", None))
        self.label_1001.setText(QCoreApplication.translate("MainWindow", u"Vertical Swing: ", None))
        self.lineEdit_1001.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_1002.setText(QCoreApplication.translate("MainWindow", u"Horizontal Swing: ", None))
        self.lineEdit_1002.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        ########################################################################
        #                                                                      #
        ## END  --------------- PAGE_LEFTHAND DEFINITION -----------------    ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START -------------- PAGE_CONTROLLER DEFINITION ----------------   ##
        #                                                                      #
        ## 2001                                                               ##
        ########################################################################
        self.page_controller = QWidget()
        self.page_controller.setObjectName(u"page_controller")
        self.gridLayout_2001 = QGridLayout(self.page_controller)
        self.gridLayout_2001.setObjectName(u"gridLayout_2001")
        self.gridLayout_2001.setRowStretch(0, 2)
        self.gridLayout_2001.setRowStretch(1, 1)
        self.gridLayout_2001.setRowStretch(2, 1)
        self.gridLayout_2001.setRowStretch(3, 1)
        self.gridLayout_2001.setRowStretch(4, 1)
        self.gridLayout_2001.setRowStretch(5, 1)
        self.gridLayout_2001.setRowStretch(6, 3)
        self.gridLayout_2001.setColumnStretch(0, 5)
        self.gridLayout_2001.setColumnStretch(1, 2)
        self.gridLayout_2001.setColumnStretch(2, 4)
        ##########
        self.label_2003 = QLabel(self.page_controller)
        self.label_2003.setObjectName(u"label_2003")
        font2001 = QFont()
        font2001.setFamily(u"Roboto Thin")
        font2001.setPointSize(30)
        self.label_2003.setFont(font2001)
        self.label_2003.setStyleSheet(u"")
        self.gridLayout_2001.addWidget(self.label_2003, 0, 0, 1, 3)
        ##########
        font2002 = QFont()
        font2002.setFamily(u"Roboto Thin")
        font2002.setPointSize(15)
        self.label_2001 = QLabel(self.page_controller)
        self.label_2001.setObjectName(u"label_2001")
        self.label_2001.setFont(font2002)
        self.label_2001.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_2001.addWidget(self.label_2001, 1, 0, 1, 1)
        ##########
        self.lineEdit_2001 = QLineEdit(self.page_controller)
        self.lineEdit_2001.setObjectName(u"lineEdit_2001")
        self.lineEdit_2001.setFont(font1003)
        self.lineEdit_2001.setMaxLength(1)
        self.lineEdit_2001.setValidator(self.validator)
        self.lineEdit_2001.setMinimumSize(QSize(0, 30))
        self.lineEdit_2001.setMaximumWidth(220)
        self.lineEdit_2001.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_2001.addWidget(self.lineEdit_2001, 1, 1, 1, 2)
        ##########
        self.label_2002 = QLabel(self.page_controller)
        self.label_2002.setObjectName(u"label_2002")
        self.label_2002.setFont(font2002)
        self.label_2002.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_2001.addWidget(self.label_2002, 2, 0, 1, 1)
        ##########
        self.lineEdit_2002 = QLineEdit(self.page_controller)
        self.lineEdit_2002.setObjectName(u"lineEdit_2002")
        self.lineEdit_2002.setFont(font1003)
        self.lineEdit_2002.setMaxLength(1)
        self.lineEdit_2002.setValidator(self.validator)
        self.lineEdit_2002.setMinimumSize(QSize(0, 30))
        self.lineEdit_2002.setMaximumWidth(220)
        self.lineEdit_2002.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_2001.addWidget(self.lineEdit_2002, 2, 1, 1, 2)
        ##########
        self.label_2004 = QLabel(self.page_controller)
        self.label_2004.setObjectName(u"label_2004")
        self.label_2004.setFont(font2002)
        self.label_2004.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_2001.addWidget(self.label_2004, 3, 0, 1, 1)
        ##########
        self.lineEdit_2003 = QLineEdit(self.page_controller)
        self.lineEdit_2003.setObjectName(u"lineEdit_2003")
        self.lineEdit_2003.setReadOnly(True)
        self.lineEdit_2003.setFont(font1003)
        self.lineEdit_2003.setMaxLength(1)
        self.lineEdit_2003.setValidator(self.validator)
        self.lineEdit_2003.setMinimumSize(QSize(0, 30))
        self.lineEdit_2003.setMaximumWidth(220)
        self.lineEdit_2003.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_2001.addWidget(self.lineEdit_2003, 3, 1, 1, 2)
        ##########
        self.label_2005 = QLabel(self.page_controller)
        self.label_2005.setObjectName(u"label_2005")
        self.label_2005.setFont(font2002)
        self.label_2005.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_2001.addWidget(self.label_2005, 4, 0, 1, 1)
        ##########
        self.lineEdit_2004 = QLineEdit(self.page_controller)
        self.lineEdit_2004.setObjectName(u"lineEdit_2004")
        self.lineEdit_2004.setReadOnly(True)
        self.lineEdit_2004.setFont(font1003)
        self.lineEdit_2004.setMaxLength(1)
        self.lineEdit_2004.setValidator(self.validator)
        self.lineEdit_2004.setMinimumSize(QSize(0, 30))
        self.lineEdit_2004.setMaximumWidth(220)
        self.lineEdit_2004.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_2001.addWidget(self.lineEdit_2004, 4, 1, 1, 2)
        ##########
        self.label_2006 = QLabel(self.page_controller)
        self.label_2006.setObjectName(u"label_2006")
        self.label_2006.setFont(font2002)
        self.label_2006.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_2001.addWidget(self.label_2006, 5, 0, 1, 1)
        ##########
        self.lineEdit_2005 = QLineEdit(self.page_controller)
        self.lineEdit_2005.setObjectName(u"lineEdit_2005")
        self.lineEdit_2005.setReadOnly(True)
        self.lineEdit_2005.setFont(font1003)
        self.lineEdit_2005.setMaxLength(1)
        self.lineEdit_2005.setValidator(self.validator)
        self.lineEdit_2005.setMinimumSize(QSize(0, 30))
        self.lineEdit_2005.setMaximumWidth(220)
        self.lineEdit_2005.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_2001.addWidget(self.lineEdit_2005, 5, 1, 1, 2)
        ##########
        self.stackedWidget.addWidget(self.page_controller)

        self.label_2003.setText(QCoreApplication.translate("MainWindow", u"Controller Keymappings", None))
        self.label_2001.setText(QCoreApplication.translate("MainWindow", u"Button X: ", None))
        self.lineEdit_2001.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_2002.setText(QCoreApplication.translate("MainWindow", u"Button Y: ", None))
        self.lineEdit_2002.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_2004.setText(QCoreApplication.translate("MainWindow", u"Button A: ", None))
        self.lineEdit_2003.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_2005.setText(QCoreApplication.translate("MainWindow", u"Trigger 1: ", None))
        self.lineEdit_2004.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_2006.setText(QCoreApplication.translate("MainWindow", u"Trigger 2: ", None))
        self.lineEdit_2005.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        ########################################################################
        #                                                                      #
        ## END --------------- PAGE_CONTROLLER DEFINITION -----------------   ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START  -------------- PAGE_LEFTLEG DEFINITION ----------------     ##
        #                                                                      #
        ## 3001                                                               ##
        ########################################################################
        self.page_leftLeg = QWidget()
        self.page_leftLeg.setObjectName(u"page_leftLeg")
        self.gridLayout_3001 = QGridLayout(self.page_leftLeg)
        self.gridLayout_3001.setObjectName(u"gridLayout_3001")
        self.gridLayout_3001.setRowStretch(0, 2)
        self.gridLayout_3001.setRowStretch(1, 1)
        self.gridLayout_3001.setRowStretch(2, 1)
        self.gridLayout_3001.setRowStretch(3, 6)
        self.gridLayout_3001.setColumnStretch(0, 5)
        self.gridLayout_3001.setColumnStretch(1, 2)
        self.gridLayout_3001.setColumnStretch(2, 4)
        ##########
        self.label_3003 = QLabel(self.page_leftLeg)
        self.label_3003.setObjectName(u"label_3003")
        font3001 = QFont()
        font3001.setFamily(u"Roboto Thin")
        font3001.setPointSize(30)
        self.label_3003.setFont(font3001)
        self.label_3003.setStyleSheet(u"")
        self.gridLayout_3001.addWidget(self.label_3003, 0, 0, 1, 3)
        ##########
        font3002 = QFont()
        font3002.setFamily(u"Roboto Thin")
        font3002.setPointSize(15)
        self.label_3001 = QLabel(self.page_leftLeg)
        self.label_3001.setObjectName(u"label_3001")
        self.label_3001.setFont(font3002)
        self.label_3001.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_3001.addWidget(self.label_3001, 1, 0, 1, 1)
        ##########
        self.lineEdit_3001 = QLineEdit(self.page_leftLeg)
        self.lineEdit_3001.setObjectName(u"lineEdit_3001")
        self.lineEdit_3001.setReadOnly(True)
        self.lineEdit_3001.setFont(font1003)
        self.lineEdit_3001.setMaxLength(1)
        self.lineEdit_3001.setValidator(self.validator)
        self.lineEdit_3001.setMinimumSize(QSize(0, 30))
        self.lineEdit_3001.setMaximumWidth(220)
        self.lineEdit_3001.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_3001.addWidget(self.lineEdit_3001, 1, 1, 1, 2)
        ##########
        self.label_3002 = QLabel(self.page_leftLeg)
        self.label_3002.setObjectName(u"label_3002")
        self.label_3002.setFont(font3002)
        self.label_3002.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_3001.addWidget(self.label_3002, 2, 0, 1, 1)
        ##########
        self.lineEdit_3002 = QLineEdit(self.page_leftLeg)
        self.lineEdit_3002.setObjectName(u"lineEdit_3002")
        self.lineEdit_3002.setReadOnly(True)
        self.lineEdit_3002.setFont(font1003)
        self.lineEdit_3002.setMaxLength(1)
        self.lineEdit_3002.setValidator(self.validator)
        self.lineEdit_3002.setMinimumSize(QSize(0, 30))
        self.lineEdit_3002.setMaximumWidth(220)
        self.lineEdit_3002.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_3001.addWidget(self.lineEdit_3002, 2, 1, 1, 2)
        ##########
        self.stackedWidget.addWidget(self.page_leftLeg)

        self.label_3003.setText(QCoreApplication.translate("MainWindow", u"Left Leg Keymappings", None))
        self.label_3001.setText(QCoreApplication.translate("MainWindow", u"Stepping: ", None))
        self.lineEdit_3001.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_3002.setText(QCoreApplication.translate("MainWindow", u"Stepping With Button: ", None))
        self.lineEdit_3002.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        ########################################################################
        #                                                                      #
        ## END   --------------- PAGE_LEFTLEG DEFINITION -----------------    ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START  -------------- PAGE_RIGHTLEG DEFINITION ----------------    ##
        #                                                                      #
        ## 4001                                                               ##
        ########################################################################
        self.page_rightLeg = QWidget()
        self.page_rightLeg.setObjectName(u"page_rightLeg")
        self.gridLayout_4001 = QGridLayout(self.page_rightLeg)
        self.gridLayout_4001.setObjectName(u"gridLayout_4001")
        self.gridLayout_4001.setRowStretch(0, 2)
        self.gridLayout_4001.setRowStretch(1, 1)
        self.gridLayout_4001.setRowStretch(2, 1)
        self.gridLayout_4001.setRowStretch(3, 6)
        self.gridLayout_4001.setColumnStretch(0, 5)
        self.gridLayout_4001.setColumnStretch(1, 2)
        self.gridLayout_4001.setColumnStretch(2, 4)
        ##########
        self.label_4003 = QLabel(self.page_rightLeg)
        self.label_4003.setObjectName(u"label_4003")
        font4001 = QFont()
        font4001.setFamily(u"Roboto Thin")
        font4001.setPointSize(30)
        self.label_4003.setFont(font4001)
        self.label_4003.setStyleSheet(u"")
        self.gridLayout_4001.addWidget(self.label_4003, 0, 0, 1, 3)
        ##########
        font4002 = QFont()
        font4002.setFamily(u"Roboto Thin")
        font4002.setPointSize(15)
        self.label_4001 = QLabel(self.page_rightLeg)
        self.label_4001.setObjectName(u"label_4001")
        self.label_4001.setFont(font4002)
        self.label_4001.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_4001.addWidget(self.label_4001, 1, 0, 1, 1)
        ##########
        self.lineEdit_4001 = QLineEdit(self.page_rightLeg)
        self.lineEdit_4001.setObjectName(u"lineEdit_4001")
        self.lineEdit_4001.setReadOnly(True)
        self.lineEdit_4001.setFont(font1003)
        self.lineEdit_4001.setMaxLength(1)
        self.lineEdit_4001.setValidator(self.validator)
        self.lineEdit_4001.setMinimumSize(QSize(0, 30))
        self.lineEdit_4001.setMaximumWidth(220)
        self.lineEdit_4001.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_4001.addWidget(self.lineEdit_4001, 1, 1, 1, 2)
        ##########
        self.label_4002 = QLabel(self.page_rightLeg)
        self.label_4002.setObjectName(u"label_4002")
        self.label_4002.setFont(font4002)
        self.label_4002.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.gridLayout_4001.addWidget(self.label_4002, 2, 0, 1, 1)
        ##########
        self.lineEdit_4002 = QLineEdit(self.page_rightLeg)
        self.lineEdit_4002.setObjectName(u"lineEdit_4002")
        self.lineEdit_4002.setReadOnly(True)
        self.lineEdit_4002.setFont(font1003)
        self.lineEdit_4002.setMaxLength(1)
        self.lineEdit_4002.setValidator(self.validator)
        self.lineEdit_4002.setMinimumSize(QSize(0, 30))
        self.lineEdit_4002.setMaximumWidth(220)
        self.lineEdit_4002.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_4001.addWidget(self.lineEdit_4002, 2, 1, 1, 2)
        ##########
        self.stackedWidget.addWidget(self.page_rightLeg)

        self.label_4003.setText(QCoreApplication.translate("MainWindow", u"Right Leg Keymappings", None))
        self.label_4001.setText(QCoreApplication.translate("MainWindow", u"Stepping: ", None))
        self.lineEdit_4001.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        self.label_4002.setText(QCoreApplication.translate("MainWindow", u"Stepping With Button: ", None))
        self.lineEdit_4002.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Keymapping", None))
        ########################################################################
        #                                                                      #
        ## END   --------------- PAGE_RIGHTLEG DEFINITION -----------------   ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START  -------------- PAGE_profiles DEFINITION ----------------    ##
        #                                                                      #
        ## 5001                                                               ##
        ########################################################################
        self.page_profiles = QWidget()
        self.page_profiles.setObjectName(u"page_profiles")
        self.verticalLayout_5001 = QVBoxLayout(self.page_profiles)
        self.verticalLayout_5001.setObjectName(u"verticalLayout_5001")
        ##########
        self.label_5002 = QLabel(self.page_profiles)
        self.label_5002.setObjectName(u"label_002")
        font5003 = QFont()
        font5003.setFamily(u"Roboto Thin")
        font5003.setPointSize(30)
        self.label_5002.setFont(font5003)
        self.label_5002.setStyleSheet(u"")
        self.verticalLayout_5001.addWidget(self.label_5002, alignment=Qt.AlignCenter)
        ##########
        self.pushButton_load = QPushButton(self.page_profiles)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setMinimumSize(QSize(150, 80))
        self.pushButton_load.setFixedWidth(600)
        font5001 = QFont()
        font5001.setFamily(u"Segoe UI")
        font5001.setPointSize(15)
        self.pushButton_load.setFont(font5001)
        self.pushButton_load.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5001 = QIcon()
        icon5001.addFile(u":/16x16/icons/16x16/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_load.setIcon(icon5001)
        self.pushButton_load.clicked.connect(MainWindow.profilePageButtons)
        self.verticalLayout_5001.addWidget(self.pushButton_load, alignment=Qt.AlignCenter)
        ##########
        self.pushButton_save = QPushButton(self.page_profiles)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(150, 80))
        self.pushButton_save.setFixedWidth(600)
        self.pushButton_save.setFont(font5001)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5002 = QIcon()
        icon5002.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon5002)
        self.pushButton_save.clicked.connect(MainWindow.profilePageButtons)
        self.verticalLayout_5001.addWidget(self.pushButton_save, alignment=Qt.AlignCenter)
        ##########
        self.pushButton_delete = QPushButton(self.page_profiles)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(150, 80))
        self.pushButton_delete.setFixedWidth(600)
        self.pushButton_delete.setFont(font5001)
        self.pushButton_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5003 = QIcon()
        icon5003.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon5003)
        self.pushButton_delete.clicked.connect(MainWindow.profilePageButtons)
        self.verticalLayout_5001.addWidget(self.pushButton_delete, alignment=Qt.AlignCenter)
        ##########
        self.label_5001 = QLabel(self.page_profiles)
        self.label_5001.setObjectName(u"label_5001")
        font5002 = QFont()
        font5002.setFamily(u"Segoe UI")
        font5002.setPointSize(15)
        self.label_5001.setFont(font5002)
        self.label_5001.setFixedHeight(100)
        self.label_5001.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5001.addWidget(self.label_5001)
        ##########
        self.stackedWidget.addWidget(self.page_profiles)

        self.label_5002.setText(QCoreApplication.translate("MainWindow", u"Game Profiles", None))
        self.pushButton_load.setText(QCoreApplication.translate("MainWindow", u"   Load Profile", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"   Save Profile", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"   Delete Profile", None))
        self.label_5001.setText(QCoreApplication.translate("MainWindow", u"", None))
        ########################################################################
        #                                                                      #
        ## END   --------------- PAGE_profiles DEFINITION -----------------   ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START    -------------- PAGE_setUp DEFINITION ----------------     ##
        #                                                                      #
        ## 6001                                                               ##
        ########################################################################
        self.page_setUp = QWidget()
        self.page_setUp.setObjectName(u"page_setUp")
        self.verticalLayout_6001 = QVBoxLayout(self.page_setUp)
        self.verticalLayout_6001.setObjectName(u"verticalLayout_6001")
        ##########
        font6001 = QFont()
        # font6001.setFamily(u"Segoe UI") 
        font6001.setFamily(u"Roboto Thin")
        font6001.setPointSize(11)
        self.plainTextEdit_6001 = QPlainTextEdit(self.page_setUp)
        self.plainTextEdit_6001.setObjectName(u"plainTextEdit_6001")
        self.plainTextEdit_6001.setFont(font6001)
        self.plainTextEdit_6001.setMinimumSize(QSize(200, 200))
        self.plainTextEdit_6001.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}")
        self.verticalLayout_6001.addWidget(self.plainTextEdit_6001)
        ##########
        self.stackedWidget.addWidget(self.page_setUp)

        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"This software requires a simple setup before the first use.\n====================\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"Step 1: Check If SSHKey Exist.\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     In a terminal type ' ls ~/.ssh ' and see if file ' id_rsa.pub ' or ' id_dsa.pub '\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     is present. If so, skip step 2.\n\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"Step 2: Generate SSHKey.\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     Type ' ssh-keygen ' and save the key in the default location by hitting ' Enter '.\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     You could also skip adding a passphrase by hitting ' Enter ' again.\n\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"Step 3: Create A Directory On Raspberry.\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     Type the command ' ssh pi@raspberrypi.local mkdir -p .ssh '\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     and supply password ' raspberry '.\n\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"Step 4: Copy The SSHKey To Raspberry.\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     Type the command:\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     ' cat ~/.ssh/id_rsa.pub | ssh pi@raspberrypi.local 'cat >> .ssh/authorized_keys' '\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     and supply password ' raspberry '.\n\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"Step 5: If You Are Using macOS:\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"     Add the SSHKey to your keychain with ' ssh-add -K ~/.ssh/id_rsa '.\n====================\n", None))
        self.plainTextEdit_6001.insertPlainText(QCoreApplication.translate("MainWindow", u"And setup is complete!", None))
        ########################################################################
        #                                                                      #
        ## END     --------------- PAGE_setUp DEFINITION -----------------    ##
        #                                                                      #
        ############################## ---/--/--- ##############################
        

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        font_cred = QFont()
        font_cred.setPointSize(12)
        self.label_credits.setFont(font_cred)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"2021 ISDN Year 2 Project - INNOSPORT - Brandon, Harry, Simon, Will", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.1.0", None))
    # retranslateUi