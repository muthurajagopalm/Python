class rectangle :
    def __init__(self, length, width):
        print("test")

        self.length = length
        self.width = width
        #self.radius = radius
        print(self.length, self.width)
    def area(self):
        print("Area of rectangle:", self.length * self.width)

    def perimeter(self):
         print("Perimeter of rectangle:", self.length + self.width)

my_rectangle = rectangle(10,20)
#my_rectangle.area()


'''1. Create a Person Class
Attributes: name, age

Method: introduce() – prints "Hi, I'm [name] and I'm [age] years old."

2. BankAccount Class
Attributes: account_number, balance

Methods:

deposit(amount)

withdraw(amount)

check_balance()

3. Rectangle and Circle Classes
Attributes: dimensions (length, width, radius)

Methods:

area()

perimeter() or circumference()

4. Animal Class with Inheritance
Base Class: Animal – method speak()

Derived Classes: Dog, Cat – override speak()

5. Library System
Classes:

Book: title, author, ISBN

Library: manages a collection of books

Methods: add_book(), remove_book(), list_books()

6. Student and Course Relationship
Class Student: name, ID, list of courses

Class Course: name, code, list of enrolled students

Methods to enroll and drop students from courses

7. Simple Inventory System
Class Item: name, price, quantity

Class Inventory: list of items

Methods: add_item(), remove_item(), get_total_value()

8. Shape Abstract Class
Abstract method: area(), perimeter()

Derived classes: Rectangle, Circle, Triangle

9. Encapsulation Example
Create a class Employee with private attributes (__salary) and provide getter/setter methods.

10. Simple ATM Simulator
Class ATM: pin verification, balance check, withdrawal

Use encapsulation to secure sensitive data'''
