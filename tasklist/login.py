from filefunctions import FileFunctions

class Login:
    filename = "users.csv"
    userdata = []

    def __init__(self):
        self.load_file()

    def check_username(self, username):
        retval = False
        for row in self.userdata:
            if row[0].lower() == username.lower():
                retval = True
                break

        return retval

    def create_user(self, userName, password):
        if self.check_username(userName) == False:
            myfile = FileFunctions(self.filename)
            myfile.write_file(f"{userName},{password}\n", "a")
 
    def authenticate_user(self, userName, password):
        self.load_file()
        if len(self.userdata) > 0:
            for sublist in self.userdata:
                if sublist[0].lower() == userName.lower() and sublist[1] == password:
                    return True
        return False

    def load_file(self):
        myfile = FileFunctions(self.filename)
        self.userdata = myfile.read_csv()




