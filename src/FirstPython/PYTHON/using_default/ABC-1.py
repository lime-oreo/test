class Person:
    def __intit__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("invalid salary")

person = Person("Alice", 30, 5000)

print(person.name)

print(person._age)

print(person.get_salary())

person.set_salary(6000)
print(person.get_salary())