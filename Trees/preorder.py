#depth-first search where nodes are visited in the order- current node, left subtree, right subtree

class PreorderMixin:
    '''support for performing Preorder traversal of all positions; mixed into any concrete subclass of TreeBase'''


    def preorder(self):
        '''generates a preorder iteration of all position in the tree'''
        if not self.is_empty(): #in implementation,'self' refers to an instance of a TreeBase subclass
            for pos in self._subtree_preorder(self.root()): #preorder traversal starting at root
                yield pos
    
    def _subtree_preorder(self, pos, order=[]):
        '''non-public generalized preorder traversal; returns ordered list'''
        order.append(pos)
        for child in self.children(pos):
            order = self._subtree_preorder(child, order)
        return order




    













