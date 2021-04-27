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
        if (self.ui.lineEdit_1001.isModified() and self.ui.lineEdit_1001.text()):
            main.keymapList[main.leftHand_verticalSwing] = self.ui.lineEdit_1001.text()
        if (self.ui.lineEdit_2001.isModified() and self.ui.lineEdit_2001.text()):
            main.keymapList[main.controller_buttonX] = self.ui.lineEdit_2001.text()
        if (self.ui.lineEdit_3001.isModified() and self.ui.lineEdit_3001.text()):
            main.keymapList[main.leftLeg_stepping] = self.ui.lineEdit_3001.text()
        if (self.ui.lineEdit_4001.isModified() and self.ui.lineEdit_4001.text()):
            main.keymapList[main.rightLeg_stepping] = self.ui.lineEdit_4001.text()
    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################

class configFunctions(MainWindow):
    def writeDefaultConfig(self):	#Write default mappings to config.txt
        with open('config.txt', 'w') as file:
            file.write('LeftHand_VerticalSwing: ' + 'x' + '\n')
            file.write('Controller_ButtonX: ' + 'y' + '\n')
            file.write('LeftLeg_Stepping: ' + 'w' + '\n')
            file.write('RightLeg_Stepping: ' + 's' + '\n')

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
                main.keymapList.append(temp[x][1])
        if len(main.keymapList) != len(main.verifyList):
            main.corrupted = True
        if ((not main.keymapList) or main.corrupted):
            configFunctions.writeDefaultConfig(self)

    def updateConfigFile(self):	#Save config from keymapList[] to config.txt
        with open('config.txt', 'w') as file:
        	file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.leftHand_verticalSwing] + '\n')
        	file.write('Controller_ButtonX: ' + main.keymapList[main.controller_buttonX] + '\n')
        	file.write('LeftLeg_Stepping: ' + main.keymapList[main.leftLeg_stepping] + '\n')
        	file.write('RightLeg_Stepping: ' + main.keymapList[main.rightLeg_stepping] + '\n')

    def restoreDefault(self):
        configFunctions.writeDefaultConfig(self)
        configFunctions.readConfig(self)

    def updateSettingsOnPi(self):
        if (not main.runningCmd):
            main.runningCmd = True
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
            main.runningCmd = False


class profileFunctions(MainWindow):
        def loadProfile(self):
            filename = QFileDialog.getOpenFileName(self,caption = "Select Profile", filter = "Profiles (*.txt)")
            path = filename[0]
            if (path):
                with open(path, 'r') as profiletxt:
                    temp = profiletxt.read().splitlines()
                    with open('config.txt', 'w') as file:
                        for x in range(len(temp)):
                            file.write(temp[x] + '\n')
                configFunctions.readConfig(self)
                self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", u"Profile Loaded", None))
                self.ui.label_5001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")
        
        def saveProfile(self):
            filename = QFileDialog.getSaveFileName(self, caption="Save Profile", filter="Profiles (*.txt)")
            path = filename[0]
            if (path):
                with open(path, 'w') as file:
                    file.write('LeftHand_VerticalSwing: ' + main.keymapList[main.leftHand_verticalSwing] + '\n')
                    file.write('Controller_ButtonX: ' + main.keymapList[main.controller_buttonX] + '\n')
                    file.write('LeftLeg_Stepping: ' + main.keymapList[main.leftLeg_stepping] + '\n')
                    file.write('RightLeg_Stepping: ' + main.keymapList[main.rightLeg_stepping] + '\n')
                self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", u"Profile Saved", None))
                self.ui.label_5001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")

        def deleteProfile(self):
            filename = QFileDialog.getOpenFileName(self,caption = "Select Profile", filter = "Profiles (*.txt)")
            path = filename[0]
            if (path):
                os.remove(path)
                self.ui.label_5001.setText(QCoreApplication.translate("MainWindow", u"Profile Deleted", None))
                self.ui.label_5001.setStyleSheet("QLabel { color : rgb(115, 230, 223) }")