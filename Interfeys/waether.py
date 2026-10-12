import sys
import requests
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QLineEdit, QPushButton, QLabel)


def get_weather(city):
    try:
        geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
        geo_response = requests.get(geo_url, headers={'User-Agent': 'WeatherApp'}, timeout=10)
        geo_data = geo_response.json()

        if not geo_data:
            return None

        lat, lon = geo_data[0]['lat'], geo_data[0]['lon']


        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation&timezone=auto"
        weather_response = requests.get(weather_url, timeout=10)
        weather_data = weather_response.json()
        current = weather_data['current']
        result = {
            "shahar": city,
            "harorat": current['temperature_2m'],
            "namlik": current['relative_humidity_2m'],
            "shamol_tezligi": current['wind_speed_10m'],
            "yogingarchilik": current['precipitation']
        }

        return result

    except Exception as e:
        return None


class WeatherWorker(QThread):
    finished_signal = pyqtSignal(object)

    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        self.finished_signal.emit(get_weather(self.city))


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.value_labels = {}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ob-havo")
        self.setFixedSize(380, 360)

        main = QVBoxLayout(self)
        search_row = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Shahar nomini kiriting...")
        self.city_input.returnPressed.connect(self.search)
        self.search_btn = QPushButton("Qidirish")
        self.search_btn.clicked.connect(self.search)
        search_row.addWidget(self.city_input)
        search_row.addWidget(self.search_btn)
        main.addLayout(search_row)

        self.status = QLabel("Shahar nomini kiriting va «Qidirish» tugmasini bosing.")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setWordWrap(True)
        main.addWidget(self.status)


        self.city_title = QLabel("")
        self.city_title.setAlignment(Qt.AlignCenter)
        self.city_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        main.addWidget(self.city_title)

        grid = QGridLayout()
        rows = [
            ("harorat", "Harorat:", "°C"),
            ("namlik", "Namlik:", "%"),
            ("shamol_tezligi", "Shamol tezligi:", "km/soat"),
            ("yogingarchilik", "Yog'ingarchilik:", "mm"),
        ]
        self.units = {}
        for i, (key, title, unit) in enumerate(rows):
            name_lbl = QLabel(title)
            val_lbl = QLabel("—")
            val_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            val_lbl.setStyleSheet("font-size: 16px; font-weight: bold;")
            grid.addWidget(name_lbl, i, 0)
            grid.addWidget(val_lbl, i, 1)
            self.value_labels[key] = val_lbl
            self.units[key] = unit
        main.addLayout(grid)
        main.addStretch()

    def search(self):
        city = self.city_input.text().strip()
        if not city:
            self.status.setText("Iltimos, shahar nomini kiriting.")
            return

        self.search_btn.setEnabled(False)
        self.status.setText("Yuklanmoqda...")

        self.worker = WeatherWorker(city)
        self.worker.finished_signal.connect(self.show_result)
        self.worker.start()

    def show_result(self, data):
        self.search_btn.setEnabled(True)

        if data is None:
            self.status.setText("Ma'lumot topilmadi. Shahar nomini yoki internetni tekshiring.")
            self.city_title.setText("")
            for lbl in self.value_labels.values():
                lbl.setText("—")
            return

        self.status.setText("")
        self.city_title.setText(data["shahar"].title())
        for key, lbl in self.value_labels.items():
            lbl.setText(f"{data[key]} {self.units[key]}")



app = QApplication(sys.argv)
window = WeatherApp()
window.show()
sys.exit(app.exec_())