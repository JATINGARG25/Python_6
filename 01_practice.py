class Programmer:
    company = "Microsoft"

    def __init__(self,name,languages):
        self.name= name
        self.language= languages
    def details(self):
        print(f"The name of the programmer is {self.name}.")
        print(f"The languages known by the programmer is {self.language}.")

jatin = Programmer("Jatin", "C++ and Python")
harry = Programmer("Harry", "C")
jatin.details()
