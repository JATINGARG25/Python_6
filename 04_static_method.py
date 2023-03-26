from typing_extensions import Self


class Employee:
    company = "Google"
    def greet(self,signature):
        print(f"Good Morning, {self.name} Sir. \n{signature}")

jatin  = Employee()
jatin.salary = 100000
jatin.greet("Have a nice day.")
