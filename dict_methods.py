empty_dict = {}
nested_dict = {"name": "Krishna", "house_no": 233, "employee": {"id": 143, "company": "abcd"}, "isEmployee": True}

get_dict_name_key = nested_dict["name"]
get_dict_company_key = nested_dict.get("employee").get("company")
nested_dict["name"] = "Gopi"
dict_keys = nested_dict.keys()
dict_values = nested_dict.values()
dict_items = nested_dict.items()
nested_dict["city"] = "City"
