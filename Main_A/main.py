import sys,os
sys.path.append(os.getcwd())
import re
import json
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox,QVBoxLayout, QWidget, QLineEdit, QCompleter
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Ui_city_ import Ui_MainWindow as Ui_MainWindow_2
from Ui_country_ import Ui_MainWindow as Ui_MainWindow_3
import requests
from bs4 import BeautifulSoup
import pymongo
import datetime


# client = pymongo.MongoClient("mongodb+srv://serkanbakisgan:1HDz6rhbbN4bjMQF@cluster0.8v7bpzg.mongodb.net/")
# db = client["weather_app"]
# collection = db["weather"]
# client = pymongo.MongoClient("mongodb+srv://kdurukanmert:6gZk8x0IdL0vtZra@cluster0.mpnw7uc.mongodb.net/")
class Main_Window(QMainWindow, Ui_MainWindow_3):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.resize(650,850)       
        self.setWindowTitle("Weather App")
        client = pymongo.MongoClient("mongodb+srv://serkanbakisgan:1HDz6rhbbN4bjMQF@cluster0.8v7bpzg.mongodb.net/")
        db = client["weather_app"]
        collection = db["weather"]
        collection2 = db["weather_condition"]
        self.collection = collection
        self.collection2 = collection2
     
        self.region_combobox.hide()
        self.city_line.hide()
        self.country_line.setPlaceholderText("Type country name")
        self.completer = QCompleter(self.get_country_names())
        self.completer_city = QCompleter(self.fetch_distinct_cities())
        self.city_line.setCompleter(self.completer_city)
        self.country_line.setCompleter(self.completer)
        self.country_line.textChanged.connect(self.show_country_data)
        self.city_line.textChanged.connect(self.show_city_data)
        self.region_combobox.currentIndexChanged.connect(self.show_city_line)
        self.city_line.textChanged.connect(self.weather_update_city)
        
        # self.load_loaction_infos()
        
        
        #self.country_line.textChanged.connect(self.show_region_combobox)
        
        #QPushButton clicked open 
        # self.search_button.clicked.connect(self.show_region_combobox)

        # Bölge seçildiğinde çağrılacak fonksiyonu bağla
          
        

        
        # for region in regions:
        #     item = QStandardItem(region)
        #     model.appendRow(item)
        # self.region_combobox.setModel(model)
        
        

    def show_city_label(self, index):
        if index >= 0:
            self.city_line.show()
        else:
            self.city_line.hide()  
    
    def load_loaction_infos(self):

        base_site_usa="https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
        base_site_netherland="https://en.wikipedia.org/wiki/Municipalities_of_the_Netherlands"
        base_site_belgium="https://en.wikipedia.org/wiki/List_of_most_populous_municipalities_in_Belgium"
        self.collection.delete_many({})
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

        data_to_insert = [{"Country": "United States Of America", "City": city, "State": state, "Population": population} for city, state, population in zip(cities, states, populations)]

        # Insert the data into MongoDB collection
        self.collection.insert_many(data_to_insert)

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
        self.collection.insert_many(data_to_insert)

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
        self.collection.insert_many(data_to_insert)

        print("Belgium Data has been inserted into MongoDB.")
    
    def get_country_names(self):
        # Query MongoDB to get a list of country names
        country_names = self.collection.distinct("Country")
        return country_names
    
    def show_country_data(self):
        typed_text = self.country_line.text().title()  # Capitalize the first letter of each word
        self.country_line.setText(typed_text)
        self.region_combobox.setCurrentIndex(-1)


        model = QStandardItemModel()
        if not typed_text:
            self.completer.setModel(model)
            return  # No need to query if the text is empty

        # Create a regex pattern for case-insensitive matching
        regex_pattern = f"^{re.escape(typed_text)}"  # Start with the typed text
        query = {"Country": {"$regex": regex_pattern, "$options": "i"}}  # Case-insensitive regex search
  

        matching_countries = self.collection.distinct("Country", query)

        for country in matching_countries:
            item = QStandardItem(country)
            model.appendRow(item)

        # Set the completer's filtered list to matching country names
        self.completer.setModel(model)

        try:

            if country==self.country_line.text():
                self.populate_states()
                self.region_combobox.show()
                self.city_line.hide()
        except:
            pass
        
        self.city_line.setText("")

        
    
    def populate_states(self):
        selected_country = self.country_line.text()
        self.region_combobox.clear()
        query = {"Country":selected_country}

        if selected_country:
            matching_states = self.fetch_distinct_states(selected_country)
            self.region_combobox.addItems(matching_states)

    def fetch_distinct_states(self, selected_country):
        # Query MongoDB to fetch distinct states (regions) based on the selected country
        query = {"Country": selected_country}
        matching_states = self.collection.distinct("State", query)
        return matching_states
    
    def fetch_distinct_cities(self):
        # Query MongoDB to fetch distinct states (regions) based on the selected country
        selected_country = self.country_line.text()
        selected_state = self.region_combobox.currentText()
        query = {"Country": selected_country, "State": selected_state}
        matching_cities = self.collection.distinct("City", query)
        return matching_cities
    
    def show_city_data(self):
        typed_text = self.city_line.text().title()  # Capitalize the first letter of each word
        self.city_line.setText(typed_text)

        model = QStandardItemModel()
        if not typed_text:
            self.completer.setModel(model)
            return  # No need to query if the text is empty
        selected_country = self.country_line.text()
        selected_state = self.region_combobox.currentText()

        # Create a regex pattern for case-insensitive matching
        regex_pattern = f"^{re.escape(typed_text)}"  # Start with the typed text
        query = {"Country": selected_country, "State": selected_state, "City": {"$regex": regex_pattern, "$options": "i"}}  # Case-insensitive regex search
  

        matching_cities = self.collection.distinct("City", query)

        for city in matching_cities:
            item = QStandardItem(city)
            model.appendRow(item)

        # Set the completer's filtered list to matching country names
        self.completer_city.setModel(model)
        self.city_line.show()

    def show_city_line(self):
        if self.region_combobox.currentIndex() >= 0:
            self.city_line.show()
            self.getWeather(self.city_line.text())

    def getWeather(self, place):
        self.collection2.delete_many({}) 
        api_key = "117f044f4a9859852256841562b5e3a5"
        units = "metric"
        lang = "en"

        url2 = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}&units={units}&lang={lang}"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units={units}&lang={lang}'

        response  = requests.get(url2)

        # print(response)
        # print(response.text)
        # print(response.json())

        weathers = response.json()

        if (weathers["cod"] != "400"):

                
            # print(len(weathers["list"]))

            result = []
            five_day = []

            hour = int(datetime.datetime.now().timetuple()[3])
            print(hour)
            if hour >= 21:
                baslangic = 0
            elif hour >= 18:
                baslangic = 1
            elif hour >= 15:
                baslangic = 2
            elif hour >= 12:
                baslangic = 3
            elif hour >= 9:
                baslangic = 4
            elif hour >= 6:
                baslangic = 5
            elif hour >= 3:
                baslangic = 6
            else:
                baslangic = 7

            for i in range(baslangic, len(weathers["list"]), 8):
                data = {
                    "condition": weathers["list"][i]["weather"][0]["description"],
                    "icon": f"https://openweathermap.org/img/wn/{weathers["list"][i]["weather"][0]["icon"]}@2x.png",
                    "temp": weathers["list"][i]["main"]["temp"],
                    "hour": weathers["list"][i]["dt_txt"][11:16],
                    "date": f"{weathers["list"][i]["dt_txt"][0:10]}",
                    "wind": weathers["list"][i]["wind"]["speed"]
                }
                five_day.append(data)

            for i in range(1, 6):
                data = {
                    "condition": weathers["list"][i]["weather"][0]["description"],
                    "icon": f"https://openweathermap.org/img/wn/{weathers["list"][i]["weather"][0]["icon"]}@2x.png",
                    "temp": weathers["list"][i]["main"]["temp"],
                    "hour": weathers["list"][i]["dt_txt"][11:16]
                }
                result.append(data)

            data = {
                "name": place,
                "province": self.region_combobox.currentText(),
                "country": f"{weathers["city"]["country"]}",
                "current": {
                    "condition_current": f"{weathers["list"][0]["weather"][0]["description"]}",
                    "icon": f"https://openweathermap.org/img/wn/{weathers["list"][0]["weather"][0]["icon"]}@2x.png",
                    "temp" : f"{weathers["list"][0]["main"]["temp"]}",
                    "date": f"{weathers["list"][0]["dt_txt"][0:10]}"
                },
                "detail": {
                    "first_15h": result
                },
                "next_5": five_day
            }

            file_path = os.path.join(os.getcwd(), "weather.json")
            with open(file_path, 'w', encoding="utf-8") as json_file:
                json.dump(data, json_file)
            file_path = os.path.join(os.getcwd(), "weathers.json")
            with open(file_path, 'w', encoding="utf-8") as json_file:
                json.dump(weathers, json_file)

            # print(data)
            self.collection2.insert_one(data)

        

    def weather_update_city(self):
        typed_text = self.city_line.text().title()
        selected_country = self.country_line.text()
        selected_state = self.region_combobox.currentText()

        regex_pattern = f"^{re.escape(typed_text)}"  # Start with the typed text
        query = {"Country": selected_country, "State": selected_state, "City": {"$regex": regex_pattern, "$options": "i"}}  # Case-insensitive regex search
  

        matching_cities = self.collection.distinct("City", query)

        if typed_text in matching_cities:
            self.getWeather(typed_text)




    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())

