import os

def save_to_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)