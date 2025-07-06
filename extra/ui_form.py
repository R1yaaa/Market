# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1183, 600)
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 1171, 531))
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        self.pushButtonLogin = QPushButton(self.pageLogin)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setGeometry(QRect(470, 320, 131, 41))
        self.pushButtonRegister = QPushButton(self.pageLogin)
        self.pushButtonRegister.setObjectName(u"pushButtonRegister")
        self.pushButtonRegister.setGeometry(QRect(619, 320, 121, 41))
        self.lineEditUsername = QLineEdit(self.pageLogin)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setGeometry(QRect(530, 180, 201, 28))
        self.lineEditPassword = QLineEdit(self.pageLogin)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(530, 230, 201, 28))
        self.labelUsername = QLabel(self.pageLogin)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setGeometry(QRect(420, 180, 101, 31))
        self.labelPassword = QLabel(self.pageLogin)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(420, 230, 101, 31))
        self.labelStatus = QLabel(self.pageLogin)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(430, 390, 341, 31))
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageMarket = QWidget()
        self.pageMarket.setObjectName(u"pageMarket")
        self.tableGueter = QTableWidget(self.pageMarket)
        if (self.tableGueter.columnCount() < 6):
            self.tableGueter.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableGueter.setObjectName(u"tableGueter")
        self.tableGueter.setGeometry(QRect(10, 60, 981, 471))
        self.tableGueter.setColumnCount(6)
        self.tableGueter.verticalHeader().setProperty("showSortIndicator", False)
        self.tableGueter.verticalHeader().setStretchLastSection(False)
        self.pushButtonLogout = QPushButton(self.pageMarket)
        self.pushButtonLogout.setObjectName(u"pushButtonLogout")
        self.pushButtonLogout.setGeometry(QRect(1050, 10, 111, 41))
        self.pushButtonInventory = QPushButton(self.pageMarket)
        self.pushButtonInventory.setObjectName(u"pushButtonInventory")
        self.pushButtonInventory.setGeometry(QRect(930, 10, 111, 41))
        self.labelCoins = QLabel(self.pageMarket)
        self.labelCoins.setObjectName(u"labelCoins")
        self.labelCoins.setGeometry(QRect(820, 15, 81, 31))
        self.label_4 = QLabel(self.pageMarket)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(760, 20, 61, 21))
        self.label_5 = QLabel(self.pageMarket)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 131, 21))
        self.label_5.setMaximumSize(QSize(131, 21))
        self.stackedWidget.addWidget(self.pageMarket)
        self.pageInventar = QWidget()
        self.pageInventar.setObjectName(u"pageInventar")
        self.tableWidgetInventory = QTableWidget(self.pageInventar)
        if (self.tableWidgetInventory.columnCount() < 4):
            self.tableWidgetInventory.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tableWidgetInventory.setObjectName(u"tableWidgetInventory")
        self.tableWidgetInventory.setGeometry(QRect(10, 70, 581, 451))
        self.label_6 = QLabel(self.pageInventar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 161, 31))
        self.label_6.setMaximumSize(QSize(161, 31))
        self.pushButtonZurueck = QPushButton(self.pageInventar)
        self.pushButtonZurueck.setObjectName(u"pushButtonZurueck")
        self.pushButtonZurueck.setGeometry(QRect(1060, 10, 101, 41))
        self.pushButtonSell = QPushButton(self.pageInventar)
        self.pushButtonSell.setObjectName(u"pushButtonSell")
        self.pushButtonSell.setGeometry(QRect(940, 10, 101, 41))
        self.labelCoins_2 = QLabel(self.pageInventar)
        self.labelCoins_2.setObjectName(u"labelCoins_2")
        self.labelCoins_2.setGeometry(QRect(410, 10, 61, 21))
        self.label_7 = QLabel(self.pageInventar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 10, 51, 21))
        self.tableWidget = QTableWidget(self.pageInventar)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(600, 70, 551, 451))
        self.label_8 = QLabel(self.pageInventar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(600, 10, 191, 31))
        self.stackedWidget.addWidget(self.pageInventar)
        self.pageVerkaufen = QWidget()
        self.pageVerkaufen.setObjectName(u"pageVerkaufen")
        self.lineEditGoodName = QLineEdit(self.pageVerkaufen)
        self.lineEditGoodName.setObjectName(u"lineEditGoodName")
        self.lineEditGoodName.setGeometry(QRect(500, 110, 211, 31))
        self.lineEditVerkaufPreis = QLineEdit(self.pageVerkaufen)
        self.lineEditVerkaufPreis.setObjectName(u"lineEditVerkaufPreis")
        self.lineEditVerkaufPreis.setGeometry(QRect(500, 180, 211, 31))
        self.spinBoxAnzahl = QSpinBox(self.pageVerkaufen)
        self.spinBoxAnzahl.setObjectName(u"spinBoxAnzahl")
        self.spinBoxAnzahl.setGeometry(QRect(500, 250, 61, 26))
        self.label = QLabel(self.pageVerkaufen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 120, 101, 16))
        self.label_2 = QLabel(self.pageVerkaufen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 190, 101, 16))
        self.label_3 = QLabel(self.pageVerkaufen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 250, 58, 16))
        self.pushButtonAngebot = QPushButton(self.pageVerkaufen)
        self.pushButtonAngebot.setObjectName(u"pushButtonAngebot")
        self.pushButtonAngebot.setGeometry(QRect(490, 330, 171, 41))
        self.label_10 = QLabel(self.pageVerkaufen)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(390, 420, 371, 31))
        self.stackedWidget.addWidget(self.pageVerkaufen)
        self.lschen = QWidget()
        self.lschen.setObjectName(u"lschen")
        self.stackedWidget.addWidget(self.lschen)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("Widget", u"Log in", None))
        self.pushButtonRegister.setText(QCoreApplication.translate("Widget", u"Register", None))
        self.labelUsername.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">Username:</span></p></body></html>", None))
        self.labelPassword.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">Password:</span></p></body></html>", None))
        self.labelStatus.setText("")
        ___qtablewidgetitem = self.tableGueter.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem1 = self.tableGueter.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Preis", None));
        ___qtablewidgetitem2 = self.tableGueter.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Anzahl", None));
        ___qtablewidgetitem3 = self.tableGueter.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Verk\u00e4ufer", None));
        ___qtablewidgetitem4 = self.tableGueter.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Anzahl zu kaufen", None));
        ___qtablewidgetitem5 = self.tableGueter.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"Kaufen", None));
        self.pushButtonLogout.setText(QCoreApplication.translate("Widget", u"Log out", None))
        self.pushButtonInventory.setText(QCoreApplication.translate("Widget", u"Inventar", None))
        self.labelCoins.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">100 zb idk</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coins:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:16pt;\">Markt</span></p></body></html>", None))
        ___qtablewidgetitem6 = self.tableWidgetInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem7 = self.tableWidgetInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"Preis", None));
        ___qtablewidgetitem8 = self.tableWidgetInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"Anzahl", None));
        ___qtablewidgetitem9 = self.tableWidgetInventory.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget", u"verkaufen", None));
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:16pt;\">Inventar</span></p></body></html>", None))
        self.pushButtonZurueck.setText(QCoreApplication.translate("Widget", u"zur\u00fcck", None))
        self.pushButtonSell.setText(QCoreApplication.translate("Widget", u"verkaufen", None))
        self.labelCoins_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">zb 100</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">coins:</span></p></body></html>", None))
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget", u"Preis", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Widget", u"Anzahl", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Widget", u"Runternehmen", None));
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt;\">Meine Angebote</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Name des Guts:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Preis pro St\u00fcck:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Anzahl:", None))
        self.pushButtonAngebot.setText(QCoreApplication.translate("Widget", u"Angebot erstellen", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
    # retranslateUi

