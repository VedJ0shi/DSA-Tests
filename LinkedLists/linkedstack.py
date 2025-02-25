#implementing Stack using a Linked List instead of Array (Python list) for storage
#removing node from tail of a singly linked list takes O(n) time
#Stack push() and pop() must run in true O(1) time
#--> top of Stack will be at head of linked list
#push() will be insertion at the head
#pop() will be a removal from the head

class Empty(Exception):
    '''raised when accessing element from empty object'''
    pass

class LinkedStack:
    '''LIFO Stack using singly-linked list for storage'''

    #-----------non-public (nested) Node class-----------------#
    class _Node:
        '''a Node object is a pair of references to the primary data and the next Node on linked list'''
        def __init__(self, obj, next):
            self._element = obj
            self._next = next
    #----------------------------------------------------------#
    
    def __init__(self): #lazy approach--> storage not initialized
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    
    def push(self, obj):
        '''insertion at the head (top of stack at head, bottom of stack at tail)'''
        self._head = self._Node(obj, self._head ) #new node's _next points to the existing head node
        self._size = self._size + 1
        if self._size == 1:
            self._tail = self._head
    
    def pop(self):
        '''removing and returning from head'''
        if self.is_empty():
            raise Empty('Stack is empty')
        top_node = self._head
        self._head = self._head._next #releases and replaces reference to current _head (irreversible)
        self._size = self._size - 1
        if self._size == 0:
            self._tail = None
        return top_node._element


    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    

    def __str__(self):
        try:
            return f'Stack(top={self.top()}, bottom={self._tail._element}, length={self._size})'     
        except:
            return '<Stack()>'
        
        
    '''Using an underlying linked list, push() and pop() run on true (unamortized) O(1) time'''