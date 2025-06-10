########## Method Overriding ############
'''class animal:
    def speak(self):
        print("This animal speaks")

class dog:
    def speak(self):
        print("This animal barks")

a = animal()
b = dog()
a.speak()
b.speak()'''


############### Duck Typing #############

'''class animal:
    def speak(self):
        print("This animal speaks")
    

class dog:
    def speak(self):
        print("This animal barks")
        

def func (entity):
    entity.speak()
    entity.speak()
func(animal())
func(dog())'''

#################### Method overloading #############

class maths:
    def adding(self, *args):
        summm = 0
        for i in (args):
            summm += i
        return summm
a = maths()
print(a.adding(4,5))







