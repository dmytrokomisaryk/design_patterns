import abc

class Project:

    def gather_requirements(self):
        print('Gather requirements')

    def start_sprint(self):
        print('Start sprint')

    def deliver_release(self):
        print('Deliver release')

class AbstractCommand(abc.ABC):
    project = None

    def __init__(self, project):
        self.project = project

    @abc.abstractmethod
    def perform():
        pass

class GatherRequirements(AbstractCommand):

    def perform(self):
        self.project.gather_requirements()

class StartSprint(AbstractCommand):

    def perform(self):
        self.project.start_sprint()

class DeliverRelease(AbstractCommand):

    def perform(self):
        self.project.deliver_release()

class ProjectManager:
    gather_requirements = None
    start_sprint = None
    deliver_release = None

    def __init__(self, gr, ss, dr):
        self.gather_requirements = gr
        self.start_sprint = ss
        self.deliver_release = dr

    def gather_project_requirements(self):
        self.gather_requirements.perform()

    def start_project_sprint(self):
        self.start_sprint.perform()

    def deliver_project_release(self):
        self.deliver_release.perform()

project = Project()

project_manager = ProjectManager(GatherRequirements(project),StartSprint(project),DeliverRelease(project))
project_manager.gather_project_requirements() #Gather requirements
project_manager.start_project_sprint() #Start sprint
project_manager.deliver_project_release() #Deliver release

