from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        """Alternative constructor to create a Date object from a DD-MM-YYYY string."""
        day, month, year = map(int, date_str.split('-'))

        return cls(day, month, year)

    def display_date(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age} years old.")

class BankAccount():
    def __init__(self, balance):
        self.__balance = balance # private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

def main():
    p1 = Person("Abanoub", 21)
    p1.info()

    acc = BankAccount(53)
    acc.deposit(12)

    c = Circle(5)
    print(c.area())
    print(Circle.area(c))

    date1 = Date(25, 10, 2024)
    print(f"Standard init: {date1.display_date()}")

    date_string = "01-01-2025"
    date2 = Date.from_string(date_string)
    print(f"Alternative init: {date2.display_date()}")


if __name__ == "__main__":
    main()