"""
Sodda Timer Dasturi (PyQt5)
---------------------------
00:00:00 dan boshlab oldinga sanaydigan sodda dizaynli timer (sekundomer).

Ishga tushirish:
    pip install PyQt5
    python timer_app.py
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer


class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.is_running = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Timer")
        self.setFixedSize(340, 260)
        self.setStyleSheet("background-color: #f5f5f5;")

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(25)

        # Vaqt ko'rsatkichi
        self.time_display = QLabel("00:00:00")
        self.time_display.setAlignment(Qt.AlignCenter)
        self.time_display.setStyleSheet("""
            color: #222222;
            font-size: 48px;
            font-weight: 600;
            font-family: 'Consolas', monospace;
        """)
        layout.addWidget(self.time_display)

        # Tugmalar
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        self.start_btn = self.create_button("Boshlash")
        self.reset_btn = self.create_button("Tozalash")

        self.start_btn.clicked.connect(self.toggle_timer)
        self.reset_btn.clicked.connect(self.reset_timer)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.reset_btn)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def create_button(self, text):
        btn = QPushButton(text)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedHeight(42)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #222222;
                font-size: 14px;
                font-weight: 500;
                border: 1px solid #dddddd;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #eeeeee;
            }
        """)
        return btn

    # ---------- Mantiq ----------
    def toggle_timer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_btn.setText("Boshlash")
        else:
            self.timer.start(1000)
            self.is_running = True
            self.start_btn.setText("To'xtatish")

    def reset_timer(self):
        self.timer.stop()
        self.is_running = False
        self.seconds = 0
        self.start_btn.setText("Boshlash")
        self.refresh_display()

    def update_timer(self):
        self.seconds += 1
        self.refresh_display()

    def refresh_display(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        self.time_display.setText(f"{h:02d}:{m:02d}:{s:02d}")


def main():
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()