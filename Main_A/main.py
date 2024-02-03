import sys,os
sys.path.append(os.getcwd())
import re
import json
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Ui_city_ import Ui_MainWindow as Ui_MainWindow_2
from Ui_country_ import Ui_MainWindow as Ui_MainWindow_3



class Main_Window(QMainWindow, Ui_MainWindow_3):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.resize(650,850)       
        self.setWindowTitle("Weather App")
     
        self.region_combobox.hide()
        self.city_line.hide()
        
        
        #self.country_line.textChanged.connect(self.show_region_combobox)
        
        #QPushButton clicked open 
        self.search_button.clicked.connect(self.show_region_combobox)

        # Bölge seçildiğinde çağrılacak fonksiyonu bağla
        self.region_combobox.currentIndexChanged.connect(self.show_city_label)  
        
    def show_region_combobox(self):
        country = self.country_line.text()
        if country=='Netherlands':
            self.netherlands_regions(country)

    def netherlands_regions(self, country):
        regions = [
            "Drenthe",
            "Flevoland",
            "Friesland",
            "Gelderland",
            "Groningen",
            "Limburg",
            "Noord-Brabant",
            "Noord-Holland",
            "Overijssel",
            "Utrecht",
            "Zuid-Holland",
            "Zeeland"
        ]

        model = QStandardItemModel()
        
        for region in regions:
            item = QStandardItem(region)
            model.appendRow(item)
        self.region_combobox.setModel(model)
        self.region_combobox.show()
        

    def show_city_label(self, index):
        if index > 0:
            self.city_line.show()
        else:
            self.city_line.hide()  
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())

