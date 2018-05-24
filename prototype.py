class Cloneable:

    def clone():
        pass

class Server(Cloneable):
    os = ''
    cpu = ''
    ram = ''
    hdd = ''

    def __init__(self, os, cpu, ram, hdd):
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def clone(self):
        server = Server(self.os, self.cpu, self.ram, self.hdd)
        return server

server = Server('Linux', 'x4', 16, 500)
print(f'{server.os}, {server.cpu}, {server.ram}, {server.hdd}')

server_clone = server.clone()
print(f'{server_clone.os}, {server_clone.cpu}, {server_clone.ram}, {server_clone.hdd}')

# to use with factory
class ServerFactory:
    server = ''

    def __init__(self, server):
        self.set_prototype(server)

    def set_prototype(self, server):
        self.server = server

    def makeCopy(self):
        return self.server.clone()

server_factory = ServerFactory(server)
server_factory.makeCopy()
# change server to clone
server_factory.set_prototype(server_clone)
server_factory.makeCopy()

