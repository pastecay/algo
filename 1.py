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

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)



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
