num_list = [54, 145, 765, 245, 85, 245, 843, 22, 56, 70]

square_of = lambda x: x * x     # Defining a lambda
print(square_of(4))     # Invoking a lambda

print((lambda x: x**x)(4))      # Defining and invoking a lambda

add_lambda = lambda a, b: a + b
print(add_lambda(1, 2))

subtract_lambda = lambda a, b: a - b
print(subtract_lambda(1, 2))

multiply_lambda = lambda a, b: a * b
print(multiply_lambda(1, 2))

divide_lambda = lambda a, b: a / b
print(divide_lambda(1, 2))

def calculator_lambda(a, b, lambda_fn=add_lambda):
    return lambda_fn(a, b)

print(calculator_lambda(1, 2))      # Invokes add_lambda
print(calculator_lambda(1, 2, subtract_lambda))     # Invokes subtract_lambda
print(calculator_lambda(1, 2, multiply_lambda))     # Invokes multiply_lambda
print(calculator_lambda(1, 2, divide_lambda))       # Invokes divide_lambda
print(calculator_lambda(1, 2, lambda a, b: a // b))       # Invokes lambda function on the fly

# Using input arguments
total_score = lambda maths, physics, chemistry, biology: maths + physics + chemistry + biology
print(total_score(10, 20, 30, 40))      # Invocation using positional arguments
print(total_score(10, 20, chemistry=30, biology=40))
print(total_score(maths=10, physics=20, chemistry=30, biology=40))      # Invocation using keyword arguments

# Using input and default arguments
total_score_with_defaults = lambda maths, physics, chemistry=50, biology=10: maths + physics + chemistry + biology
print(total_score_with_defaults(10, 20))    # Invocation using default values
print(total_score_with_defaults(10, 20, chemistry=30))
print(total_score_with_defaults(maths=10, physics=20, chemistry=30, biology=40))    # Overriding default values

# Using variable length arguments
print((lambda *args: sum(args))(1, 2, 3, 4, 5))

# Using Keyword variable length arguments
print((lambda **kwargs: sum(kwargs.values()))(a=22, b=23, c=24))

# Use of lambda function in filter() function
filtered_even_list = list(filter(lambda x : x % 2 == 0, num_list))
print(filtered_even_list)

filtered_range_list = list(filter(lambda x : x > 10 and x < 100, num_list))
print(filtered_range_list)
