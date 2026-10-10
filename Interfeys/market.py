import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QScrollArea,
    QGridLayout, QComboBox, QLineEdit
)
from PyQt5.QtCore import Qt
import json



style_matn1 = """
    font-size: 45px;
    color: red;
    font-weight: bold;
"""

style_category = """
    font-size: 25px;
    color: #de5207;
    background-color: #c5f542;
    border: 2px solid black;
"""

style_search = """
    font-size: 25px;

"""

style_btnsearch = """
    font-size: 25px;
    background-color: #b2f202;
    color: #de5207;
    padding: 5px 15px;
    border: 2px solid black;
    border-radius: 15px;
"""

class MarketApp(QWidget):
    def  __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 1000, 600)
        # self.move(1000, 100)
        self.container = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)   # juda muhim!
        self.scroll.setWidget(self.container)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.box = QGridLayout(self.container)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)

        self.matn1 = QLabel("Najot Market")
        self.matn1.setStyleSheet(style_matn1)
        self.matn1.setAlignment(Qt.AlignTop)
        self.box.addWidget(self.matn1, 1, 1)

        self.category = QComboBox()
        with open("N223/Interfeys/products.json") as file:
            self.products = json.load(file)
            categories = set()
            for product in self.products:
                categories.add(product['kategoriyasi'])
        self.category.addItems(categories)
        self.category.setStyleSheet(style_category)
        self.category.currentTextChanged.connect(self.load_products_by_category)
        self.box.addWidget(self.category, 2,1)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Mahsulot nomi...")
        self.search.setStyleSheet(style_search)
        self.box.addWidget(self.search, 2,2)

        self.btn_search = QPushButton("Qidirish")
        self.box.addWidget(self.btn_search, 2, 3)
        self.btn_search.setStyleSheet(style_btnsearch)
        self.btn_search.clicked.connect(self.search_product)
        self.load_products()

        self.setLayout(self.vbox)
        self.show()

    def clear_cell(self):
        q, u = 3, 1
        for i in self.products:
            if u == 4:
                q += 1
                u = 1
            item = self.box.itemAtPosition(q, u)
            if item is None:          # katak bo'sh
                return
            widget = item.widget()
            if widget:
                self.box.removeWidget(widget)
                widget.deleteLater()
            u += 1 

    def load_products(self):
        with open("N223/Interfeys/products.json") as file:
            products = json.load(file)
        
        self.labels = []
        q, u = 3, 1
        for  product in products:
            label = QLabel(f"{product['nomi']}\n{product['narxi']} so'm\n{product['kategoriyasi']}\n{product['ishlab-chiqarilgan vaqti']}")
            label.setStyleSheet("font-size:18px; border: 1px solid black;")
            self.box.addWidget(label, q, u)
            u += 1
            if u == 4:
                q += 1
                u = 1
            self.labels.append(label)

    def load_products_by_category(self):
        self.clear_cell()
        
        self.labels = []
        q, u = 3, 1
        for  product in self.products:
            if product['kategoriyasi'] == self.category.currentText():
                label = QLabel(f"{product['nomi']}\n{product['narxi']} so'm\n{product['kategoriyasi']}\n{product['ishlab-chiqarilgan vaqti']}")
                label.setStyleSheet("font-size:18px; border: 1px solid black;")
                self.box.addWidget(label, q, u)
                u += 1
                if u == 4:
                    q += 1
                    u = 1
                self.labels.append(label)


    def search_product(self):
        self.clear_cell()
        self.labels = []
        q, u = 3, 1
        for  product in self.products:
            if product['nomi'].lower() == self.search.text().lower():
                label = QLabel(f"{product['nomi']}\n{product['narxi']} so'm\n{product['kategoriyasi']}\n{product['ishlab-chiqarilgan vaqti']}")
                label.setStyleSheet("font-size:18px; border: 1px solid black;")
                self.box.addWidget(label, q, u)
                u += 1
                if u == 4:
                    q += 1
                    u = 1
                self.labels.append(label)

app = QApplication([])
win = MarketApp()
app.exec_()