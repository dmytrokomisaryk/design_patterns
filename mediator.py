import abc

class User(abc.ABC):
    chat = ''
    name = ''

    def __init__(self, chat, name):
        self.chat = chat
        self.name = name

    def send_message(self, message):
        self.chat.send_message(message, self)

    @abc.abstractmethod
    def get_message(self, message, user):
        pass

class Admin(User):

    def get_message(self, message, user):
        print(f'Admin {self.name} receive: {message} from: {user.name}')

class Participant(User):

    def get_message(self, message, user):
        print(f'User {self.name} receive: {message} from: {user.name}')

class Chat(abc.ABC):

    @abc.abstractmethod
    def send_message(self, message, user):
        pass

class TextChat(Chat):
    admin = ''
    users = []

    def set_admin(self, admin):
        self.admin = admin

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, author):
        for user in self.users:
            if user != author: user.get_message(message, author)
        self.admin.get_message(message, author)

chat = TextChat()

admin = Admin(chat, 'Joe')
john = Participant(chat, 'John')
judy = Participant(chat, 'Judy')

chat.set_admin(admin)
chat.add_user(john)
chat.add_user(judy)

john.send_message('Hello world!')

# console output
# User Judy receive: Hello world! from: John
# Admin Joe receive: Hello world! from: John
