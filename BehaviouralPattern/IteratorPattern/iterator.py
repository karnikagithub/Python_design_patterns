class MyIterator:

    def __init__(self,data):
        self._index = 0
        self._data = data

    def __iter__(self):
        # this method makes the class iterable
        return self
    
    def __next__(self):
        # return the next item in the iteration
        if self._index >= len(self._data):
            raise StopIteration
        
        else:
            item = self._data[self._index]
            self._index += 1
            return item
        


my_iter_obj = MyIterator([1,2,3,45,6,78,9])

for item in my_iter_obj:
    print(item)

