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



def googleProblemTwo(stackList, number):
   tracker = []
   checker_ = 0
   while checker_  <= number:
     if checker_==number:
         break
     else:
       for stack in stackList:
         popElem = stack.pop()
         tracker = tracker + [popElem]
         checker_ =  sum(tracker)
   return tracker
employeeDict={'AAA':['BBB', 'CCC', 'EEE'], 'CCC':['DDD']}
#googleProblemOne(employeeDict)
number_ = 6
lol= [[1, 2], [3, 4]]
out_ = googleProblemTwo(lol, number_)
print out_
