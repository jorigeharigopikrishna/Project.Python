class Employee:             # Class Declaration
    company = "MNC"         # Class attribute
    name = ""               # Class Attribute
    isEmployee = True       # Class Attribute
    email = ""              # Class Attribute

    def __init__(self, name, is_employee=True):    # Class constructor used for class initialization
        self.name = name                           # Updating class attribute value, self.name is instance variable.
        self.isEmployee = is_employee               # self.isEmployee is instance variable
        self.email = f"{name}@gmail.com"            # self.email is instance variable

    def get_details(self):      # Use of self to access specific object
        return f"Employee name is {self.name} and company is {Employee.company}"    # self.name is instance variable and Employee.company is class variable.

    def get_company_details(self):
        return Employee.company     # Employee.company is class variable.


employee_object_1 = Employee("Gopi")        # Object creation of Employee
employee_object_1.city = "Bangalore"     # Object Attribute
employee_object_1.name = "Krishna"       # Updating class attribute value for object_1
print(employee_object_1.get_details())
print(employee_object_1.email)
print(employee_object_1.get_company_details())

employee_object_2 = Employee("Gopi", False)        # Object creation of Employee
print(employee_object_2.name)         # Default value of class attribute
print(employee_object_2.get_details())      # 1st way of invoking a class function
Employee.get_details(employee_object_2)     # 2nd way of invoking a class function
print(employee_object_2.get_company_details())  # accessing class variable.
