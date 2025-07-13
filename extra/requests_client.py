import requests
import json

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QTableWidgetItem
from PySide6 import QtWidgets
from ui_form import Ui_Widget
from PySide6.QtCore import QTimer
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

        #TStyling
        self.setup_gui_styling()

        # Login verbinden
        self.ui.pushButtonLogin.clicked.connect(self.login)

        #Register verbinden
        self.ui.pushButtonRegister.clicked.connect(self.register)

        # Logout verbinden
        self.ui.pushButtonLogout.clicked.connect(self.logout)

        #Inventar verbinden
        self.ui.pushButtonInventory.clicked.connect(self.inventory)

        #Zurück Button
        self.ui.pushButtonZurueck.clicked.connect(self.back)

        #Kauf Button
        self.ui.pushButtonBuy.clicked.connect(self.buy)

        #Verkaufen Button
        self.ui.pushButtonSell.clicked.connect(self.sell)




        #Startwerte
        self.username = ""
        self.password = ""





        #Timer für Preisupdates
        self.timer = QTimer()
        self.timer.timeout.connect(self.prices)
        self.timer.start(2000) # alle 2 Sekunden


    


    def login(self):
        self.username = self.ui.lineEditUsername.text()
        self.password = self.ui.lineEditPassword.text()

        response = requests.post(f"{BASE}/login", json={"username" : self.username, "password" : self.password})
    
        if response.status_code != 200:
            self.ui.labelStatus.setText(response.json().get("detail"))
            return

        data = response.json()
        self.ui.labelStatus.setText(data["message"])

        self.load_account()
        self.load_market()

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)





    def register(self):
        self.username = self.ui.lineEditUsername.text()
        self.password = self.ui.lineEditPassword.text()

        response = requests.post(f"{BASE}/register", json={"username" : self.username, "password" : self.password})
    
        if response.status_code != 200:
            self.ui.labelStatus.setText(response.json().get("detail"))
            return
            
        data = response.json()
        self.ui.labelStatus.setText(data["message"])
        self.load_account()
        self.load_market()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)





    def load_account(self):
            response = requests.get(f"{BASE}//{self.username}/accountinfo", json={self.username})

            if response.status_code == 200:
                balance = response.json()["balance"]        
                self.ui.labelCoins.setText(str(balance))            #aktueller Kontostand
                self.ui.labelCoins_2.setText(str(balance))
            else:
                self.ui.labelStatus.setText("Fehler beim Laden des Accounts.")




    def logout(self):
        self.clear_all_inputs()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLogin)



    #Hilfsfunktion
    def clear_all_inputs(self):
        for widget in self.findChildren(QtWidgets.QLineEdit):
            widget.clear()

        for spin in self.findChildren(QtWidgets.QSpinBox):
            spin.setValue(0)

        self.ui.labelStatus.clear()
        self.ui.labelSellInfo.clear()
        self.ui.labelBuyInfo.clear()


    def inventory(self):
        self.load_inventory()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageInventar)


    def load_inventory(self):

        try:
            response = requests.get(f"{BASE}/{self.username}/accountinfo")

            if response.status_code == 200:
                self.ui.tableWidgetInventory.setRowCount(0)
                inv = response.json()

                for i, (name, preis, menge, gid) in enumerate(zip(
                    inv["Name"], inv["Price"], inv["QUantity"], inv["ID"]
                )):
                    self.ui.tableWidgetInventory.setItem(i, 0, QTableWidgetItem(str(name)))
                    self.ui.tableWidgetInventory.setItem(i, 1, QTableWidgetItem(str(preis)))
                    self.ui.tableWidgetInventory.setItem(i, 2, QTableWidgetItem(str(menge)))
                    self.ui.tableWidgetInventory.setItem(i, 3, QTableWidgetItem(str(gid)))
                    
            else:
                self.ui.labelSellInfo.setText("Fehler beim Laden des Inventars")

        except Exception as e:
            self.ui.labelSellInfo.setText(f"Fehler: {e}")



    def back(self):
        self.load_market()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMarket)




    def accountinfo(self):                              

        response = requests.post(f"{BASE}/{self.username}/accountinfo", json={self.username})

        if response.status_code != 200:
            print(response.json().get("detail"))
            return None

        else:
            data = response.json()
            balance = data["balance"]
            inventory = {
                "ID": data["ID"],
                "Name" : data["Name"],
                "Price" : data["Price"],
                "Quantity" : data["Quantity"]
            }
            return balance, inventory


    def prices(self):
        try:
            response = requests.get(f"{BASE}/prices")
            self.load_market()
        except Exception:
            pass
        

    def load_market(self):
        self.ui.tableGueter.clearContents()
        try:
            response = requests.get(f"{BASE}/offers")

            if response.status_code == 200:
                self.ui.tableGueter.setRowCount(0)
                goods = response.json()

                for i, (name, preis, menge, gid) in enumerate(zip(
                    goods["Name"], goods["Price"], goods["Quantity"], goods["ID"])):
                 
                    self.ui.tableGueter.insertRow(i)
                    self.ui.tableGueter.setItem(i, 0, QTableWidgetItem(name))
                    self.ui.tableGueter.setItem(i, 1, QTableWidgetItem(str(preis)))
                    self.ui.tableGueter.setItem(i, 2, QTableWidgetItem(str(menge)))
                    self.ui.tableGueter.setItem(i, 3, QTableWidgetItem(str(gid)))
        except Exception as e:
            self.ui.labelBuyInfo.setText(f"Fehler beim Laden des Markts: {e}")


        

    def buy(self):
        zeile = self.ui.tableGueter.currentRow()
        if zeile == -1:
            self.ui.labelBuyInfo.setText("Bitte Gut auswählen")
            return
        
        password = self.ui.lineEditBuyPassword.text()
        menge = self.ui.spinBoxBuy.value()

        good_id = int(self.ui.tableGueter.item(zeile, 3).text())
        good_name = self.ui.tableGueter.item(zeile, 0).text()

        payload = {
            "data": {
                "goodname": good_name,
                "goodid" : good_id,
                "quantity" : menge
            },
            "userdata": {
                "username" : self.username,
                "password" : password
            }
        }

        response = requests.post(f"{BASE}/{password}/buy", json=payload)

        if response.status_code == 200:
            self.ui.labelBuyInfo.setText("Kauf erfolgreich!")
            self.load_account()
            self.load_inventory()
            self.load_market()

            self.ui.lineEditBuyPassword.clear()
            self.ui.lineEditBuyUsername.clear()
        else:
            self.ui.labelBuyInfo.setText(response.json().get("detail", "Kauf fehlgeschlagen"))
        


    def sell(self):
        zeile = self.ui.tableWidgetInventory.currentRow()
        if zeile == -1:
            self.ui.labelSellInfo.setText("Bitte Gut auswählen.")
            return
        
        password = self.ui.lineEditSellPassword.text()
        menge = self.ui.spinBoxSell.value()

        good_name = self.ui.tableWidgetInventory.item(zeile, 3).text()
        good_id = int(self.ui.tableWidgetInventory.item(zeile, 3).text())

        payload = {
            "data": {
                "goodname": good_name,
                "goodid" : good_id,
                "quantity" : menge
            },
            "userdata": {
                "username" : self.username,
                "password" : password
            }
        }

        response = requests.post(f"{BASE}/{password}/sell", json=payload)

        if response.status_code != 200:
            self.ui.labelSellInfo.setText(response.json().get("detail", "Verkauf fehlgeschlagen."))
        else:
            self.ui.labelSellInfo.setText("Verkauf erfolgreich!")
            self.load_account()
            self.load_inventory()
            self.load_market()

            self.ui.lineEditSellPassword.clear()
            self.ui.lineEditSellUsername.clear()
        



