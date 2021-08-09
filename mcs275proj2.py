"""
MCS 275 Project 2 - Recursive Ternary Tree

A ternary tree is a tree with in which every node has at most three edges coming out of it (as opposed to a binary tree in which every node has at most two edges coming out of it).

Write a Python implementation for a recursive ternary tree. The data for the construction is a list of integers L. In addition,
your code should contain at least one class, for example, TernaryTree(), which must contain the following three methods:
generate_tree(), traverse_LMRW(), leaf_count().


generate_tree(L) - First element in L is the root node.
All other elements in L are placed recursively inside the tree according to the following set of rules: smaller than root - left;
equal to the root - middle; larger than root - right.

traverse_LMRW() - traverses an instance of the object TernaryTree recursively.
The recursion rules LMRW stand for go (traverse) Left, go (traverse) Middle, go (traverse) Right,
Write node value (print to screen). That is, we traverse the tree on the left until we cannot go any further,
then we go to the middle until we cannot go any further, then we go right until we cannot go any further.
When these have been exhausted, we print the node value to screen.

leaf_count() - returns the number of leaves for an instance of the object TernaryTree.
As a reminder, a leaf nodes are nodes that have no edges coming out of them. In other words, they are at the periphery of the tree.
"""
class TernaryTree(object):

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None


    def insert_node(self, new_value):
        """
        this method inserts a new node into the object
        recursively, using the standard convention:
        values equal or smaller than the root go to the left,
        the rest goes to the right.
        """
        if new_value < self.value:
            if self.left == None:
                self.left = TernaryTree(new_value)#self.value =  new_value # TernaryTree(new_value)
            else:
                self.left.insert_node(new_value)
        elif new_value == self.value:  # case when new_value =  self.value:
            if self.middle == None:
                self.middle = TernaryTree(new_value)#self.value = new_value #TernaryTree(new_value)
            else:
                self.middle.insert_node(new_value)
        else:  # case when new_value > self.value:
            if self.right == None:
                self.right = TernaryTree(new_value)#self.value = new_value #TernaryTree(new_value)
            else:
                self.right.insert_node(new_value)



    def traverse_LMRW(self):

        if self.left != None:
            self.left.traverse_LMRW()
        if self.middle != None:
            self.middle.traverse_LMRW()
        if self.right != None:
            self.right.traverse_LMRW()
        print(self.value)



    def generate_tree(self, L):
        self.value = L[0] #first element in L
        for e in L[1:]:
            self.insert_node(e)
        #return self.value

"""
class Node(object):


class Tree(object):
    self.Node("dummy")
    def __init__(self): #you can't do this here! y?


def main():
    T=Tree(L)
    T.generate_tree(L)
"""


def main():
    L = ([4,1,2,2,3,1,0,4,6,5,6,4])
    T = TernaryTree()
    T.generate_tree(L)
    #print("traverse LMRW")
    #T.traverse_LMRW()
    #print("leaf count")
    #T.leaf_count()

main()