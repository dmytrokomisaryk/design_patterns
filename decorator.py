import abc

class Title():

    def show():
        pass

class EmployeeTitle(Title):

    def show(self):
        return 'Python'

class TitleDecorator(abc.ABC, Title):
    title = ''

    def __init__(self, title):
        self.title = title

    @abc.abstractmethod
    def show():
        pass

class SeniorityDecorator(TitleDecorator):
    def show(self):
        return f'Senior {self.title.show()}'

class RoleDecorator(TitleDecorator):
    def show(self):
        return f'{self.title.show()} Engineer'

title = SeniorityDecorator(RoleDecorator(EmployeeTitle()))
print(title.show()) #Senior Python Engineer
