import requests
from bs4 import BeautifulSoup
import datetime

class Cralwer:

    def __init__(self):
        self.dolar_data = None
        self.euro_data = None

    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def extract_from_dolar_hoje(self):
        raw_dolar = self.request_data('https://dolarhoje.com/')
        # Find Currency and price element
        currency_element = raw_dolar.find('span', {'class': 'cotMoeda nacional'})
        if currency_element:
            input_element = currency_element.find('input', {'id': 'nacional'})
            if input_element:
                value = input_element.get('value')
                self.dolar_data = {
                    'currency': 'Dólar Americano',
                    'value': value,
                    'time_of_extract': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                print("Input element not found.")
        else:
            print("Currency element not found.")
        print(self.dolar_data)

    def extract_from_euro_hoje(self):
        raw_euro = self.request_data('https://dolarhoje.com/euro-hoje/')
        # Find Currency and price element
        currency_element = raw_euro.find('span', {'class': 'cotMoeda nacional'})
        if currency_element:
            input_element = currency_element.find('input', {'id': 'nacional'})
            if input_element:
                value = input_element.get('value')
                self.euro_data = {
                    'currency': 'Euro',
                    'value': value,
                    'time_of_extract': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                print("Input element not found.")
        else:
            print("Currency element not found.")
        print(self.euro_data)
        
if __name__ == "__main__":
    crawler = Cralwer()
    crawler.extract_from_dolar_hoje()
    crawler.extract_from_euro_hoje()