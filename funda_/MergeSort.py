# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:00:12 2015

@author: akond
"""

def mergeSort(listP): 
 if len(listP) <=1 :
  return listP    
 mid = len(listP)/2
 left = mergeSort(listP[:mid]) 
 right = mergeSort(listP[mid:])
 return merge(left, right)
  


def merge(leftP, rightP):
  if not leftP:
    return rightP
  if not rightP:
    return leftP 
  if leftP[0] < rightP[0]:
    return [leftP[0]] + merge(leftP[1:], rightP)
  return [rightP[0]] + merge(leftP, rightP[1:]) 

##testing tiem 
listOTest = [10, 1, 4, 3, 6, 8,9, 2 , 7]
ans = mergeSort(listOTest)
print "Ans is ", ans      