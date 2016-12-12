'''
Dec 12, 2016, Monday
'''

def googleProblemOne(dictParam):
    for k_, v_ in dictParam.iteritems():
        strToPrint='-' + k_ + '\n'
        for elem in v_:
            strToPrint = strToPrint + '\t' +'-' + elem + '\n'
        print strToPrint
        strToPrint=''

employeeDict={'AAA':['BBB', 'CCC', 'EEE'], 'CCC':['DDD']}
googleProblemOne(employeeDict)
