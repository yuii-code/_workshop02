class Person:
    def __init__ (self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_info(self):
        return {"Name" : self.name, "Age": self.age}

name = "Onthicha Srikun"
age = "21"
address = "Bangkok"

person = Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_info())





