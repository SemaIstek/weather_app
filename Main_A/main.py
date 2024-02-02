import sys,os
sys.path.append(os.getcwd())
import re
import json
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_city_ import Ui_MainWindow as Ui_MainWindow_2
from Ui_country_ import Ui_MainWindow as Ui_MainWindow_3




class Main_Window(QMainWindow, Ui_MainWindow_3):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.resize(650,850)       
        self.setWindowTitle("Weather App")
        
    # Hide Combobox and Label 
        self.region_combobox.hide()
        self.city_line.hide()
        self.frame.hide()

        # Call the country
        self.country_line.textChanged.connect(self.show_region_combobox)
        text=self.country_line.text()
        #QPushButton  clicked open 
        self.search_button.clicked.connect(self.show_region_combobox)

        # Bölge seçildiğinde çağrılacak fonksiyonu bağla
        self.region_combobox.currentIndexChanged.connect(self.show_city_label)  
        
    def show_region_combobox(self, text):
        
        if text:  # Eğer text boş değilse
            self.region_combobox.show()
        else:
            self.region_combobox.hide()

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

