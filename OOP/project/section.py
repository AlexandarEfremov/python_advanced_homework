from OOP.project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        if task_name in self.tasks:
            Task.completed = True
            return f"Completed task {self.name}"
        return f"Could not find task with the name {self.name}"

    def clean_section(self):
        len_clear = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {len_clear} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for comment in self.comments:


        return
