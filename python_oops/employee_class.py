class Employee:             # Class Declaration
    name = ""               # Class Attribute
    isEmployee = True       # Class Attribute
    email = ""              # Class Attribute

    def __init__(self, name, is_employee=True):    # Class constructor used for class initialization
        self.name = name                                    # Updating class attribute value
        self.isEmployee = is_employee
        self.email = f"{name}@gmail.com"

    def get_details(self):      # Use of self to access specific object
        return f"Employee name is {self.name} and email is {self.email}"    # Accessing class attributes of that object


employee_object_1 = Employee("Gopi")        # Object creation of Employee
employee_object_1.city = "Bangalore"     # Object Attribute
employee_object_1.name = "Krishna"       # Updating class attribute value for object_1
print(employee_object_1.get_details())
print(employee_object_1.email)

employee_object_2 = Employee("Gopi", False)        # Object creation of Employee
print(employee_object_2.name)         # Default value of class attribute
print(employee_object_2.get_details())      # 1st way of invoking a class function
Employee.get_details(employee_object_2)     # 2nd way of invoking a class function
