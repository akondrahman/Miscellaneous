'''
Code for binary tree
Dec 02, 2018 
'''

class node: 
    def __init__(self, data_):
        self.left = None 
        self.right = None 
        self.data = data_ 
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print self.data
        if self.right:
            self.right.printTree()

    def insertData(self, data_):
        if self.data: 
           if data_ < self.data: 
               if self.left is None: 
                   self.left = node(data_)
               else:
                   self.left.insertData(data_)
           elif data_ > self.data : 
               if self.right is None:
                   self.right = node(data_)
               else:
                   self.right.insertData(data_)
        else: 
           self.data = data_
    
    

if __name__=='__main__':
    root = node(99)
    root.insertData(6)
    root.insertData(14)
    root.insertData(3)
    root.printTree()

