'''
Code for binary tree
Dec 02, 2018 
'''

class node: 
    def __init__(self, data_):
        self.left = None 
        self.right = None 
        self.data = data_ 
    
    def printTree():
        print self.data 
    

if __name__=='__main__':
    root = node(99)
    root.printTree()

