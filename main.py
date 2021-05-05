import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from app_modules import * 


########################################################################
## tkinter Import
########################################################################
import subprocess
from subprocess import Popen, PIPE
import os
from os.path import isfile

runningCmd = False

# Keymaps
keymapList = []
verifyList = ['LeftHand_VerticalSwing',
'LeftHand_HorizontalSwing',
'Controller_ButtonX',
'Controller_ButtonY',
'LeftLeg_Stepping',
'LeftLeg_SteppingWithBtn',
'RightLeg_Stepping',
'RightLeg_SteppingWithBtn']
corrupted = False
# Left Hand
leftHand_verticalSwing = 0
leftHand_horizontalSwing = 1
# Controller
controller_buttonX = 2
controller_buttonY = 3
# Left Leg
leftLeg_stepping = 4
leftLeg_steppingWithBtn = 5
# Right Leg
rightLeg_stepping = 6
rightLeg_steppingWithBtn = 7
########################################################################
## END - tkinter Import
############################## ---/--/--- ##############################


########################################################################
## Splash Screen Import
########################################################################
from ui_splash_screen import Ui_SplashScreen
from ui_main_splash_screen import Ui_MainWindow_SS
import time
counter = 0
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)

        self.show()

        configFunctions.readConfig(self)

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter == 50:
            self.ui.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<strong>Loading Config...</strong>", None))
        if counter == 84 and main.corrupted:
            self.ui.label_loading.setText(QCoreApplication.translate("SplashScreen", u"Config Corrupted, <strong>Restoring Defaults...</strong>", None))
        if counter == 85 and main.corrupted:
            time.sleep(2)
        if counter >= 99:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1
