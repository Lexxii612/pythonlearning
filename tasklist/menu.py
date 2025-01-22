#add Expense
#view Expenses
#Track Budget
#Save Expenses
#Exit
from tasklist import TaskList
from filefunctions import FileFunctions
from user import User


class Menu:

    is_active= True
    user_selection = 0
    my_taskList = TaskList("my expenses")
    my_file = FileFunctions("tasks")
    my_user = User("", "")


    def __init__(self):
        #file = self.my_file.load_file()
        # budget from file
        #my_budget = self.my_file.load_file()
        pass

    def display_menu(self):
        if self.my_user.is_authenticated():
            print("1 Add a Task")
            print("2 View Tasks")
            print("3 Mark a Task as Completed")
            print("4 Delete a Task")
            print("5 Exit")
            print("\n")
        else:
            print("1 Log in")
            print("2 Register User")
            print("\n")
            
        self.user_selection = int(input("Select from the above options: \n"))
        self.invoke_option()


    def invoke_option(self):

        if not self.my_user.is_authenticated() and self.user_selection == 1:
             self.my_user.create_user()
        elif not self.my_user.is_authenticated() and self.user_selection ==2:
             self.my_user.authenticate_user()
        elif self.my_user.is_authenticated() and self.user_selection == 5:
            self.is_active = False
        elif self.my_user.is_authenticated() and self.user_selection == 1:
            self.my_taskList.add_item()
        elif self.my_user.is_authenticated() and self.user_selection == 2:
            self.my_taskList.view_budget()
        elif self.my_user.is_authenticated() and self.user_selection == 3:
            self.my_taskList.set_budget()
        elif self.my_user.is_authenticated() and self.user_selection == 4:
            self.my_file.save_file(self.my_taskList)
        else:
            self.display_menu()

        if self.is_active:
            self.display_menu()