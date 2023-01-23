employee_name = "Hari Gopi Krishna"
fruits_list = ["Apple", "Banana", "Custard", "Grape", "Lemon"]
int_tuple = (1, 2, 3, 4, 5, (6, 7))
details_dict = {"name": "Krishna", "house_no": 233, "employee": {"id": 143, "company": "abcd"}, "isEmployee": True}
veg_set = {"Potato", "Tomato", "Corn"}

for char in employee_name:
    print(char)

for ele in veg_set:
    print("Vegetable is", ele)

for index, element in enumerate(int_tuple):
    print(f"Element at index {index} is {element}")

for key in details_dict:
    print(key)

for value in details_dict.values():
    print(value)

for key in details_dict:
    print(f"Key is {key} and its value is {details_dict[key]}")

for key, value in details_dict.items():
    print(f"Key is {key} and its value is {value}")

for fruit in fruits_list:
    print(fruit)
else:
    print("Executed all elements in the list")

for num in range(1, 5):
    print(num)

for num in range(1, 10, 3):
    print(num)

for num in reversed(range(1, 5)):
    print(num)

for fruit in fruits_list:
    if fruit == "Custard":
        print("Custard is found")
        break
        print("Code after break statement")
    print(fruit)
else:
    print("Executed all elements in the list")

for fruit in fruits_list:
    if fruit == "Custard":
        print("Custard is found")
        continue
        print("Code after continue statement")
    print(fruit)
else:
    print("Executed all elements in the list")

for fruit in fruits_list:
    if fruit == "Custard":
        print("Custard is found")
        pass
        print("Code after pass keyword")
    print(fruit)
else:
    print("Executed all elements in the list")

for fruit in fruits_list:
    if fruit == "Custard":
        print("Custard is found")
        exit()
        print("Code after exit method")
    print(fruit)
else:
    print("Executed all elements in the list")

var_number = 20
while var_number < 25:
    print(var_number)
    var_number += 1
print(var_number)

var_string_1 = ""
while var_string_1:
    print("While loop in case of empty string")
print("Empty", var_string_1)

var_num = 1
while var_num in range(1, 5):
    print(var_num)
    var_num += 1
print("Last element", var_num)

var_number_2 = 5
while var_number_2: print("Element is"); print(var_number_2); var_number_2 -= 1
print("Last element is", var_number_2)

it = 0
while it < len(fruits_list):
    print(it)
    print(fruits_list[it])
    it += 1
print(it)

it = 0
while it < len(fruits_list):
    print(it)
    print(fruits_list[it])
    if fruits_list[it] == "Grape":
        break
        print("After break statement")
    it += 1
else:
    print("Executed all elements in the list")


it = 0
while it < len(fruits_list):
    print(it)
    print(fruits_list[it])
    if fruits_list[it] == "Grape":
        it += 1
        continue
        print("After continue statement")
    it += 1
else:
    print("Executed all elements in the list")

it = 0
while it < len(fruits_list):
    print(it)
    print(fruits_list[it])
    if fruits_list[it] == "Grape":
        pass
        print("After pass keyword")
    it += 1
else:
    print("Executed all elements in the list")

it = 0
while it < len(fruits_list):
    print(it)
    print(fruits_list[it])
    if fruits_list[it] == "Grape":
        exit()
        print("After exit() method")
    it += 1
else:
    print("Executed all elements in the list")
print("Last index while looping", it)
