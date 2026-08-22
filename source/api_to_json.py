
import requests
import json
import os
from dotenv import load_dotenv
import logging
load_dotenv()

logging.basicConfig(
    level=logging.INFO , 
format= '%(asctime)s - %(levelname)s -%(message)s'
)
url = os.getenv('WEATHER_API_URL')
def weather_fetch():
    try:

        response= requests.get(url)
        response.raise_for_status()
        data= response.json()
        with open ('data/weather.json' , 'w') as file:
            json.dump(data, file , indent=4)
        logging.info('data saved succesfully!')
    except requests.exceptions.RequestException as e :
        logging.error (f'failed: {e}') 

weather_fetch()