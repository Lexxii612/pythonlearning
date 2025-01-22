
class FileFunctions:
    fileName = "test"

    def __init__(self, fileName):
        self.fileName = fileName

    def read_file(self):
        with open(self.fileName) as file:
            content = file.read()
        return content

    def write_file(self, content, filemode):
        with open(self.fileName, mode=filemode) as file:
            file.write(content)

