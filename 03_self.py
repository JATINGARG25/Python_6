class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

jatin  = Employee()
jatin.salary = 100000
jatin.getsalary()
