# the main file for the program
import requests
import ccxt
from pprint import pprint as pp

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QAbstractItemView, QHeaderView, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFrame, QMainWindow)

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        self.market = ccxt.bittrex()
        self.price = self.get_prices()

        self.get_coins()

        super(WidgetGallery, self).__init__(parent)

        self.createTopLeftWidget()
        self.createBottomLeftWidget()
        self.createTopRightWidget()
        self.createMidRightWidget()
        self.createBottomRightWidget()

        mainLayout = QGridLayout()

        mainLayout.addWidget(self.asset_list, 0, 0, 8, 1)
        mainLayout.addWidget(self.bottomLeftWidget, 8, 0, 2, 1)

        mainLayout.addLayout(self.search_box, 0, 1, 1, 1)
        mainLayout.addWidget(self.crypto_list, 1, 1, 7, 1)
        mainLayout.addWidget(self.bottomRightWidget, 8, 1, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("blockview")
        # self.setBaseSize(1200, 1200)
        self.setFixedSize(1200, 1200)
        self.changeStyle()



    def changeStyle(self):
        # set style of the application. Fusion or vista are options.
        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def createTopLeftWidget(self):
        self.asset_list = QTableWidget(0, 4)
        self.asset_list.hideColumn(4)
        self.asset_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.asset_list.verticalHeader().setVisible(False)
        self.asset_list_labels = ['Asset', 'Price', 'Position', 'Value']
        self.asset_header = self.asset_list.horizontalHeader()
        try:
            self.asset_header.setSectionResizeMode(QHeaderView.Stretch)

        except:
            self.asset_header.setResizeMode(QHeaderView.Stretch)
        self.asset_list.setHorizontalHeaderLabels(self.asset_list_labels)

    def createTopRightWidget(self):
        self.search_box = QHBoxLayout()

        self.crypto_search = QLineEdit()
        self.search_button = QPushButton('Search')

        self.search_box.addWidget(self.crypto_search)
        self.search_box.addWidget(self.search_button)

    def createMidRightWidget(self):
        self.crypto_list = QTableWidget(0, 4)
        self.crypto_list.hideColumn(3)
        self.crypto_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.crypto_list.verticalHeader().setVisible(False)
        self.crypto_list.horizontalHeader().setVisible(False)

        for coin in self.coin_list:
            self.crypto_list.insertRow(1)

    def createBottomRightWidget(self):
        self.bottomRightWidget = QGroupBox()

    def createBottomLeftWidget(self):
        self.bottomLeftWidget = QGroupBox()


    def get_prices(self):
        price = self.market.fetch_ticker(symbol='BTC/USDT').get('bid')

        return price

    def get_coins(self):
        self.coin_list = []

        for coin in self.market.currencies:
            current_coin = self.market.currencies[coin].get('info').get('name')
            self.coin_list.append(current_coin)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    gallery = WidgetGallery()

    gallery.show()

    # frm = QFrame()
    # win = QMainWindow()
    # win.setCentralWidget(frm)
    # win.resize(w, h)
    # win.show()

    sys.exit(app.exec())