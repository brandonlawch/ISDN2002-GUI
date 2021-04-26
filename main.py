import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from app_modules import *\


########################################################################
## tkinter Import
########################################################################
import subprocess
from subprocess import Popen, PIPE
import os

runningCmd = False
updateStatus = 'incomplete'

# Keymaps
keymapList = []
# Left Hand
leftHand_verticalSwing = 0
# Controller
controller_buttonX = 1
# Left Leg
leftLeg_stepping = 2
# Right Leg
rightLeg_stepping = 3

def writeDefaultConfig():	#Write default mappings to config.txt
	with open('config.txt', 'w') as file:
		file.write('LeftHand_VerticalSwing: ' + 'X' + '\n')
		file.write('Controller_ButtonX: ' + 'Y' + '\n')
		file.write('LeftLeg_Stepping: ' + 'W' + '\n')
		file.write('RightLeg_Stepping: ' + 'S' + '\n')

def readConfig():	#read config from config.txt and save to keymapList[]
    global keymapList
    if (os.path.isfile('config.txt') == False):	#if config.txt does not exist, create one with default config
        writeDefaultConfig()
    with open('config.txt', 'r') as file:
        temp = file.read().splitlines()
        for x in range(len(temp)):
            temp[x] = temp[x].split(': ')
        keymapList.clear()
        for x in range(len(temp)):
            keymapList.append(temp[x][1])

def updateConfigFile():	#Save config from keymapList[] to config.txt
	with open('config.txt', 'w') as file:
		file.write('LeftHand_VerticalSwing: ' + keymapList[leftHand_verticalSwing] + '\n')
		file.write('Controller_ButtonX: ' + keymapList[controller_buttonX] + '\n')
		file.write('LeftLeg_Stepping: ' + keymapList[leftLeg_stepping] + '\n')
		file.write('RightLeg_Stepping: ' + keymapList[rightLeg_stepping] + '\n')

def restoreDefault():
	writeDefaultConfig()
	readConfig()
########################################################################
## END - tkinter Import
############################## ---/--/--- ##############################


########################################################################
## Splash Screen Import
########################################################################
from ui_splash_screen import Ui_SplashScreen
from ui_main_splash_screen import Ui_MainWindow_SS
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

        readConfig()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1
########################################################################
## END - Splash Screen Import
############################## ---/--/--- ##############################


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('INNOSPORT - Keymap Settings')
        UIFunctions.labelTitle(self, 'INNOSPORT - Keymap Settings')
        UIFunctions.labelDescription(self, 'Primary Settings Controls')

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        UIFunctions.enableMaximumSize(self, 500, 720)

        ## ==> CREATE MENUS
        ########################################################################
        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 180, True))

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Left Hand", "btn_leftHand", "url(:/16x16/icons/16x16/cil-x-circle.png)", True)
        UIFunctions.addNewMenu(self, "Controller", "btn_controller", "url(:/16x16/icons/16x16/cil-x-circle.png)", True)
        UIFunctions.addNewMenu(self, "Left Leg", "btn_leftLeg", "url(:/16x16/icons/16x16/cil-x-circle.png)", True)
        UIFunctions.addNewMenu(self, "Right Leg", "btn_rightLeg", "url(:/16x16/icons/16x16/cil-x-circle.png)", True)
        UIFunctions.addNewMenu(self, "Game Profiles", "btn_profiles", "url(:/16x16/icons/16x16/cil-gamepad.png)", True)

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "INNO", "", False)


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################


        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
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

        # PAGE LEFT HAND
        if btnWidget.objectName() == "btn_leftHand":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_leftHand")
            UIFunctions.labelDescription(self, 'Change Keybindings For Left Hand IMU')
            UIFunctions.labelPage(self, "LEFT HAND")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE CONTROLLER
        if btnWidget.objectName() == "btn_controller":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_controller")
            UIFunctions.labelDescription(self, 'Change Keybindings For Controller Input and IMU')
            UIFunctions.labelPage(self, "CONTROLLER")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE LEFT LEG
        if btnWidget.objectName() == "btn_leftLeg":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_leftLeg")
            UIFunctions.labelDescription(self, 'Change Keybindings For Left Leg IMU')
            UIFunctions.labelPage(self, "LEFT LEG")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE RIGHT LEG
        if btnWidget.objectName() == "btn_rightLeg":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_rightLeg")
            UIFunctions.labelDescription(self, 'Change Keybindings For Right Leg IMU')
            UIFunctions.labelPage(self, "RIGHT LEG")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_profiles":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home) #page_widgets
            UIFunctions.resetStyle(self, "btn_profiles")
            UIFunctions.labelDescription(self, 'Manage Game Profiles')
            UIFunctions.labelPage(self, "Game Profiles")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    # window = MainWindow()
    window = SplashScreen()
    sys.exit(app.exec_())
