class Student:
    def __init__(self, name, age, average_score):
        self.name = name
        self.age = age
        self.average_score = average_score

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_score(self):
        return self.average_score

    def set_average_score(self, average_score):
        self.average_score = average_score
student1 = Student("Иван", 20, 4.5)
print(f"Имя: {student1.get_name()}, Возраст: {student1.get_age()}, Средний балл: {student1.get_average_score()}")
student1.set_name("Петр")
student1.set_average_score(4.8)
print(f"Измененное имя: {student1.get_name()}, Новый средний балл: {student1.get_average_score()}")

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

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Mileage: {self.mileage} miles"


car1 = Car("Toyota", "Camry", 2020, 35000)
print(car1.get_info())
car1.set_mileage(40000)
print("Измененный пробег:", car1.get_info())

class BankAccount:
    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


account1 = BankAccount("Иван Петров", 1000)
account1.deposit(500)
account1.withdraw(200)
print(f"Баланс: {account1.get_balance()} руб.")
print("История транзакций:", account1.get_transactions())

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "Равнобедренный"
        else:
            return "Разносторонний"

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3))**0.5

triangle1 = Triangle(5, 5, 5)
triangle2 = Triangle(4, 4, 6)
print("Треугольник 1:", triangle1.triangle_type(), "Площадь:", triangle1.calculate_area())
print("Треугольник 2:", triangle2.triangle_type(), "Площадь:", triangle2.calculate_area())
