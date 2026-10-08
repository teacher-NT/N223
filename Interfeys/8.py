import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QCheckBox, QRadioButton, QMessageBox
)

app = QApplication([])


style_combo = """
    font-size: 22px;
    background-color: yellow;
    border: 2px solid black;
"""

style_checkbox = """
    font-size: 22px;
    font-weight: bold;
"""

style_radio = """
    font-size: 20px;
    color: blue;
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1400, 100, 400, 700)
        self.setWindowTitle("Dastur")
        self.vbox = QVBoxLayout()

        self.matn1 = QLabel("Welcome to Milliy Food")
        self.matn1.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            color: blue;
        """)
        self.vbox.addWidget(self.matn1)

        self.matn2 = QLabel("Taom tanlanmagan")
        self.matn2.setStyleSheet("""
                    font-size: 22px;
                    font-weight: bold;
                    color: black;
                """)
        self.vbox.addWidget(self.matn2)

        self.matn3 = QLabel("Ichimlik tanlanmagan")
        self.matn3.setStyleSheet("""
                    font-size: 20px;
                    font-weight: bold;
                    color: black;
                """)
        self.vbox.addWidget(self.matn3)

        self.add_combo()
        self.add_checkbox()
        self.add_radio()

        self.btn1 = QPushButton("Buyurtma berish")
        self.btn1.setStyleSheet("""
            font-size: 20px;
            background-color: lightgreen;
            border: 2px solid black;
        """)
        self.btn1.clicked.connect(self.buyurtma_berish)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

        self.show()
    
    def add_combo(self):
        self.menu = QComboBox()
        self.menu.addItems(['Palov', 'Somsa', "Sho'rva", "Shashlik", "Manti"])
        self.menu.setStyleSheet(style_combo)
        self.menu.currentTextChanged.connect(self.set_food)
        self.vbox.addWidget(self.menu)

    def set_food(self):
        food = self.menu.currentText()
        self.matn2.setText(f"Savatingizda: {food}")

    def add_checkbox(self):
        self.ch1 = QCheckBox("Choy 🫖")
        self.ch1.setStyleSheet(style_checkbox)
        self.ch1.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch1)

        self.ch2 = QCheckBox("Coffee ☕️")
        self.ch2.setStyleSheet(style_checkbox)
        self.ch2.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch2)

        self.ch3 = QCheckBox("Pepsi 🥃")
        self.ch3.setStyleSheet(style_checkbox)
        self.ch3.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch3)

        self.ch4 = QCheckBox("Moxito 🥤")
        self.ch4.setStyleSheet(style_checkbox)
        self.ch4.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch4)

        self.ch5 = QCheckBox("Suv 🥛")
        self.ch5.setStyleSheet(style_checkbox)
        self.ch5.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch5)

    def set_drink(self):
        drinks = []
        if self.ch1.isChecked():
            drinks.append(self.ch1.text())
        if self.ch2.isChecked():
            drinks.append(self.ch2.text())
        if self.ch3.isChecked():
            drinks.append(self.ch3.text())
        if self.ch4.isChecked():
            drinks.append(self.ch4.text())
        if self.ch5.isChecked():
            drinks.append(self.ch5.text())

        drinks = "\n- ".join(drinks)
        self.matn3.setText(f"Tanlangan ichimliklar: \n- {drinks}")

    def add_radio(self):
        self.r1 = QRadioButton("Naqd")
        self.r1.setStyleSheet(style_radio)
        self.vbox.addWidget(self.r1)

        self.r2 = QRadioButton("Terminal")
        self.r2.setStyleSheet(style_radio)
        self.vbox.addWidget(self.r2)

        self.r3 = QRadioButton("Onlayn")
        self.r3.setStyleSheet(style_radio)
        self.vbox.addWidget(self.r3)

    def buyurtma_berish(self):
        QMessageBox.question(self, "Xabar", "Buyurtmangizni tasdiqlaysizmi!")

win = Window()
app.exec_()