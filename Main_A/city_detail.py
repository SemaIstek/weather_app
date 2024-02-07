from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox,QVBoxLayout, QWidget, QLineEdit, QCompleter
from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QStyleOptionViewItem,QLabel
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup
import pymongo
import datetime
from Ui_city_ import *
import sys, os
import json


class City_Main_Window(QMainWindow, Ui_MainWindow):
    main = pyqtSignal(bool)
    def __init__(self):
        super(City_Main_Window, self).__init__()
        self.ui = uic.loadUi('./Main_A/city_.ui', self)
        #self.setupUi(self)
        self.resize(700,900)       
        self.setWindowTitle("Weather App")
        self.load_json_data()

        self.returnButton.clicked.connect(self.mainPage)
        self.returnButton.clicked.connect(self.close)
        
    def mainPage(self):
        self.close()
        self.main.emit(True)

        
    def load_json_data(self):
        # Path to the JSON file
        file_path = os.path.join(os.getcwd(), "./weather.json")

        try:
            with open(file_path, 'r', encoding="utf-8") as json_file:
                weather_data = json.load(json_file)
                # Display relevant information in the UI
                self.display_information(weather_data)
        except FileNotFoundError:
            print("No weather data found.")

        # Extract and display relevant information (name, population, temperature, etc.)
        #self.display_information(data)

    def display_information(self, weather_data):
        if "name" in weather_data:
            city_name = weather_data["name"]
            self.city_label.setText(f"{city_name}")

        if "current" in weather_data and "date" in weather_data["current"]:
            date = weather_data["current"]["date"]
            self.date_label.setText(f"{date}")

        if "current" in weather_data and "temp" in weather_data["current"]:
            temperature = round(weather_data["current"]["temp"])
            self.temp_label.setText(f"{temperature} °C")
        
        if "current" in weather_data and "icon" in weather_data["current"]:
            icon_url = weather_data["current"]["icon"]
            self.update_icon_label(icon_url)
            
        if "next_5" in weather_data:
                next_5_data = weather_data["next_5"]

                # Günlerin listesini al
                days = [data["date"] for data in next_5_data]

                # TableWidget'i temizle
                self.tableWidget_days.clearContents()
                self.tableWidget_days.setRowCount(len(days))
                self.tableWidget_days.setColumnCount(5)  # date, condition, temp, wind, icon

                # Sütun başlıklarını ayarla
                self.tableWidget_days.setHorizontalHeaderLabels(["Date", "Condition", "Temp (°C)", "Wind", "Icon"])

                # Tabloya verileri ekle
                for row, day_data in enumerate(next_5_data):
                    self.tableWidget_days.setItem(row, 0, QTableWidgetItem(str(day_data.get("date", ""))))
                    self.tableWidget_days.setItem(row, 1, QTableWidgetItem(str(day_data.get("condition", ""))))
                    self.tableWidget_days.setItem(row, 2, QTableWidgetItem(str(day_data.get("temp", ""))))
                    self.tableWidget_days.setItem(row, 3, QTableWidgetItem(str(day_data.get("wind", ""))))

                    # İconları eklemek için QLabel oluştur
                    icon_label = QLabel()
                    icon_pixmap = self.load_pixmap_from_url(day_data.get("icon", ""))
                    if icon_pixmap is not None:
                        icon_label.setPixmap(icon_pixmap)
                    self.tableWidget_days.setCellWidget(row, 4, icon_label)
                for col in range(self.tableWidget_days.columnCount()):
                    self.tableWidget_days.horizontalHeaderItem(col).setTextAlignment(Qt.AlignCenter)


        self.display_3_hour_forecast(weather_data)
    def display_3_hour_forecast(self, weather_data):
    # Her bir infoLabel için display_3_hour_forecast_for_label fonksiyonunu çağır
        for label_index in range(1, 5):
            label_name = f"infoLabel_{label_index}"
            img = f"img_label_{label_index+1}"
            
            if hasattr(self, label_name) and hasattr(self, img):
                info_label = getattr(self, label_name)
                img_label = getattr(self, img)
                if info_label:
                    info_label.setAlignment(Qt.AlignCenter)
                # self.display_3_hour_forecast_for_label(weather_data, info_label)
                label_content = ""
                time = weather_data.get("detail", {}).get("first_15h", [])[label_index]["hour"]
                icon_url = weather_data.get("detail", {}).get("first_15h", [])[label_index]["icon"]
                temp = f"{weather_data.get('detail', {}).get('first_15h', [])[label_index]['temp']} °C"

                # Label içeriğine ekle
                #icon_img = self.load_pixmap_from_url(icon_url)
                img_label.setPixmap(self.load_pixmap_from_url(icon_url))
                #label_content += f"<img src='{icon_img.scaledToWidth(15)}'/><br>"  # Fix the image width 15 pixel
                label_content = f"<b>{time}</b><br>{temp}<br><br>"

                # QLabel'a içeriği set et
                info_label.setText(label_content)

    def update_icon_label(self, icon_url):
        pixmap = self.load_pixmap_from_url(icon_url)
        if pixmap is not None:
            self.img_label.setPixmap(pixmap)

    def load_pixmap_from_url(self, url):
        pixmap = QPixmap()
        data = requests.get(url).content
        pixmap.loadFromData(data)
        return pixmap