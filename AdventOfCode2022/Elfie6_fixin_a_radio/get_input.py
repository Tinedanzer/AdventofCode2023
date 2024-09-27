def get_input(file_name: str):
    with open(file_name, "r") as in_file:
        input_list = in_file.read().split("\n")
    return input_list