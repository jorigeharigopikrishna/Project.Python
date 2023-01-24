name, isEmployee, employee_id = "Krishna", True, 123
veg_set = {"Potato", "Tomato", "Corn"}
int_tuple = (1, 2, 3, 0, 4, 5, 6)

def function_documented_example():
    """Documentation of the function"""
    print("Print documentation")


print(function_documented_example.__doc__)
function_copy = function_documented_example
function_copy()


def function_with_positional_arguments(name, lname):
    print(f"First name is {name}")
    print(f"Is Employee: {isEmployee}")


# Overriding positional arguments with global variables
function_with_positional_arguments("hari", "krishna")

def function_with_positional_arguments_complex_type(items):
    print(items)
    for i in items:
        print(i)

function_with_positional_arguments_complex_type(veg_set)

def function_with_return(number):
    if number > 0:
        return number*number
    return 0

comprehension_list_using_function = [function_with_return(x) for x in int_tuple]
print(comprehension_list_using_function)