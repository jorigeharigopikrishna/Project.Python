empty_set = set()
number_set_1 = {1, 2, 3, 4, 5}
number_set_2 = {4, 5, 6, 7, 8}
veg_set = {"Potato", "Tomato", "Corn"}

veg_set.add("Carrot")
veg_set.discard("Carrot")
union_set = number_set_1.union(number_set_2)
intersection_set = number_set_1.intersection(number_set_2)
difference_set = number_set_1.difference(number_set_2)
number_set_1.intersection_update(number_set_2)
number_set_2.difference_update(number_set_1)
