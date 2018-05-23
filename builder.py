import abc

class Task:
    title = ''
    description = ''
    estimate = 0

    def set_title(self, txt):
        self.title = txt

    def set_description(self, txt):
        self.description = txt

    def set_estimate(self, hours):
        self.estimate = hours

# Abstract class
class TaskBuilder(abc.ABC):
    task = ''

    def create_task(self):
        self.task = Task()

    @abc.abstractmethod
    def addTitle():
        pass

    @abc.abstractmethod
    def addDescription():
        pass

    @abc.abstractmethod
    def addEstimate():
        pass

    def get_task(self):
        return self.task

# builders
class TechTaskBuilder(TaskBuilder):

    def addTitle(self):
        self.task.set_title('Implement login loader')

    def addDescription(self):
        self.task.set_description('User should have ability to login via Facebook')

    def addEstimate(self):
        self.task.set_estimate(16)

class BugBuilder(TaskBuilder):

    def addTitle(self):
        self.task.set_title('Fix login loader')

    def addDescription(self):
        self.task.set_description('Loader keeps spinning after click logn button')

    def addEstimate(self):
        self.task.set_estimate(16)

class TaskCreator:
    task_builder = ''

    def set_builder(self, builder):
        self.task_builder = builder

    def build_task(self):
        self.task_builder.create_task()
        self.task_builder.addTitle()
        self.task_builder.addDescription()
        self.task_builder.addEstimate()
        return self.task_builder.get_task()

task_creator = TaskCreator()
task_creator.set_builder(TechTaskBuilder()) # .set_builder(BugBuilder())
task = task_creator.build_task()

print(f'{task.title}, {task.description}, {task.estimate}')