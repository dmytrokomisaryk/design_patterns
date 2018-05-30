class DevBranch:
    version = 0
    author = ''

    def commit(self, version, author):
        self.version = version
        self.author = author

    def pull(self, push):
        self.version = push.version
        self.author = push.author

    def push(self):
        return Push(self.version, self.author)

    def __str__(self):
        return f'version: {self.version}, author: {self.author}'

class Push:
    version = ''
    author = ''

    def __init__(self, version, author):
        self.version = version
        self.author = author

    @property
    def version(self):
        return self._version

    @property
    def author(self):
        return self._author

    @version.setter
    def version(self, version):
        self._version = version

    @author.setter
    def author(self, author):
        self._author = author

class Git:
    push = ''

    def set_commit(self, push):
        self.push = push

    def get_commit(self):
        return self.push

branch = DevBranch()
branch.commit(1, 'John Smith')
print(branch)  #version: 1, author: John Smith

git = Git()
git.set_commit(branch.push())

branch.commit(2, 'John Smith')
print(branch) #version: 2, author: John Smith

#revert to previos version
branch.pull(git.get_commit())
print(branch) #version: 1, author: John Smith
