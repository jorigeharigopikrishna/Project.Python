import math


def function_introduction(name):
    print("Hello: ", name)


function_introduction("Gopi")  # Function invocation
function_copy = function_introduction  # Function assignment - Example of first class citizen
function_copy("Hari")


def circle_diameter(radius):
    diameter = 2 * radius
    print("Diameter is: ", diameter)
    return diameter


def circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    print("Perimeter: ", perimeter)
    return perimeter


def circle_area(radius):
    area = math.pi * radius * radius
    print("Area is: ", area)
    return area


def rectangle_perimeter(length, breadth):
    perimeter = 2 * (length + breadth)
    print("Perimeter: ", perimeter)
    return perimeter


def rectangle_area(length, breadth):
    area = length * breadth
    print("Area is: ", area)
    return area


def calculations_with_positional_arguments(radius,
                                           fn):  # Declaring other function as argument  - Example of first class citizen
    return fn(radius)  # Invoking other function


calculations_with_positional_arguments(5, circle_diameter)  # Passing other function circle_diameter() as value
calculations_with_positional_arguments(5, circle_perimeter)  # Passing other function circle_perimeter() as value
calculations_with_positional_arguments(5, circle_area)  # Passing other function circle_area() as value


def calculations_with_variable_length_arguments(*args,
                                                fn):  # Declaring other function as argument  - Example of first class citizen
    return fn(*args)  # Invoking other function


calculations_with_variable_length_arguments(5,
                                            fn=circle_perimeter)  # Passing other function circle_perimeter() as value
calculations_with_variable_length_arguments(5, fn=circle_area)  # Passing other function circle_area() as value
calculations_with_variable_length_arguments(10, 10,
                                            fn=rectangle_perimeter)  # Passing other function rectangle_perimeter() as value
calculations_with_variable_length_arguments(10, 10,
                                            fn=rectangle_area)  # Passing other function rectangle_area() as value


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator(operation="+"):
    if operation == "+":
        return add  # Returns an function from other function - Example of first class citizen
    if operation == "-":
        return subtract  # Returns an function from other function - Example of first class citizen
    if operation == "*":
        return multiply  # Returns an function from other function - Example of first class citizen
    if operation == "/":
        return divide  # Returns an function from other function - Example of first class citizen


add_function = calculator()  # Returns an add() function
add_function(1, 2)  # Invoke an add() function

subtract_function = calculator("-")  # Returns an subtract() function
subtract_function(5, 2)  # Invoke subtract() function

multi_function = calculator("*")  # Returns an mutiply() function
multi_function(5, 2)  # Invoke multiply() function

divide_function = calculator("/")  # Returns an divide() function
divide_function(5, 2)  # Invoke divide() function

calculator_dictionary = {
    "+": add,   # Use of function as value in dict - Example of first class citizen
    "-": subtract,  # Use of function as value in dict - Example of first class citizen
    "*": multiply,  # Use of function as value in dict - Example of first class citizen
    "/": divide     # Use of function as value in dict - Example of first class citizen
}

add_function_dict = calculator_dictionary["+"]  # Returns an add() function object
add_function_dict(1, 2)
sub_function_dict = calculator_dictionary["-"]  # Returns an subtract() function object
sub_function_dict(5, 2)
mul_function_dict = calculator_dictionary["*"]  # Returns an multiply() function object
mul_function_dict(5, 2)
div_function_dict = calculator_dictionary["/"]  # Returns an divide() function object
div_function_dict(5, 2)
