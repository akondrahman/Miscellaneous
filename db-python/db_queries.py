# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:55:31 2015

@author: akond
"""
#### PEARSON ZONE ##############
def doDummyQuery():
 import db_connection 
 connection = db_connection.giveConnection() 
 try:
    with connection.cursor() as cursor: 
     sql = 'SELECT * from `dummy` WHERE  `temp`=%s'
     dataTuple=('99')
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     print(result)

 finally:
   connection.close()    
#doDummyQuery()     



def queryOne(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result  
def queryTwo(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result     
def queryThree(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result      
def queryFour(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def queryFive(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def querySix(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result   
def query7(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query8(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query9(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result    
def query10(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query11(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query12(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result  
################# PRINT FOCUS DETAILS ############## 
def query13(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result



def query14(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query15(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`< %s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query16(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_StateI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result



def query17(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_StateI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query18(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_StateI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 



def query19(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result



def query20(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query21(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result  
 
 
################# PRINT File Interleaving DETAILS ##############  
def query22(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result



def query23(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query24(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_focus_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result   
 
################# PRINT File Interleaving DETAILS ##############  
def query25(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_fileInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result



def query26(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_fileInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query27(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_fileInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result   
 
################# PRINT Project Interleaving  DETAILS ##############  
 
def query28(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_projectInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result



def query29(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_projectInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
 
 
def query30(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_projectInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result


################# PRINT State Interleaving  DETAILS ##############  
def query31(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_stateInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_StateI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result

def query32(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_stateInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_StateI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
def query33(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_stateInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_StateI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 

################# PRINT Namespace Interleaving  DETAILS ##############  
def query34(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_nspaceInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result

def query35(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_nspaceInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
def query36(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_nspaceInterleaving_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 


################# PRINT Unique FILE  Interleaving  DETAILS ##############  
def query37(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_ufile_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result

def query38(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_ufile_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
def query39(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_ufile_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_FileI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result  
################# PRINT Unique PROJECT  Interleaving  DETAILS ##############  
def query40(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_uProject_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result

def query41(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_uProject_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
def query42(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_uProject_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_ProjI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result


################# PRINT Unique NAMESPACE  Interleaving  DETAILS ##############  
def query43(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_unspace_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result

def query44(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`>=%s AND `pearson`<=%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_unspace_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.0", "0.499", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result 
 
def query45(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=[]
 try:
    with connection.cursor() as cursor: 
     sql2 = "SELECT `fileName` FROM `file_correlation_summary` WHERE `corr_category`=%s AND `pearson`<%s AND `pearson_p`<=%s AND `foc_type`=%s  AND `thresholdP`=%s"
     sql1 = "SELECT  `mean` FROM `file_unspace_summary` WHERE `foc_type`=%s AND fileName IN "
     sql = sql1 + "( " + sql2 + " )" 
     dataTuple=("H", "Foc_NamespaceI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print "ZZZZ", result

 finally:
   connection.close() 
 return result   
############ SPEARMAN ZONE #################
def query46(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result  
def query47(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result     
def query48(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result      
def query49(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query50(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query51(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result   
def query52(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query53(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query54(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result    
def query55(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query56(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`<=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.499", "0.0", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query57(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `spearman`>=%s AND `spearman_p`<=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.50", "0.05", "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result  
############ MIC ZONE #################
def query58(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`>=%s AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.50",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result  
def query59(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.499", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result     
def query60(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_FileI", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result      
def query61(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query62(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.499", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query63(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_ProjI", "0.50",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result   
def query64(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query65(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.499", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query66(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_StateI", "0.50",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result    
def query67(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result        
def query68(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`<=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.499", "0.0",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result 
def query69(thresholdParam):
 import db_connection 
 connection = db_connection.giveConnection() 
 result=0
 try:
    with connection.cursor() as cursor: 
     sql = "SELECT COUNT(`fileName`) FROM `file_correlation_summary` WHERE `corr_category`=%s AND `mic`>=%s  AND `foc_type`=%s AND `thresholdP`=%s"
     dataTuple=("Foc_NamespaceI", "0.50",  "H", thresholdParam)
     cursor.execute(sql, dataTuple)
     result = cursor.fetchall()
     #print(result)

 finally:
   connection.close() 
 return result   
def performSessCategoriBasedOnPosCorrelation(
        thresholdP, 
        sessHeavy,
        sessCat, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql1 = "SELECT COUNT(`sessionID`) FROM `sess_Focus_heaviness` WHERE `focVal`>=1.0 AND `thresholdP`=%s AND "
         sql2 = " `sessHeavy`=%s AND `sessCat`=%s AND fileName IN (SELECT `fileName` FROM `file_correlation_summary` WHERE `pearson` >=%s AND pearson_p <=%s "
         sql3 = " AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s) " 
         sql = sql1 + sql2 + sql3
         dataTuple=(   thresholdP,  sessHeavy, 
                     sessCat, pearson, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result         
      
      
      
def performSessCategoryBasedOnMedCorrelation(
        thresholdP, 
        sessHeavy,
        sessCat, 
        pearson1, 
        pearson2,         
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql1 = "SELECT COUNT(`sessionID`) FROM `sess_Focus_heaviness` WHERE `focVal`>=1.0 AND `thresholdP`=%s AND "
         sql2 = " `sessHeavy`=%s AND `sessCat`=%s AND fileName IN (SELECT `fileName` FROM `file_correlation_summary`  "
         sql3 = "WHERE `pearson` <=%s AND `pearson`>=%s AND pearson_p <=%s " 
         sql4 =  "AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s)"
         sql = sql1 + sql2 + sql3 + sql4 
         dataTuple=(   thresholdP,  sessHeavy, 
                     sessCat, pearson1, pearson2, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result 


def performSessCategoryBasedOnNegCorrelation(
        thresholdP, 
        sessHeavy,
        sessCat, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql1 = "SELECT COUNT(`sessionID`) FROM `sess_Focus_heaviness` WHERE `focVal`>=1.0 AND `thresholdP`=%s AND "
         sql2 = " `sessHeavy`=%s AND `sessCat`=%s AND fileName IN (SELECT `fileName` FROM `file_correlation_summary` WHERE `pearson` < %s AND pearson_p <=%s "
         sql3 = " AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s) " 
         sql = sql1 + sql2 + sql3
         dataTuple=(   thresholdP,  sessHeavy, 
                     sessCat, pearson, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result  
  
def getAllCorrelationCategories():    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql = " SELECT DISTINCT(`corr_category`) FROM `file_correlation_summary`"
         cursor.execute(sql)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result             
def performFileExtQuery(cntTypeItem, tableP):
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql = " SELECT `" + cntTypeItem + "` FROM `"+ tableP +"`"
         cursor.execute(sql)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result            

########## session duration of highly productive sessions for different correlations ############## 
def getSessDurPosCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql1 = " SELECT `mean` FROM `file_duration_summary` WHERE `foc_type`=%s AND `thresholdP`=%s AND `fileName` IN  "
         sql2 = " (SELECT `fileName` FROM `file_correlation_summary` WHERE `pearson` >=%s  "
         sql3 = " AND `pearson_p` <=%s AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s) " 
         sql = sql1 + sql2 + sql3
         dataTuple=( focType,  thresholdP,  pearson, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result         
      

       
      
def getSessDurMedCorrelation(
        thresholdP, 
        pearson1, 
        pearson2,         
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql1 = "SELECT `mean` FROM `file_duration_summary` WHERE foc_type=%s AND `thresholdP`=%s AND fileName IN "
         sql2 = "  (SELECT `fileName` FROM `file_correlation_summary` WHERE `pearson` <=%s   "
         sql3 = "AND pearson >=%s AND pearson_p <=%s  " 
         sql4 =  "AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s)"
         sql = sql1 + sql2 + sql3 + sql4 
         dataTuple=( focType,   thresholdP, pearson1, pearson2, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result 

 


def getSessDurNegCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql1 = " SELECT `mean` FROM `file_duration_summary` WHERE `foc_type`=%s AND `thresholdP`=%s AND `fileName` IN  "
         sql2 = " (SELECT `fileName` FROM `file_correlation_summary` WHERE `pearson` <%s  "
         sql3 = " AND `pearson_p` <=%s AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s) " 
         sql = sql1 + sql2 + sql3
         dataTuple=( focType,  thresholdP,  pearson, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result    
########## session duration of highly productive sessions for different correlations ############## 
def getSessCountPosCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql2 = " SELECT `foc_type_cnt` FROM `file_correlation_summary` WHERE `pearson` >=%s  "
         sql3 = " AND `pearson_p` <=%s AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s " 
         sql =  sql2 + sql3
         dataTuple=(  pearson, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result         
def getSessCountMedCorrelation(
        thresholdP, 
        pearson1, 
        pearson2,         
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql2 = "  SELECT `foc_type_cnt` FROM `file_correlation_summary` WHERE `pearson` <=%s   "
         sql3 = "AND pearson >=%s AND pearson_p <=%s  " 
         sql4 =  "AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s"
         sql =  sql2 + sql3 + sql4 
         dataTuple=( pearson1, pearson2, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result 
def getSessCountNegCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql2 = " SELECT `foc_type_cnt` FROM `file_correlation_summary` WHERE `pearson` <%s  "
         sql3 = " AND `pearson_p` <=%s AND `corr_category`=%s AND `foc_type`=%s AND `thresholdP`=%s " 
         sql =  sql2 + sql3
         dataTuple=(   pearson, pearson_p, corr_Cat, focType, thresholdP)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result    
      
########## session duration of highly productive sessions for different correlations ############## 
def getSessCharOverall(
        fieldNameP, 
        thresholdP, 
        focType
    ):    
      import db_connection 
      connection = db_connection.giveConnection() 
      result=0
      try:
        with connection.cursor() as cursor: 
         sql = " SELECT `"+ fieldNameP   +"` FROM `file_duration_summary` WHERE `thresholdP`=%s AND `foc_type`=%s"
         dataTuple=(thresholdP, focType)
         cursor.execute(sql, dataTuple)
         result = cursor.fetchall()
         #print(result)
      finally:
        connection.close() 
      return result               