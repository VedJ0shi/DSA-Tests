from inspect import Signature, Parameter


'''Execution steps will run in order of class definitions in the code; 
the __new__ method defined in a metaclass is called when the class itself 
is being created, not when instances of the class are being created. 
This is distinct to inheriting __new__ from a parent class.'''


def make_func_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class MyType(type): 
    #custom metaclass 
    print('execution step: 1')
    def __new__(cls, *args): #args includes name of class, inherited base classes & body of class definition
        #__new__ method of metaclass is called when cls is defined NOT later when cls instances are created
        print('execution step: 3 / 5 / 7 / 9')
        cls = super().__new__(cls,*args) #returns a class callable
        if "_fields" in vars(cls): #if a '_fields' class attr defined for the class
            print('__signature__ to be added to class:', cls.__name__)
            setattr(cls,"__signature__", make_func_signature(cls._fields)) #sets '__signature__' attr for the class
        return cls
    
class MyStruct(metaclass=MyType):
    _fields = [] #hence, every instance will have '__signature__' attr
    def __init__(self, *args, **kwargs):
        binding = self.__signature__.bind(*args, **kwargs) #handles positional and keyword args
        for fieldname, val in binding.arguments.items():
            setattr(self, fieldname, val) #sets instance attrs
    print('execution step: 2')

class MyStructClone(metaclass=MyType):
    _fields = [] #hence, every instance will have '__signature__' attr
    def __init__(self, *args, **kwargs):
        binding = self.__signature__.bind(*args, **kwargs) #handles positional and keyword args
        for fieldname, val in binding.arguments.items():
            setattr(self, fieldname, val) #sets instance attrs
    print('execution step: 4')


class Stock(MyStruct):
    _fields = ['ticker','price']
    print('execution step: 6')

class Foo(MyStruct):
    pass
    print('execution step: 8')








