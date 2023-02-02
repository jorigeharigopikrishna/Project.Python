import math


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


class Circle(Shape):  # Inheritance - Derived Class
    """This is a derived class inherited from Shape base class"""
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


class Rectange(Shape):  # Inheritance - Derived Class
    """This is a derived class inherited from Shape base class"""

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
