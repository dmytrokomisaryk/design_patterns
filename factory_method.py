# interface
class Task:

    def title(self):
        pass

class DevelopmentTask(Task):

    def title(self):
        print('Tech task')

class TestingTask(Task):

    def title(self):
        print('QA task')

class TaskCreator:

    # factory method
    def create_task(self):
        pass

class DevelopmentTaskCreator(TaskCreator):

    def create_task(self):
        return DevelopmentTask()

class TestingTaskCreator(TaskCreator):

    def create_task(self):
        return TestingTask()

task_creator = DevelopmentTaskCreator() # or TestingTaskCreator()

# main logic will not be chaged
task = task_creator.create_task()
task.title() # Tech task

