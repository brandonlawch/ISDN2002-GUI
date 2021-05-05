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

## ==> GUI FILE
import main
import ui_styles
from main import *

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(ui_styles.Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(45, 60, 65); }") #default rgb: 44 49 60
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(45, 60, 65); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def updateKeymapUI(self):
        #Left Hand ==========
        if (self.ui.lineEdit_1001.isModified() and self.ui.lineEdit_1001.text()):
            main.keymapList[main.leftHand_verticalSwing] = self.ui.lineEdit_1001.text()
        if (self.ui.lineEdit_1002.isModified() and self.ui.lineEdit_1002.text()):
            main.keymapList[main.leftHand_horizontalSwing] = self.ui.lineEdit_1002.text()
        #Controller ==========
        if (self.ui.lineEdit_2001.isModified() and self.ui.lineEdit_2001.text()):
            main.keymapList[main.controller_buttonX] = self.ui.lineEdit_2001.text()
        if (self.ui.lineEdit_2002.isModified() and self.ui.lineEdit_2002.text()):
            main.keymapList[main.controller_buttonY] = self.ui.lineEdit_2002.text()
        #Left Leg ==========
        if (self.ui.lineEdit_3001.isModified() and self.ui.lineEdit_3001.text()):
            main.keymapList[main.leftLeg_stepping] = self.ui.lineEdit_3001.text()
        if (self.ui.lineEdit_3002.isModified() and self.ui.lineEdit_3002.text()):
            main.keymapList[main.leftLeg_steppingWithBtn] = self.ui.lineEdit_3002.text()
        #Right Leg ==========
        if (self.ui.lineEdit_4001.isModified() and self.ui.lineEdit_4001.text()):
            main.keymapList[main.rightLeg_stepping] = self.ui.lineEdit_4001.text()
        if (self.ui.lineEdit_4002.isModified() and self.ui.lineEdit_4002.text()):
            main.keymapList[main.rightLeg_steppingWithBtn] = self.ui.lineEdit_4002.text()

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################

LeftHand_VerticalSwing_default = 'h'
LeftHand_HorizontalSwing_default = 'q'
Controller_ButtonX_default = 'x'
Controller_ButtonY_default = 'y'
LeftLeg_Stepping_default = 'w'
LeftLeg_SteppingWithBtn_default = 'a'
RightLeg_Stepping_default = 's'
RightLeg_SteppingWithBtn_default = 'j'
class configFunctions(MainWindow):
    def writeDefaultConfig(self):  #Write default mappings to config.txt
        if (os.path.isfile('config.txt') == False):
            with open('config.txt', 'w') as file:
                file.write('LeftHand_VerticalSwing: ' + LeftHand_VerticalSwing_default + '\n')
                file.write('LeftHand_HorizontalSwing: ' + LeftHand_HorizontalSwing_default + '\n')
                file.write('Controller_ButtonX: ' + Controller_ButtonX_default + '\n')
                file.write('Controller_ButtonY: ' + Controller_ButtonY_default + '\n')
                file.write('LeftLeg_Stepping: ' + LeftLeg_Stepping_default + '\n')
                file.write('LeftLeg_SteppingWithBtn: ' + LeftLeg_SteppingWithBtn_default + '\n')
                file.write('RightLeg_Stepping: ' + RightLeg_Stepping_default + '\n')
                file.write('RightLeg_SteppingWithBtn: ' + RightLeg_SteppingWithBtn_default + '\n')
        else:
            with open('config.txt', 'r+') as file:
                file.truncate(0)
                file.write('LeftHand_VerticalSwing: ' + LeftHand_VerticalSwing_default + '\n')
                file.write('LeftHand_HorizontalSwing: ' + LeftHand_HorizontalSwing_default + '\n')
                file.write('Controller_ButtonX: ' + Controller_ButtonX_default + '\n')
                file.write('Controller_ButtonY: ' + Controller_ButtonY_default + '\n')
                file.write('LeftLeg_Stepping: ' + LeftLeg_Stepping_default + '\n')
                file.write('LeftLeg_SteppingWithBtn: ' + LeftLeg_SteppingWithBtn_default + '\n')
                file.write('RightLeg_Stepping: ' + RightLeg_Stepping_default + '\n')
                file.write('RightLeg_SteppingWithBtn: ' + RightLeg_SteppingWithBtn_default + '\n')
        subprocess.check_call(["attrib","+H","config.txt"])


    def readConfig(self):  #read config from config.txt and save to keymapList[]
        main.corrupted = False
        if (os.path.isfile('config.txt') == False):	#if config.txt does not exist, create one with default config
            configFunctions.writeDefaultConfig(self)
        with open('config.txt', 'r') as file:
            temp = file.read().splitlines()
            for x in range(len(temp)):
                temp[x] = temp[x].split(': ')
            main.keymapList.clear()
            for x in range(len(temp)):
                if (temp[x][0] != main.verifyList[x] or temp[x][1] == ""):
                    main.corrupted = True
                main.keymapList.append(temp[x][1][0])
        if len(main.keymapList) != len(main.verifyList):
            main.corrupted = True
        if ((not main.keymapList) or main.corrupted):
            configFunctions.writeDefaultConfig(self)

    def updateConfigFile(self):  #Save config from keymapList[] to config.txt
        if (os.path.isfile('config.txt') == False):
            configFunctions.writeDefaultConfig(self)
        with open('config.txt', 'r+') as file:
            file.truncate(0)
            file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.leftHand_verticalSwing] + '\n')
            file.write('LeftHand_HorizontalSwing: ' + main.keymapList[main.leftHand_horizontalSwing] + '\n')
            file.write('Controller_ButtonX: ' + main.keymapList[main.controller_buttonX] + '\n')
            file.write('Controller_ButtonY: ' + main.keymapList[main.controller_buttonY] + '\n')
            file.write('LeftLeg_Stepping: ' + main.keymapList[main.leftLeg_stepping] + '\n')
            file.write('LeftLeg_SteppingWithBtn: ' + main.keymapList[main.leftLeg_steppingWithBtn] + '\n')
            file.write('RightLeg_Stepping: ' + main.keymapList[main.rightLeg_stepping] + '\n')
            file.write('RightLeg_SteppingWithBtn: ' + main.keymapList[main.rightLeg_steppingWithBtn] + '\n')

    def restoreDefault(self):
        main.keymapList[main.leftHand_verticalSwing] = LeftHand_VerticalSwing_default
        main.keymapList[main.leftHand_horizontalSwing] = LeftHand_HorizontalSwing_default
        main.keymapList[main.controller_buttonX] = Controller_ButtonX_default
        main.keymapList[main.controller_buttonY] = Controller_ButtonY_default
        main.keymapList[main.leftLeg_stepping] = LeftLeg_Stepping_default
        main.keymapList[main.leftLeg_steppingWithBtn] = LeftLeg_SteppingWithBtn_default
        main.keymapList[main.rightLeg_stepping] = RightLeg_Stepping_default
        main.keymapList[main.rightLeg_steppingWithBtn] = RightLeg_SteppingWithBtn_default

    def updateSettingsOnPi(self):
        configFunctions.updateConfigFile(self)
        self.ui.label_001.setText(QCoreApplication.translate("MainWindow", u"Update Settings", None))
        
        main.runningCmd = True
        process = subprocess.Popen(['scp', 'config.txt', 'pi@raspberrypi.local:/home/pi/INNOSPORT/new_config.txt'],creationflags=0x08000000)
        try:
            process.wait(5)
        except subprocess.TimeoutExpired:
            process.kill()
        if (process.returncode != 0):
            self.ui.label_001.setText(QCoreApplication.translate("MainWindow", u"Update Error", None))
            self.ui.label_001.setStyleSheet("QLabel { color : rgb(255, 15, 140) }")
        else:
            self.ui.label_001.setText(QCoreApplication.translate("MainWindow", u"Update Complete", None))
            self.ui.label_001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")


