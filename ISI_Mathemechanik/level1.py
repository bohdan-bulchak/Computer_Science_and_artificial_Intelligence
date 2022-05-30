import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, \
    QMainWindow, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QCursor

import main


def set_label(label, x, y):
    label.setFixedHeight(73)
    label.setFixedWidth(73)
    label.move(x, y)
    label.setStyleSheet(
        "*{font-size: 22px;" +
        "color: 'white';" +
        "border: 2px solid #BC006C;" +
        "border-radius: 3px;" +
        "text-align: center;}" +
        "*:hover{background: '#350032';}"
    )
    label.setText("")


def set_sum_label(label):
    label.setStyleSheet(
        "*{font-size: 22px;" +
        "color: 'white';" +
        "border: 2px solid #BC006C;" +
        "text-align: center;" +
        "background: '#F96BA0';}"
    )


def read_numbers(path):
    numbers = []
    with open(path) as fileHandler:
        for line in fileHandler:
            line1 = line.strip()
            numbers.append(line1)
    fileHandler.close()
    return numbers


def grid_3x3(parent):
    list_ = [parent.label1, parent.label2, parent.label3, parent.label4, parent.label5,
             parent.label6, parent.label7, parent.label8, parent.label9, parent.label10,
             parent.label11, parent.label12, parent.label13, parent.label14, parent.label15,
             parent.label16, parent.label17, parent.label18, parent.label19, parent.label20,
             parent.label21, parent.label22, parent.label23, parent.label24, parent.label25]

    list_sum = [parent.label8, parent.label9, parent.label10, parent.label12,
                parent.label17, parent.label22]

    a = 0
    b = 400
    for i in list_:
        set_label(i, b, 95 - a)
        a -= 78
        if a == -390:
            a = 0
            b += 78
    for i in list_sum:
        set_sum_label(i)


def set_text(parent, map):
    list_ = [parent.label1, parent.label2, parent.label3, parent.label4, parent.label5,
             parent.label6, parent.label7, parent.label8, parent.label9, parent.label10,
             parent.label11, parent.label12, parent.label13, parent.label14, parent.label15,
             parent.label16, parent.label17, parent.label18, parent.label19, parent.label20,
             parent.label21, parent.label22, parent.label23, parent.label24, parent.label25]

    try:
        numbers = read_numbers(map)
    except (UnicodeDecodeError, ValueError):
        parent.msg_box("Error")
    else:
        i = 0
        for label in list_:
            label.setText(str(numbers[i]))
            i += 1



def clickable_labels(parent):

    parent.label13.clicked.connect(
        lambda: step(parent, parent.label13, parent.label3, parent.label11, parent.label8, parent.label12))  # 161219
    parent.label14.clicked.connect(
        lambda: step(parent, parent.label14, parent.label4, parent.label11, parent.label9, parent.label12))
    parent.label15.clicked.connect(
        lambda: step(parent, parent.label15, parent.label5, parent.label11, parent.label10, parent.label12))

    parent.label18.clicked.connect(
        lambda: step(parent, parent.label18, parent.label3, parent.label16, parent.label8, parent.label17))
    parent.label19.clicked.connect(
        lambda: step(parent, parent.label19, parent.label4, parent.label16, parent.label9, parent.label17))
    parent.label20.clicked.connect(
        lambda: step(parent, parent.label20, parent.label5, parent.label16, parent.label10, parent.label17))

    parent.label23.clicked.connect(
        lambda: step(parent, parent.label23, parent.label3, parent.label21, parent.label8, parent.label22))
    parent.label24.clicked.connect(
        lambda: step(parent, parent.label24, parent.label4, parent.label21, parent.label9, parent.label22))
    parent.label25.clicked.connect(
        lambda: step(parent, parent.label25, parent.label5, parent.label21, parent.label10, parent.label22))


