import random

class Memory:
    def __init__(self, size_max, size_min):
        self._samples = []
        self._size_max = size_max
        self._size_min = size_min


    def add_sample(self, sample):
        #Adding sample into the memory to check
        self._samples.append(sample)
        if self._size_now() > self._size_max:
            #if the length is greater than the size of memory, remove the oldest item
            self._samples.pop(0)  


    def get_samples(self, n):
        #Get n samples randomly from the memory
        if self._size_now() < self._size_min:
            return []

        if n > self._size_now():
            # get all the samples
            return random.sample(self._samples, self._size_now())  
        else:
            # get "batch size" number of samples
            return random.sample(self._samples, n)  


    def _size_now(self):
        #Check how full the memory is
        return len(self._samples)