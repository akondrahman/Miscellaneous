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

def compareElectionResults(demResult, repResult, seatCount): 
  strToRet = ""  
  detectInvalidity = lambda x : True if x * -1 == abs(x) else False 
  if (len(demResult) == seatCount) and ( len(repResult) == seatCount):    
    for dem, rep in zip(demResult, repResult):
      if (detectInvalidity(dem)) or (detectInvalidity(rep)):
        strToRet = "Invalid input"
        break   
      elif dem == rep: 
        strToRet = "Democratic and Republican results are equal "
      else: 
        strToRet = "Democratic and Republican results are unequal"  
        break
  else: 
        strToRet =  "Length of party results do not match with seat count"
  
  return strToRet    
          
res_1=[12, 3, 5, 4, -7]
res_2=[12, 3, 5, 4, 7]
seats = 5
print "Election Analysis : ", compareElectionResults(res_1, res_2, seats) 


def _sortByMSB(listOfInts): 
  import math
  tempMax = -1
  tempElem =  -1
  lowList = []
  sortedList = []
  for itm in listOfInts: 
    len_ = len(str(itm)) - 1
    tmp = int(itm / math.pow(10, len_))
    #print "tmmp", tmp
    if tmp > tempMax:      
      tempMax = tmp 
      tempElem = itm
    else: 
      lowList.append(itm)
      
  sortedList = sortedList + [tempElem]
  #print "sorted lsit ...", sortedList
  lowList = sorted(lowList, reverse=True)
  sortedList = sortedList + [x for x in lowList]  
  return sortedList        
        
def concatForLargestNumber(listOfInts):
  sortedByMSB = _sortByMSB(listOfInts)
  conatenatedList = [str(x) for x in sortedByMSB]
  #print "lsit, ",conatenatedList
  out=""
  for itm in conatenatedList:
   out = out + itm  
  return out  
      
listOfints = [9, 918,  917]
print "Largest Concatenated Value: ", concatForLargestNumber(listOfints)
