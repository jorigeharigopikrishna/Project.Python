import argparse     # Importing argparse module

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--name", required=True, help="Mandatory Command Line Argument")
argument_parser.add_argument("--city", required=False, help="Optional Command Line Argument")

# Cmd command 1 - python use_of_cmd_line_arguments.py
# Cmd command 2 - python use_of_cmd_line_arguments.py --name "Gopi"
# Cmd command 3 - python use_of_cmd_line_arguments.py --name "Gopi" --city "Hyd"
# Cmd command 4 - python use_of_cmd_line_arguments.py --name "Gopi" --city "Hyd" 23
argument_dict = vars(argument_parser.parse_args())      # Use of vars() to convert object to dict
print(argument_dict)        # Cmd command 1 - Prints error as --name is required
                            # Cmd command 2 - Prints {"name": "Gopi", "city": None}
                            # Cmd command 3 - Prints {"name": "Gopi", "city": "Hyd"}
                            # Cmd command 4 - Prints error as unrecognized arguments : 23
