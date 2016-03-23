# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:46:11 2016

@author: akond
"""



def readFile(fileP):
  import pickle
  listToRet=[]
  listToUse = pickle.load( open( fileP, "rb" ) )
  for subList in listToUse: 
      for tokens in subList:
        listToRet.append(tokens)    
  #print "--------------Completed Loading Tokens---------------"        
  return listToRet  

def writeTokensToFile(dirToWrite, file_name_to_write, elem1_tokns, elem2_tokns):
  file_ = dirToWrite + "/" + file_name_to_write
  strToWrite=""
  if (len(elem1_tokns)==len(elem2_tokns)):
    print "Generating content ..." 
    for inde in xrange(len(elem1_tokns)):
      str_part_1=""
      str_part_2=""
      str_for_each_line=""
      for elem1 in elem1_tokns[inde]:
        #print inde  
        str_part_1 = str_part_1 + elem1 + " "    
      for elem2 in elem2_tokns[inde]:
        str_part_2 = str_part_2 + elem2 + " "    
      str_for_each_line = str_part_1 + "\t" + str_part_2
      strToWrite = strToWrite + str_for_each_line + "\n"         
           

  fileToWrite = open( file_, 'w')
  fileToWrite.write(strToWrite )  
  fileToWrite.close()               