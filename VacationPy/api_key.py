#import library

import config
import pandas as pd
from sodapy import Socrata

client = Socrata("VacationPy_WeatherPy",
                 config.api_key,                 
                 # OpenWeatherMap API Key
                    weather_api_key = "8f5e9846fd0aac243658733b5f61183e"

                 # Google API Key
                    g_key = "AIzaSyD6mXtyyzXGXUmCb9NgGYszQE7Pgr5VnqE"
