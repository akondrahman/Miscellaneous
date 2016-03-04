# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:10:57 2015

@author: akond
"""



class binaryTree:
  def __init__(self, ID, left=None, right=None):
    self.ID = ID 
    self.left = left 
    self.right = right 
  def __str__(self):
    return str(self.ID)
  


leftChild = binaryTree(2) 
rightChild = binaryTree(3)
theTree = binaryTree("T1", leftChild, rightChild)
print theTree
print "----- Expression evaluation ----- "
exprTree = binaryTree(2, binaryTree(3), binaryTree(4))
def total(treeParam):
  if treeParam==None: 
    return 0
  else:
    return  treeParam.ID + total(treeParam.left) + total(treeParam.right)  
print total(exprTree)
print "----- Tree Traversal -----"
print "--- Pre Order ---"
algebraExpreTree = binaryTree("*", binaryTree( "+", binaryTree("a"), binaryTree("-", binaryTree("b") , binaryTree("c"))    ) , binaryTree("z"))
def print_tree_preorder(treeP):
  if treeP== None:
    return 
  print treeP.ID ,  
  print_tree_preorder(treeP.left)     
  print_tree_preorder(treeP.right)
print print_tree_preorder(algebraExpreTree)       
print "--- Post Order ---"
def print_tree_postorder(treeP):
  if treeP== None:
    return 
  print_tree_postorder(treeP.left)     
  print_tree_postorder(treeP.right)
  print treeP.ID  , 
print print_tree_postorder(algebraExpreTree)        
print "--- Indented Tree ---"
numericExpr = binaryTree( "+", binaryTree(1), binaryTree( "*", binaryTree(2), binaryTree(3)  ))
def print_tree_indented(treeP, level = 0):
  if treeP== None:
    return 
  print_tree_indented(treeP.left, level + 1)     
  print '-' * level + str(treeP.ID)
  print_tree_indented(treeP.right, level + 1)
print print_tree_indented(numericExpr)         