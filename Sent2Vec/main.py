# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:46:44 2016

@author: akond
"""



import resgen
import sys 



####### Open loggger ####
old_stdout = sys.stdout
output_file_name="tsv_100000.txt"
log_file = open( output_file_name,  "w")
sys.stdout = log_file





#dir_to_read="/Users/akond/Documents/Simila_Work/MicrosoftChallenge/paikhan"
dir_to_read="/Users/akond/Documents/Simila_Work/MicrosoftChallenge/for-tsv"
dir_to_write="/Users/akond/Documents/Simila_Work/MicrosoftChallenge/tsv_output"
num_of_dcos = 100000
resgen.createcombinatorialFiles(dir_to_read, num_of_dcos, dir_to_write)





#### close logger       
sys.stdout = old_stdout
log_file.close()  
