txt_file_object = open("sample_files/text_file_1.txt")
file_data = txt_file_object.read()      # Read entire contents of the file
cursor_pointer = txt_file_object.tell()     # Returns current cursor pointer location
move_cursor_pointer = txt_file_object.seek(10)      # Sets the current cursor location to 10 from start
file_data_5 = txt_file_object.read(5)       # Read 5 bytes from current cursor location
file_line_from_15 = txt_file_object.readline()   # Read entire line from cursor pointer 15
file_lines_from_40 = txt_file_object.readlines()   # Read entire lines from cursor pointer 40
txt_file_object.close()     # Used to close the file that is opened
path_of_file = txt_file_object.name     # Used to return the path of the file
mode_of_file = txt_file_object.mode     # used to return the mode of the file

with open("sample_files/text_file_1.txt") as file:      # It opens the file in read mode
    file_lines = file.readlines()
    for line in file_lines:
        print(line)
print(file.closed)      # True

with open("sample_files/text_file_2.txt", "w") as file_write:   # Create file if not found, otherwise open existing file in write mode
    file_write.write("New file\n")      # It starts replacing original content with new content
    file_write.writelines(["This is a new file 3\n", "Next line\n"])    # It appends with above content
    file_write.write("New file 3\n")    # It appends with above content

with open("sample_files/text_file_2.txt", "w") as file_write_2:
    file_write_2.write("New file replace\n")    # It replace entire contents of the file that we added before

with open("sample_files/text_file_3.txt", "a") as file_append:
    file_append.write("New content 3\n")    # It appends new content to end of the file

with open("sample_files/text_file_3.txt", "a") as file_append_2:
    file_append_2.write("Append to the end New content 3\n")    # It appends new content to end of the file

with open("sample_files/text_file_4.txt", "r+") as file_read_and_write: # Open existing file in read and write mode
    file_read_and_write.write("Start writing\n")
    file_read_and_write.writelines(["This is a existing file 4\n", "Next line\n"])    # It appends with above content
    for line in file_read_and_write:
        print(line)

with open("sample_files/text_file_4.txt", "r+") as file_read_and_write_2:   # Open existing file in read and write mode
    file_read_and_write_2.write("Top of the file\n")
    for line in file_read_and_write_2:
        print(line)

with open("sample_files/text_file_5.txt", "a+") as file_read_and_append: # Create file if not found, otherwise open existing file in read and append mode
    file_read_and_append.write("Start writing 5\n")
    file_read_and_append.writelines(["This is a new file 5\n", "Next line\n"])
    for line in file_read_and_append:
        print(line)

with open("sample_files/text_file_5.txt", "a+") as file_read_and_append_2: # Create file if not found, otherwise open existing file in read and append mode
    file_read_and_append_2.write("End of the file\n")
    for line in file_read_and_append_2:
        print(line)
