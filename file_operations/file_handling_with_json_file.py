import json

json_string = """{"role":"sdet", "company":"ab"}"""
json_dict_from_json_string = json.loads(json_string)    # loads() converts string to dict
print(json_dict_from_json_string)

json_dict = {"role": "sdet", "company": "mnc"}
json_string_from_json_dict = json.dumps(json_dict)      # dumps() converts dict to string
print(json_string_from_json_dict)

json_dict_job = {"job-role": "sdet", "job-company": "mnc"}
json_string_from_json_dict_job = json.dumps(json_dict_job)      # dumps() converts dict to string
print(json_string_from_json_dict_job)

json_file_object = open("sample_files/json_file_1.json")
json_data_on_file = json.load(json_file_object)
print(json_data_on_file)

with open("sample_files/json_file_1.json") as json_file:      # It opens the json file in read mode
    json_data = json.load(json_file)        # load() used to read contents of the json file
    for key in json_data:
        print(json_data[key])
print(json_file.closed)      # True

with open("sample_files/json_file_2.json", "w") as json_file_write:   # Create file if not found, otherwise open existing file in write mode
    json_file_write.write(json_string_from_json_dict)   # write() accepts json_string and it replaces json data to the file.

with open("sample_files/json_file_2.json", "w") as json_file_write_2:   # Create file if not found, otherwise open existing file in write mode
    json.dump(json_dict_job, json_file_write_2)   # dump() used to write contents to the json file and it eplaces json data to the file.

with open("sample_files/json_file_3.json", "a") as json_file_append:   # Create file if not found, otherwise open existing file in write mode
    json_file_append.write(json_string_from_json_dict)      # write() accepts json_string and it appends json data to the file.

with open("sample_files/json_file_3.json", "a") as json_file_append_2:   # Create file if not found, otherwise open existing file in write mode
    json.dump(json_dict_job, json_file_append_2)   # dump() used to write contents to json file and it appends json data to the file.
