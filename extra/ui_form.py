# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
        self.pushButtonLogin.setGeometry(QRect(340, 310, 131, 31))
        self.pushButtonRegister = QPushButton(self.pageLogin)
        self.pushButtonRegister.setObjectName(u"pushButtonRegister")
        self.pushButtonRegister.setGeometry(QRect(489, 310, 121, 31))
        self.lineEditUsername = QLineEdit(self.pageLogin)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setGeometry(QRect(400, 170, 201, 28))
        self.lineEditPassword = QLineEdit(self.pageLogin)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(400, 220, 201, 28))
        self.labelUsername = QLabel(self.pageLogin)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setGeometry(QRect(310, 170, 81, 31))
        self.labelPassword = QLabel(self.pageLogin)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(310, 220, 81, 31))
        self.labelStatus = QLabel(self.pageLogin)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(340, 380, 261, 31))
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageMarket = QWidget()
        self.pageMarket.setObjectName(u"pageMarket")
        self.tableGueter = QTableWidget(self.pageMarket)
        if (self.tableGueter.columnCount() < 4):
            self.tableGueter.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableGueter.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableGueter.setObjectName(u"tableGueter")
        self.tableGueter.setGeometry(QRect(10, 50, 681, 481))
        self.tableGueter.setColumnCount(4)
        self.tableGueter.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableGueter.verticalHeader().setStretchLastSection(False)
        self.pushButtonLogout = QPushButton(self.pageMarket)
        self.pushButtonLogout.setObjectName(u"pushButtonLogout")
        self.pushButtonLogout.setGeometry(QRect(1060, 20, 90, 28))
        self.pushButtonInventory = QPushButton(self.pageMarket)
        self.pushButtonInventory.setObjectName(u"pushButtonInventory")
        self.pushButtonInventory.setGeometry(QRect(950, 20, 90, 28))
        self.labelCoins = QLabel(self.pageMarket)
        self.labelCoins.setObjectName(u"labelCoins")
        self.labelCoins.setGeometry(QRect(860, 20, 71, 31))
        self.label_4 = QLabel(self.pageMarket)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(810, 25, 41, 21))
        self.label_5 = QLabel(self.pageMarket)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 5, 131, 21))
        self.label_5.setMaximumSize(QSize(131, 21))
        self.stackedWidget.addWidget(self.pageMarket)
        self.pageInventar = QWidget()
        self.pageInventar.setObjectName(u"pageInventar")
        self.tableWidgetInventory = QTableWidget(self.pageInventar)
        if (self.tableWidgetInventory.columnCount() < 3):
            self.tableWidgetInventory.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetInventory.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidgetInventory.setObjectName(u"tableWidgetInventory")
        self.tableWidgetInventory.setGeometry(QRect(10, 50, 681, 471))
        self.label_6 = QLabel(self.pageInventar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 161, 31))
        self.label_6.setMaximumSize(QSize(161, 31))
        self.pushButtonZurueck = QPushButton(self.pageInventar)
        self.pushButtonZurueck.setObjectName(u"pushButtonZurueck")
        self.pushButtonZurueck.setGeometry(QRect(1070, 20, 90, 28))
        self.pushButtonSell = QPushButton(self.pageInventar)
        self.pushButtonSell.setObjectName(u"pushButtonSell")
        self.pushButtonSell.setGeometry(QRect(970, 20, 90, 28))
        self.labelCoins_2 = QLabel(self.pageInventar)
        self.labelCoins_2.setObjectName(u"labelCoins_2")
        self.labelCoins_2.setGeometry(QRect(890, 30, 58, 16))
        self.label_7 = QLabel(self.pageInventar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(820, 30, 58, 16))
        self.stackedWidget.addWidget(self.pageInventar)
        self.pageVerkaufen = QWidget()
        self.pageVerkaufen.setObjectName(u"pageVerkaufen")
        self.lineEditGoodName = QLineEdit(self.pageVerkaufen)
        self.lineEditGoodName.setObjectName(u"lineEditGoodName")
        self.lineEditGoodName.setGeometry(QRect(310, 110, 211, 31))
        self.lineEditVerkaufPreis = QLineEdit(self.pageVerkaufen)
        self.lineEditVerkaufPreis.setObjectName(u"lineEditVerkaufPreis")
        self.lineEditVerkaufPreis.setGeometry(QRect(310, 180, 211, 31))
        self.spinBoxAnzahl = QSpinBox(self.pageVerkaufen)
        self.spinBoxAnzahl.setObjectName(u"spinBoxAnzahl")
        self.spinBoxAnzahl.setGeometry(QRect(310, 250, 61, 26))
        self.label = QLabel(self.pageVerkaufen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 120, 101, 16))
        self.label_2 = QLabel(self.pageVerkaufen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 190, 101, 16))
        self.label_3 = QLabel(self.pageVerkaufen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 250, 58, 16))
        self.pushButtonAngebot = QPushButton(self.pageVerkaufen)
        self.pushButtonAngebot.setObjectName(u"pushButtonAngebot")
        self.pushButtonAngebot.setGeometry(QRect(300, 330, 171, 41))
        self.stackedWidget.addWidget(self.pageVerkaufen)
        self.lschen = QWidget()
        self.lschen.setObjectName(u"lschen")
        self.stackedWidget.addWidget(self.lschen)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("Widget", u"Log in", None))
        self.pushButtonRegister.setText(QCoreApplication.translate("Widget", u"Register", None))
        self.labelUsername.setText(QCoreApplication.translate("Widget", u"Username:", None))
        self.labelPassword.setText(QCoreApplication.translate("Widget", u"Password:", None))
        self.labelStatus.setText("")
        ___qtablewidgetitem = self.tableGueter.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem1 = self.tableGueter.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Preis", None));
        ___qtablewidgetitem2 = self.tableGueter.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Verk\u00e4ufer", None));
        ___qtablewidgetitem3 = self.tableGueter.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Kaufen", None));
        self.pushButtonLogout.setText(QCoreApplication.translate("Widget", u"Log out", None))
        self.pushButtonInventory.setText(QCoreApplication.translate("Widget", u"Inventory", None))
        self.labelCoins.setText(QCoreApplication.translate("Widget", u"100 zb idk", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Coins:", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Markt", None))
        ___qtablewidgetitem4 = self.tableWidgetInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem5 = self.tableWidgetInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"Preis", None));
        ___qtablewidgetitem6 = self.tableWidgetInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"verkaufen", None));
        self.label_6.setText(QCoreApplication.translate("Widget", u"Inventar", None))
        self.pushButtonZurueck.setText(QCoreApplication.translate("Widget", u"zur\u00fcck", None))
        self.pushButtonSell.setText(QCoreApplication.translate("Widget", u"verkaufen", None))
        self.labelCoins_2.setText(QCoreApplication.translate("Widget", u"zb 100", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"coins:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Name des Guts:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Preis pro St\u00fcck:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Anzahl:", None))
        self.pushButtonAngebot.setText(QCoreApplication.translate("Widget", u"Angebot erstellen", None))
    # retranslateUi

