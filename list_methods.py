fruits_list = ["Apple", "Banana", "Custard", "Grape", "Lemon"]

element_1 = fruits_list[1]
print(element_1)
fruits_list[1] = "Berry"
print(fruits_list[1])
fruits_list.append("Mango")
print(fruits_list)
fruits_list.insert(3, "Dragon Fruit")
print(fruits_list)
fruits_list.extend(["Papaya", "Strawberry"])
print(fruits_list)
lemon_index = fruits_list.index("Lemon")
print(lemon_index)
fruits_list.remove("Papaya")
print(fruits_list)
element_minus5 = fruits_list[-5]
print(element_minus5)
