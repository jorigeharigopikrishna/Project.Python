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


# Input arguments with simple datatype
def function_with_input_arguments(name, lname):
    print(f"First name is {name}")
    print(f"Is Employee: {isEmployee}")


# Overriding input arguments with global variables which are simple datatypes
function_with_input_arguments("hari", "krishna")
# Using positional arguments to invoke function
function_with_input_arguments("hari", "krishna")
# Using keyword arguments to invoke function
function_with_input_arguments(name="hari", lname="krishna")
# Using mix up of positional and keyword arguments to invoke function
function_with_input_arguments("hari", lname="krishna")

# Input arguments with complex datatype
def function_with_input_arguments_complex_type(items):
    if len(items) == 0:
        print("No elements in the collection")
        return None

    max_element = items[0]
    for item in items:
        print(item)
        if item > max_element:
            max_element = item
    return max_element

# Using positional arguments to invoke function
result_max = function_with_input_arguments_complex_type(int_tuple)
print("Maximum element is ", result_max)
# Using keyword arguments to invoke function
result_max = function_with_input_arguments_complex_type(items=int_tuple)
print("Maximum element is ", result_max)

# Default Arguments with simple datatype
def function_with_default_arguments_with_simple_datatype(emp_id, emp_name, is_employee=False):
    if is_employee:
        print("Employee id:", emp_id)
    print("Employee name:", emp_name)
function_with_default_arguments_with_simple_datatype(101, "Gopi", True)
function_with_default_arguments_with_simple_datatype(102, "Hari")

# Default Arguments with complex datatype
def function_with_default_arguments_with_complex_datatype(list, is_empty=False):
    if is_empty:
        print("Is Empty list:", is_empty)
    else:
        print("First element: ", list[0])
function_with_default_arguments_with_complex_datatype([], True)
function_with_default_arguments_with_complex_datatype(int_tuple)

# Variable Length Arguments with simple datatype
def function_with_variable_length_arguments_with_simple_datatype(emp_id, *args):
    print("Variable length values starts: ", emp_id)
    for i in args:      # Here, args is a tuple, so looping over a tuple here
        print(i)

function_with_variable_length_arguments_with_simple_datatype(100)
function_with_variable_length_arguments_with_simple_datatype(101, "Hari")
function_with_variable_length_arguments_with_simple_datatype(102, "Hari", [1, 2])
function_with_variable_length_arguments_with_simple_datatype(103, "Gopi", 123, {1, 2, 3})

# Variable Length Arguments with complex datatype
def function_with_variable_length_arguments_with_complex_datatype(full_name, *args):
    print("Variable length values starts: ", full_name)
    for i in args:      # Here, args is a tuple, so looping over a tuple here
        print(i)

function_with_variable_length_arguments_with_complex_datatype("Hari")
function_with_variable_length_arguments_with_complex_datatype("Hari", [1, 2, 3])
function_with_variable_length_arguments_with_complex_datatype("Gopi", (1, 2, 3), [4, 5])
function_with_variable_length_arguments_with_complex_datatype("Krishna", {1, 2, 3}, {"id": 101, "city": "ab"})