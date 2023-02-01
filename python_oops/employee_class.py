class Employee:             # Class Declaration
    """ This is a employee class"""     # Documentation of class
    company = "MNC"         # Public Class attribute
    name = ""               # Public Class Attribute
    isEmployee = True       # Public Class Attribute
    email = ""              # Public Class Attribute
    __employee_type = "FullTime"    # Private Class Attribute

    def __init__(self, name, role, skillset, is_employee=True):     # Class constructor used for class initialization
        self.name = name                            # public object attribute  - self.name is instance variable.
        self.isEmployee = is_employee               # public object attribute - self.isEmployee is instance variable
        self.email = f"{name}@gmail.com"            # public object attribute - self.email is instance variable
        self.__job_role = role                      # private object attribute - self.__job_role is instance variable
        self.__skills = skillset                    # private object attribute - self.__skills is instance variable

    def get_details(self):      # Use of self to access specific object
        return f"Employee name is {self.name} and company is {Employee.company}"    # self.name is instance variable and Employee.company is class variable.

    def get_company_details(self):
        return Employee.company     # Employee.company is class variable.

    def get_employee_job_title(self):
        return self.__job_role      # self.__job_role is private instance variable.

    def get_employee_skills(self):
        return self.__skills        # self.__skills is private instance variable.


employee_object_1 = Employee("Gopi", "Developer", ["Python"])        # Object creation of Employee
employee_object_1.city = "Bangalore"        # Object Attribute
employee_object_1.name = "Krishna"          # Updating public object attribute value for object_1
# employee_object_1.__job_role                # Error cant access __job_role as it is private. It creates a object attribute
# employee_object_1.__skills                  # Error cant access __skills as it is private. It creates a object attribute.
print(employee_object_1._Employee__job_role)  # Way to access __job_role though it is private
print(employee_object_1._Employee__skills)    # Way to access __skills though it is private
print(Employee._Employee__employee_type)    # Way to access __employee_type though it is private
print(employee_object_1.get_employee_job_title())
print(employee_object_1.get_employee_skills())

employee_object_2 = Employee("Gopi", "Developer", ["Python"], False)        # Object creation of Employee
print(employee_object_2.name)               # Value of public object attribute
print(employee_object_2.get_details())      # 1st way of invoking a class function
Employee.get_details(employee_object_2)     # 2nd way of invoking a class function
print(employee_object_2.get_company_details())  # accessing class variable.
