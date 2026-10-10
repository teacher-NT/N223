import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QComboBox, QLabel, QTextEdit,
    QVBoxLayout
)
from PyQt5.QtCore import Qt

from translate import Translator


style_title = """
    font-size: 40px;
    color:  #0cb310;
"""

style_combo = """
    font-size: 20px;
    border: 2px solid blue;
"""

style_input = """
    font-size: 22px;
    border:2px solid #066908;
    color: #474747;
"""

style_btn = """
    font-size: 28px;
    border: 3px solid #066908;
    border-radius: 20px;
    background-color: #54eb57;
    padding: 15px;
"""


LANGUAGES = {
    "O'zbek": "uz",
    "Rus": "ru",
    "Ingliz": "en",
    "Turk": "tr",
    "Arab": "ar"
}

class TarjimonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarjimon")
        self.move(1400, 100)
        self.vbox = QVBoxLayout()

        self.sarlavha = QLabel("Tarjimon")
        self.sarlavha.setStyleSheet(style_title)
        self.sarlavha.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.sarlavha)

        self._from_lang = QComboBox()
        self._from_lang.addItems(LANGUAGES.keys())
        self._from_lang.setFixedWidth(400)
        self._from_lang.setStyleSheet(style_combo)
        self.vbox.addWidget(self._from_lang)
        
        self.input_area = QTextEdit()
        self.input_area.setFixedSize(400, 200)
        self.input_area.setStyleSheet(style_input)
        # self.input_area.textChanged.connect(self.tarjima_qilish)
        self.vbox.addWidget(self.input_area)
         

        self._to_lang = QComboBox()
        self._to_lang.addItems(LANGUAGES.keys())
        self._to_lang.setFixedWidth(400)
        self._to_lang.setStyleSheet(style_combo)
        self.vbox.addWidget(self._to_lang)
        
        self.result_area = QTextEdit()
        self.result_area.setDisabled(True)
        self.result_area.setFixedSize(400, 200)
        self.result_area.setStyleSheet(style_input)
        self.vbox.addWidget(self.result_area)

        self.tarjima_btn = QPushButton("Tarjima qilish")
        self.tarjima_btn.setStyleSheet(style_btn)
        self.tarjima_btn.clicked.connect(self.tarjima_qilish)
        self.vbox.addWidget(self.tarjima_btn)

        self.setLayout(self.vbox)
        self.show()

    def tarjima_qilish(self):
        _from = self._from_lang.currentText()
        _to = self._to_lang.currentText()
        tarjimon = Translator(from_lang=LANGUAGES[_from], to_lang=LANGUAGES[_to])
        text = self.input_area.toPlainText()
        result = tarjimon.translate(text)
        self.result_area.setText(result)

app = QApplication([])
win = TarjimonApp()
app.exec_()