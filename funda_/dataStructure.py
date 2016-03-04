# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:23:19 2015

@author: akond
"""



class Node(object):
  def __init__(self, data=None, next_node=None):
    self.data = data 
    self.next_node = next_node
  def getData(self):
    return self.data
  def getNextNode(self):
    return self.next_node
  def setNextNode(self, nextNodeP):
    self.next_node = nextNodeP 
class LinkedList(object):
  def __init__(self, head=None):
    self.head = head     
  def insert(self, data):
    new_node = Node(data)
    new_node.setNextNode(new_node)
    self.head = new_node    
  def size(self):
    curr_ = self.head
    count = 0     
    while curr_:
      count += 1 
      curr_ = curr_.getNextNode()
    return count  
  def search(self, data):
    current=self.head
    found = False     
    while current and (found==False):
      if current.data == data: 
        found = True  
      else:
        current = current.getNextNode()
    return current  
    
        
  def delete(self, data):
    current_ = self.head 
    previous = None 
    found = False 
    while current_ and found==False:
      if current_.getData() == data:
        found = True 
      else:
        previous = current_
        current_ = current_.getNextNode()
    if current_ is None:
      raise ValueError("Data not in list")
    if previous is None:
      self.head = current_.getNextNode() 
    else:
      previous.setNextNode(current_.getNextNode()) 
      
      
      
      
class MyStack:
  def __init__(self):
    self.items=[]  
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop() 
  def isEmpty(self):
    val = False
    if(len(self.items) == 0):
      val = True 
    return val  
    
    
    
class DoublyNode(object):
  def __init__(self, data=None, next_=None, prev_=None):
    self.data = data 
    self.next_ = next_
    self.prev_ = prev_ 
  def __str__(self):
    return "Node[Data = %s]" %(self.data)
class DoublyLinkedList(object):   
  def __init__(self):
    self.head = None 
    self.tail = None 
  def insert(self, data):
    if(self.head == None):
      self.head = DoublyNode(data)
      self.tail = self.head 
    else:
      current = self.head 
      while(current.next_ != None):
        current = current.next_
      current.next_ = Node(data, None, current)
      self.tail = current.next_
      
        
      
  
def findOccurance(stringParam,splitParam):
  strLen = len(stringParam)
  strDict={}
  end = 0 
  for cnt in xrange(strLen):
   if cnt==0:     
    start = cnt   
    while end <= strLen:
      end = start + splitParam - 1 
      if(end < strLen):
       subStr =  stringParam[start:end+1]    
       if strDict.has_key(subStr):  
        strDict[subStr] = strDict.get(subStr) + [subStr]
       else:
        theStrList = []   
        strDict[subStr] = theStrList
      start = end + 1
  print strDict
  return strDict
def sortKeys(dictParam):
  outputList = []  
  for key,valI in dictParam.items():
    if (len(valI) > 0):
      outputList.append(key)
  sorted(outputList)
  return outputList    
strParam = "acctacctacctctgactgactgaaaaa"
splitParam=4
strDict = findOccurance(strParam, splitParam)       
print "Sorted strings :",  sortKeys(strDict)
def towerOfHanoi(diskList, firstTower, lastTower):
  tempStack =[]  
  for it in diskList:
    firstTower.append(it)
  for cnt in xrange(len(diskList)):
    tempStack.append(firstTower.pop())
  for cnt in xrange(len(diskList)):
    lastTower.append(tempStack.pop())
  return lastTower 

animals=['D1', 'D2', 'C1']  
def enqueAnimals(animals=None, animalsParam=None):
  animals.append(animalsParam)
  print "animals ... so far ...", animals

def dequeDog():
  animalOfInterest = dequeAny()
  animalToRet=""  
  if animalOfInterest[0]=='D':
    animalToRet = animalOfInterest 
  else:
    animalToRet = "Dog not available ... "
  return animalToRet


def dequeCat():
  animalOfInterest = dequeAny()
  animalToRet=""  
  if animalOfInterest[0]=='C':
    animalToRet = animalOfInterest 
  else:
    animalToRet = "Cat not available ... "
  return animalToRet      
def dequeAny():
  return animals.pop(0)    
def detectPalindrome(str_):
  strLen  = len(str_)
  if (strLen%2)==0:
    middlePoint = (strLen-1)/2 
    firstHalf = str_[0:middlePoint + 1]
    secondHalf = str_[middlePoint + 1 : strLen]
    #print firstHalf
    #print "-----"
    #print secondHalf    
  else:
    middlePoint = strLen/2
    #print str_
    firstHalf =str_[0:middlePoint]
    secondHalf = str_[middlePoint+1 : strLen]
    ## strings are weird ... abcde[0:2]=ab, abcde[3:strLen]=de, strLen=len("abcde") = 5 

  return _cmp(firstHalf, secondHalf)  
def _cmp(firstHalf, secHalf):
  valToret = False   
  firstHalf = sorted(firstHalf)
  secHalf = sorted(secHalf)
  if firstHalf == secHalf:
    valToret = True
  return valToret      
      
    
if __name__ == '__main__':  
 diskList = ['z','y', 'x','w']
 lastTower = towerOfHanoi(diskList, [], [])  
 print "last twer ... ",lastTower
 enqueAnimals(animals, 'C2')
 print "The dog that you got ... ", dequeDog()
 print "The cat that you got ... ", dequeCat() 

 palinStr="rotor"
 palinStr="anna"
 print "Palindrome problem for ", palinStr
 print "Result: ", detectPalindrome(palinStr) 