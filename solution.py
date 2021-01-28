class FileReader:

    def __init__(self, path_to_file):
        self.path = path_to_file

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except FileNotFoundError as e:
            return ""


if __name__ == '__main__':
    pass