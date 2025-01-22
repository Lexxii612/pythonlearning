from login import Login

class User:
    __user_name=""
    __password=""
    __is_authenticated=False

    def __init__(self, userName, password):
        self.__user_name = userName
        self.__password = password
        self.__is_authenticated = False

    def create_user(self):
        self.__prompt_user()
        login = Login()
        is_successful = login.create_user(self.__user_name, self.__password)
        return is_successful

    def is_authenticated(self):
        return self.__is_authenticated
    
    def authenticate_user(self):
        self.__prompt_user()
        login = Login()
        self.__is_authenticated = login.authenticate_user(self.__user_name, self.__password)
        return self.__is_authenticated

    def __prompt_user(self):
        self.__user_name = input("Enter username: \n")
        password = input("Enter password: \n")
        #need to encrypt password