#--------------------------------Styling und so-----------------------------------
    def setup_gui_styling(self):
        # Farbpalette
        cream = "#FAF7F3"
        beige = "#F0E4D3"
        brown = "#DCC5B2"
        peach = "#D9A299"
        dark_brown = "#4B3F39"

        # Tabellen: Markt und Inventar
        for table in [self.ui.tableGueter, self.ui.tableWidgetInventory]:
            table.setStyleSheet(f"""
                QTableWidget {{
                    background-color: {beige};
                    color: {dark_brown};  /* Textfarbe in Zellen */
                    gridline-color: {brown};
                    font-size: 12pt;
                    border: 1px solid {brown};
                }}
                QHeaderView::section {{
                    background-color: {peach};
                    color: {dark_brown};  /* Text in Kopfzeile */
                    font-weight: bold;
                    font-size: 12pt;
                    border: 1px solid {brown};
                }}
            """)
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table.verticalHeader().setDefaultSectionSize(35)

        # Coin-Labels
        for label in [self.ui.labelCoins, self.ui.labelCoins_2]:
            font = label.font()
            font.setPointSize(16)
            label.setFont(font)
            label.setStyleSheet(f"color: {dark_brown};")

        # Info-/Status-Labels
        for label in [self.ui.labelStatus, self.ui.labelBuyInfo, self.ui.labelSellInfo]:
            font = label.font()
            font.setPointSize(14)
            label.setFont(font)
            label.setStyleSheet(f"color: {dark_brown};")

        #elemten braun färben
        for element in [self.ui.labelUsername, self.ui.labelPassword, self.ui.label, self.ui.label_10, self.ui.label_11, self.ui.label_12,
                     self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5, self.ui.label_6, self.ui.label_7, self.ui.label_8,self.ui.label_9,
                     self.ui.lineEditBuyPassword, self.ui.lineEditBuyUsername, self.ui.lineEditPassword, self.ui.lineEditSellPassword, self.ui.lineEditSellUsername,
                     self.ui.lineEditUsername, self.ui.spinBoxBuy, self.ui.spinBoxSell]:
            element.setStyleSheet(f"color: {dark_brown};")



        # Buttons: Peach-Farbe
        for button in self.findChildren(QPushButton):
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {peach};
                    color: white;
                    font-size: 12pt;
                    border-radius: 6px;
                    padding: 6px 12px;
                }}
                QPushButton:hover {{
                    background-color: {brown};
                }}
            """)

        # Gesamter Hintergrund der App
        self.setStyleSheet(f"background-color: {cream};")

#---------------------------------------------------------------



#mocking
from unittest.mock import patch

mocked_goods = {
    "ID": [1, 2, 3],
    "Name": ["Kaktus", "Banane", "test"],
    "Price": [12.5, 7.2, 5.0],
    "Quantity": [10, 20, 5]
}

class MockResponse:
    def __init__(self, json_data, status_code):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        return self._json

def mock_post_func(url, json, *args, **kwargs):
    if "login" in url:
        if json["username"] == "riya" and json["password"] == "1234":
            return MockResponse({"message": "Eingeloggt!"}, 200)
        return MockResponse({"detail": "Falscher Username oder Passwort"}, 400)
    elif "register" in url:
        return MockResponse({"message": "Registriert!"}, 200)
    return MockResponse({}, 404)

def mock_get_func(url, *args, **kwargs):
    if "offers" in url:
        return MockResponse(mocked_goods, 200)
    elif "accountinfo" in url:
        return MockResponse({"balance": 123.45, "inventory": {1: 3, 2: 1}}, 200)
    return MockResponse({}, 404)

if __name__ == "__main__":
    with patch("requests.post", side_effect=mock_post_func), \
         patch("requests.get", side_effect=mock_get_func):

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())


#if __name__ == "__main__":
  #  app = QApplication(sys.argv)
   # window = MainWindow()
   # window.show()
   # sys.exit(app.exec())




