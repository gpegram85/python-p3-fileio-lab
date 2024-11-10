def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode="w", encoding='UTF-8') as example_file:
        example_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode="a", encoding='UTF-8') as example_file:
        example_file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', mode="r", encoding='UTF-8') as example_file:
        return example_file.read()
