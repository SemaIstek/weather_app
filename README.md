# Weather App

## Overview

This Weather App is a Python-based application that provides users with weather information for selected cities and states in three countries: Netherlands (NL), United States (USA), and Belgium. The application fetches data such as states, provinces, and populations from Wikipedia using the Scrapy library. The retrieved information is then stored in a MongoDB database.

For weather data, the app utilizes the OpenWeather API to provide users with current weather conditions, the forecast for the first 15 hours, and the upcoming 5-day forecast. The graphical user interface (GUI) is implemented using PyQt5, offering an intuitive and user-friendly experience for selecting cities and states and viewing weather details.

## Technologies Used

- Python
- PyQt5
- Scrapy
- MongoDB
- OpenWeather API

## Features

### Country Information Retrieval:

Data for NL, USA, and Belgium, including states, provinces, and populations, is fetched from Wikipedia using Scrapy.

### Database Storage:

The retrieved information is stored in a MongoDB database for efficient data management.

### Weather Data:

OpenWeather API is used to fetch current weather conditions, the first 15 hours' forecast, and the next 5-day forecast.

### Graphical User Interface:

PyQt5 is employed to create a GUI that allows users to select cities and states and view detailed weather information.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/SemaIstek/weather_app.git
    cd weather_app
    cd Main_A
    ```

2. **Run the Application:**

    ```bash
    python main.py
    ```

## Usage

1. **Launch the App:**

   Run the application using the provided command.

2. **Select Country, City, and State:**

   Use the GUI to choose the desired country, city, and state.

3. **View Weather Data:**

   The app will display current weather conditions, the first 15 hours' forecast, and the next 5-day forecast for the selected location.

4. **Explore and Customize:**

   Explore different cities and states to get comprehensive weather information.

## Contributors

- [Sema Istek]
- [Kemal Mert]
- [Serkan Bakisgan]
- [Melike Bilgin Can]

## Acknowledgments

- Special thanks to OpenWeather for providing the weather API.
- Thanks to Scrapy for simplifying web scraping tasks.
- PyQt5 made it easy to develop a feature-rich graphical interface.
