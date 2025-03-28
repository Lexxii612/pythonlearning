
from filefunctions import FileFunctions

class TaskItem:
    PENDING = 1
    COMPLETED = 2

    id = 0
    description = ''
    status = PENDING
    user_name = ''

    def __init__(self, my_id, my_description, user_name):
        self.id = my_id
        self.description = my_description
        self.status = self.PENDING
        self.user_name = user_name

    def print_item(self):
        print(f"{self.id}   {self.status}   {self.description}")
    
    def csv_row(self):
        return self.id + ',' + self.status + ',' + self.description + ',' + self.user_name


class TaskList:

    __task_list = {}

    def __init__(self, name):
        self.name = name
        self.load_file()
    
    def add_item(self, user_name):
        task_name = input("Enter Task: \n") 
        task = TaskItem(self.get_task_item_id(), task_name, user_name)
        self.__task_list[task.id] = task
        print(self.__task_list)

    def view_tasks(self, user_name):
        print("\nId Status  Task")
        for key in self.__task_list:
            if (self.__task_list[key].user_name.lower() == user_name.lower()):
                self.__task_list[key].print_item()
    
    def mark_task_complete(self, user_name):
        id = input("Enter Id of completed task: \n") 
        if (id in self.__task_list) and self.__task_list[id].user_name == user_name:
            self.__task_list[id].status = TaskItem.COMPLETED
            print(self.__task_list)
    
    def delete_task(self, id, user_name):
        if ((id in self.__task_list) and self.__task_list[id].user_name == user_name):
            deleted_item = self.__task_list.pop(id)
            print(f"\"{deleted_item.id} {deleted_item.description}\" was deleted")
            print(self.__task_list)

    def save_list(self):
        myfile = FileFunctions(self.filename)
        content = ''
        for key in self.__task_list:
            content = content + (self.__task_list[key].csv_row()) + '\n'
        
        myfile.write_file(content, "w")


    def load_file(self):
        myfile = FileFunctions(self.filename)
        self.userdata = myfile.read_csv()

    def get_task_item_id(self):
        next_id = 0
        if len(self.__task_list.keys()):
            next_id = max(self.__task_list.keys())+1
        return next_id
    

        