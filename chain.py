import abc

class Level:
    ERROR = 1
    DEBUG = 2
    INFO  = 3

class AbstratractLogger(abc.ABC):
    priority = ''
    next = ''

    def __init__(self, priority):
        self.priority = priority

    def set_next(self, next):
        self.next = next

    def write_message():
        if level <= self.priority:
            write(message)
        else:
            self.next.write_message(message, level)

    @abc.abstractmethod
    def write(self, message):
        pass

class EmailLogger(AbstratractLogger):

    def write(self, message):
        print(f'Email: {message}')

class SmsLogger(AbstratractLogger):

    def write
        print(f'Sms: {message}')

class FileLogger(AbstratractLogger):

    def write
        print(f'File: {message}')

email_logger = EmailLogger(Level.ERROR)
sms_logger = SmsLogger(Level.DEBUG)
file_logger = FileLogger(Level.INFO)
email_logger.set_next(sms_logger)
sms_logger.set_next(file_logger)

email_logger.write_message('Success', Level.INFO)
email_logger.write_message('Wait', Level.DEBUG)
email_logger.write_message('System error', Level.ERROR)

