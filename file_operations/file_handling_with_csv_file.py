import csv

csv_comma_file_object = open("sample_files/csv_file_using_comma.csv")
csv_reader = csv.reader(csv_comma_file_object)

csv_data_set = [
    ["Name", "Initial"],    # Column Headers
    ["ab", "cd"],           # Row 1
    ["ef", "gh"],           # Row 2
    ["ij", "kl"]            # Row 3
]

csv_dict_data_set = [
    {
        "Name":"ab", "Initial": "cd"
    },
    {
        "Name": "ef", "Initial": "gh"
    }
]
csv_dict_headers = ["Name", "Initial"]

with open("sample_files/csv_file_using_comma.csv") as csv_file:      # It opens the csv file in read mode
    csv_reader_rows = csv.reader(csv_file)        # reader() used to read contents of the csv file and returns lists of list
    for csv_row in csv_reader_rows:
        for csv_cell in csv_row:
            print(csv_cell)
print(csv_file.closed)      # True

with open("sample_files/csv_file_using_pipe.csv") as csv_file_pipe:      # It opens the csv file in read mode
    csv_reader_pipe_rows = csv.reader(csv_file_pipe, delimiter="|")      # reader() used to read contents of the csv file and returns lists of list
    for csv_row in csv_reader_pipe_rows:
        for csv_cell in csv_row:
            print(csv_cell)
print(csv_file_pipe.closed)      # True

with open("sample_files/csv_file_using_comma.csv") as csv_file_comma_1:      # It opens the csv file in read mode
    csv_dict_reader_rows = csv.DictReader(csv_file_comma_1)        # DictReader() used to read contents of the csv file and returns lists of dict
    for csv_dict_row in csv_dict_reader_rows:
        for csv_key in csv_dict_row:
            print(csv_dict_row)
            print(csv_dict_row[csv_key])
print(csv_file.closed)      # True

with open("sample_files/csv_file_using_pipe.csv") as csv_file_pipe_2:      # It opens the csv file in read mode
    csv_dict_reader_pipe_rows = csv.DictReader(csv_file_pipe_2, delimiter="|")        # DictReader() used to read contents of the csv file and returns lists of dict
    for csv_dict_row in csv_dict_reader_pipe_rows:
        for csv_key in csv_dict_row:
            print(csv_dict_row)
            print(csv_dict_row[csv_key])
print(csv_file_pipe.closed)      # True

with open("sample_files/csv_new_file_using_comma.csv", "w") as csv_new_file_comma_1:      # Create file if not found, otherwise open existing file in write mode
    csv_writer = csv.writer(csv_new_file_comma_1)        # writer() used to write contents to the csv file
    for csv_row_data in csv_data_set:
        csv_writer.writerow(csv_row_data)

with open("sample_files/csv_new_file_2_using_comma.csv", "w") as csv_new_file_comma_2:      # Create file if not found, otherwise open existing file in write mode
    csv_writer_2 = csv.writer(csv_new_file_comma_2)        # writer() used to write contents to the csv file
    csv_writer_2.writerows(csv_data_set)

with open("sample_files/csv_new_file_3_using_comma.csv", "w") as csv_new_file_comma_3:      # Create file if not found, otherwise open existing file in write mode
    csv_dict_writer = csv.DictWriter(csv_new_file_comma_3, fieldnames=csv_dict_headers)        # DictWriter() used to write contents to the csv file
    csv_dict_writer.writeheader()       # Setting headers
    for csv_row_data in csv_dict_data_set:
        csv_dict_writer.writerow(csv_row_data)

with open("sample_files/csv_new_file_4_using_comma.csv", "w") as csv_new_file_comma_4:      # Create file if not found, otherwise open existing file in write mode
    csv_dict_writer = csv.DictWriter(csv_new_file_comma_4, fieldnames=csv_dict_headers)        # DictWriter() used to write contents to the csv file
    csv_dict_writer.writeheader()       # Setting headers
    csv_dict_writer.writerows(csv_dict_data_set)

csv.register_dialect("pipe", delimiter="|")     # Registering delimiter of | as pipe

with open("sample_files/csv_file_using_pipe_1.csv") as csv_file_dialect_pipe:      # It opens the csv file in read mode
    csv_reader_pipe_rows = csv.reader(csv_file_dialect_pipe, dialect="pipe")       # Use of registered dialect to access content of csv file.
    for csv_row in csv_reader_pipe_rows:
        for csv_cell in csv_row:
            print(csv_cell)
print(csv_file_dialect_pipe.closed)      # True