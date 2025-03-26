from filefunctions import FileFunctions

class Login:
    filename = "users.csv"
    userdata = []

    def __init__(self):
        self.load_file()

    def check_username(self, username):
        retval = False
        #self.load_file()
        for row in self.userdata:
            if row[0].lower() == username:
                retval = True
                break

        return retval

    def create_user(self, userName, password):
        if self.check_username(userName) == True:
            myfile = FileFunctions(self.filename)
            myfile.write_file(f"{userName},{password}\n", "a")
 
    def authenticate_user(self, userName, password):
        retval = False
        if len(self.userdata) > 0:
            check = self.userdata[userName]
            if check[1] == password:
                retval = True
        return retval

    def load_file(self):
        myfile = FileFunctions(self.filename)
        self.userdata = myfile.read_csv()



