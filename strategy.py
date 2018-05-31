import abc

class Client:

    def set_sort_strategy(self, strategy):
        self.sort_strategy = strategy

    def exec_sort_strategy(self, array):
        self.sort_strategy.sort(array)

class Sort(abc.ABC):  #strategy interface

    @abc.abstractmethod
    def sort(self):
        pass

class SimpleSort(Sort): #strategy

    def sort(self, array):
        return array.sort()

class ReverseSort(Sort): #strategy

    def sort(self, array):
        return array.reverse()

array = [84,5,1,4,31,6,8,9,11,3,7]
client = Client()

client.set_sort_strategy(SimpleSort())
client.exec_sort_strategy(array)
print(array) # [1, 3, 4, 5, 6, 7, 8, 9, 11, 31, 84]

client.set_sort_strategy(ReverseSort())
client.exec_sort_strategy(array)
print(array) #[84, 31, 11, 9, 8, 7, 6, 5, 4, 3, 1]

