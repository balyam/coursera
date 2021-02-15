import tempfile
import os
from random import choice
from string import digits


class File:

    TEMP_PATH = tempfile.gettempdir()

    def __init__(self, path_to_file):
        if not os.path.isfile(path_to_file):
            with open(path_to_file, 'w') as f:
                f.write("")
        # else:
        #     with open(path_to_file, 'r') as f:
        #         f.read()

    def __add__(self, file):
        file_name = ''.join(choice(digits) for i in range(5))
        new_file = type(self)(os.path.join(self.TEMP_PATH, file_name))
        new_file.write(self.read)
        new_file.write(file)
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __str__(self):
        return f"{os.path.abspath(self)}"

    def read(self):
        with open(self, 'r') as f:
            return f.read()

    def write(self, value_string):
        with open(self, 'a') as f:
            f.write(value_string)
