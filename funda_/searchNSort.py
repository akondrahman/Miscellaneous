# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:41:44 2015

@author: akond
"""

def doBasicBinarySearch(listParam, firstIndexP, lastIndexP, elementToSearchP): 
  indexToRet = 0  
  firstIndex = firstIndexP
  lastIndex=lastIndexP
  #print "First and lst index {}:{}".format(firstIndex, lastIndex)
  if firstIndex < lastIndex:
   splitIndex = (firstIndex + lastIndex)/2 
   splitElement = listParam[splitIndex]
   #print "{}vs{}@{}--> ({}, {})".format(splitElement, elementToSearchP, splitIndex, firstIndex, lastIndex)
   if elementToSearchP > splitElement:
      return doBasicBinarySearch(listParam, splitIndex +1 , lastIndex, elementToSearchP)
   else: 
      return doBasicBinarySearch(listParam, firstIndex, splitIndex, elementToSearchP)
  else:
   #print "first index is ", firstIndex  
   #print "ek bar i to ..."  
   if elementToSearchP == listParam[firstIndex]:
      indexToRet = firstIndex
      return indexToRet
      
def doModBasicBinarySearch(listParam, firstIndexP, lastIndexP, elementToSearchP): 
  indexToRet = 0  
  firstIndex = firstIndexP
  lastIndex=lastIndexP
  #print "First and lst index {}:{}".format(firstIndex, lastIndex)
  if firstIndex < lastIndex:
   splitIndex = (firstIndex + lastIndex)/2 
   splitElement = listParam[(splitIndex+1)]
   #print "{}vs{}@{}--> ({}, {})".format(splitElement, elementToSearchP, splitIndex, firstIndex, lastIndex)
   if elementToSearchP < splitElement:
      return doModBasicBinarySearch(listParam, firstIndex, splitIndex, elementToSearchP) 
   else: 
      return doModBasicBinarySearch(listParam, splitIndex +1 , lastIndex, elementToSearchP)
  else:
   #print "first index is ", firstIndex  
   #print "ek bar i to ..."  
   if elementToSearchP == listParam[lastIndex]:
      indexToRet = lastIndex
      return indexToRet  
      
      
def rotate(listParam, noOfTimes):
    return listParam[noOfTimes:] + listParam[:noOfTimes]   
    
def eleven_three(listA, elParam):
   print "Initial list : ", listA  
   print "Min element:  ", min(listA)
   for cnt in range(len(listA)):
       if listA[cnt]==min(listA):
         indexToUse = cnt
   print "index to use ", indexToUse      
   #rotDiff = (len(listA) - indexToUse ) +  
   originalListToUse = rotate(listA, indexToUse)
   print "original list to use ", originalListToUse
   indexToret = indexToUse + doBasicBinarySearch(originalListToUse, 0, len(originalListToUse)-1, elParam) 
   if indexToret >= len(listA):
     indexToret = indexToret % len(listA)     
   print "Final answer: ", indexToret 
     
def _ModifyStrList(strList):
  listToret =[]  
  prevItem ="" 
  currItem ="" 
  for item in strList:
    if len(item)==0:   
     currItem = prevItem
    else:
     currItem =  item
     prevItem = item 
    listToret.append(currItem) 
  return listToret         
def eleven_five(strList, strToSee):
  print "The original list is ", strList
  modifiedList = _ModifyStrList(strList)
  print "Modified str list is ", modifiedList
  modifiedAsciiList = [ ord(elem[0]) for elem in modifiedList ]
  print "modified ascii list: ", modifiedAsciiList
  asciiIndexTosearch = ord(strToSee[0])
  indexReturned  = doBasicBinarySearch(modifiedAsciiList, 0, len(modifiedAsciiList) - 1, asciiIndexTosearch)
  print "Final result: {} is at position {}".format(strToSee, indexReturned)       


def _doMatrixSearchAsBinSearch(matrixParam, low, high, elementToSearch_, matColsP):
  indicesToRet=()  
  if low < high:
    mid = (low + high)/2
    splitRow = matrixParam[mid]
    print "thsi si ssplit row ", splitRow
    if elementToSearch_ > splitRow[matColsP]:
      return _doMatrixSearchAsBinSearch(matrixParam, mid+1, high, elementToSearch_, matColsP)    
    else:
      return _doMatrixSearchAsBinSearch(matrixParam, low, mid, elementToSearch_, matColsP)
  else:
   if elementToSearch_ in matrixParam[low]:
     rowNum=low
     colNum = doBasicBinarySearch(matrixParam[low], 0, len(matrixParam[low]) - 1, elementToSearch_)
     indicesToRet = (rowNum, colNum)
   else:
     indicesToRet = (0, 0)
  return indicesToRet        

def eleven_six_loglogn(matrixToSearch, elementP):
  from numpy import matrix
  matrixToSearch_mod = matrix(matrixToSearch) 
  print "numpy version fo the matrix to search ", matrixToSearch
  matRows=matrixToSearch_mod.shape[0]
  matCols=matrixToSearch_mod.shape[1]  
  indices_to_print = _doMatrixSearchAsBinSearch(matrixToSearch, 0, matRows-1, elementP, matCols-1)  
  print "Final answer: {} was found at position={}".format(elementP, indices_to_print)
  


def eleven_six_nlogn(matrixToSearch, elementP):
  indicesToRet=()  
  for cnt in range(len(matrixToSearch)):
    rowOfInterest=matrixToSearch[cnt]
    colOfInterest = doBasicBinarySearch(rowOfInterest, 0, len(rowOfInterest) - 1, elementP)
    if colOfInterest !=None:
       indicesToRet=(cnt, colOfInterest)
  return indicesToRet     
        

def eleven_seven(listOfTupP):
  finalList = []  
  sortedByht = sorted(listOfTupP, key = lambda elem: elem[0] )
  print "tuples soretd by height ... ", sortedByht  
  #sortedByWeight = sorted(sortedByht, key = lambda element: element[1])   
  #print "sorted by weight ", sortedByWeight
  prevWt_ =  0   
  for cnt in range(len(sortedByht)):
    wt_ = sortedByht[cnt][1]     
    if cnt > 0:
      if wt_ >= prevWt_:
        finalList.append(sortedByht[cnt])
      prevWt_  = wt_  
    else:
      finalList.append(sortedByht[cnt])  
      prevWt_ = wt_
  return finalList 


   
def one_three(strAP,strBP):
  asci_A_tot = sum([ ord(elemnt) for elemnt in strAP ])    
  asci_B_tot = sum([ ord(elemnt) for elemnt in strBP ])
  if asci_A_tot == asci_B_tot:
    return True 
  else:
    return False   
    
    
    
def nine_three(arraInp):
  finalMagicList =[]  
  for elem in arraInp:
    firstOccuIndex = doBasicBinarySearch(arraInp, 0, len(arraInp) - 1, elem)
    lastOccurIndex = doModBasicBinarySearch(arraInp, 0, len(arraInp)-1, elem)
    lisToLook = [_ for _ in range(firstOccuIndex, lastOccurIndex+1)]
    #print "list to look ", lisToLook
    if len(lisToLook) > 0:
      if elem in lisToLook:
        tupToadd = (elem, lisToLook )
        if tupToadd not in finalMagicList:
          finalMagicList.append(tupToadd)
        tupToadd=()
 
  return finalMagicList          
def seventeen_six(arr):
  diffList=[]
  unsorted = [_ for _ in arr]
  #print arr
  #sorted_ = arr.sort() 
  #print sorted_
  arr.sort() 
  for elem in arr:   
   tupToAdd=(elem, unsorted.index(elem), arr.index(elem))
   print "sanity check : ", tupToAdd
   if arr.index(elem) != unsorted.index(elem):
     diffList.append(arr.index(elem))
  return (min(diffList), max(diffList))    
        

def seventeen_tweleve(theArr, theTot):
  listToret=[]  
  for cnt in range(len(theArr)):
    otherPart = theTot - theArr[cnt]
    if otherPart <= theTot:
      if otherPart in theArr[cnt:]:
        tupToAdd=(theArr[cnt], otherPart)
        listToret.append(tupToAdd)
  return listToret      
#################### Testing time: 
print "Problem: general and modified binary search  "
listTotest= [1, 2, 4, 4, 4, 5, 6, 7, 8, 8, 8]
elementToSearch = 8
firstIndex = 0 
lastIndex = len(listTotest) - 1 
answer = doBasicBinarySearch(listTotest, firstIndex, lastIndex, elementToSearch)
print "{} was found at {} by normal_BSEARCH()".format(elementToSearch, answer)  
mod_Index = doModBasicBinarySearch(listTotest, firstIndex, lastIndex, elementToSearch)
print"{} was found at {} by modified_BSEARCH()".format(elementToSearch, mod_Index) 
###
print "---------------------"
print "Problem 11.3: "
rotatedList = rotate([1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25], 7)
print "rotated list: ", rotatedList
elementToSearch = 10
print "element to search : ", elementToSearch

eleven_three(rotatedList, elementToSearch) 
###
print "---------------------"
print "Problem 11.5: "
eleven_five(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball")
###
print "---------------------"
elem=1
print "Problem 11.6-loglogn: "
eleven_six_loglogn([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [100, 101, 103, 105, 110]], elem)
print "Problem 11.6-nlogn: "
indices=eleven_six_nlogn([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [100, 101, 103, 105, 110]], elem)
print "Final answer using nlogn approach: {} was foudn at {}".format(elem, indices)
print "---------------------"
print "Problem 11. 7"
listOfTup=[(65, 100), (70, 150), (56, 90), (75, 190), (60, 95)]
answer_eleven_seven = eleven_seven(listOfTup)
print "Thge list is {}, length of tower is {}".format(answer_eleven_seven, len(answer_eleven_seven))
print "--------------------"
print "Problem 1.3: "
strA="abd"
strB="bda"
answer_one_three = one_three(strA, strB)
print "Was it a permutation ? Ans ={}".format(answer_one_three)
print "Problem 9.3-Disticnt"
#arrayToSearch=[1, 2, 4, 4, 4, 5, 6, 7, 8, 8, 8]
arrayToSearch=[0, 1, 2, 3, 4, 5, 6, 7, 8]
ans_nine_three = nine_three(arrayToSearch)
print "the magic list is ", ans_nine_three 
print "######"
print "Problem 9.3-Not distinct"
arrayToSearch=[1, 2, 4, 4, 4, 5, 6, 7, 8, 8, 8]
ans_nine_three = nine_three(arrayToSearch)
print "the magic list is ", ans_nine_three 
print "------------------------------"
print "Problem 17.6: "
theArr=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
ans_17_6=seventeen_six(theArr)
print "Answer to 17.6: ", ans_17_6 
print "------------------------------"
print "Problem 17.12: "
theArr=[ 7, 10, 11, 1, 2, 4, 8, 12]
theTot=15
ans_17_12=seventeen_tweleve(theArr, theTot)
print "Answer to 17.12: ", ans_17_12 