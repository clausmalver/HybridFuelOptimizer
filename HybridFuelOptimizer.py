import requests
from bs4 import BeautifulSoup

url = 'https://www.q8.dk/priser/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

fuels = soup.find_all('div', class_='crate prices')

for fuel in fuels:
    fuel_type = fuel.find('span', class_='display-name').text.strip()
    gas_price = fuel.find('div', class_='price').text.strip()
    # Remove the text scrape, random spaces and replace ',' with '.'
    gas_price = gas_price.replace(' kr./l', '').replace(' ', '').replace(',','.')
    print("The current gasoline price per liter for the fuel type " + f'{fuel_type}'+ " is " f'{gas_price}')

# Mitsubishi Outlander 2020 PHEV
# It drives around 14.5 km per liter gasoline
# Average reach on the battery around 37 km on a full battery charge 13.8 kwh

km_per_liter = 14.5
km_per_kwh = 2.68

# Change the gas_price variable string to float, to make calculations happen.
gas_price = float(gas_price)
el_price = float(input("What is the current electricity price in DKK (kr/kWh): "))

gas_price_per_km = gas_price / km_per_liter
el_price_per_km = el_price / km_per_kwh

print(f"\n{'-'*30}\nGasoline: {gas_price_per_km:.2f} kr/km")
print(f"Electricity: {el_price_per_km:.2f} kr/km\n{'-'*30}\n")

cheaper_fuel_type = "electricity" if el_price_per_km < gas_price_per_km else "gasoline"
expensive_fuel_type = "electricity" if el_price_per_km > gas_price_per_km else "gasoline"

print(f"It is cheaper to drive on {cheaper_fuel_type} than {expensive_fuel_type}. You should {'charge your electric vehicle tonight.' if cheaper_fuel_type == 'electricity' else 'fill up your gasoline vehicle.'}")