def step(parent, label, label_sum_l, label_sum_t, label_fixed_l, label_fixed_t):
    colorr = label.palette().window().color().name()
    if colorr == '#161219':
        num_label = int(label.text())
        num_sum1 = int(label_sum_l.text())
        num_sum2 = int(label_sum_t.text())
        num_sum1_new = str(num_label + num_sum1)
        num_sum2_new = str(num_label + num_sum2)
        label_sum_l.setText(num_sum1_new)
        label_sum_t.setText(num_sum2_new)
        label.setStyleSheet(
            "*{font-size: 22px;" +
            "color: 'white';" +
            "border: 2px solid #b47be3;" +  # BC006C
            "text-align: center;"
            "background: '#98579c';}"
        )
        if label_sum_l.text() == label_fixed_l.text():
            label_sum_l.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #bd9b3e;" +
                "text-align: center;"
                "background: '#428a55';}"
            )
        else:
            label_sum_l.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #BC006C;" +
                "text-align: center;"
                "background: '#161219';}"
            )
        if label_sum_t.text() == label_fixed_t.text():
            label_sum_t.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #bd9b3e;" +
                "text-align: center;"
                "background: '#428a55';}"
            )
        else:
            label_sum_t.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #BC006C;" +
                "text-align: center;"
                "background: '#161219';}"
            )
    else:
        num_label = int(label.text())
        num_sum1 = int(label_sum_l.text())
        num_sum2 = int(label_sum_t.text())
        num_sum1_new = str(num_sum1 - num_label)
        num_sum2_new = str(num_sum2 - num_label)
        label_sum_l.setText(num_sum1_new)
        label_sum_t.setText(num_sum2_new)
        label.setStyleSheet(
            "*{font-size: 22px;" +
            "color: 'white';" +
            "border: 2px solid #BC006C;" +
            "text-align: center;"
            "background: '#161219';}"
        )
        if label_sum_l.text() != label_fixed_l.text():
            label_sum_l.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #BC006C;" +
                "text-align: center;"
                "background: '#161219';}"
            )
        else:
            label_sum_l.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #bd9b3e;" +
                "text-align: center;"
                "background: '#428a55';}"
            )

        if label_sum_t.text() != label_fixed_t.text():
            label_sum_t.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #BC006C;" +
                "text-align: center;"
                "background: '#161219';}"
            )
        else:
            label_sum_t.setStyleSheet(
                "*{font-size: 22px;" +
                "color: 'white';" +
                "border: 2px solid #bd9b3e;" +
                "text-align: center;"
                "background: '#428a55';}"
            )

    check_winning(parent)


def check_winning(parent):
    color3 = parent.label3.palette().window().color().name()
    color4 = parent.label4.palette().window().color().name()
    color5 = parent.label5.palette().window().color().name()
    color11 = parent.label11.palette().window().color().name()
    color16 = parent.label16.palette().window().color().name()
    color21 = parent.label21.palette().window().color().name()

    if color3 == color4 == color5 == color11 == color16 == color21 == "#428a55":
        msg_box(parent)
        #parent.new_hide()
        parent.field_init('3x3', 'level1')
        #parent.field_init('3x3', 'level1')



def msg_box(parent):

    msg = QMessageBox(parent)
    msg.setWindowTitle(f'Gongrats!')
    msg.setStyleSheet(
        "QMessageBox{background-color: #161219;" + "color: white;" + "font: bold;" + "width: 700px;" + "height: 500px;}"
        + "QLabel{background:transparent;" + "color:#fff;" +
        "font-size: 25px; min-width: 300px; min-height: 200px;}"
        "QPushButton{width: 150px;" + "border: 2px solid '#BC006C';" +
        "border-radius: 3px;" +
        "font-size: 15px;" +
        "color: 'white';}" + "QPushButton:hover{background-color: '#BC006C';}")
    msg.setText(f'            You won!')
    msg.setStandardButtons(QMessageBox.Ok)

    #msg.buttonClicked.connect(lambda: parent.close_level(parent.level1))
    msg.buttonClicked.connect(lambda: parent.field_init('3x3', 'level1'))
    #msg.buttonClicked.connect(parent.new_hide)
    #msg.buttonClicked.connect(parent.new_hide)
    parent.change_level()

    msg.show()
    return msg



