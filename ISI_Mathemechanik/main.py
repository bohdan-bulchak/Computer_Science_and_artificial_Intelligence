import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, \
    QMainWindow, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QCursor

import levels2_3_4
import level1
import levels5_6
import decl

a = 2


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setStyleSheet("background: #161219;")

        self.complexity_text = QtWidgets.QLabel(self)
        self.welcome = QtWidgets.QLabel(self)

        self.closeButton = QtWidgets.QPushButton(self)

        self.level1 = QtWidgets.QPushButton(self)
        self.level2 = QtWidgets.QPushButton(self)
        self.level3 = QtWidgets.QPushButton(self)
        self.level4 = QtWidgets.QPushButton(self)
        self.level5 = QtWidgets.QPushButton(self)
        self.level6 = QtWidgets.QPushButton(self)
        self.change_level_button = QtWidgets.QPushButton(self)

        # decl.create_labels(self)

        self.label1 = QtWidgets.QPushButton(self)
        self.label2 = QtWidgets.QPushButton(self)
        self.label3 = QtWidgets.QPushButton(self)
        self.label4 = QtWidgets.QPushButton(self)
        self.label5 = QtWidgets.QPushButton(self)
        self.label6 = QtWidgets.QPushButton(self)
        self.label7 = QtWidgets.QPushButton(self)
        self.label8 = QtWidgets.QPushButton(self)
        self.label9 = QtWidgets.QPushButton(self)
        self.label10 = QtWidgets.QPushButton(self)
        self.label11 = QtWidgets.QPushButton(self)
        self.label12 = QtWidgets.QPushButton(self)
        self.label13 = QtWidgets.QPushButton(self)
        self.label14 = QtWidgets.QPushButton(self)
        self.label15 = QtWidgets.QPushButton(self)
        self.label16 = QtWidgets.QPushButton(self)
        self.label17 = QtWidgets.QPushButton(self)
        self.label18 = QtWidgets.QPushButton(self)
        self.label19 = QtWidgets.QPushButton(self)
        self.label20 = QtWidgets.QPushButton(self)
        self.label21 = QtWidgets.QPushButton(self)
        self.label22 = QtWidgets.QPushButton(self)
        self.label23 = QtWidgets.QPushButton(self)
        self.label24 = QtWidgets.QPushButton(self)
        self.label25 = QtWidgets.QPushButton(self)
        self.label26 = QtWidgets.QPushButton(self)
        self.label27 = QtWidgets.QPushButton(self)
        self.label28 = QtWidgets.QPushButton(self)
        self.label29 = QtWidgets.QPushButton(self)
        self.label30 = QtWidgets.QPushButton(self)
        self.label31 = QtWidgets.QPushButton(self)
        self.label32 = QtWidgets.QPushButton(self)
        self.label33 = QtWidgets.QPushButton(self)
        self.label34 = QtWidgets.QPushButton(self)
        self.label35 = QtWidgets.QPushButton(self)
        self.label36 = QtWidgets.QPushButton(self)
        self.label37 = QtWidgets.QPushButton(self)
        self.label38 = QtWidgets.QPushButton(self)
        self.label39 = QtWidgets.QPushButton(self)
        self.label40 = QtWidgets.QPushButton(self)
        self.label41 = QtWidgets.QPushButton(self)
        self.label42 = QtWidgets.QPushButton(self)
        self.label43 = QtWidgets.QPushButton(self)
        self.label44 = QtWidgets.QPushButton(self)
        self.label45 = QtWidgets.QPushButton(self)
        self.label46 = QtWidgets.QPushButton(self)
        self.label47 = QtWidgets.QPushButton(self)
        self.label48 = QtWidgets.QPushButton(self)
        self.label49 = QtWidgets.QPushButton(self)
        self.hide_list = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6,
                     self.label7, self.label8, self.label9, self.label10, self.label11, self.label12,
                     self.label13, self.label14, self.label15, self.label16, self.label17, self.label18,
                     self.label19, self.label20, self.label21, self.label22, self.label23, self.label24, self.label25,
                     self.label26, self.label27, self.label28, self.label29, self.label30, self.label31,
                     self.label32, self.label33, self.label34, self.label35, self.label36, self.label37,
                     self.label38, self.label39, self.label40, self.label41, self.label42, self.label43,
                     self.label44, self.label45, self.label46, self.label47, self.label48, self.label49]
        #
        # self.label1_2 = QtWidgets.QPushButton(self)
        # self.label2_2 = QtWidgets.QPushButton(self)
        # self.label3_2 = QtWidgets.QPushButton(self)
        # self.label4_2 = QtWidgets.QPushButton(self)
        # self.label5_2 = QtWidgets.QPushButton(self)
        # self.label6_2 = QtWidgets.QPushButton(self)
        # self.label7_2 = QtWidgets.QPushButton(self)
        # self.label8_2 = QtWidgets.QPushButton(self)
        # self.label9_2 = QtWidgets.QPushButton(self)
        # self.label10_2 = QtWidgets.QPushButton(self)
        # self.label11_2 = QtWidgets.QPushButton(self)
        # self.label12_2 = QtWidgets.QPushButton(self)
        # self.label13_2 = QtWidgets.QPushButton(self)
        # self.label14_2 = QtWidgets.QPushButton(self)
        # self.label15_2 = QtWidgets.QPushButton(self)
        # self.label16_2 = QtWidgets.QPushButton(self)
        # self.label17_2 = QtWidgets.QPushButton(self)
        # self.label18_2 = QtWidgets.QPushButton(self)
        # self.label19_2 = QtWidgets.QPushButton(self)
        # self.label20_2 = QtWidgets.QPushButton(self)
        # self.label21_2 = QtWidgets.QPushButton(self)
        # self.label22_2 = QtWidgets.QPushButton(self)
        # self.label23_2 = QtWidgets.QPushButton(self)
        # self.label24_2 = QtWidgets.QPushButton(self)
        # self.label25_2 = QtWidgets.QPushButton(self)
        # self.label26_2 = QtWidgets.QPushButton(self)
        # self.label27_2 = QtWidgets.QPushButton(self)
        # self.label28_2 = QtWidgets.QPushButton(self)
        # self.label29_2 = QtWidgets.QPushButton(self)
        # self.label30_2 = QtWidgets.QPushButton(self)
        # self.label31_2 = QtWidgets.QPushButton(self)
        # self.label32_2 = QtWidgets.QPushButton(self)
        # self.label33_2 = QtWidgets.QPushButton(self)
        # self.label34_2 = QtWidgets.QPushButton(self)
        # self.label35_2 = QtWidgets.QPushButton(self)
        # self.label36_2 = QtWidgets.QPushButton(self)

        self.setGeometry(100, 60, 860, 650)
        self.setWindowTitle("Mathemechanik")
        self.init_startUI()


    def init_startUI(self):

        self.welcome.setText("Mathemechanik")
        self.welcome.move(480, 20)
        self.welcome.setFixedWidth(250)
        self.welcome.setFixedHeight(70)
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setStyleSheet(
            "*{font-size: 35px;" +
            "color: 'white';}"
        )

        ###   init text "Compexity"  ###

        self.complexity_text.setText("Chose a level")
        self.complexity_text.move(70, 50)
        self.complexity_text.setFixedWidth(250)
        self.complexity_text.setFixedHeight(70)
        self.complexity_text.setAlignment(QtCore.Qt.AlignCenter)
        self.complexity_text.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}"
        )

        ###   init button level1###

        self.level1.setText("Level 1")
        self.level1.move(70, 140)
        # self.label1 = QtWidgets.QPushButton(self)
        # self.create_labels()
        self.level1.clicked.connect(lambda: self.hide_levels("1"))
        self.level1.clicked.connect(lambda: self.field_init('3x3', 'level1'))
        # self.level1.clicked.connect(lambda: self.field_init('3x3', 'level1'))

        # self.b5.clicked.connect(self.set_text)
        self.level1.setFixedWidth(120)

        self.level1.setFixedHeight(40)
        # self.complexity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.level1.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        ###   init button level2###

        self.level2.setText("Level 2")
        self.level2.move(200, 140)
        self.level2.clicked.connect(lambda: self.hide_levels("2"))
        self.level2.clicked.connect(lambda: self.field_init('4x4', 'level2'))
       # self.level2.clicked.connect(lambda: self.field_init('4x4', 'level2'))
        # self.b5.clicked.connect(self.set_text)
        self.level2.setFixedWidth(120)
        self.level2.setFixedHeight(40)
        # self.complexity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.level2.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        ###  init button level3 ###

        self.level3.setText("Level 3")
        self.level3.move(70, 185)
        self.level3.clicked.connect(lambda: self.hide_levels("3"))
        self.level3.clicked.connect(lambda: self.field_init('4x4', 'level3'))
        # self.b5.clicked.connect(self.set_text)
        self.level3.setFixedWidth(120)
        self.level3.setFixedHeight(40)
        # self.complexity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.level3.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        ###   init button level4  ###

        self.level4.setText("Level 4")
        self.level4.move(200, 185)
        self.level4.clicked.connect(lambda: self.hide_levels("4"))
        self.level4.clicked.connect(lambda: self.field_init('4x4', 'level4'))
        # self.b5.clicked.connect(self.set_text)
        self.level4.setFixedWidth(120)
        self.level4.setFixedHeight(40)
        # self.complexity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.level4.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        ###   init button level5   ###

        self.level5.setText("Level 5")
        self.level5.move(70, 230)
        self.level5.clicked.connect(lambda: self.hide_levels("5"))
        self.level5.clicked.connect(lambda: self.field_init('5x5', 'level5'))
        # self.b5.clicked.connect(self.set_text)
        self.level5.setFixedWidth(120)
        self.level5.setFixedHeight(40)
        # self.complexity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.level5.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        ###   init button level6  ###

        self.level6.setText("Level 6")
        self.level6.move(200, 230)
        self.level6.clicked.connect(lambda: self.hide_levels("6"))
        self.level6.clicked.connect(lambda: self.field_init('5x5', 'level6'))
        # self.b5.clicked.connect(self.set_text)
        self.level6.setFixedWidth(120)
        self.level6.setFixedHeight(40)
        # self.complexity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.level6.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )



        ###  init button "Close" ###

        self.closeButton.setText("Close")
        self.closeButton.move(70, 563)
        self.closeButton.clicked.connect(self.closeApp)
        self.closeButton.setFixedWidth(250)
        self.closeButton.setFixedHeight(40)
        self.closeButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#FC0000';}"
        )

    ###  init field with certain size, and set this field with numbers from a map (level)   ###

    def field_init(self, size, level):

        if size == '3x3':
            level1.grid_3x3(self)
            # level1.clickable_labels(self)

        elif size == '4x4':
            levels2_3_4.grid_4x4(self)
            # levels2_3_4.clickable_labels(self)

        elif size == '5x5':
            levels5_6.grid_5x5(self)
            # levels5_6.clickable_labels(self)

        if level == 'level1':
            # self.hide_field("hide_list1")
            level1.clickable_labels(self)
            level1.set_text(self, "map1.txt")
            self.new_show()
        elif level == 'level2':
            # self.hide_field("hide_list2")
            levels2_3_4.clickable_labels(self, "level2")
            levels2_3_4.set_text(self, "map2.txt")
            self.new_show()

        elif level == 'level3':
            levels2_3_4.clickable_labels(self, "level3")
            levels2_3_4.set_text(self, "map3.txt")
            self.new_show()

        elif level == 'level4':
            levels2_3_4.clickable_labels(self, "level4")
            levels2_3_4.set_text(self, "map4.txt")
            self.new_show()

        elif level == 'level5':
            levels5_6.clickable_labels(self, "level5")
            levels5_6.set_text(self, "map5.txt")
            #self.new_show()

        elif level == 'level6':
            levels5_6.clickable_labels(self, "level6")
            levels5_6.set_text(self, "map6.txt")
            #self.new_show()

    def closeApp(self):
        self.close()

    # def close_level(self, level):
    #     level.hide()
    #

    def change_level(self):
        self.change_level_button.setText("Change Level")
        self.change_level_button.move(70, 330)
        #self.Restart.hide()
        self.change_level_button.clicked.connect(lambda: self.change_level_())
        self.change_level_button.setFixedWidth(250)

        self.change_level_button.setFixedHeight(40)
        self.change_level_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.change_level_button.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

    @staticmethod
    def change_level_():
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)

    def hide_levels(self, current_level):
        self.level1_buttons = [self.level2, self.level3, self.level4, self.level5, self.level6]
        self.level2_buttons = [self.level1, self.level3, self.level4, self.level5, self.level6]
        self.level3_buttons = [self.level1, self.level2, self.level4, self.level5, self.level6]
        self.level4_buttons = [self.level1, self.level2, self.level3, self.level5, self.level6]
        self.level5_buttons = [self.level1, self.level2, self.level3, self.level4, self.level6]
        self.level6_buttons = [self.level1, self.level2, self.level3, self.level4, self.level5]
        if current_level == "1":
            for i in self.level1_buttons:
                i.hide()
        elif current_level == "2":
            for i in self.level2_buttons:
                i.hide()
        elif current_level == "3":
            for i in self.level3_buttons:
                i.hide()
        elif current_level == "4":
            for i in self.level4_buttons:
                i.hide()
        elif current_level == "5":
            for i in self.level5_buttons:
                i.hide()
        elif current_level == "6":
            for i in self.level6_buttons:
                i.hide()

    def new_show(self):
        for label in self.hide_list:
            label.show()

    def new_hide(self):
        for label in self.hide_list:
            label.hide()

    def hide_field(self, show):

        hide_list1 = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6,
                        self.label7, self.label8, self.label9, self.label10, self.label11, self.label12,
                        self.label13, self.label14, self.label15, self.label16, self.label17, self.label18,
                        self.label19, self.label20, self.label21, self.label22, self.label23, self.label24, self.label25]

        hide_list2 = [self.label1_2, self.label2_2, self.label3_2, self.label4_2, self.label5_2, self.label6_2,
                        self.label7_2, self.label8_2, self.label9_2, self.label10_2, self.label11_2, self.label12_2,
                        self.label13_2, self.label14_2, self.label15_2, self.label16_2, self.label17_2, self.label18_2,
                        self.label19_2, self.label20_2, self.label21_2, self.label22_2, self.label23_2, self.label24_2,
                        self.label25_2, self.label26_2, self.label27_2, self.label28_2, self.label29_2, self.label30_2,
                        self.label31_2, self.label32_2, self.label33_2, self.label34_2, self.label35_2, self.label36_2]

        # for label in hide_list1:
        #     label.hide()
        # for label in hide_list2:
        #     label.hide()
        print("hide_funkc")
        if show == "hide_list1":
            for label in hide_list2:
                label.hide()
            print("druhu zakriv")
            for label in hide_list1:
                label.show()
            print("pershu vidkryv")
        elif show == "hide_list2":
            for label in hide_list2:
                label.show()
            print("druhu vidryv")
            for label in hide_list1:
                label.hide()
            print("pershu zakriv")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
