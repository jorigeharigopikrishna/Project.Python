# Ternary condition
num = 101
num_str = "Greater than" if num > 100 else "Less than"
print(num_str)

# List Comprehensions
int_list = [1, 2, 3, 4, 5]
string_list = ["Apple", "Banana", "America", "Custard", "China", "Brazil"]
int_comprehension_list = [i * i for i in int_list]
string_comprehension_list = [word for word in string_list if word.startswith("A")]
print(int_list)
print(int_comprehension_list)
print(string_comprehension_list)

# Tuple Comprehensions
int_tuple = (1, 2, 3, 4, 5)
string_tuple = ["Apple", "Banana", "America", "Custard", "China", "Brazil"]
int_comprehension_tuple = (i * i for i in int_tuple)
string_comprehension_tuple = (word for word in string_list if len(word) > 5)
print(int_tuple)
print(tuple(int_comprehension_tuple))
print(tuple(string_comprehension_tuple))

# Set Comprehensions
int_set = {1, 2, 3, 4, 5}
string_set = ["Apple", "Banana", "America", "Custard", "China", "Brazil"]
int_comprehension_set = {i * i for i in int_set}
string_comprehension_set = {word for (index, word) in enumerate(string_set) if index % 2 == 0}
print(int_set)
print(int_comprehension_set)
print(string_comprehension_set)

fname, lname = "Gopi", "Krishna"  # Global Variables
print(fname, lname)  # Updated original Global Variables - fname, lname


def update_global_variables_with_local():
    global fname, lname  # Referencing Global Variables
    fname = fname + " Jorige"  # Updating Global Variables - fname
    lname = lname + " Jorige"  # Updating Global Variables - lname

    print(fname, lname)


update_global_variables_with_local()
print(fname, lname)  # Updated Global Variables - fname, lname
