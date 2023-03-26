class Employee:
    company = "Google"
    salary = 100

jatin = Employee()
harry  = Employee()
jatin.salary = 300
harry.salary = 400

# print(jatin.company)
# Employee.company = "Youtube"
# print(jatin.company)

print(jatin.salary)
print(harry.salary)

jatin.salary = 500 
harry.salary = 700

print(f"The salary of jatin is {jatin.salary}")
print(f"The salary of harry is {harry.salary}")
