name, isEmployee, employee_id = "Krishna", True, 123
veg_set = {"Potato", "Tomato", "Corn"}
int_tuple = (1, 2, 3, 0, 4, 5, 6)
global_number_1, global_number_2, global_number_3 = 10, 20, 30
nested_dict = {"name": "Krishna", "house_no": 233, "employee": {"id": 143, "company": "abcd"}, "isEmployee": True}


def function_documented_example():
    """Documentation of the function"""
    print("Print documentation")


print(function_documented_example.__doc__)
function_copy = function_documented_example
function_copy()


# Function returning integer
def function_with_assert(number):
    assert number > 0  # Used for assertion check
    print("Assertion function")


function_with_assert(2)  # No Assertion error
function_with_assert(-5)  # Assertion error


# Function returning integer
def function_with_return(number):
    if number > 0:
        return number * number
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


# Variable Length Arguments of args with simple datatype
def function_with_variable_length_arguments_using_args_with_simple_datatype(emp_id, *args):
    print("Variable length with args simple values starts: ", emp_id)
    print(type(args))  # args is a tuple by default
    for i in args:  # Here, args is a tuple, so looping over a tuple here
        print(i)


# Collection passed as ()
function_with_variable_length_arguments_using_args_with_simple_datatype(100)
# Collection passed as ("Hari")
function_with_variable_length_arguments_using_args_with_simple_datatype(101, "Hari")
# Collection passed as ("Hari", 121)
function_with_variable_length_arguments_using_args_with_simple_datatype(102, "Hari", 121)
# Collection passed as ("Gopi", True, 123)
function_with_variable_length_arguments_using_args_with_simple_datatype(103, "Gopi", True, 123)


# Variable Length Arguments of args with complex datatype
def function_with_variable_length_arguments_using_args_with_complex_datatype(full_name, *args):
    print("Variable length with args complex values starts: ", full_name)
    print(type(args))  # args is a tuple by default
    print(args)
    for i in args:  # Here, args is a tuple, so looping over a tuple here
        print(i)


# Collection passed as ()
function_with_variable_length_arguments_using_args_with_complex_datatype("Hari")
# Collection passed as ([1, 2, 3])
function_with_variable_length_arguments_using_args_with_complex_datatype("Hari", [1, 2, 3])
# Use of * to split elements of collection into individual elements instead of sending as collection.
# Without *, collections will be passed as ((1, 2, 3), [4, 5]). It wont split individual elements as (1, 2, 3, 4, 5)
# If *, collections will be passed as (1, 2, 3, 4, 5) instead of ((1, 2, 3), [4, 5]).
function_with_variable_length_arguments_using_args_with_complex_datatype("Gopi", (1, 2, 3), [4, 5])
# Collection passed as (1, 2, 3, "id", "city")
function_with_variable_length_arguments_using_args_with_complex_datatype("Krishna", *{1, 2, 3},
                                                                         *{"id": 101, "city": "ab"})
# Collection passed as ("Corn", "Potato", "Tomato")
function_with_variable_length_arguments_using_args_with_complex_datatype("Krishna", *veg_set)


# Variable Length Arguments of kwargs with simple datatype
def function_with_variable_length_arguments_using_kwargs_with_simple_datatype(emp_id, **kwargs):
    print("Variable length with kwargs simple values starts: ", emp_id)
    print(type(kwargs))  # kwargs is a dict by default
    for key in kwargs:  # Here, kwargs is a dict, so looping over a dict here
        print(kwargs[key])


# Collection passed as {}
function_with_variable_length_arguments_using_kwargs_with_simple_datatype(100)
# Collection passed as {"name":"Hari"}
function_with_variable_length_arguments_using_kwargs_with_simple_datatype(101, name="Hari")
# Collection passed as {"name":"Hari", "id": 121}
function_with_variable_length_arguments_using_kwargs_with_simple_datatype(102, name="Hari", id=121)
# Collection passed as {"name":"Gopi", "isEmp": True, "id": 121}
function_with_variable_length_arguments_using_kwargs_with_simple_datatype(103, name="Gopi", isEmp=True, id=123)


# Variable Length Arguments of kwargs with complex datatype
def function_with_variable_length_arguments_using_kwargs_with_complex_datatype(full_name, **kwargs):
    print("Variable length with kwargs complex values starts: ", full_name)
    print(type(kwargs))  # kwargs is a dict by default
    print(kwargs)
    for key in kwargs:  # Here, kwargs is a dict, so looping over a dict here
        print(kwargs[key])


# Collection passed as {}
function_with_variable_length_arguments_using_kwargs_with_complex_datatype("Hari")
# Collection passed as {"num_list":[1, 2, 3]}
function_with_variable_length_arguments_using_kwargs_with_complex_datatype("Hari", num_list=[1, 2, 3])
# Collection passed as {"num_tuple":(1, 2, 3), "num_list":[4, 5]}
function_with_variable_length_arguments_using_kwargs_with_complex_datatype("Gopi", num_tuple=(1, 2, 3), num_list=[4, 5])
# Collection passed as {"num_set": {1, 2, 3}, "student_dict": {"id": 101, "city": "ab"}}
function_with_variable_length_arguments_using_kwargs_with_complex_datatype("Krishna", num_set={1, 2, 3},
                                                                           student_dict={"id": 101, "city": "ab"})
# Collection passed as {"student_dict"={"name": "Krishna", "house_no": 233, "employee": {"id": 143, "company": "abcd"}, "isEmployee": True}}
function_with_variable_length_arguments_using_kwargs_with_complex_datatype("Krishna", student_dict=nested_dict)
# Use of ** to pass dictionary directly without using keyword arguments.
# Without **, keyword needs to be passed even though its a dictionary collection.
# Collection passed as {"name": "Krishna", "house_no": 233, "employee": {"id": 143, "company": "abcd"}, "isEmployee": True}
function_with_variable_length_arguments_using_kwargs_with_complex_datatype("Krishna", **nested_dict)


# Variable Length Arguments with both args and kwargs with complex datatype
def function_with_variable_length_arguments_using_args_and_kwargs_with_simple_datatype(full_name, *args, **kwargs):
    print("Variable length with args complex values starts: ", full_name)
    print(type(args))  # args is a tuple by default
    print(args)
    for arg in args:  # Here, args is a tuple, so looping over a tuple here
        print(arg)

    print("Variable length with kwargs complex values starts: ", full_name)
    print(type(kwargs))  # kwargs is a dict by default
    print(kwargs)
    for key in kwargs:  # Here, kwargs is a dict, so looping over a dict here
        print(kwargs[key])


function_with_variable_length_arguments_using_args_and_kwargs_with_simple_datatype("Gopi", 1, 2, 3, age=1, city="ab")
