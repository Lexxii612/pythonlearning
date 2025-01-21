import datetime as dt


class BudgetItem:
    id = 0
    #is_credit = False
    amount = 0.00
    date = dt.datetime.now().date()
    category = ''
    description = ''

    def __init__(self, my_id, my_date, my_amount, my_category, my_description):
        self.id = my_id
        #self.is_credit = is_credit
        if len(my_date) > 0:
            self.date = my_date
        self.amount = my_amount
        self.category = my_category
        self.description = my_description


    def print_item(self):
        if self.amount != 0.0 and len(self.category) and len(self.description):
            print(f"{self.date}     {self.category}     ${"{:.2f}".format(self.amount)}      {self.description}")



class Budget:
    name = ""
    budget_items = {}
    total_debit = 0.0
    total_credit = 0.0


    def __init__(self, name):
        self.name = name

    def add_item(self):
        date = input("Enter expense date format 'YYYY-MM-DD': (if skipped today will be used) \n")
        category = input("Enter category: \n")
        amount = float(input("Enter amount: \n"))
        description= input("Enter description: \n")
        #need key but for now this will allow for testing
        new_item = BudgetItem(self.get_budget_item_id(), date, amount, category, description)
        self.budget_items[new_item.id] = new_item

        if self.get_budget_items_total() > self.total_credit:
            print("You are at your budget total for the month. \n")


    def get_budget_item_id(self):
        next_id = 0
        if len(self.budget_items.keys()):
            next_id = max(self.budget_items.keys())+1
        return next_id

    def get_budget_items_total(self):
        total = 0.0
        for key in self.budget_items:
            total += self.budget_items[key].amount

        return total

    #def remove_item(self):
    #    pass

    def load_budget(self):
        pass

    def view_budget(self):
        print(f"Date        Category    Amount  Description")
        for key in self.budget_items:
            self.budget_items[key].print_item()
        print("\n")

    def set_budget(self):
        my_budget_amount = float(input("Enter your budget amount: \n"))
        self.total_credit = my_budget_amount

    def get_budget(self):
        print(f"Budget is currently set at {self.total_credit}.")
        print("\n")

    def check_budget(self):
        pass