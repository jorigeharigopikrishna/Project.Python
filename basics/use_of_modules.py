import math     # Importing math module
import os     # Importing os module
import random as rand   # Importing random module
import datetime # Importing datetime module
from datetime import date   # Import only date file
from datetime import time   # Import only time file
import copy

print(help("modules"))  # Prints all modules installed

fruits_list = ["Apple", "Banana", "Custard", "Grape", "Lemon"]

# Using math module
pi_value = math.pi  # 3.1415
e_value = math.e  # 2.718
ceiled_value = math.ceil(8.1)   # 9
floor_value = math.floor(8.1)   # 8
power_of = math.pow(4, 2)   # 16
sqrt_value = math.sqrt(24)      # 4.8989
factorial_value = math.factorial(6)      # 720

# Using os module
cwd_path = os.getcwd()      # Return \Python\Project.Python\basics\use_of_modules.py
current_env_variables = os.environ  # Returns environment variables
current_system_user = os.environ["USERNAME"]    # Returns current user
list_directories = os.listdir()     # Return list of files and directories in current folder

# Using random module
random_num_without_range = rand.random()    # Random decimal between 0 and 1
random_num_with_range = rand.randint(1, 10)     # Random integer between 1 and 10
random_fruit = rand.choice(fruits_list)     # Random element from the list

# Using datetime module
today_date = date.today()   # 2023-01-26
current_date_and_time = datetime.datetime.now()     # 2023-01-26 23:56:55.842

# Using copy module
shallow_copy = copy.copy([1, 2, 3])
deep_copy = copy.deepcopy([1, 2, 3])