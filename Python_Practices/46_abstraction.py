from abc import ABC, abstractmethod

class car:
    @abstractmethod
    def moveforward(self):
        pass
    @abstractmethod
    def movebackward(self):
        pass
    @abstractmethod
    def audio(self):
        pass

class audi(car):

    def moveforward(self):
        print("Audi is moving forward")
    def movebackward(self):
        print("Audi is moving backward")
    def audio(self):
        print("Audi has the audio system")


class benz(car):

    def moveforward(self):
        print("benz is moving forward")
    def movebackward(self):
        print("benz is moving backward")
    def audio(self):
        print("benz has the audio system") 

audi = audi()
audi.moveforward()

