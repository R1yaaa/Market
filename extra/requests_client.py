import requests
import json

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton
from PySide6 import QtWidgets
from ui_form import Ui_Widget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Beispiel: Nach dem Start Login-Seite anzeigen
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLogin)

        # Login verbinden
        self.ui.pushButtonLogin.clicked.connect(self.login)

        # Logout verbinden
        self.ui.pushButtonLogout.clicked.connect(self.logout)

        # Tabelle konfigurieren
        #self.setup_markttabelle()

    def login(self):
        name = self.ui.lineEditUsername.text()
        if name:
            self.ui.labelCoins.setText("Coins: 100.00")
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)
        else:
            self.ui.labelStatus.setText("Bitte Namen eingeben")

    def logout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLogin)

    def setup_markttabelle(self):
        table = self.ui.tableMarkt
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Name", "Preis", "Verkäufer", "Kaufen"])
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        angebote = [
            {"name": "Kaktus", "preis": 12.5, "verkaeufer": "Max123"},
            {"name": "Banane", "preis": 7.2, "verkaeufer": "AnnaB"},
        ]

        table.setRowCount(len(angebote))
        for i, a in enumerate(angebote):
            table.setItem(i, 0, QTableWidgetItem(a["name"]))
            table.setItem(i, 1, QTableWidgetItem(f"{a['preis']}"))
            table.setItem(i, 2, QTableWidgetItem(a["verkaeufer"]))
            button = QPushButton("Kaufen")
            button.clicked.connect(lambda _, row=i: self.kaufen(row))
            table.setCellWidget(i, 3, button)

    def kaufen(self, zeile):
        name = self.ui.tableMarkt.item(zeile, 0).text()
        print(f"Gekauft: {name}")
        # später REST-Request senden

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


#BASE = "http://localhost:8000"

