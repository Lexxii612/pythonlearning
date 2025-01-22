class User:
    __user_name=""
    __password=""
    __is_authenticated=False

    def __init__(self, userName, password):
        self.__user_name = userName
        self.__password = password
        self.__is_authenticated = False

    def create_user(self, userName, password):
        return False

    def is_authenticated(self):
        return self.__is_authenticated
    
    def authenticate_user(self):
        pass

