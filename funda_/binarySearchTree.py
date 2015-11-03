# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:43:46 2015

@author: akond
"""



class BST(object): 
 def __init__(self, value, left=None, right=None):
  self.value = value 
  self.left = left 
  self.right = right 
 def insert(self, data):
  if self.value < data:
    if self.left is None:
        self.left = BST(data)
    else:
        self.left.insert(data)
  elif data > self.value: 
    if self.right is None:
      self.right = BST(data)
    else:
      self.right.insert(data)
  else:
      self.value = data 
      
 def lookup(self, data, parent=None): 
   if data < self.value:
     if self.value is None:
       return None, None
     self.left.lookup(data, self)
   elif data > self.value:
     if self.value is None:
       return None, None 
     self.right.lookup(data, self)
   else:
       return self, parent 
 def delete(self, data):
  node, parent = self.lookup(data)
  if node is not None:
    childCount = self.countChildren() 
    if childCount==0: 
      if parent is not None:
        if parent.left is node:
          parent.left = None            
        elif parent.right is node:
          parent.right = None   
        del node 
      else:
        self.value = None             
    elif childCount == 1:
      if node.left is not None:
        n_ = node.left
      elif node.right is not None:
        n_ = node.right
      if parent is not None:
        if parent.left is node :
          parent.left = n_ 
        elif parent.right is node:
          parent.right = n_
        del node   
      else:
          self.left = n_.left  
          self.right = n_.right
          self.value = n_.value
    else:
      parent =  node 
      successor = node.right 
      while successor.left:
        parent = successor
        successor = successor.left
      node.value = successor.value
      if parent.left == successor:
        parent.left = successor.right 
      else:
        parent.right = successor.right   
        
 def printTree(self):
   if self.left:
     self.left.printTree() 
   print self.value 
   if self.right:
     self.right.printTree() 
 def comapre_trees(self, nodeP):
   if nodeP is None:
     return False 
   if self.value != node.value:
     return False 
   res_ = True 
   if self.left is None:
     if nodeP.left:
       return False 
   else:
     res_ = self.left.comapre_trees(nodeP.left) 
   if res_ is False: 
     return False 
   if self.right is None: 
     if nodeP.right:
       return False 
   else:
     res_ = self.right.comapre_trees(nodeP.right)
   return res_  
 def countChildren(self):
   cnt = 0 
   if self.left is not None:
     cnt += 1     
   if self.right is not None:
     cnt += 1   
   return cnt     

############ print zone #######
root = BST(8)      
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
print root.lookup(6)