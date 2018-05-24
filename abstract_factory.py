import abc

# Abstract Factory
class AbstractEngineersFactory(abc.ABC):

    @abc.abstractmethod
    def add_primary_skill(self):
        pass

    @abc.abstractmethod
    def add_tools(self):
        pass

    def self_present(self):
        print(f'Primary skill is {self.primary_skill.to_show()}. Tools are {self.tools.to_show()}.')

# Interfaces
class AbstractPrimarySkill(abc.ABC):

    @abc.abstractmethod
    def to_show(self):
        pass

class AbstractTools(abc.ABC):

    @abc.abstractmethod
    def to_show(self):
        pass

# Concrete classes
class PythonSkill(AbstractPrimarySkill):

    def to_show(self):
        return 'Python'

class PythonTools(AbstractTools):

    def to_show(self):
        return 'Sublime, BitBucket, PyLint'

class RubySkill(AbstractPrimarySkill):

    def to_show(self):
        return 'Ruby'

class RubyTools(AbstractTools):

    def to_show(self):
        return 'RubyMine, Git, RuboCop'

# Concrete Factories
class PythonEngineerFactory(AbstractEngineersFactory):

    def add_primary_skill(self):
        self.primary_skill = PythonSkill()

    def add_tools(self):
        self.tools = PythonTools()

class RubyEngineerFactory(AbstractEngineersFactory):

    def add_primary_skill(self):
        self.primary_skill = RubySkill()

    def add_tools(self):
        self.tools = RubyTools()

engineer = PythonEngineerFactory() # RubyEngineerFactory()

# main logic will not be changed
engineer.add_primary_skill()
engineer.add_tools()
engineer.self_present()

