#seeing how Python saves list objects (mutable) internally with sys.getsizeof()
import sys

'''lists are saved as dynamic reference arrays'''


data = []
size = sys.getsizeof(data)
print('sys.getsizeof([]):', size)
print()

for i in range(25):
    data.append(None) #append the None type obj
    print('data:', data)
    print(f'id(data[{i}]):', id(data[i])) #references the same object in memory (None obj)
    print('sys.getsizeof(data):', sys.getsizeof(data))
    if sys.getsizeof(data) > size:
        print(f'New array dynamically created with {sys.getsizeof(data)-size} bytes more reserved capacity!')
        size = sys.getsizeof(data)
    print()

'''on 64-bit machine, each memory address is 8 bytes/64 bits-- 
thus, reference array on this machine has 8 byte cells'''
