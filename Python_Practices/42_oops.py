class car:
    no_of_wheels = 4
    no_of_airbags = 6
    tank_capacity = 600
    #print(tank_capacity)

    def movingforward(self):
        print("While acceleration moving forward")
    def movingbackward(self):
         print("While acceleration moving backward")

car1 = car()
print(car1.no_of_wheels)

car2 = car()
car2.no_of_wheels = 5
car2.tank_capacity = 900
print(car2.tank_capacity)
print(car2.no_of_wheels)

car3 = car()
car3.movingbackward()