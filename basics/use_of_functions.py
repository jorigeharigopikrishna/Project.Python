name, isEmployee, employee_id = "Krishna", True, 123
veg_set = {"Potato", "Tomato", "Corn"}
int_tuple = (1, 2, 3, 0, 4, 5, 6)
global_number_1, global_number_2, global_number_3 = 10, 20, 30

def function_documented_example():
    """Documentation of the function"""
    print("Print documentation")


print(function_documented_example.__doc__)
function_copy = function_documented_example
function_copy()

# Function returning integer
def function_with_return(number):
    if number > 0:
        return number*number
    return 0

comprehension_list_using_function = [function_with_return(x) for x in int_tuple]
print(comprehension_list_using_function)

# Function returning list
def function_with_operations(num_1, num_2):
    add_result = num_1 + num_2
    subtract_result = num_1 - num_2

    return [add_result, subtract_result]

print(function_with_operations(global_number_1, global_number_2))

result_sum, result_subtract = function_with_operations(global_number_1, global_number_2)
print(result_sum, result_subtract)


# Positional arguments with simple datatype
def function_with_positional_arguments(name, lname):
    print(f"First name is {name}")
    print(f"Is Employee: {isEmployee}")


# Overriding positional arguments with global variables which are simple datatypes
function_with_positional_arguments("hari", "krishna")

# Positional arguments with complex datatype
def function_with_positional_arguments_complex_type(items):
    print(items)
    for i in items:
        print(i)

function_with_positional_arguments_complex_type(veg_set)
