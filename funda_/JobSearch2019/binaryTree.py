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
    
    def inOrderTraversal(self, root_):
        res_ = [] 
        if root_:
            res_ = root_.inOrderTraversal(root_.left)
            res_.append(root_.data)
            res_ = res_ + root_.inOrderTraversal(root_.right)    
        return res_
    def preOrderTraversal(self, root_):
        res_ = [] 
        if root_:
            res_.append(root_.data)
            res_ = res_ + self.preOrderTraversal(root_.left) 
            res_ = res_ + self.preOrderTraversal(root_.right) 
        return res_
    def postOrderTraversal(self, root_):
        res_ = []
        if root_:
            res_ = root_.postOrderTraversal(root_.left)
            res_ = res_ + root_.postOrderTraversal(root_.right) 
            res_.append(root_.data) 
        return res_

if __name__=='__main__':
    root = node(27)
    root.insertData(14)
    root.insertData(35)
    root.insertData(10)
    root.insertData(19)
    root.insertData(31)
    root.insertData(42)
    # root.printTree()
    print root.inOrderTraversal(root)
    print '-'*25
    print root.preOrderTraversal(root)
    print '-'*25
    print root.postOrderTraversal(root)
    print '-'*25