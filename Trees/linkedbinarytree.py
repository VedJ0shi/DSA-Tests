from binarytreebase import BinaryTreeBase

class LinkedBinaryTree(BinaryTreeBase):
    '''linked representation of binary tree, with some additional general purpose update/mutate methods'''
    class _Node:
        def __init__(self, obj, parent=None, left=None, right=None):
            self._element = obj
            self._parent = parent
            self._left = left
            self._right = right #if _left and _right are None, then node is a leaf
        
    class _Position:
        def __init__(self, container, node):
            self._container = container #if _container is not 'self', then position does not belong to current Tree
            self._node = node 
    
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            if type(self) is type(other):
                return self._node is other._node
            return False
        
    def _validate(self, pos):
        if not isinstance(pos, self._Position):
            raise TypeError('must be a position')
        if not pos._container is self:
            raise ValueError('position does not belong to this tree')
        if pos._node._parent is pos._node: #convention for deprecated nodes on Tree (recursive parent definition)
            raise ValueError('position no longer valid')
        return pos._node #unwraps
    
    def _make_position(self, node):
            if node is None:
                return None
            print(f'returning position of element={node._element}...')
            return self._Position(self, node) #wraps
    
    
    def __init__(self):
        self._root = None #root node
        self._size = 0

    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)

    def parent(self, pos):
        node = self._validate(pos)
        return self._make_position(node._parent)
    
    def left(self, pos):
        node = self._validate(pos)
        return self._make_position(node._left)
    
    def right(self, pos):
        node = self._validate(pos)
        return self._make_position(node._right)
    
    def num_children(self, pos):
        node = self._validate(pos)
        count = 2
        if node._left is None:
            count = count - 1
        if node._right is None:
            count = count - 1
        return count
    
    #------------------private update/mutate methods for any public methods of subclasses---------------#
    def _add_root(self, obj):
        if not self._root is None:
            raise ValueError('root already exists for this tree')
        self._size = 1
        self._root = self._Node(obj)
        return self._make_position(self._root)

    def _add_left(self, pos, obj):
        node = self._validate(pos)
        if not node._left is None:
            raise ValueError('left child already exists')
        node._left = self._Node(obj, parent=node)
        self._size = self._size + 1
        return self._make_position(node._left)
    

    def _add_right(self, pos, obj):
        node = self._validate(pos)
        if not node._right is None:
            raise ValueError('right child already exists')
        node._right = self._Node(obj, parent=node)
        self._size = self._size + 1
        return self._make_position(node._right) 

    def _replace(self, pos, obj):
        node = self._validate(pos)
        old = node._element
        node._element = obj
        return old

    def _delete(self, pos):
        if self.num_children(pos) == 2:
            raise ValueError('cannot delete this node since it has two children')
        node = self._validate(pos)
        if node._left:
            child = node._left
        else:
            child = node._right
        parent = node._parent
        if node is parent._left:
            parent._left = child
        else:
            parent._right = child
        self._size = self._size - 1
        node._parent = node #deprecate node
        obj = node._element
        node._element = None #dereference data for garbage collection
        return obj

    def _attach(self, pos, t1, t2):
        if not self.is_leaf(pos):
            raise ValueError('position must be that of a leaf')
        node = self._validate(pos)
        left_root = t1._root
        right_root = t2._root
        node._left = left_root
        node._right = right_root
        left_root._parent = node
        right_root._parent = node
        t1._root = None 
        t2._root = None #t1 & t2 no longer have a root, since they are subtrees of 'self'

        


        





        
