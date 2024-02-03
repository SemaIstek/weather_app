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
import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("mongodb+srv://serkanbakisgan:1HDz6rhbbN4bjMQF@cluster0.8v7bpzg.mongodb.net/")
db = client["weather_app"]
collection = db["weather"]

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
    
    def load_loaction_infos():

        base_site_usa="https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
        base_site_netherland="https://en.wikipedia.org/wiki/Municipalities_of_the_Netherlands"
        base_site_belgium="https://en.wikipedia.org/wiki/List_of_most_populous_municipalities_in_Belgium"
        collection.delete_many({})
    # USA
        response = requests.get(base_site_usa)
        html = response.content
        soup = BeautifulSoup(html,"lxml")
        table = soup.find("table", class_="sortable wikitable sticky-header static-row-numbers col1left col2center")
        rows = table.find_all("tr")

        # Initialize lists to store the data
        cities = []
        states = []
        populations = []
    

        # Iterate through the rows starting from the second row (to skip the header row)
        for row in rows[1:]:
            # Extract the columns
            columns = row.find_all("td")
            
            # Check if there are enough columns (at least 3) to extract city, state, and population
            if len(columns) >= 3:
                # Extract city, state, and population
                city = columns[0].text.strip()
                state = columns[1].text.strip()
                population = columns[2].text.strip()
                
                # Append the data to the respective lists
                cities.append(city)
                states.append(state)
                populations.append(population)

        data_to_insert = [{"Country": "USA", "City": city, "State": state, "Population": population} for city, state, population in zip(cities, states, populations)]

        # Insert the data into MongoDB collection
        collection.insert_many(data_to_insert)

        print("USA Data has been inserted into MongoDB.")

    # Netherland
        response = requests.get(base_site_netherland)
        html = response.content
        soup = BeautifulSoup(html,"lxml")
        table = soup.find("table", class_="wikitable plainrowheaders sortable")
        rows = table.find_all("tr")

        # Initialize lists to store the data
        cities = []
        states = []
        populations = []
    

        # Iterate through the rows starting from the second row (to skip the header row)
        for row in rows[1:]:
            # Extract the columns
            columns = row.find_all("td")
            
            # Check if there are enough columns (at least 3) to extract city, state, and population
            if len(columns) >= 3:
                # Extract city, state, and population
                city = columns[1].text.strip()
                state = columns[3].text.strip()
                population = columns[4].text.strip()
                
                # Append the data to the respective lists
                cities.append(city)
                states.append(state)
                populations.append(population)

        data_to_insert = [{"Country": "Netherland", "City": city, "State": state, "Population": population} for city, state, population in zip(cities, states, populations)]

        # Insert the data into MongoDB collection
        collection.insert_many(data_to_insert)

        print("Netherland Data has been inserted into MongoDB.")

    # Belgium
        response = requests.get(base_site_belgium)
        html = response.content
        soup = BeautifulSoup(html,"lxml")
        table = soup.find("table", class_="wikitable sortable")
        rows = table.find_all("tr")

        # Initialize lists to store the data
        cities = []
        states = []
        populations = []
    

        # Iterate through the rows starting from the second row (to skip the header row)
        for row in rows[1:]:
            # Extract the columns
            columns = row.find_all("td")
            
            # Check if there are enough columns (at least 3) to extract city, state, and population
            if len(columns) >= 3:
                # Extract city, state, and population
                city = columns[1].text.strip()
                state = columns[8].text.strip()
                population = columns[6].text.strip()
                
                # Append the data to the respective lists
                cities.append(city)
                states.append(state)
                populations.append(population)

        data_to_insert = [{"Country": "Belgium", "City": city, "State": state, "Population": population} for city, state, population in zip(cities, states, populations)]

        # Insert the data into MongoDB collection
        collection.insert_many(data_to_insert)

        print("Belgium Data has been inserted into MongoDB.")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())

