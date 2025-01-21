#add Expense
#view Expenses
#Track Budget
#Save Expenses
#Exit

from budget import Budget
from fileFunctions import FileFunctions

class MenuItem:



    def __init__(self, name):
        self.name = name

class Menu:

    is_active= True
    user_selection = 0
    my_budget = Budget("my expenses")
    my_file = FileFunctions("budget")

    def __init__(self):
        file = self.my_file.load_file()
        # budget from file
        #my_budget = self.my_file.load_file()

    def display_menu(self):
        print("1 Add Expense")
        print("2 View Expense")
        print("3 Track Expense")
        print("4 Save Expense")
        print("5 Exit")
        print("\n")
        self.user_selection = int(input("Select from the above options: \n"))
        self.invoke_option()


    def invoke_option(self):

        if self.user_selection == 5:
            self.is_active = False
        elif self.user_selection == 1:
            self.my_budget.add_item()
            self.display_menu()
        elif self.user_selection == 2:
            self.my_budget.view_budget()
            self.display_menu()
        elif self.user_selection == 3:
            self.my_budget.set_budget()
            self.display_menu()
        elif self.user_selection == 4:
            self.my_file.save_file(self.my_budget)
            self.display_menu()
        else:
            self.display_menu()