from user import User



class Person:
    def __init__(self, name, surname, age, address, foreign_key, key = None):
        self.foreign_key = foreign_key
        self.key = key
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
