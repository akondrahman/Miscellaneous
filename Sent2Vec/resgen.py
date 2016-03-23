# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:50:21 2016

@author: akond
"""



import os , IO_  



def splitit(lst, n):
    division = len(lst) / float(n)
    return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n) ]

def _prcessed_tokens(array_type_tokens):
  list_to_ret=[]  
  for sublist in array_type_tokens:
    sublist_token = []  
    for elem in sublist:
      sublist_token.append(elem)
    list_to_ret.append(sublist_token)
  return list_to_ret  
        

def pre_process_tokens(elem1_tokns_param, elem2_tokns_param, doc_count_param):
  #print "Count of  for file # 1 ", len(elem1_tokns_param)
  splitted_elem1_array = _prcessed_tokens( splitit(elem1_tokns_param, doc_count_param)  )  
  splitted_elem2_array = _prcessed_tokens( splitit(elem2_tokns_param, doc_count_param)  ) 
  print "Final tokens for file # 1 ", len(splitted_elem1_array[0] )
  print "Final tokens for file # 2 ", len(splitted_elem2_array[0]   )
  return splitted_elem1_array, splitted_elem2_array   
      
    

def createcombinatorialFiles(dirParam, doc_count_param, dir_to_write_Param):
  all_file_names = os.listdir(dirParam)
  valid_file_names = [x for x in all_file_names if x.endswith("dump")]
  for elem1 in valid_file_names:
    elem1_fileName= dirParam +   "/"  + elem1     
    
    elem1_tokns =  IO_.readFile(elem1_fileName) 
    #print "Count of tokens for {} is {}".format(elem1, len(elem1_tokns))

    for elem2 in valid_file_names:
        elem2_fileName= dirParam +   "/"  + elem2   

        elem2_tokns =   IO_.readFile(elem2_fileName)            
        file_name_to_write = elem1 + "_" + elem2 + ".tsv"
        print "Cmparing {} and {}".format(elem1, elem2)   
        print "Cmparing {} and {}".format(len(elem1_tokns), len(elem2_tokns))           
        bothfiletokens = pre_process_tokens(elem1_tokns, elem2_tokns, doc_count_param)   
        filtered_elem1_tokns  = bothfiletokens[0]
        filtered_elem2_tokns = bothfiletokens[1]
        IO_.writeTokensToFile(dir_to_write_Param, file_name_to_write, filtered_elem1_tokns, filtered_elem2_tokns)
        
                             