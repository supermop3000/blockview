# the main file for the program
#test
import requests

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        self.price = self.get_prices()
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        self.createTopLeftGroupBox()

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)

        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("blockview")
        self.changeStyle()

    def changeStyle(self):
        # set style of the application. Fusion or vista are options.
        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Cryptocurrencies: ")

        first_coin_name = "Bitcoin"
        first_coin_price = self.price

        labelCoin1 = QLabel(first_coin_name)
        priceCoin1 = QLabel(first_coin_price)

        layout = QVBoxLayout()
        layout.addWidget(labelCoin1)
        layout.addWidget(priceCoin1)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def get_prices(self):
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()

        price = data['bpi']['USD']['rate']

        return price

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())