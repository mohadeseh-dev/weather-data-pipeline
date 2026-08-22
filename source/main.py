
import logging
from extract import extract_weather
from load import load_weather

logging.basicConfig(
    level=logging.INFO , 
    format= '%(asctime)s - %(levelname)s -%(message)s'
)

def main():
    data = extract_weather()
    if data is None:
        logging.error("pipeline stopped because extraction failed")
        return
    load_weather(data)
if __name__ == '__main__':
        main()
