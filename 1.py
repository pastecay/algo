class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_grade(self):
        return self.average_grade

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

student1 = Student("Иван", 20, 4.5)
print(f"Имя: {student1.get_name()}, Возраст: {student1.get_age()}, Средний балл: {student1.get_average_grade()}")
student1.set_name("Петр")
student1.set_average_grade(4.8)
print(f"Измененное имя: {student1.get_name()}, Новый средний балл: {student1.get_average_grade()}")



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(5, 3)
area = rectangle1.calculate_area()
perimeter = rectangle1.calculate_perimeter()
print(f"Площадь: {area}, Периметр: {perimeter}")


class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def change_make(self, make):
        self.make = make

    def change_model(self, model):
        self.model = model

    def change_year(self, year):
        self.year = year

    def change_mileage(self, mileage):
        self.mileage = mileage

    def display_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}, Пробег: {self.mileage} км"

car1 = Car("Toyota", "Camry", 2020, 35000)
print(car1.display_info())
car1.change_mileage(40000)
print("Измененный пробег:", car1.display_info())




class BankAccount:
    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Пополнение: +{amount} руб.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Снятие: -{amount} руб.")
        else:
            return "Недостаточно средств на счете."

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

account1 = BankAccount("Иван Петров", 1000)
account1.deposit(500)
account1.withdraw(200)
print(f"Баланс: {account1.get_balance()} руб.")
print("История транзакций:", account1.get_transaction_history())





class Trinit    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side3 == self.side1:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area



triangle1 = Triangle(5, 5, 5)
triangle2 = Triangle(4, 4, 6)
print("Треугольник 1:", triangle1.determine_type(), "Площадь:", triangle1.calculate_area())
print("Треугольник 2:", triangle2.determine_type(), "Площадь:", triangle2.calculate_area())


