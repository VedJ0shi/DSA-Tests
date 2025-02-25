from priorqueuebase import *
from utils.linkedlists import Empty


class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self, _initial=[]):
        self._data = [] 
        if _initial:
            self._data = _initial
    
    def __len__(self):
        return len(self._data)

    @classmethod
    def construct(cls, contents=()): #contents should be a sequence of (key, value) tuples
        '''bottom up heap constructor i.e. heapification of a given sequence of values based on their keys'''
        temp = cls([cls._Item(key,val) for (key,val) in contents])
        #procedure to rearrange temp._data with repeated calls to _downheap():
        if len(temp) > 1:
            for j in range(len(temp)-1, -1, -1):
                temp._downheap(j) #all initial leaf positions will return immediately (trivial indices)
        return temp
    
    def __str__(self):
        return f'{[(item._key, item._value) for item in self._data]}'
        
#----------------------private utility methods-------------------------#
    def _parent_index(self, j):
        if j % 2 == 1:
            return (j-1)//2
        else:
            return (j-2)//2
    
    def _left_index(self, j):
        return 2*j + 1
    
    def _right_index(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left_index(j) <= len(self._data) - 1   #index beyond end of array ?
    
    def _has_right(self, j):
        return self._right_index(j) <= len(self._data) - 1

    def _swap(self, i, j):
        self._data[j], self._data[i] = (self._data[i], self._data[j]) #parallel assignment
    
    def _upheap(self, j):
        if j == 0:
            return
        parent_j = self._parent_index(j)
        if self._data[j] < self._data[parent_j]:
            self._swap(j, parent_j)
            self._upheap(parent_j) 
    
    def _downheap(self, j):
        if not self._has_left(j):
            return        
        child_j = self._left_index(j)
        if self._has_right(j) and self._data[self._right_index(j)] < self._data[child_j]:
            child_j = self._right_index(j)
        if self._data[j] > self._data[child_j]:
            self._swap(j, child_j)
            self._downheap(child_j)
#-----------------------------------------------------------------------------#
            
    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data)-1)
    
    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        root = self._data[0]
        return (root._key, root._value)
    
        
    def dequeue_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        root = self._data[0]
        self._swap(0, len(self._data) -1)
        self._data.pop()
        self._downheap(0)
        return (root._key, root._value)


    

    
