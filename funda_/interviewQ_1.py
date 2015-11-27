# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:29:31 2015

@author: akond
"""



def detectValidJSONString(strParam):
  comma_counter = strParam.count(",") 
  if comma_counter > 0: 
    subStrList = strParam.split(",") 
    for elem in subStrList:
      if elem.count(":") == 1:
        colonSplit = elem.split(":")
        #print "colon splitted element ", colonSplit[1]
        if len(colonSplit[1])!=1 and ((colonSplit[1].count("{")==1) and (colonSplit[1].count("}")==1)): 
          print "JSON String is in invalid format"   
    else:
        print "JSON is good ! " , strParam 
  else:
    if(strParam.count(":") != 1): 
      print "JSON String is in invalid format"
    else: 
      print "JSON is good for ", strParam  
      


def _sumEqualLists(listA, listB):
    tempList = []  
    outputList = []
    tempList = [0 for _ in listA]  
    cnt = len(listA)  - 1
    carry  = 0 
    while cnt > -1: 
      listElemSum = (listA[cnt] + listB[cnt])  
      temp = listElemSum  + carry  
      #print "the temp ... ", temp
      carry = temp / 10
      remin = temp % 10
      tempList[cnt] = remin  
      #print "Carry ...", carry
      if (cnt==0) and (carry==1):
        #print "temp List .." , tempList    
        outputList = outputList + [carry]
        outputList = outputList + [x for x in tempList]  
      elif (cnt==0): 
        #print "temp ;ist .." , tempList  
        outputList =  outputList   + [x for x in tempList]  
      cnt = cnt -  1
    return outputList  
def addListsWithCarry(listA, listB):
  output = []
  if len(listA)==len(listB): 
    output = _sumEqualLists(listA, listB)
  else: 
    dummyList = []  
    otherList = [] 
    print "The two lists are unequal in length! Filling the smaller list with zero" 
    if (len(listA) > len(listB)): 
      print "list A is bigger! "
      dummyList  = dummyList  + [0]
      dummyList = dummyList + [x for x in listB]
      otherList = [y for y in listA]
    elif(len(listB) > len(listA)): 
      print "list B is bigger! "
      dummyList  = dummyList  + [0]
      dummyList = dummyList + [x for x in listA]   
      otherList = [y for y in listB]      
    output = _sumEqualLists(dummyList, otherList)
  return output  
      
jsonStr="{{a}}"
detectValidJSONString(jsonStr)
listA=[9, 9, 2]
listB=[1, 3]
print "Summing ...", addListsWithCarry(listA, listB)      