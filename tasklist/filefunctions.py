import csv
import os
class FileFunctions:
    fileName = "test.txt"

    def __init__(self, fileName):
        self.fileName = fileName

    def read_file(self):
        if os.path.exists(self.fileName):
            with open(self.fileName) as file:
                content = file.read()
            return content
        else:
            return []
    
    def read_csv(self):
        retVal = []
        if os.path.exists(self.fileName):
            with open(self.fileName) as file:
                data = csv.reader(file)
                for row in data:
                    retVal.append(row)
                    
        return retVal


    def write_file(self, content, filemode):
        #if os.path.exists(self.fileName):
        #create file?
        with open(self.fileName, mode=filemode) as file:
            file.write(content)

