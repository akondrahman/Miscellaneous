# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:29:41 2015

@author: akond
"""



def example():
    a = 60            # 60 = 0011 1100 
    b = 13            # 13 = 0000 1101 
    c = 0
    
    c = a & b;        # 12 = 0000 1100
    print "Line 1 - Value of c is ", c
    
    c = a | b;        # 61 = 0011 1101 
    print "Line 2 - Value of c is ", c
    
    c = a ^ b;        # 49 = 0011 0001
    print "Line 3 - Value of c is ", c
    
    c = ~a;           # -61 = 1100 0011
    print "Line 4 - Value of c is ", c
    
    c = a << 2;       # 240 = 1111 0000
    print "Line 5 - Value of c is ", c
    
    c = a >> 2;       # 15 = 0000 1111
    print "Line 6 - Value of c is ", c   
def setBit(numP, position):
  temp = 1 << position
  return numP | temp      
def clearBit(numP, position):
  temp = ~(1 << position)
  return numP & temp        
    
def getBit(numberParam, position):
#position starts from zero 
  temp =1 << position 
  return ((numberParam & temp)!=0)    
def clearMSBThroughI(num, pos):
  temp = (1 << pos) - 1 
  return num & temp 
def clearIThroughZero(num, pos):
  temp = ~(1 >> (31 - pos))  
  return num & temp     
 
def updateBits(num, pos, updates):
  temp = updates << pos 
  return clearBit(num, pos) | temp   
def gayle5_1(N, i, j, M):
  for cnt_ in xrange(i, j+1, 1): # as starts from 0 and ends at 1... we need to traverse from 0 ~ 2
    #print "traversing ", cnt_  
    N = updateBits(N, cnt_, M[cnt_])
  return N     
def gayle5_3(N):
  cnt_ = 1   
  
  while cnt_ >= 0 :
    lowerB = bin(N - cnt_)
    upperB = bin(N + cnt_)
    lowerBoundLen = lowerB.count('1') 
    upperBoundLen = upperB.count('1') 
    if lowerBoundLen == upperBoundLen:
      break;     
    else:
      cnt_ += 1   
  return lowerB, upperB   
def gayle_5_5(num1,num2):
 return bin(num1 ^ num2).count('1')     
def gayle_5_6(num1):
  str_ ='0' +  'b'  
  for cnt in xrange(2, len(bin(num1))):
    if (cnt%2 == 0):
      temp = bin(num1)[cnt]
      if cnt+1 < len(bin(num1)):
        str_ += bin(num1)[cnt+1]
        str_ += temp     
        
  return int(str_, 2)    
def gayle_5_7(arra, num_):
  answer=0   
  for cnt in xrange(num_):
    #print cnt 
    if (int(arra[cnt], 2)!=cnt):
      answer = cnt   
      #print "mismatch detected! ... ", answer
  return answer     
#example()
print "GetBit: (True means 1, False means 0)", getBit(60, 5) 
print "Setbit 2 becomes 10 ", setBit(2, 3)
print "Clearbit ---> 9 becomes  ... ", clearBit(9, 3)
print "Clear through 1 ---> 11 becomes  ... ", clearMSBThroughI(11, 1)
print "Clear through 2 ---> 15 becomes  ... ", clearMSBThroughI(15, 2)
##i through zero not working 
#print "Clear from 2 to 0 ---> 15 becomes  ... ", clearIThroughZero(15, 2)
print "Update bits: ---> 15 becomes  ... ", updateBits(15, 3, 0)
print "Gayle-5.1: "
print "N=1000, i=0, j=2, M=111--->", gayle5_1(8, 0,  2, [1,1,1])
print "Practising binary pesentation ... 8 ----->{0:b}".format(8) 
print "Gayle-5.3: "
print "A=8--->", gayle5_3(8)
print "Gayle-5.5: "
print "A=31, B=14--->", gayle_5_5(31, 14)
print "Gayle-5.6: "
print "A=13 ---> ", gayle_5_6(13)
print "Gayle-5.7: "
A=['0b0000','0b0001','0b0010','0b0100'] 
print "With n= 4 ---> ", gayle_5_7(A, 4)
 