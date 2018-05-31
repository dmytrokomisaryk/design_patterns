import abc

class WebSite(abc.ABC):

    @abc.abstractmethod
    def accept(self, visitor):
        pass

class Ebay(WebSite):

    def accept(self, visitor):
        visitor.visit(self)

class StackOverflow(WebSite):

    def accept(self, visitor):
        visitor.visit(self)

class Visitor:

    @abc.abstractmethod
    def visit(self, web_site):
        pass

class User(Visitor):

    def visit(self, web_site):
        print(f'Browsing {web_site.__class__.__name__}...')

class Hacker(Visitor):

    def visit(self, web_site):
        print(f'Hack {web_site.__class__.__name__}...')

hacker = Hacker()
user = User()

ebay = Ebay()
ebay.accept(hacker) # Hack Ebay...

stack_overflow = StackOverflow()
stack_overflow.accept(user) # Browsing StackOverflow...

