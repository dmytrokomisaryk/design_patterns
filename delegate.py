class Engineer:

    def implement(self):
        print('Task has been done')

    def invistigate(self):
        print('Investigation has been done')

class TemaLead:

    def __init__(self):
        self.team_member = Engineer()

    def implement(self):
        return self.team_member.implement()

    def invistigate(self):
        return self.team_member.invistigate()

team_lead = TemaLead()
team_lead.implement()
team_lead.invistigate()

