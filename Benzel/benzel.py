KMperLiter = 13.5
KMperkWh = 2.68

gasPrice = float(input("Gasoline price in DKK (kr/L): "))
elPrice = float(input("Electricity price in DKK (kr/kWh): "))

pricePerKMgas = gasPrice/KMperLiter
pricePerKMElectric = elPrice/KMperkWh

print("\n-----------------------------\nBenzin: {:.2f} kr/km".format(pricePerKMgas))
print("El: {:.2f} kr/km\n-----------------------------\n".format(pricePerKMElectric))

if pricePerKMElectric < pricePerKMgas:
    print("It is cheaper to drive on electricity than gasoline. You should charge your electric vehicle tonight.")
else:
print("It is cheaper to drive on gasoline than electricity.")
