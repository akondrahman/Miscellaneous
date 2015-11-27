# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:28:22 2015

@author: akond
"""



class Node(object):
  def __init__(self, val):
    self.value = val    
  def __str__(self):
    return str(self.value)  
class BinaryTree(object): 
  def __init__(self, rootNode, lChild, rChild):
    self.root = rootNode
    self.left = lChild
    self.right = rChild
  def __str__(self):
    return str(self.root.value) + ", l: " + str(self.left.value) + ", r: " + str(self.right.value)   



def reverse(self):
    self.right =self.left 
    self.left  =self.right 
    if self.left != None:
      self.left.reverse() 
    if self.right != None: 
      self.right.reverse()  
def findNode(binTreeParam, rootParam, nodeParam):
    rootToret = Node(float('Nan') )
    if rootParam == None : 
      rootToret = Node(float('Nan') )
    if (binTreeParam.left.value== nodeParam.value) or (binTreeParam.right.value==nodeParam.value):
      rootToret = rootParam
    else: 
      if nodeParam.value > binTreeParam.left.value: 
          rootToUse = binTreeParam.right
      else: 
          rootToUse = binTreeParam.left 
      rootToret  = findNode(binTreeParam, rootParam, rootToUse )  
    return rootToret 
rootNode = Node(4) 
leftNode = Node(3)
rightNode = Node(7)
tree = BinaryTree(rootNode, leftNode, rightNode)
print "The tree ... ", tree 

nodeToFind=Node(7)
print "Finding 7 ... ", findNode(tree, rootNode, nodeToFind) 