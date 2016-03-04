# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:55:09 2015

@author: akond
"""



def giveConnection():
    import pymysql.cursors
    codealike_host = "localhost"
    codealike_user = "codealike"
    codealike_password = "codealike"
    codealike_database = "codealike"
    # Connect to the database
    codealike_connection = pymysql.connect(host=codealike_host,
                                 user=codealike_user,
                                 password=codealike_password,
                                 db=codealike_database,
                                 cursorclass=pymysql.cursors.DictCursor) 
    return codealike_connection 