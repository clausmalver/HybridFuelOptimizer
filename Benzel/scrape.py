import requests
from bs4 import BeautifulSoup

url = 'https://www.q8.dk/priser/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

fuels = soup.find_all('div', class_='crate prices')

for fuel in fuels:
    fuel_type = fuel.find('span', class_='display-name').text.strip()
    price = fuel.find('div', class_='price').text.strip()
    price = price.replace(' kr./l', '').replace(' ', '')
    print(f'{fuel_type}: {price}')
