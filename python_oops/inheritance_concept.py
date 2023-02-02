import math


# Single Inheritance
class Shape:  # Base class
    """This is a base class"""

    def __init__(self, name):
        self.__shape_name = name  # Private object variable

    def get_shape_name(self):  # Base class Method
        print("Shape is: ", self.__shape_name)

    def perimeter_of_shape(self):  # Base class Method
        print(f"Perimeter of {self.__shape_name} is: ")

    def area_of_shape(self):  # Base class Method
        print(f"Area of {self.__shape_name} is: ")


class Circle(Shape):  # Single Inheritance - Derived Class
    """This is a derived class inherited from Shape base class.
        This is a single inheritance.
        Inheritance hierarchy goes from Circle -> Shape -> Built-in object
    """
    circle_radius = 0  # Public class variable

    def __init__(self, radius):
        Shape.__init__(self, "circle")  # Use of baseclassname to invoke base class __init__()
        self.circle_radius = radius  # Public object variable

    def perimeter_of_shape(self):  # Overriding base class method
        Shape.perimeter_of_shape(self)  # Invoking base class definition using baseclassname
        return 2 * math.pi * self.circle_radius

    def area_of_shape(self):  # Overriding base class method
        Shape.area_of_shape(self)  # Invoking base class definition using baseclassname
        return math.pi * self.circle_radius * self.circle_radius


class Rectange(Shape):  # Single Inheritance - Derived Class
    """This is a derived class inherited from Shape base class.
        This is a single inheritance.
        Inheritance hierarchy goes from Rectangle -> Shape -> Built-in object
    """

    length = 0  # Public class variable
    breadth = 0  # Public class variable

    def __init__(self, name, length, breadth):
        super().__init__(name)  # Use of super() function to invoke base class __init__()
        self.length = length  # Public object variable
        self.breadth = breadth  # Public object variable

    def perimeter_of_shape(self):  # Overriding base class method
        super().perimeter_of_shape()  # Invoking base class definition using super() function
        return 2 * (self.length + self.breadth)

    def area_of_shape(self):  # Overriding base class method
        super().area_of_shape()  # Invoking base class definition using super() function
        return self.length * self.breadth


base_class = Shape("base_shape")  # Base class object
base_class.get_shape_name()  # Invoking base class method
derived_class_circle = Circle(10)  # Derived class object
print(derived_class_circle.perimeter_of_shape())  # Invoking Derived class method
print(derived_class_circle.area_of_shape())  # Invoking Derived class method
print(derived_class_circle.get_shape_name())  # Invoking Base class method using derived class object

derived_class_rectangle = Rectange("rectangle", 10, 10)  # Derived class object
print(derived_class_rectangle.perimeter_of_shape())  # Invoking Derived class method
print(derived_class_rectangle.area_of_shape())  # Invoking Derived class method
print(derived_class_rectangle.get_shape_name())  # Invoking Base class method using derived class object


# Multiple Inheritance
class Father:  # Base class
    """This is a base class 1"""

    def __init__(self, name):
        self.__name = name      # Private instance variable

    def print_name(self):       # Base class method
        print("Name is: ", self.__name)


class Mother:  # Base class
    """This is a base class 2"""

    def __init__(self, name):
        self.__name = name      # Private instance variable

    def print_name(self):       # Base class method
        print("Name is: ", self.__name)


class Child(Father, Mother):  # Multiple Inheritance - Derived Class
    """ This is a multiple inheritance.
        Inheritance hierarchy goes from left to right i.e.,
        Child -> Father -> Mother -> Built-in object
    """

    def __init__(self, father_name, mother_name, name):
        Father.__init__(self, father_name)      # Invoking base class Father init() method
        Mother.__init__(self, mother_name)      # Invoking base class Mother init() method
        self.__name = name                      # Private instance variable

    def print_name(self):                       # Overriding base class method
        Father.print_name(self)                 # Invoking base class Father print_name() method
        Mother.print_name(self)                 # Invoking base class Mother print_name() method
        print("Name is: ", self.__name)


child_object = Child("Father-1", "Mother-1", "Child-1")  # Multiple Derived class object
child_object.print_name()


# Multilevel Inheritance
class GrandFather:  # Base class
    """This is a base class"""

    def __init__(self, name):
        self.__name = name      # Private instance variable

    def print_name(self):       # Base class method
        print("Name of grand father: ", self.__name)

    def print_grand_father_name(self):  # Base class method
        print("Invoked Name of grand father: ", self.__name)


class Son(GrandFather):  # Multilevel Inheritance - Level 1 Derived Class
    """ This is a multilevel inheritance.
        It is level 1 derived class
        Inheritance hierarchy goes from bottom to top i.e.,
        Son -> GrandFather -> Built-in object
    """

    def __init__(self, father_name, name):
        super().__init__(father_name)   # Invocation of base class - GrandFather using super()
        self.__name = name              # Private instance variable

    def print_name(self):               # Overriding base class method
        super().print_name()            # Invoking base class GrandFather print_name() method
        print("Name of son is: ", self.__name)

    def print_son_name(self):           # Derived class 1 method
        print("Invoked Name of son: ", self.__name)


class Grandson(Son):  # Multilevel Inheritance - Level 2 Derived Class
    """ This is a multilevel inheritance.
        It is level 2 derived class
        Inheritance hierarchy goes from bottom to top i.e.,
        Grandson -> Son -> GrandFather -> Built-in object
    """

    def __init__(self, grand_father_name, father_name, name):
        super().__init__(grand_father_name, father_name)    # Invocation of derived class 1 - Son using super()
        self.__name = name      # Private instance variable

    def print_name(self):       # Overriding base class method
        super().print_name()    # Invocation of derived class 1 print_name() method using super()
        print("Name of grandson is: ", self.__name)

    def print_grand_son_name(self):     # Derived class 2 method
        print("Invoked Name of grand son: ", self.__name)


grandfather_object = GrandFather("Grandfather-1")
grandfather_object.print_name()  # Using base class object and invoke base class method
                                 # Polymorphism as base class object invoked its base class method only

son_object = Son("Grandfather-2", "Son-1")
son_object.print_name()  # Using derived class 1 object and invoke derived class 1 method
                         # Polymorphism as derived class 1 object invoked its derived class 1 method only instead of base class method.
son_object.print_grand_father_name()    # Using derived class 1 object and invoke base class method
son_object.print_son_name()             # Using derived class 1 object and invoke derived class 1 method

grandson_object = Grandson("GrandFather-3", "Son-2", "Grandson-1")
grandson_object.print_name()  # Using derived class 2 object and invoke derived class 2 method
                              # Polymorphism as derived class 2 object invoked its derived class 2 method only instead of derived class 1 method and base class method.
grandson_object.print_grand_son_name()  # Using derived class 2 object and invoke derived class 2 method
grandson_object.print_son_name()        # Using derived class 2 object and invoke derived class 1 method
grandson_object.print_grand_father_name()        # Using derived class 2 object and invoke base class method
