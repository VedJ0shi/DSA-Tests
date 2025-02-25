#the obj instatiation process calls __new__() and __init__() special methods

'''Inside parent class, __new__() should return a new empty instance in memory which is referred to by 
'self' (1st arg) in __init__() and the rest of the class's instance methods'''

'''Inside  metaclass, __new__() should return the class callable in memory which is referred to by 
'cls' (1st arg) in __call__() and the rest of the metaclass's class methods'''

'''__init__() should not return anything (return None)'''

class TempType(type):
    def __new__(cls, *args):
        cls = super().__new__(cls, *args)
        print(cls.__name__, 'invoking custom metaclass at class definition')
        return cls
    
    def __call__(cls, *args, **kwargs):
        print(cls.__name__, 'invoking custom metaclass at instance creation')
        return super().__call__(*args, **kwargs)

class Rectangle:
    def __new__(cls, *args, **kwargs):
        print('creating new instance of Rectangle class')
        return super().__new__(cls) #returns empty object of class Rectangle as 1st arg to __init__()

    def __init__(self, l, w):
        print('initialzing state of the Rectangle instance')
        self.length = l
        self.width = w
    
    def area(self):
        return self.length * self.width
    
   
class Square(Rectangle, metaclass=TempType):
    def __init__(self, l):
        print('initialzing state of the Square instance')
        super().__init__(l, l)
    

class BoundedRectangle(Rectangle):
    def __init__(self, l, w): #conducts validation
        if l * w <= 20:
            print('initialzing state of the BoundedSquare instance')
            super().__init__(l, w)
        else:
            raise ValueError('arguments are too large')


class Unit(Rectangle):
    def __new__(cls, *args, **kwargs): #override __new__() 
        return Rectangle(1, 1) #returns non-empty instance of parent class lol
    
    def __init__(self): #will NOT get called since self no longer refers to a Unit instance
        print('initialzing state of the Unit instance')
        self.length = 0
        self.width = 0


class Singleton(Rectangle): #implements singleton design pattern
    #thus, all instances of the Singleton are actually references to the same object (synchronizes across instances)
    _instance = None #stores singleton object
    def __new__(cls, *args, **kwargs): #override __new__() 
        if not cls._instance:
            print('creating singleton instance of Rectangle class')
            cls._instance = super().__new__(cls)
        return cls._instance #returns the cached object


class Cached(Rectangle): #emulates caching by tracking object ids
    _loaded = {} 
    def __new__(cls, id, *args, **kwargs):
        if cls._loaded.get(id, None) == None:
            print(f'creating new instance of Rectangle class with id {id}')
            cls._loaded[id] = super().__new__(cls)
        else:
            print(f'pulling instance with id {id} from cache')
        return cls._loaded[id] #returns the cached object identified by 'id'
    
    def __init__(self, id, l, w): #'self' will necessarily be the object identified by 'id'
        super().__init__(l, w)