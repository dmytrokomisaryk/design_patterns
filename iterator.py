class JiraTicket:

    def __init__(self, title, issue_type):
        self.title = title
        self.issue_type = issue_type

    def __str__(self):
        return f'title: {self.title}, issue_type: {self.issue_type}'

class TaskIterator:

    def __init__(self, jira_tickets):
        self.index = 0
        self.jira_tickets = jira_tickets

    def has_next(self):
        return self.index < len(self.jira_tickets)

    def next(self):
        task = self.jira_tickets[self.index]
        self.index += 1
        return task

class Developer:

    def __init__(self):
        self.jira_tickets = []

    def assign_ticket(self, ticket):
        self.jira_tickets.append(ticket)

    def iterator(self):
        return TaskIterator(self.jira_tickets)

setup_server = JiraTicket('Configure apache', 'tech_task')
login_page = JiraTicket('login page', 'story')
payment_system = JiraTicket('Payment system', 'spike')

software_engineer = Developer()
software_engineer.assign_ticket(setup_server)
software_engineer.assign_ticket(login_page)
software_engineer.assign_ticket(payment_system)

iterator = software_engineer.iterator()

while iterator.has_next():
    print(iterator.next())

# in console tasks will be iterated
# title: Configure apache, issue_type: tech_task
# title: login page, issue_type: story
# title: Payment system, issue_type: spike

