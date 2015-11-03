# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:30:22 2015

@author: akond
"""

def findArrayCoverage(arrayA, arrayB):
  dictToUse ={}
  for intem in arrayA:
    dictToUse[intem] = []   
  print "Dictionary before assigning ", dictToUse  
  for cnt in xrange(len(arrayB)):
    if dictToUse.has_key(arrayB[cnt]):
      dictToUse.get(arrayB[cnt]).append(arrayB[cnt]) 
  print "Dictionary after assigning ", dictToUse
  validKeyList = []  
  for key, val in dictToUse.items():
    if len(val) > 0:
      validKeyList.append(key)
  print "the range is : {}, {}".format(min(validKeyList), max(validKeyList))



arrayA=[1, 2, 3, 4, 5]
arrayB=[3, 4, 5]
print"--------------------------"
print"FindArrayCoverage()"
findArrayCoverage(arrayA, arrayB)   
print"--------------------------"

def findProduct(dictParam):
  import operator   
  sortedDict = sorted(dictParam.items(), key=operator.itemgetter(1))
  sortedDict.reverse()
  print sortedDict[0]
  
prodDict={'Bal': 10, 'Putkey': 100, 'Leura': 5 }
print"--------------------------"
print"FindProduct()"
findProduct(prodDict)        
print"--------------------------"


def removeDup(arrayParam):
  curr=0
  prev=0
  outputArray=[] 
  
  arrayParam.sort()
  for it in arrayParam:
    curr = it 
    if curr!=prev:
      outputArray.append(curr)
      prev = curr 
      
  return outputArray
inpArray=[1, 2, 4, 2, 6]    
print"--------------------------"
print"RemoveDup()"
print removeDup(inpArray)        
print"--------------------------" 


print"--------------------------"
numberDict={}
def getNumber(numberParam):
  getKey = numberParam%10
  if numberDict.has_key(getKey):
      if reqNumber(numberParam):
        print "Number already taken !"
      else:
        numberDict[getKey] = numberParam
  else:
      numberDict[getKey] = numberParam   
  print "Current dictionary : "
  print numberDict    
def reqNumber(numP):
  return numP in numberDict.values()      
print"getNumber and request Number()"
numberOfInterest = 99
getNumber(99) 
#print reqNumber(inpArr)       
print"--------------------------" 
peopleDict={123 : ['A', 'X', 'Teacher'], 456:['B', 'Y', 'Student'], 789 :['C', 'Z', 'Programmer'] }

def searchFName(fNameParam):
  for key, valP in peopleDict.items():
    if valP[0] == fNameParam:
      return   "{} exists !; corrsponding identifier (phone  number) {}".format(fNameParam, str(key))
    else:
      str_ = "Nope !"  
  return str_    
def searchLName(lNameParam):
  for key, val in peopleDict.items():
    if val[1] == lNameParam:
      return   "{} exists !; corrsponding identifier (phone  number) {}".format(lNameParam, str(key))  
    else:
       str_ = "Nope !"    
  return str_    
def searchPhone(phoneNumber):
  if (peopleDict.has_key(phoneNumber)):
     return   "{} exists !".format(phoneNumber) 
  else:
      str_ =  "Nope !"  
  return str_ 
def searchTitle(tit):
  for key, val in peopleDict.items():
    if val[2] == tit:
      return   "{} exists !; corrsponding identifier (phone  number) {}".format(tit, str(key))  
    else:
       str_ = "Nope !"    
  return str_ 

    
print"searchFName()"
print searchFName('B')        
print"searchLName()"
print searchLName('Z')  
print "searchPhone()"
print searchPhone(789)      
print "searchTitle()"
print searchTitle('Programmer')      
print"--------------------------"      
airportDict={} 
#routeList = []
def createAirportDict(listP):
    
  for cnt in xrange(len(listP)):
    if cnt %2 == 0:
      if (cnt + 1) < len(listP):
        airportDict[listP[cnt]] = listP[cnt+1]
  print airportDict           
def findAirportRoute(startA, endA, routeList):
  destVal=''  
  if airportDict.has_key(startA):
    destVal=airportDict[startA] 
    routeList.append(startA)
    routeList.append(destVal)
    
    if destVal != endA:
      
      return findAirportRoute(destVal, endA, routeList)
    else:
      return routeList  

         
print"--------------------------"
airportList = ['LVA', 'SJC', 'ORD', 'LVA', 'JFK', 'ORD', 'SJC', 'SEA']      
createAirportDict(airportList)
print findAirportRoute('JFK', 'SEA', [])
print"--------------------------"      
     