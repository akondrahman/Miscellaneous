# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:46:30 2015

@author: akond
"""



class SortedStack(object):
  def  __init__(self):
    self.items=[]    
  def push(self, item):
    self.items = self.items + [item]
    #self.items.sort()
    self.items = sorted(self.items)    
    ## this changes the list wherease sorted() does not chnage the list ... you need a holder to hold the changed result 
    #print "lala ..",self.items    
  def pop(self):
    return self.items.pop() 
  def peek(self):
    return self.items[-1]
  #def __str__(self):
  #  print self.items    
    
    
    
if __name__=="__main__":    
 myStack = SortedStack()
 myStack.push(2)
 myStack.push(3)
 myStack.push(5)
 myStack.push(1)
 print "Stack after all the pushes ..", myStack.items
 print "Peek @ stack ...", myStack.peek()
 print "Stack ... after popping ...", myStack.pop()
    