
class TaskItem:
    PENDING = 1
    COMPLETED = 2

    id = 0
    description = ''
    status = PENDING

    def __init__(self, my_id, my_description):
        self.id = my_id
        self.description = my_description
        self.status = self.PENDING


class TaskList:

    task_list = {}

    def __init__(self, name):
        self.name = name