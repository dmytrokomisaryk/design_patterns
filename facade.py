class TeamLead:

    def prepare_team(self):
        print('Team is ready.')

    def get_user_stories(self):
        print('Tasks assigned to engineers.')

    def finish_sprint(self):
        print('All tasks are successfully done!')

class Customer:

    def provide_details(self):
        print('Details has been sent.')

    def provide_priorities(self):
        print('Stories are ready for development.')

    def test_release(self):
        print('Release is success!')

# Facade
class ProjectManager:

    def __init__(self):
        self.team_lead = TeamLead()
        self.customer = Customer()

    def start_project(self):
        self.team_lead.prepare_team()
        self.customer.provide_details()

    def start_sprint(self):
        self.customer.provide_priorities()
        self.team_lead.get_user_stories()

    def deliver_release(self):
        self.team_lead.finish_sprint()
        self.customer.test_release()

project_manager = ProjectManager()
project_manager.start_project() # Team is ready. \n Details has been sent.
project_manager.start_sprint() # Stories are ready for development. \n asks assigned to engineers.
project_manager.deliver_release() # All tasks are successfully done! \n Release is success!

