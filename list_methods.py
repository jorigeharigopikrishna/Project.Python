fruits_list = ["Apple", "Banana", "Custard", "Grape", "Lemon"]
nested_list = [
    ["HTML", "CSS", "Javascript"],
    ["Angular", "React"],
    ["C", "C++", "C#", "Java", "Python"],
    ["ML", "AI", "Data Science"]
]

element_1 = fruits_list[1]
fruits_list[1] = "Berry"
fruits_list.append("Mango")
fruits_list.insert(3, "Dragon Fruit")
fruits_list.extend(["Papaya", "Strawberry"])
lemon_index = fruits_list.index("Lemon")
fruits_list.remove("Papaya")
element_minus5 = fruits_list[-5]
print(fruits_list)
reverse_list = fruits_list[::-1]
list_1_3_5 = fruits_list[1:6:2]
print(list_1_3_5)
list_reverse_5_7 = fruits_list[-4::2]
print(list_reverse_5_7)