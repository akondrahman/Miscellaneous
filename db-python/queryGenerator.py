# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:25:43 2015

@author: akond
"""

import utility, plotter
import db_queries
def doCorrelationDBQueries(thresholdParam):
    print "P-E-A-R-S-O-N !!!"
    print "File interleaving .... "
    print "#####"
    queryOneRes = db_queries.queryOne(thresholdParam)
    #print "Query One: >=0.5, file interleaving ", queryOneRes
    queryTwoRes = db_queries.queryTwo(thresholdParam)
    #print "Query two: >=0.0 and <=0.499, file interleaving ", queryTwoRes 
    queryThreeRes = db_queries.queryThree(thresholdParam)
    #print "Query three: <0.0, file interleaving ", queryThreeRes
    #############
    print "Project interleaving .... "
    print "#####"
    queryFourRes = db_queries.queryFour(thresholdParam)
    #print "Query Four: < 0.0, project interleaving", queryFourRes
    queryFiveRes = db_queries.queryFive(thresholdParam)
    #print "Query Five: >=0.0 and <=0.499, project interleaving", queryFiveRes 
    querySixRes = db_queries.querySix(thresholdParam)
    #print "Query Six: >=0.5, project interleaving ", querySixRes 
    #############
    print "State interleaving .... "
    print "#####"
    query7Res = db_queries.query7(thresholdParam)
    #print "Query 7: < 0.0, state interleaving", query7Res
    query8Res = db_queries.query8(thresholdParam)
    #print "Query 8: >=0.0 and <=0.499, state interleaving", query8Res 
    query9Res = db_queries.query9(thresholdParam)
    #print "Query 9: >=0.5, state interleaving ", query9Res
    #############
    print "Namespace interleaving .... "
    print "#####"
    query10 = db_queries.query10(thresholdParam)
    #print "Query 10: < 0.0, Namespace interleaving", query10
    query11 = db_queries.query11(thresholdParam)
    #print "Query 11: >=0.0 and <=0.499, Namespace interleaving", query11 
    query12 = db_queries.query12(thresholdParam)
    #print "Query 12: >=0.5, Namespace interleaving ", query12     
    
    ##PEARSON 
    val_query1=utility.convertDictToVal(queryOneRes)
    val_query2=utility.convertDictToVal(queryTwoRes)
    val_query3=utility.convertDictToVal(queryThreeRes)
    val_query4=utility.convertDictToVal(queryFourRes)
    val_query5=utility.convertDictToVal(queryFiveRes)
    val_query6=utility.convertDictToVal(querySixRes)
    val_query7=utility.convertDictToVal(query7Res)
    val_query8=utility.convertDictToVal(query8Res)
    val_query9=utility.convertDictToVal(query9Res)
    val_query10=utility.convertDictToVal(query10)
    val_query11=utility.convertDictToVal(query11)
    val_query12=utility.convertDictToVal(query12)    
    

    pearsonList = [val_query1, val_query2, val_query3, val_query6, val_query5, val_query4, val_query9, val_query8, 
                   val_query7, val_query12, val_query11, val_query10]
    print "Plotting P-E-A-R-S-O-N as bar graphs ... "
    plotter.plotCorrelations("Pearson", pearsonList)               
    #print "Query-1", val_query1
    #print "Query-2", val_query2
    #print "Query-3", val_query3
    #print "Query-4", val_query4
    #print "Query-5", val_query5
    #print "Query-6", val_query6
    #print "Query-7", val_query7
    #print "Query-8", val_query8
    #print "Query-9", val_query9
    #print "Query-10", val_query10
    #print "Query-11", val_query11
    #print "Query-12", val_query12    
def getDetails(thresholdParam):
    #############
    print "Focus details .... for namespace interleaving correlation"
    query13 = db_queries.query13(thresholdParam)
    #print "Query 13: focus details corr >= 0.50 ", len(query13)
    
    query14 = db_queries.query14(thresholdParam)
    #print "Query 14: focus details corr >= 0.0 and corr <=0.499 ", len(query14)
    query15 = db_queries.query15(thresholdParam)
    #print "Query 15: focus details corr < 0.0 ", len(query15)
    #############
    print "Focus details .... for state interleaving correlation"
    query16 = db_queries.query16(thresholdParam)
    #print "Query 16: focus details corr >= 0.50 ", len(query16)
    query17 = db_queries.query17(thresholdParam)
    #print "Query 17: focus details corr >= 0.0 and corr <=0.499 ", len(query17)
    query18 = db_queries.query18(thresholdParam)
    #print "Query 18: focus details corr < 0.0 ", len(query18)
    #############
    print "Focus details .... for project interleaving correlation"
    query19 = db_queries.query19(thresholdParam)
    #print "Query 19: focus details corr >= 0.50 ", len(query19)
    query20 = db_queries.query20(thresholdParam)
    #print "Query 20: focus details corr >= 0.0 and corr <=0.499 ", len(query20)
    query21 = db_queries.query21(thresholdParam)
    #print "Query 21: focus details corr < 0.0 ", len(query21)
    #############
    print "File Interleaving details .... for file interleaving correlation"
    query22 = db_queries.query22(thresholdParam)
    #print "Query 22: focus details corr >= 0.50 ", len(query22)
    query23 = db_queries.query23(thresholdParam)
    #print "Query 23: focus details corr >= 0.0 and corr <=0.499 ", len(query23)
    query24 = db_queries.query24(thresholdParam)
    #print "Query 24: focus details corr < 0.0 ", len(query24)
    #############
    print "Focus details .... for file interleaving correlation"
    query25 = db_queries.query25(thresholdParam)
    #print "Query 25:  details corr >= 0.50 ", len(query25)
    query26 = db_queries.query26(thresholdParam)
    #print "Query 26:  details corr >= 0.0 and corr <=0.499 ", len(query26)
    query27 = db_queries.query27(thresholdParam)
    #print "Query 27:  details corr < 0.0 ", len(query27)
    #############
    print "Project interleaving details .... for project interleaving correlation"
    query28 = db_queries.query28(thresholdParam)
    #print "Query 28:  details corr >= 0.50 ", len(query28)
    query29 = db_queries.query29(thresholdParam)
    #print "Query 29:  details corr >= 0.0 and corr <=0.499 ", len(query29)
    query30 = db_queries.query30(thresholdParam)
    #print "Query 30:  details corr < 0.0 ", len(query30)
    #############
    print "State details .... for state interleaving correlation"
    query31 = db_queries.query31(thresholdParam)
    #print "Query 31:  details corr >= 0.50 ", len(query31)
    query32 = db_queries.query32(thresholdParam)
    #print "Query 32:  details corr >= 0.0 and corr <=0.499 ", len(query32)
    query33 = db_queries.query33(thresholdParam)
    #print "Query 33:  details corr < 0.0 ", len(query33)
    #############
    print "Namespace interleaving details .... for namespace interleaving correlation"
    query34 = db_queries.query34(thresholdParam)
    #print "Query 34:  details corr >= 0.50 ", len(query34)
    query35 = db_queries.query35(thresholdParam)
    #print "Query 35:  details corr >= 0.0 and corr <=0.499 ", len(query35)
    query36 = db_queries.query36(thresholdParam)
    #print "Query 36:  details corr < 0.0 ", len(query36)   
    ################ CONVERSION OF DICTS TO LISTS ###########
    list_query13=utility.convertDictToList(query13)
    list_query14=utility.convertDictToList(query14)
    list_query15=utility.convertDictToList(query15) 
    print "---------------------"    
    print "Getting box-plots done for F-O-C-U-S values in Namespace Interleaving Correlation ... " 
    plotter.compareViaBoxPlot(list_query13, list_query14, list_query15, "Focus_Values_In_Namespace_Corr")
    print "---------------------"
    # t - test 
    print "doing T-Tests for F-O-C-U-S values in Namespace Interleaving Correlation ... " 
    t_13_14, p_13_14 =  utility.doTTest(list_query13, list_query14)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_13_14, p_13_14)    
    t_13_15, p_13_15 =  utility.doTTest(list_query13, list_query15)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_13_15, p_13_15)        
    t_14_15, p_14_15 =  utility.doTTest(list_query14, list_query15)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_14_15, p_14_15)    
    print "---------------------"                
    # A12 - test 
    print "doing A12 for F-O-C-U-S values in Namespace Interleaving  Correlation ... " 
    a12_13_14 =  utility.performA12(list_query13, list_query14)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_13_14)    
    a12_13_15 =  utility.performA12(list_query13, list_query15)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_13_15)        
    a12_14_15 =  utility.performA12(list_query14, list_query15)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_14_15)           
    print "---------------------"                
    list_query16=utility.convertDictToList(query16)
    list_query17=utility.convertDictToList(query17)
    list_query18=utility.convertDictToList(query18)
    print "---------------------"    
    print "Getting box-plots done for F-O-C-U-S values in State Interleaving Correlation ... "     
    plotter.compareViaBoxPlot(list_query16, list_query17, list_query18, "Focus_Values_In_State_Corr")
    print "---------------------"
    # t - test 
    print "doing T-Tests for F-O-C-U-S values in State Interleaving Correlation ... " 
    t_16_17, p_16_17 =  utility.doTTest(list_query16, list_query17)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_16_17, p_16_17)    
    t_16_18, p_16_18 =  utility.doTTest(list_query16, list_query18)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_16_18, p_16_18)        
    t_17_18, p_17_18 =  utility.doTTest(list_query17, list_query18)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_17_18, p_17_18)                
    print "---------------------"                
    # A12 - test 
    print "doing A12 for F-O-C-U-S values in State Interleaving  Correlation ... " 
    a12_16_17 =  utility.performA12(list_query16, list_query17)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_16_17)    
    a12_16_18 =  utility.performA12(list_query16, list_query18)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_16_18)        
    a12_17_18 =  utility.performA12(list_query17, list_query18)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_17_18)           
    print "---------------------"                                                                                                                                                                    
    list_query19=utility.convertDictToList(query19)
    list_query20=utility.convertDictToList(query20)
    list_query21=utility.convertDictToList(query21)
    print "---------------------"    
    print "Getting box-plots done for F-O-C-U-S values in Project Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query19, list_query20, list_query21, "Focus_Values_In_Project_Corr") 
    print "---------------------"    
    # t - test 
    print "doing T-Tests for F-O-C-U-S values in Project Interleaving Correlation ... " 
    t_19_20, p_19_20 =  utility.doTTest(list_query19, list_query20)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_19_20, p_19_20)    
    t_19_21, p_19_21 =  utility.doTTest(list_query19, list_query21)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_19_21, p_19_21)        
    t_20_21, p_20_21 =  utility.doTTest(list_query20, list_query21)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_20_21, p_20_21)        
    print "---------------------"                
    # A12 - test 
    print "doing A12 for F-O-C-U-S values in Project Interleaving  Correlation ... " 
    a12_19_20 =  utility.performA12(list_query19, list_query20)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_19_20)    
    a12_19_21 =  utility.performA12(list_query19, list_query21)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_19_21)        
    a12_20_21 =  utility.performA12(list_query20, list_query21)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_20_21)           
    print "---------------------"                                                                                                                                                                
    list_query22=utility.convertDictToList(query22)
    list_query23=utility.convertDictToList(query23)
    list_query24=utility.convertDictToList(query24)
    print "---------------------"    
    print "Getting box-plots done for F-O-C-U-S  values in File Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query22, list_query23, list_query24, "Focus_Values_In_File_Corr")    
    print "---------------------"    
    # t - test 
    print "doing T-Tests for F-O-C-U-S values in File Interleaving Correlation ... " 
    t_22_23, p_22_23 =  utility.doTTest(list_query22, list_query23)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_22_23, p_22_23)    
    t_22_24, p_22_24 =  utility.doTTest(list_query22, list_query24)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_22_24, p_22_24)        
    t_23_24, p_23_24 =  utility.doTTest(list_query23, list_query24)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_23_24, p_23_24) 
    print "---------------------"                
    # A12 - test 
    print "doing A12 for F-O-C-U-S values in File Interleaving  Correlation ... " 
    a12_22_23 =  utility.performA12(list_query22, list_query23)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_22_23)    
    a12_22_24 =  utility.performA12(list_query22, list_query24)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_22_24)        
    a12_23_24 =  utility.performA12(list_query23, list_query24)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_23_24)           
    print "---------------------"                                                                                                                                                    
    list_query25=utility.convertDictToList(query25)
    list_query26=utility.convertDictToList(query26)
    list_query27=utility.convertDictToList(query27)
    print "---------------------"    
    print "Getting box-plots done for F-I-L-E interleaving values in File Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query25, list_query26, list_query27, "File_Values_In_File_Corr")    
    print "---------------------"            
    # t - test 
    print "doing T-Tests for F-I-L-E interleaving values in File Interleaving Correlation ... " 
    t_25_26, p_25_26 =  utility.doTTest(list_query25, list_query26)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_25_26, p_25_26)    
    t_25_27, p_25_27 =  utility.doTTest(list_query25, list_query27)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_25_27, p_25_27)        
    t_26_27, p_26_27 =  utility.doTTest(list_query26, list_query27)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_26_27, p_26_27)                        
    list_query28=utility.convertDictToList(query28)
    list_query29=utility.convertDictToList(query29)
    list_query30=utility.convertDictToList(query30)
    print "---------------------"                
    # A12 - test 
    print "doing A12 for F-I-L-E interleaving values in File Interleaving Correlation ... " 
    a12_25_26 =  utility.performA12(list_query25, list_query26)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_25_26)    
    a12_25_27 =  utility.performA12(list_query25, list_query27)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_25_27)        
    a12_26_27 =  utility.performA12(list_query26, list_query27)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_26_27)           
    print "---------------------"                                                                                                                         
    print "---------------------"    
    print "Getting box-plots done for P-R-O-J-E-C-T interleaving values in Project Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query28, list_query29, list_query30, "Project_Values_In_Project_Corr")     
    print "---------------------"      
    # t - test 
    print "doing T-Tests for P-R-O-J-E-C-T  interleaving values in Project Interleaving Correlation ... " 
    t_28_29, p_28_29 =  utility.doTTest(list_query28, list_query29)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_28_29, p_28_29)    
    t_28_30, p_28_30 =  utility.doTTest(list_query28, list_query30)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_28_30, p_28_30)        
    t_29_30, p_29_30 =  utility.doTTest(list_query29, list_query30)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_29_30, p_29_30)                                 
    list_query31=utility.convertDictToList(query31)
    list_query32=utility.convertDictToList(query32)
    list_query33=utility.convertDictToList(query33)
    print "---------------------"                
    # A12 - test 
    print "doing A12 for P-R-O-J-E-C-T  interleaving values in Project Interleaving Correlation ... " 
    a12_28_29 =  utility.performA12(list_query28, list_query29)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_28_29)    
    a12_28_30 =  utility.performA12(list_query28, list_query30)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_28_30)        
    a12_29_30 =  utility.performA12(list_query29, list_query30)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_29_30)           
    print "---------------------"                                                                                                                     
    print "---------------------"    
    print "Getting box-plots done for S-T-A-T-E interleaving values in STATE Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query31, list_query32, list_query33, "State_Values_In_State_Corr")   
    print "---------------------"                     
    # t - test 
    print "doing T-Tests for S-T-A-T-E interleaving values in STATE Interleaving  Correlation ... " 
    t_31_32, p_31_32 =  utility.doTTest(list_query31, list_query32)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_31_32, p_31_32)    
    t_31_33, p_31_33 =  utility.doTTest(list_query31, list_query33)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_31_33, p_31_33)        
    t_32_33, p_32_33 =  utility.doTTest(list_query32, list_query33)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_32_33, p_32_33)  
    print "---------------------"                
    # A12 - test 
    print "doing A12 for S-T-A-T-E interleaving values in STATE Interleaving Correlation ... " 
    a12_31_32 =  utility.performA12(list_query31, list_query32)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_31_32)    
    a12_31_33 =  utility.performA12(list_query31, list_query33)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_31_33)        
    a12_32_33 =  utility.performA12(list_query32, list_query33)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_32_33)           
    print "---------------------"                                                                                                                 
                                   
    list_query34=utility.convertDictToList(query34)
    list_query35=utility.convertDictToList(query35)
    list_query36=utility.convertDictToList(query36) 
    print "---------------------"    
    print "Getting box-plots done for N-A-M-E-S-P-A-C-E interleaving values in NAMESPACE Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query34, list_query35, list_query36, "Namespace_Values_In_Namespace_Corr")    
    print "---------------------"                
    # t - test 
    print "doing T-Tests for N-A-M-E-S-P-A-C-E interleaving values in NAMESPACE Interleaving  Correlation ... " 
    t_34_35, p_34_35 =  utility.doTTest(list_query34, list_query35)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_34_35, p_34_35)    
    t_34_36, p_34_36 =  utility.doTTest(list_query34, list_query36)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_34_36, p_34_36)        
    t_35_36, p_35_36 =  utility.doTTest(list_query35, list_query36)
    print " 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_35_36, p_35_36)   




    print "---------------------"                
    # A12 - test 
    print "doing A12 for N-A-M-E-S-P-A-C-E interleaving values in NAMESPACE Interleaving Correlation ... " 
    a12_34_35 =  utility.performA12(list_query34, list_query35)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_34_35)    
    a12_34_36 =  utility.performA12(list_query34, list_query36)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_34_36)        
    a12_35_36 =  utility.performA12(list_query35, list_query36)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_35_36)           
    print "---------------------"                                                                                                                 
                                          
    #print "Printting lists ... " 
    #print "Query-13", list_query13
    #print "Query-14", list_query14
    #print "Query-15", list_query15
    #print "Query-16", list_query16
    #print "Query-17", list_query17
    #print "Query-18", list_query18
    #print "Query-19", list_query19
    ###
    #print "Query-20", list_query20
    #print "Query-21", list_query21
    #print "Query-22", list_query22
    #print "Query-23", list_query23
    #print "Query-24", list_query24
    #print "Query-25", list_query25
    #print "Query-26", list_query26
    #print "Query-27", list_query27
    #print "Query-28", list_query28
    #print "Query-29", list_query29
    #print "Query-30", list_query30    
    ###

    #print "Query-31", list_query31
    #print "Query-32", list_query32
    #print "Query-33", list_query33
    #print "Query-34", list_query34
    #print "Query-35", list_query35
    #print "Query-36", list_query36    

def getUniqueFileDetails(thresholdParam):
    #############
    print "Unique file details .... for file interleaving correlation"
    query37 = db_queries.query37(thresholdParam)
    #print "Query 37: file details corr >= 0.50 ", len(query37)
    query38 = db_queries.query38(thresholdParam)
    #print "Query 38: file details corr >= 0.0 and corr <=0.499 ", len(query38)
    query39 = db_queries.query39(thresholdParam)
    #print "Query 39: file details corr < 0.0 ", len(query39)
    list_query37=utility.convertDictToList(query37)
    list_query38=utility.convertDictToList(query38)
    list_query39=utility.convertDictToList(query39)  
    print "Getting box-plots done for U-N-I-Q-U-E F-I-L-E  counts in File Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query37, list_query38, list_query39, "Unique_File_Counts_In_File_Corr")                                
    #print "Query-37", list_query37
    #print "Query-38", list_query38
    #print "Query-39", list_query39  
    print "---------------------"                
    # t - test 
    print "doing T-Tests for U-N-I-Q-U-E F-I-L-E interleaving values in FILE Interleaving  Correlation ... " 
    t_37_38, p_37_38 =  utility.doTTest(list_query37, list_query38)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_37_38, p_37_38)    
    t_37_39, p_37_39 =  utility.doTTest(list_query37, list_query39)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_37_39, p_37_39)        
    t_38_39, p_38_39 =  utility.doTTest(list_query38, list_query39)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_38_39, p_38_39)  
    print "---------------------"                
    # A12 - test 
    print "doing A12 for U-N-I-Q-U-E F-I-L-E interleaving values in FILE Interleaving Correlation ... " 
    a12_37_38 =  utility.performA12(list_query37, list_query38)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_37_38)    
    a12_37_39 =  utility.performA12(list_query37, list_query39)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_37_39)        
    a12_38_39 =  utility.performA12(list_query38, list_query39)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_38_39)           
    print "---------------------"                                                                                                                 
def getUniqueProjDetails(thresholdParam):    
    #############
    print "Unique project details .... for project interleaving correlation"
    query40 = db_queries.query40(thresholdParam)
    #print "Query 40:  details corr >= 0.50 ", len(query40)
    query41 = db_queries.query41(thresholdParam)
    #print "Query 41:  details corr >= 0.0 and corr <=0.499 ", len(query41)
    query42 = db_queries.query42(thresholdParam)
    #print "Query 42:  details corr < 0.0 ", len(query42)
    
    list_query40=utility.convertDictToList(query40)
    list_query41=utility.convertDictToList(query41)
    list_query42=utility.convertDictToList(query42)    
    ###
    print "Getting box-plots done for U-N-I-Q-U-E P-R-O-J-E-C-T  counts in Project Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query40, list_query41, list_query42, "Unique_Project_Counts_In_Project_Corr")                                    
    print "---------------------"                
    # t - test 
    print "doing T-Tests for U-N-I-Q-U-E P-R-O-J-E-C-T  counts in Project Interleaving Correlation ... " 
    t_40_41, p_40_41 =  utility.doTTest(list_query40, list_query41)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_40_41, p_40_41)    
    t_40_42, p_40_42 =  utility.doTTest(list_query40, list_query42)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_40_42, p_40_42)        
    t_41_42, p_41_42 =  utility.doTTest(list_query41, list_query42)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_41_42, p_41_42)                                                     
    #print "Query-40", list_query40
    #print "Query-41", list_query41
    #print "Query-42", list_query42
    print "---------------------"                
    # A12 - test 
    print "doing A12 for U-N-I-Q-U-E P-R-O-J-E-C-T  counts in Project Interleaving Correlation ... " 
    a12_40_41 =  utility.performA12(list_query40, list_query41)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_40_41)    
    a12_40_42 =  utility.performA12(list_query40, list_query42)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_40_42)        
    a12_41_42 =  utility.performA12(list_query41, list_query42)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_41_42)           
    print "---------------------"                                                                  
def getUniqueNamespaceDetails(thresholdParam):    
    #############
    print "Unique namespace details .... for namespace interleaving correlation"
    query43 = db_queries.query43(thresholdParam)
    #print "Query 43:  details corr >= 0.50 ", len(query43)
    query44 = db_queries.query44(thresholdParam)
    #print "Query 44:  details corr >= 0.0 and corr <=0.499 ", len(query44)
    query45 = db_queries.query45(thresholdParam)
    #print "Query 45:  details corr < 0.0 ", len(query45)
    list_query43=utility.convertDictToList(query43)
    list_query44=utility.convertDictToList(query44)
    list_query45=utility.convertDictToList(query45)    
    print "Getting box-plots done for U-N-I-Q-U-E N-A-M-E-S-P-A-C-E  counts in Namespace Interleaving Correlation ... "         
    plotter.compareViaBoxPlot(list_query43, list_query44, list_query45, "Unique_NSpace_Counts_In_NSpace_Corr")                                        
    print "---------------------"                
    # t - test 
    print "doing T-Tests for  U-N-I-Q-U-E N-A-M-E-S-P-A-C-E  counts in Namespace Interleaving Correlation ... " 
    t_43_44, p_43_44 =  utility.doTTest(list_query43, list_query44)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> t: {}, p:{}".format(t_43_44, p_43_44)    
    t_43_45, p_43_45 =  utility.doTTest(list_query43, list_query45)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_43_45, p_43_45)        
    t_44_45, p_44_45 =  utility.doTTest(list_query44, list_query45)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> t: {}, p:{}".format(t_44_45, p_44_45)                                                     
    #print "Query-43", list_query43
    #print "Query-44", list_query44
    #print "Query-45", list_query45    
    print "---------------------"                
    # A12 - test 
    print "doing A12 for  U-N-I-Q-U-E N-A-M-E-S-P-A-C-E  counts in Namespace Interleaving Correlation ... " 
    a12_43_44 =  utility.performA12(list_query43, list_query44)
    print "Corr >= 0.50 vs 0.0 <= Corr <= 0.499 =====> a12: {}".format(a12_43_44)    
    a12_43_45 =  utility.performA12(list_query43, list_query45)
    print "Corr >= 0.50 vs  Corr < 0.0 =====> a12: {}".format(a12_43_45)        
    a12_44_45 =  utility.performA12(list_query44, list_query45)
    print "Corr 0.499 >= Corr >= 0.0 vs  Corr < 0.0 =====> a12: {}".format(a12_44_45)           
    print "---------------------"                                                              
def doSpearman(thresholdParam):    
    print "S-P-E-A-R-M-A-N !!!"
    print "File interleaving .... "
    print "#####"
    ###############SPEARMAN !! ########
    query46 = db_queries.query46(thresholdParam)
    #print "Query 46: >=0.5, file interleaving ", query46
    query47 = db_queries.query47(thresholdParam)
    #print "Query 47: >=0.0 and <=0.499, file interleaving ", query47 
    query48 = db_queries.query48(thresholdParam)
    #print "Query 48: <0.0, file interleaving ", query48
    #############
    print "Project interleaving .... "
    print "#####"
    query49 = db_queries.query49(thresholdParam)
    #print "Query 49: < 0.0, project interleaving", query49
    query50 = db_queries.query50(thresholdParam)
    #print "Query 50: >=0.0 and <=0.499, project interleaving", query50 
    query51 = db_queries.query51(thresholdParam)
    #print "Query 51: >=0.5, project interleaving ", query51 
    #############
    print "State interleaving .... "
    print "#####"
    query52 = db_queries.query52(thresholdParam)
    #print "Query 52: < 0.0, state interleaving", query52
    query53 = db_queries.query53(thresholdParam)
    #print "Query 53: >=0.0 and <=0.499, state interleaving", query53
    query54 = db_queries.query54(thresholdParam)
    #print "Query 54: >=0.5, state interleaving ", query54
    #############
    print "Namespace interleaving .... "
    print "#####"
    query55 = db_queries.query55(thresholdParam)
    #print "Query 55: < 0.0, Namespace interleaving", query55
    query56 = db_queries.query56(thresholdParam)
    #print "query56: >=0.0 and <=0.499, Namespace interleaving", query56
    query57 = db_queries.query57(thresholdParam)
    #print "Query 57: >=0.5, Namespace interleaving ", query57 

    ## SPEARMAN
    val_query46=utility.convertDictToVal(query46)
    val_query47=utility.convertDictToVal(query47)
    val_query48=utility.convertDictToVal(query48)
    val_query49=utility.convertDictToVal(query49)
    val_query50=utility.convertDictToVal(query50)
    val_query51=utility.convertDictToVal(query51)
    val_query52=utility.convertDictToVal(query52)
    val_query53=utility.convertDictToVal(query53)
    val_query54=utility.convertDictToVal(query54)
    val_query55=utility.convertDictToVal(query55)
    val_query56=utility.convertDictToVal(query56)
    val_query57=utility.convertDictToVal(query57)
    print "Printting S-P-E-A-R-M-A-N ... " 
    #print "Query-46", val_query46
    #print "Query-47", val_query47
    #print "Query-48", val_query48
    #print "Query-49", val_query49
    #print "Query-50", val_query50
    #print "Query-51", val_query51
    #print "Query-52", val_query52
    #print "Query-53", val_query53
    #print "Query-54", val_query54
    #print "Query-55", val_query55
    #print "Query-56", val_query56
    #print "Query-57", val_query57 
    spearmanList = [val_query46, val_query47, val_query48, val_query51, val_query50, val_query49, val_query54, val_query53, 
                   val_query52, val_query57, val_query56, val_query55]
    print "Plotting S-P-E-A-R-M-A-N as bar graphs ... "
    plotter.plotCorrelations("Spearman", spearmanList)                   
def doMIC(thresholdParam):    
    print "M!-I!-C! (MIC) !!!"
    print "File interleaving .... "
    print "#####"
    ###############SPEARMAN !! ########
    query58 = db_queries.query58(thresholdParam)
    #print "Query 58: >=0.5, file interleaving ", query58
    query59 = db_queries.query59(thresholdParam)
    #print "Query 59: >=0.0 and <=0.499, file interleaving ", query59
    query60 = db_queries.query60(thresholdParam)
    #print "Query 60: <0.0, file interleaving ", query60
    #############
    print "Project interleaving .... "
    print "#####"
    query61 = db_queries.query61(thresholdParam)
    #print "Query 61: < 0.0, project interleaving", query61
    query62 = db_queries.query62(thresholdParam)
    #print "Query 62: >=0.0 and <=0.499, project interleaving", query62 
    query63 = db_queries.query63(thresholdParam)
    #print "Query 63: >=0.5, project interleaving ", query63
    #############
    print "State interleaving .... "
    print "#####"
    query64 = db_queries.query64(thresholdParam)
    #print "Query 64: < 0.0, state interleaving", query64
    query65 = db_queries.query65(thresholdParam)
    #print "Query 65: >=0.0 and <=0.499, state interleaving", query65
    query66 = db_queries.query66(thresholdParam)
    #print "Query 66: >=0.5, state interleaving ", query66
    #############
    print "Namespace interleaving .... "
    print "#####"
    query67 = db_queries.query67(thresholdParam)
    #print "Query 67: < 0.0, Namespace interleaving", query67
    query68 = db_queries.query68(thresholdParam)
    #print "query68: >=0.0 and <=0.499, Namespace interleaving", query68
    query69 = db_queries.query69(thresholdParam)
    #print "Query 69: >=0.5, Namespace interleaving ", query69 

    ## MIC
    val_query58=utility.convertDictToVal(query58)
    val_query59=utility.convertDictToVal(query59)
    val_query60=utility.convertDictToVal(query60)
    val_query61=utility.convertDictToVal(query61)
    val_query62=utility.convertDictToVal(query62)
    val_query63=utility.convertDictToVal(query63)
    val_query64=utility.convertDictToVal(query64)
    val_query65=utility.convertDictToVal(query65)
    val_query66=utility.convertDictToVal(query66)
    val_query67=utility.convertDictToVal(query67)
    val_query68=utility.convertDictToVal(query68)
    val_query69=utility.convertDictToVal(query69)
    print "Printing M-I-C ... " 
    MICList = [ val_query58, val_query59, val_query60, val_query63, val_query62, val_query61, val_query66, val_query65, 
                val_query64, val_query69, val_query68, val_query67]
    print "Plotting M-I-C as bar graphs ... "
    plotter.plotCorrelations("MIC", MICList)                       
    #print "Query-58", val_query58
    #print "Query-59", val_query59
    #print "Query-60", val_query60
    #print "Query-61", val_query61
    #print "Query-62", val_query62
    #print "Query-63", val_query63
    #print "Query-64", val_query64
    #print "Query-65", val_query65
    #print "Query-66", val_query66
    #print "Query-67", val_query67
    #print "Query-68", val_query68
    #print "Query-69", val_query69 
    
def performSessCategoriBasedOnPosCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        dictToRet={}
        sessHeaviness = [0, 1 , 2]
        catList = ["None", "Idle", "System", "Code", "Debug", "Build",  "Navi"]
        res = []
        for catType in catList:
          for he_ in sessHeaviness:     
           res.append(utility.convertDictToVal( db_queries.performSessCategoriBasedOnPosCorrelation(  thresholdP, he_, 
                                                     catType, pearson, pearson_p, corr_Cat, focType))  )                                        
        
          dictToRet[catType] = res
          res= []
        return dictToRet                                              
def performSessCategoryBasedOnMedCorrelation(
        thresholdP, 
        pearson1, 
        pearson2,
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        dictToRet={}
        sessHeaviness = [0, 1 , 2]
        catList = ["None", "Idle", "System", "Code", "Debug", "Build",  "Navi"]
        res = []
        for catType in catList:
          for he_ in sessHeaviness:     
           res.append(utility.convertDictToVal( db_queries.performSessCategoryBasedOnMedCorrelation(  thresholdP, he_, 
                                                     catType, pearson1, pearson2, pearson_p, corr_Cat, focType))  )                                        
        
          dictToRet[catType] = res
          res= []
        return dictToRet 




def performSessCategoryBasedOnNegCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        dictToRet={}
        sessHeaviness = [0, 1 , 2]
        catList = ["None", "Idle", "System", "Code", "Debug", "Build",  "Navi"]
        res = []
        for catType in catList:
          for he_ in sessHeaviness:     
           res.append(utility.convertDictToVal( db_queries.performSessCategoryBasedOnNegCorrelation(  thresholdP, he_, 
                                                     catType, pearson, pearson_p, corr_Cat, focType))  )                                        
        
          dictToRet[catType] = res
          res= []
        return dictToRet       
    
def getAllCorrelationCategories():  
        import db_queries, utility
        res = []
        res = utility.convertDictToList(db_queries.getAllCorrelationCategories())
        return res 
def getGeneralFileExtResult(cntList, tableP): 
  import db_queries , utility , plotter 
  dict_FileExt={}
  for cntType in cntList:
    cnt_res =  utility.convertDictToList( db_queries.performFileExtQuery(cntType, tableP))
    dict_FileExt[cntType] = cnt_res                                                       
  #print "Final result = ", dict_FileExt
  print "Plotting ..."  
  plotter.compareFileExtViaBarPlots(dict_FileExt, "avg_general_file_ext", cntList)
  plotter.compareFileExtViaBoxPlots(dict_FileExt, "general_file_ext", cntList)  
  plotter.plotSharpVSOthers(dict_FileExt, "CSharp_And_Others")
  return dict_FileExt   

#######################  session duration ############################# 
def getSessDurPosCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        res =  utility.convertDictToList( db_queries.getSessDurPosCorrelation(  thresholdP, pearson, pearson_p, corr_Cat, focType))                                      
        return res                                              
def getSessDurMedCorrelation(
        thresholdP, 
        pearson1, 
        pearson2,
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        res = utility.convertDictToList( db_queries.getSessDurMedCorrelation(  thresholdP, pearson1, pearson2, pearson_p, corr_Cat, focType))                                      
        return res                                              


def getSessDurNegCorrelation(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):  

        import db_queries, utility
        res =  utility.convertDictToList( db_queries.getSessDurNegCorrelation(  thresholdP, pearson, pearson_p, corr_Cat, focType))                                       
        return res                                              
####################  Session Count ###################
def getHighFocSessCountPosCorr(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        res =  utility.convertDictToList( db_queries.getSessCountPosCorrelation(  thresholdP, pearson, pearson_p, corr_Cat, focType))                                      
        return res                                              
def getHighFocSessCountMedCorr(
        thresholdP, 
        pearson1, 
        pearson2,
        pearson_p, 
        corr_Cat, 
        focType
    ):  
        import db_queries, utility
        res = utility.convertDictToList( db_queries.getSessCountMedCorrelation(  thresholdP, pearson1, pearson2, pearson_p, corr_Cat, focType))                                      
        return res                                              


def getHighFocSessCountNegCorr(
        thresholdP, 
        pearson, 
        pearson_p, 
        corr_Cat, 
        focType
    ):  

        import db_queries, utility
        res =  utility.convertDictToList( db_queries.getSessCountNegCorrelation(  thresholdP, pearson, pearson_p, corr_Cat, focType))                                       
        return res                                                      
####################  Session Count & Duration : Overall  ###################
def getSessCharOverall(
        fieldNameP, 
        thresholdP, 
        focType
    ):  
        import db_queries, utility
        res =  utility.convertDictToList( db_queries.getSessCharOverall( fieldNameP, thresholdP, focType))                                      
        return res                                                                          