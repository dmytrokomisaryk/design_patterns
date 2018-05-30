class PullRequest: #observer
    pr_version = ''
    author = ''
    reviewers = []

    def add_commit(self, pr_version, author):
        self.pr_version = pr_version
        self.author = author
        self.notify_reviewers()

    def add_reviewer(self, reviewer):
        self.reviewers.append(reviewer)

    def notify_reviewers(self):
        for reviewer in self.reviewers:
            reviewer.handle_event(self.pr_version, self.author)

class ProjectMember: #subscriber

    def handle_event(self, pr_version, author):
        print(f'{author} add commit <a href="github.com/{pr_version}">{pr_version}</a> to PR#1 pls review')

teamlead = ProjectMember()
senior_dev = ProjectMember()

pull_request = PullRequest()
pull_request.add_reviewer(teamlead)
pull_request.add_reviewer(senior_dev)
pull_request.add_commit('asqf12a', 'John Smith') # teamlead should receive notification about new commit

# console output
# John Smith added commit <a href="github.com/asqf12a">asqf12a</a> to PR#1 pls review
# John Smith added commit <a href="github.com/asqf12a">asqf12a</a> to PR#1 pls review

