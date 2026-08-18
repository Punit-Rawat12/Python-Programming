class Employee :
    language = "Py"            #'''this is classs attribute'''
    salary = 1200000
    def getinfo(self):
        print(f"Print language is {self.language} .The salary is {self.salary}")



First = Employee()
Name = "Nikunj"              #''' This is instance  attribute'''
print(First.salary ,Name )

second = Employee()
secondname = "Anant"
print(second.salary , secondname)