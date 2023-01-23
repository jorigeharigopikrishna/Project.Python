name, isEmployee, employee_id = "Krishna", True, 123
fruits_list = ["Apple", "Banana", "Custard", "Grape", "Lemon"]
int_tuple = (1, 2, 3, 4, 5, 6)
details_dict = {"name": "Krishna", "house_no": 233, "employee": {"id": 143, "company": "abcd"}, "isEmployee": True}
veg_set = {"Potato", "Tomato", "Corn"}

if isEmployee:
    print("Is Employee")
else:
    print("Is not Employee")
if name == "Krishna":
    print("Krishna")
else:
    print("Not Krishna")
if employee_id > 100:
    print("Greater than 100")
else:
    print("Lesser than 100")
if "Grape" in fruits_list:
    print("Grape is in list")
else:
    print("Grape is not in list")
if 5 in int_tuple:
    print("5 is in tuple")
else:
    print("5 is not in tuple")
if "employee" in details_dict:
    print("Employee is in dictionary")
else:
    print("Employee is not in dictionary")
if "Tomato" in veg_set:
    print("Tomato in set")
else:
    print("Tomato is not in set")

num = 101
if num < 100:
    print("Number is less than 100")
elif 100 < num < 200:
    print("Number is between 100 and 200")
else:
    print("Number is greater than 200")
