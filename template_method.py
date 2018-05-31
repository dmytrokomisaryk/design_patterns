class Engineer:

    def show_details(self): #template method
        print('Senior Software Engineer')
        print(f'Primary skill: {self.primary_skill()}')
        print('Script Solutions')

class PythonEngineer(Engineer):

    def primary_skill(self):
        return 'python'

class RubyEngineer(Engineer):

    def primary_skill(self):
        return 'ruby'

python_engineer = PythonEngineer()
python_engineer.show_details()
# Senior Software Engineer
# Primary skill: python
# Script Solutions

ruby_engineer = RubyEngineer()
ruby_engineer.show_details()
# Senior Software Engineer
# Primary skill: ruby
# Script Solutions