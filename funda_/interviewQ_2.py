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
      print "buffer ......", buffer_  
      if char_ in lastCharList:
          indexToLook = lastCharList.index(char_)
          wordToLook = wordListP[indexToLook]
          #print "Word to look ", wordToLook
          lenToLook=len(wordToLook) 
          startPoint = (len(buffer_) - lenToLook) 
                    
          #print "start point ", buffer_[startPoint]
          strList =  buffer_[startPoint:-1] +   [buffer_[-1]]       
          strToCheck =  "".join(strList)   
          print "String to check: ", strToCheck          
          if strToCheck in wordListP: 
            print "Time t make that stupid API Call !"
            buffer_ = []
            
wordList=["ok", "test", "one", "try", "trying"]
stream="abcokdeftrying" 
print "API Call Problem: ", processStream(wordList, stream)           