import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, \
    QMainWindow, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QCursor


def set_label(label, x, y):
    label.setFixedHeight(50.7)
    label.setFixedWidth(50.7)
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


def grid_5x5(parent):
    list_ = [parent.label1, parent.label2, parent.label3, parent.label4, parent.label5,
             parent.label6, parent.label7, parent.label8, parent.label9, parent.label10,
             parent.label11, parent.label12, parent.label13, parent.label14, parent.label15,
             parent.label16, parent.label17, parent.label18, parent.label19, parent.label20,
             parent.label21, parent.label22, parent.label23, parent.label24, parent.label25,
             parent.label26, parent.label27, parent.label28, parent.label29, parent.label30,
             parent.label31, parent.label32, parent.label33, parent.label34, parent.label35,
             parent.label36, parent.label37, parent.label38, parent.label39, parent.label40,
             parent.label41, parent.label42, parent.label43, parent.label44, parent.label45,
             parent.label46, parent.label47, parent.label48, parent.label49]

    list_sum = [parent.label10, parent.label11, parent.label12, parent.label13,
                parent.label14, parent.label16, parent.label23, parent.label30,
                parent.label37, parent.label44]

    a = 0
    b = 400
    for i in list_:
        set_label(i, b, 95 - a)
        a -= 55.7
        if a <= -389:
            a = 0
            b += 55.7
    for i in list_sum:
        set_sum_label(i)


def set_text(parent, map):
    list_ = [parent.label1, parent.label2, parent.label3, parent.label4, parent.label5,
             parent.label6, parent.label7, parent.label8, parent.label9, parent.label10,
             parent.label11, parent.label12, parent.label13, parent.label14, parent.label15,
             parent.label16, parent.label17, parent.label18, parent.label19, parent.label20,
             parent.label21, parent.label22, parent.label23, parent.label24, parent.label25,
             parent.label26, parent.label27, parent.label28, parent.label29, parent.label30,
             parent.label31, parent.label32, parent.label33, parent.label34, parent.label35,
             parent.label36, parent.label37, parent.label38, parent.label39, parent.label40,
             parent.label41, parent.label42, parent.label43, parent.label44, parent.label45,
             parent.label46, parent.label47, parent.label48, parent.label49]

    try:
        numbers = read_numbers(map)
    except (UnicodeDecodeError, ValueError):
        parent.msg_box("Error")
    else:
        i = 0
        for label in list_:
            label.setText(str(numbers[i]))
            i += 1


def clickable_labels(parent, level):
    parent.label17.clicked.connect(
        lambda: step(parent, parent.label17, parent.label3, parent.label15, parent.label10, parent.label16, level))  # 161219
    parent.label18.clicked.connect(
        lambda: step(parent, parent.label18, parent.label4, parent.label15, parent.label11, parent.label16, level))
    parent.label19.clicked.connect(
        lambda: step(parent, parent.label19, parent.label5, parent.label15, parent.label12, parent.label16, level))
    parent.label20.clicked.connect(
        lambda: step(parent, parent.label20, parent.label6, parent.label15, parent.label13, parent.label16, level))
    parent.label21.clicked.connect(
        lambda: step(parent, parent.label21, parent.label7, parent.label15, parent.label14, parent.label16, level))

    parent.label24.clicked.connect(
        lambda: step(parent, parent.label24, parent.label3, parent.label22, parent.label10, parent.label23, level))
    parent.label25.clicked.connect(
        lambda: step(parent, parent.label25, parent.label4, parent.label22, parent.label11, parent.label23, level))
    parent.label26.clicked.connect(
        lambda: step(parent, parent.label26, parent.label5, parent.label22, parent.label12, parent.label23, level))
    parent.label27.clicked.connect(
        lambda: step(parent, parent.label27, parent.label6, parent.label22, parent.label13, parent.label23, level))
    parent.label28.clicked.connect(
        lambda: step(parent, parent.label28, parent.label7, parent.label22, parent.label14, parent.label23, level))

    parent.label31.clicked.connect(
        lambda: step(parent, parent.label31, parent.label3, parent.label29, parent.label10, parent.label30, level))
    parent.label32.clicked.connect(
        lambda: step(parent, parent.label32, parent.label4, parent.label29, parent.label11, parent.label30, level))
    parent.label33.clicked.connect(
        lambda: step(parent, parent.label33, parent.label5, parent.label29, parent.label12, parent.label30, level))
    parent.label34.clicked.connect(
        lambda: step(parent, parent.label34, parent.label6, parent.label29, parent.label13, parent.label30, level))
    parent.label35.clicked.connect(
        lambda: step(parent, parent.label35, parent.label7, parent.label29, parent.label14, parent.label30, level))

    parent.label38.clicked.connect(
        lambda: step(parent, parent.label38, parent.label3, parent.label36, parent.label10, parent.label37, level))
    parent.label39.clicked.connect(
        lambda: step(parent, parent.label39, parent.label4, parent.label36, parent.label11, parent.label37, level))
    parent.label40.clicked.connect(
        lambda: step(parent, parent.label40, parent.label5, parent.label36, parent.label12, parent.label37, level))
    parent.label41.clicked.connect(
        lambda: step(parent, parent.label41, parent.label6, parent.label36, parent.label13, parent.label37, level))
    parent.label42.clicked.connect(
        lambda: step(parent, parent.label42, parent.label7, parent.label36, parent.label14, parent.label37, level))

    parent.label45.clicked.connect(
        lambda: step(parent, parent.label45, parent.label3, parent.label43, parent.label10, parent.label44, level))
    parent.label46.clicked.connect(
        lambda: step(parent, parent.label46, parent.label4, parent.label43, parent.label11, parent.label44, level))
    parent.label47.clicked.connect(
        lambda: step(parent, parent.label47, parent.label5, parent.label43, parent.label12, parent.label44, level))
    parent.label48.clicked.connect(
        lambda: step(parent, parent.label48, parent.label6, parent.label43, parent.label13, parent.label44, level))
    parent.label49.clicked.connect(
        lambda: step(parent, parent.label49, parent.label7, parent.label43, parent.label14, parent.label44, level))


def step(parent, label, label_sum_l, label_sum_t, label_fixed_l, label_fixed_t, level):
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

    check_winning(parent, level)


def check_winning(parent, level):
    color3 = parent.label3.palette().window().color().name()
    color4 = parent.label4.palette().window().color().name()
    color5 = parent.label5.palette().window().color().name()
    color6 = parent.label6.palette().window().color().name()
    color7 = parent.label7.palette().window().color().name()
    color15 = parent.label15.palette().window().color().name()
    color22 = parent.label22.palette().window().color().name()
    color29 = parent.label29.palette().window().color().name()
    color36 = parent.label36.palette().window().color().name()
    color43 = parent.label43.palette().window().color().name()
    if color3 == color4 == color5 == color6 == color7 == color15 == color22 == color29 == color36 == color43 =="#428a55":
        msg_box(parent, level)
        #parent.field_init('5x5', 'level5')
        parent.field_init('5x5', level)


def msg_box(parent, level):
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
    #msg.buttonClicked.connect(parent.delete_field)
    msg.buttonClicked.connect(lambda: parent.field_init('5x5', level))
    parent.change_level()
    # msg.buttonClicked.connect(parent.init_startUI)
    #msg.buttonClicked.connect(parent.new_hide)

    msg.show()
    return msg
