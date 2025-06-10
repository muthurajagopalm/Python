class vehicle:
    no_of_airbags = 6

class car(vehicle):
    no_of_tyres = 4

a = car()
print(a.no_of_airbags,a.no_of_tyres)