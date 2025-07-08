import requests
import json

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton
from PySide6 import QtWidgets
from ui_form import Ui_Widget
import sys

BASE = "http://localhost:8000"

#pyside6-uic form.ui -o ui_form.py um py Datei zu erstellen

#sudo apt update
#sudo apt install libxcb-cursor0 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Nach dem Start Login-Seite anzeigen
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLogin)

        username = self.ui.lineEditUsername.text()
        password = self.ui.lineEditPassword.text()

        # Login verbinden
        self.ui.pushButtonLogin.clicked.connect(self.login)

        #Register verbinden
        self.ui.pushButtonRegister.clicked.connect(self.register)

        # Logout verbinden
        self.ui.pushButtonLogout.clicked.connect(self.logout)

        #Inventar verbinden
        self.ui.pushButtonInventory.clicked.connect(self.inventory)

        #Zurück-Button
        self.ui.pushButtonZurueck.clicked.connect(self.back)





        # Tabelle konfigurieren
        #self.setup_markttabelle()

    def login(self, username, password):

        response = requests.post(f"{BASE}/login", json={"username" : username, "password" : "password"})
    
        if response.status_code != 200:
            print(response.json().get("detail"))
            return None
        
        else: 

            #self.ui.labelCoins.setText(account balance?)
            data = response.json()
            self.ui.labelStatus.setText(data["message"])
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)





    def register(self, username, password):

        username = self.ui.lineEditUsername.text()
        password = self.ui.lineEditPassword.text()

        response = requests.post(f"{BASE}/register", json={"username" : username, "password" : "password"})
    
        if response.status_code != 200:
            print(response.json().get("detail"))
            
        else:
            #self.ui.labelCoins.setText(account balance?)
            data = response.json()
            self.ui.labelStatus.setText(data["message"])
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)



    def logout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLogin)


    def inventory(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageInventar)

    def back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)


    def accountinfo(username):

        response = requests.post(f"{BASE}/register", json={"username"})

        if response.status_code != 200:
            print(response.json().get("detail"))

        else:
            data = response.json()
            return data["balance"], data["inventory"]



    #def setup_inventartabelle(self):


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

    def buy(self, zeile):
        name = self.ui.tableMarkt.item(zeile, 0).text()
        print(f"Gekauft: {name}")
        # später REST-Request senden

    def sell(self):



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




