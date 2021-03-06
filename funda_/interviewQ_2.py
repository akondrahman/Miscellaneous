# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:10:21 2015

@author: akond
"""



def processStream(wordListP, streamP):
  wordDict={}
  for it_ in wordListP:
    wordDict[it_] = [it_[-1]] 
  buffer_=[]
  lenWordList=[len(x) for x in wordListP]
  lastCharList = [x[-1] for x in wordList]
  maxBuffLen = max(lenWordList)
  #print "Max buff len",maxBuffLen
  for char_ in streamP:
      if len(buffer_) <= maxBuffLen:
        buffer_.append(char_)
      else:
        buffer_ = [] 
      #print "buffer ......", buffer_  
      if char_ in lastCharList:
          indexToLook = lastCharList.index(char_)
          wordToLook = wordListP[indexToLook]
          #print "Word to look ", wordToLook
          lenToLook=len(wordToLook) 
          startPoint = (len(buffer_) - lenToLook) 
                    
          #print "start point ", buffer_[startPoint]
          strList =  buffer_[startPoint:-1] +   [buffer_[-1]]       
          strToCheck =  "".join(strList)   
          #print "String to check: ", strToCheck          
          if strToCheck in wordListP: 
            print "Time to make that stupid API Call !"
            buffer_ = []
            
wordList=["ok", "test", "one", "try", "trying"]
stream="abcokdeftrying" 
print "API Call Problem: ", processStream(wordList, stream)  


#def readEfficiently(fileParam):
#  with open(fileParam, "rb") as fh:
#    first = fh.decode() 
#    fh.seek(-1024, 2)
#    last = fh.readlines()[-1]
#  return first, last 
#fileP = "interviewQ_1.py"
#print "Reading first and last efficiently: ", readEfficiently(fileP)  
def _checkIfPrime(numP):
  return all(numP % i for i in xrange(2, numP))
def _getPrimeFactors(maxNumParam): 
  list_=[]  
  for i in range(1, maxNumParam + 1):
       if maxNumParam % i == 0:
           #print(i)
           if _checkIfPrime(i):
             list_.append(i)
  return list_         
def giveLargestExpressibleNumber(primeList, maxNumber): 
  if 1 not in primeList:  
    modPrimeList = [1]
    modPrimeList = modPrimeList + [x for x in primeList]
  else:
    modPrimeList =[x for x in primeList]  
  factorSet = set(_getPrimeFactors(maxNumber))
  primeSet = set(modPrimeList)
  diff = factorSet - primeSet
  #print "factor and prime set {}, {}".format(factorSet, primeSet)
  #print "Max Number now ..", maxNumber
  #print "Diff : ", diff  
  if (len(diff)>0):
    #print "asi mama - 2 "    
    maxNumber =  maxNumber - 1
    maxNum = giveLargestExpressibleNumber(primeList, maxNumber )
  else:  
    maxNum = maxNumber 
  return maxNum
primes=[2, 3, 5]
maxNum=1000
#print "Prime factors: ", _getPrimeFactors(maxNum)
print "Largest expressible number:  ", giveLargestExpressibleNumber(primes, maxNum)
def findLargerElem(arrayP):
  outputArray =[]  
  uniqueList = set(arrayP)
  sortedList = sorted(uniqueList, reverse=False) 
  for elem in arrayP:
    lastIndex = len(sortedList) - 1
    startIndex = sortedList.index(elem) 
    largerCnt = lastIndex - startIndex
    outputArray.append(largerCnt)
  return outputArray
arrayInp =[3, 4, 5, 9, 2, 1, 3]
print "Output for 'findLArgerElem' ... ", findLargerElem(arrayInp)    


def getOptimizedArrayRange(arrayRanges):
  lowList =[]  
  highList = []
  lowRange = []
  upperRange = []
  tempDiffLow =[]
  tempDiffHigh =[]
  for it_ in arrayRanges:  
    lowList = lowList + [it_[0]]
    highList.append(it_[1]) 
  maxElemOfInterest = max(highList)
  minElemOfInterest  = min(lowList) 
  for item in arrayRanges:
    if item[0]==minElemOfInterest:
      lowRange.append(item)
    if item[1] == maxElemOfInterest:
      upperRange.append(item)
  for lowI in lowRange:
    tempDiffLow.append(lowI[1] -lowI[0])   
  for highI in upperRange:
    tempDiffHigh.append(lowI[1] -highI[0])  
  retLow= lowRange[tempDiffLow.index(max(tempDiffLow))]
  retHigh = upperRange[tempDiffHigh.index(max(tempDiffHigh))]
  return retLow, retHigh 

arrayRange = [(2, 6), (3, 5), (7, 21), (20, 21)]
print "Optimized Array RAnge .... ", getOptimizedArrayRange(arrayRange)     
