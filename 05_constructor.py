class Employee:
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit  = subunit
        print("Employee is created!")
    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

jatin = Employee("Jatin",10000,"Photgrapher")
jatin.getdetails()