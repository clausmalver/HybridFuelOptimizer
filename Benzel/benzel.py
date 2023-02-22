# Mitsubishi Outlander 2020 PHEV
# It drives around 14.5 km per liter gasoline
# Average reach on the battery around 37 km on a full battery charge 13.8 kwh

km_per_liter = 14.5
km_per_kwh = 2.68

gas_price = float(input("What is the current gasoline price in DKK (kr/l): "))
el_price = float(input("What is the current electricity price in DKK (kr/kWh): "))

gas_price_per_km = gas_price / km_per_liter
el_price_per_km = el_price / km_per_kwh

print(f"\n{'-'*30}\nGasoline: {gas_price_per_km:.2f} kr/km")
print(f"Electricity: {el_price_per_km:.2f} kr/km\n{'-'*30}\n")

cheaper_fuel_type = "electricity" if el_price_per_km < gas_price_per_km else "gasoline"
expensive_fuel_type = "electricity" if el_price_per_km > gas_price_per_km else "gasoline"

print(f"It is cheaper to drive on {cheaper_fuel_type} than {expensive_fuel_type}. You should {'charge your electric vehicle tonight.' if cheaper_fuel_type == 'electricity' else 'fill up your gasoline vehicle.'}")