########################################################################
## END - Splash Screen Import
############################## ---/--/--- ##############################
mode = 'exercise'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        configFunctions.readConfig(self)

        UIFunctions.removeTitleBar(True)
        self.setWindowTitle('INNOSPORT - Keymap Settings')
        UIFunctions.labelTitle(self, 'INNOSPORT - Keymap Settings')
        UIFunctions.labelDescription(self, 'Primary Settings Controls')

        startSize = QSize(1000, 600)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        UIFunctions.enableMaximumSize(self, 500, 720)

        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 180, True))

        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Left Hand", "btn_leftHand", "url(:/16x16/icons/16x16/cil-circle.png)", True)
        UIFunctions.addNewMenu(self, "Controller", "btn_controller", "url(:/16x16/icons/16x16/cil-circle.png)", True)
        UIFunctions.addNewMenu(self, "Left Leg", "btn_leftLeg", "url(:/16x16/icons/16x16/cil-circle.png)", True)
        UIFunctions.addNewMenu(self, "Right Leg", "btn_rightLeg", "url(:/16x16/icons/16x16/cil-circle.png)", True)
        UIFunctions.addNewMenu(self, "Game Profiles", "btn_profiles", "url(:/16x16/icons/16x16/cil-gamepad.png)", False)
        UIFunctions.addNewMenu(self, "Set-Up", "btn_setUp", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        UIFunctions.selectStandardMenu(self, "btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        UIFunctions.userIcon(self, "INNO", "", False)

        def moveWindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)

        global selfVar
        selfVar = self

        self.show()

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelDescription(self, 'Primary Settings Controls')
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
            self.ui.label_001.setText(QCoreApplication.translate("MainWindow", u"", None))

        # PAGE LEFT HAND
        if btnWidget.objectName() == "btn_leftHand":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_leftHand)
            UIFunctions.resetStyle(self, "btn_leftHand")
            UIFunctions.labelDescription(self, 'Change Keybindings For Left Hand IMU')
            UIFunctions.labelPage(self, "LEFT HAND")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
            self.ui.lineEdit_1001.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.leftHand_verticalSwing], None))
            self.ui.lineEdit_1002.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.leftHand_horizontalSwing], None))

        # PAGE CONTROLLER
        if btnWidget.objectName() == "btn_controller":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_controller)
            UIFunctions.resetStyle(self, "btn_controller")
            UIFunctions.labelDescription(self, 'Change Keybindings For Controller Input and IMU')
            UIFunctions.labelPage(self, "CONTROLLER")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
            self.ui.lineEdit_2001.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.controller_buttonX], None))
            self.ui.lineEdit_2002.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.controller_buttonY], None))

        # PAGE LEFT LEG
        if btnWidget.objectName() == "btn_leftLeg":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_leftLeg)
            UIFunctions.resetStyle(self, "btn_leftLeg")
            UIFunctions.labelDescription(self, 'Change Keybindings For Left Leg IMU')
            UIFunctions.labelPage(self, "LEFT LEG")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
            self.ui.lineEdit_3001.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.leftLeg_stepping], None))
            self.ui.lineEdit_3002.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.leftLeg_steppingWithBtn], None))

        # PAGE RIGHT LEG
        if btnWidget.objectName() == "btn_rightLeg":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_rightLeg)
            UIFunctions.resetStyle(self, "btn_rightLeg")
            UIFunctions.labelDescription(self, 'Change Keybindings For Right Leg IMU')
            UIFunctions.labelPage(self, "RIGHT LEG")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
            self.ui.lineEdit_4001.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.rightLeg_stepping], None))
            self.ui.lineEdit_4002.setText(QCoreApplication.translate("MainWindow", main.keymapList[main.rightLeg_steppingWithBtn], None))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_profiles":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_profiles)
            UIFunctions.resetStyle(self, "btn_profiles")
            UIFunctions.labelDescription(self, 'Manage Game Profiles')
            UIFunctions.labelPage(self, "Game Profiles")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
            self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", u"", None))

        if btnWidget.objectName() == "btn_setUp":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_setUp)
            UIFunctions.resetStyle(self, "btn_setUp")
            UIFunctions.labelDescription(self, 'First Time Set-Up Before Using This Software')
            UIFunctions.labelPage(self, "Set-Up")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            UIFunctions.updateKeymapUI(self)
    ########################################################################
    ## END --- MENUS ==> DYNAMIC MENUS FUNCTIONS
    ############################ ---/--/--- ################################

    
    ########################################################################
    ## HOME PAGE ==> BUTTON FUNCTIONS
    ########################################################################
    def homePageButtons(self):
        btnWidget = self.sender()
        if btnWidget.objectName() == "pushButton_confirm":
            if not main.runningCmd:
                main.runningCmd = True
                configFunctions.updateSettingsOnPi(self)
                main.runningCmd = False
            else:
                pass

        if btnWidget.objectName() == "pushButton_undo":
            configFunctions.readConfig(self)
            self.ui.label_001.setText(QCoreApplication.translate("MainWindow", u"Config Restored", None))
            self.ui.label_001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")

        if btnWidget.objectName() == "pushButton_restore":
            configFunctions.restoreDefault(self)
            self.ui.label_001.setText(QCoreApplication.translate("MainWindow", u"Defaults Restored", None))
            self.ui.label_001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")
    ########################################################################
    ## END --- HOME PAGE ==> BUTTON FUNCTIONS
    ############################ ---/--/--- ################################


    ########################################################################
    ## PROFILE PAGE ==> BUTTON FUNCTIONS
    ########################################################################
    def profilePageButtons(self):
        btnWidget = self.sender()
        if btnWidget.objectName() == "pushButton_load":
            profileFunctions.loadProfile(self)

        if btnWidget.objectName() == "pushButton_save":
            profileFunctions.saveProfile(self)

        if btnWidget.objectName() == "pushButton_delete":
            profileFunctions.deleteProfile(self)
    ########################################################################
    ## END --- PROFILE PAGE ==> BUTTON FUNCTIONS
    ############################ ---/--/--- ################################

    
    ########################################################################
    ## MODE SWITCH
    ########################################################################
    def switchMode(self):
        global mode
        if (mode == 'exercise'):
            mode = 'gaming'
            self.ui.lineEdit_1001.setReadOnly(False)
            self.ui.lineEdit_1002.setReadOnly(False)
            self.ui.lineEdit_3001.setReadOnly(False)
            self.ui.lineEdit_3002.setReadOnly(False)
            self.ui.lineEdit_4001.setReadOnly(False)
            self.ui.lineEdit_4002.setReadOnly(False)
        else:
            mode = 'exercise'
            self.ui.lineEdit_1001.setReadOnly(True)
            self.ui.lineEdit_1002.setReadOnly(True)
            self.ui.lineEdit_3001.setReadOnly(True)
            self.ui.lineEdit_3002.setReadOnly(True)
            self.ui.lineEdit_4001.setReadOnly(True)
            self.ui.lineEdit_4002.setReadOnly(True)
    ########################################################################
    ## END --- MODE SWITCH
    ############################ ---/--/--- ################################

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = SplashScreen()
    sys.exit(app.exec_())