import requests
import os
import logging
from dotenv import load_dotenv
load_dotenv()


BASE_URL=os.getenv('BASE_URL')

def extract_weather():
    try:

        response= requests.get(BASE_URL ,
                               params={
                                   'latitude' :35.6892 ,
                                   'longitude':51.3890 ,
                                   'current' : 'temperature_2m'
                               }, 
                               timeout= 10
                               )
        response.raise_for_status()
        
        logging.info('data extraced succesfully!')
        return response.json()
    
    except requests.exceptions.RequestException as e :
        logging.error (f'failed extracting data: {e}') 
        return None