class profileFunctions(MainWindow):
        def loadProfile(self):
            path = QFileDialog.getOpenFileName(self,caption = "Select Profile", filter = "Profiles (*.txt)")[0]
            if (path):
                with open(path, 'r') as profiletxt:
                    temp = profiletxt.read().splitlines()
                    with open('config.txt', 'r+') as file:
                        for x in range(len(temp)):
                            file.write(temp[x] + '\n')
                configFunctions.readConfig(self)
                name = path.split('/')[-1].split('.')[0]
                self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", "\"" + name + "\" Profile Loaded", None))
                self.ui.label_5001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")
        
        def saveProfile(self):
            path = QFileDialog.getSaveFileName(self, caption="Save Profile", filter="Profiles (*.txt)")[0]
            if (path):
                with open(path, 'w') as file:
                    file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.leftHand_verticalSwing] + '\n')
                    file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.leftHand_horizontalSwing] + '\n')
                    file.write('Controller_ButtonX: ' + main.keymapList[main.controller_buttonX] + '\n')
                    file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.controller_buttonY] + '\n')
                    file.write('LeftLeg_Stepping: ' + main.keymapList[main.leftLeg_stepping] + '\n')
                    file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.leftLeg_steppingWithBtn] + '\n')
                    file.write('RightLeg_Stepping: ' + main.keymapList[main.rightLeg_stepping] + '\n')
                    file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.rightLeg_steppingWithBtn] + '\n')
                name = path.split('/')[-1].split('.')[0]
                self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", "\"" + name + "\" Profile Saved", None))
                self.ui.label_5001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")
                # configFiles = [f for f in os.listdir() if (os.path.splitext(f)[-1].lower() == ".txt")]

        def deleteProfile(self):
            path = QFileDialog.getOpenFileName(self,caption = "Select Profile", filter = "Profiles (*.txt)")[0]
            if (path):
                os.remove(path)
                name = path.split('/')[-1].split('.')[0]
                self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", "\"" + name + "\" Profile Deleted", None))
                self.ui.label_5001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")

class PyToggle(QCheckBox):
    def __init__(
        self,
        width=120,
        bg_color="#3BD8CE",
        circle_color="#DDD",
        active_color="#F271B1",
        animation_curve = QEasingCurve.OutQuint,
    ):
        QCheckBox.__init__(self)
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)
        #colors
        self.bg_color = bg_color
        self.circleColor = circle_color
        self.activeColor = active_color
        #animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(700)
        self.stateChanged.connect(self.start_transition)

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)
        self.animation.start()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        rect = QRect(0, 0, self.width(), self.height())
        if not self.isChecked():
            p.setBrush(QColor(self.bg_color))
            p.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height()/2, self.height()/2)
            p.setBrush(QColor(self.circleColor))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            p.setBrush(QColor(self.activeColor))
            p.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height()/2, self.height()/2)
            p.setBrush(QColor(self.circleColor))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        p.end()