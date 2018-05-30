class ServerState:

    def build_application():
        pass

    def run_application():
        pass

class ServerStart(ServerState):

    def build_application(self):
        print("Build inprogress...")

    def run_application(self):
        print("Application is running...")

class ServerStop(ServerState):

    def build_application(self):
        print("Can't build app. Pls start your server!")

    def run_application(self):
        print("Can't run app. Pls start your server!")

class ServerBuild(ServerState):

    def build_application(self):
        print("Can't build app. Pls wait while building prev version...")

    def run_application(self):
        print("Application is running...")

class ServerRunApp(ServerState):

    def build_application(self):
        print("Build inprogress...")

    def run_application(self):
        print("Can't build app. Pls wait while running...")

class AwsServer:
    state = None

    def __init__(self):
        self.stop()

    def stop(self):
        self.state = ServerStop()

    def start(self):
        self.state = ServerStart()

    def build(self):
        self.state = ServerBuild()

    def run_app(self):
        self.state = ServerRunApp()

    def build_application(self):
        self.state.build_application()

    def run_application(self):
        self.state.run_application()

aws_server = AwsServer()
aws_server.build_application() # Can't build app. Pls start your server!
aws_server.start()
aws_server.build_application() # Build inprogress...
aws_server.build()
aws_server.build_application() # Can't build app. Pls wait while building prev version...
aws_server.run_app()
aws_server.build_application() # Build inprogress...
aws_server.run_application()   # Can't build app. Pls wait while running...

