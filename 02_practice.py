class Calculator:
    def __init__(self,num):
        self.num = num 
    def square(self):
        print(f"The square of {self.num} is {self.num**2} ")
    def cube(self):
        print(f"The cube of {self.num} is {self.num**3} ")
    def squareroot(self):
        print(f"The squareroot of {self.num} is {self.num**0.5} ")
       
b = int(input("Enter the number\n"))
a = Calculator(b)
a.square()
a.cube()
a.squareroot()

    
