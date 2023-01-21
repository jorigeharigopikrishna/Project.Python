single_quote_line = 'Single Quote Line'
double_quote_line = "Single Quote Line"
triple_quote_line = """Single Quote Line"""

multi_line_quotes = """Multi Line Quote Line 1
                       Line 2
                       Line 3"""

sample_string = "python"

string_format_1 = "Welcome to " + sample_string
print(string_format_1)
string_format_2 = f"Welcome to {sample_string}"
print(string_format_2)
string_format_3 = "Welcome to {}".format(sample_string)
print(string_format_3)

num_1 = 24
num_2 = 50
string_format_4 = "Addition of %s and %s is %s" %(num_1, num_2, num_1 + num_2)
print(string_format_4)
