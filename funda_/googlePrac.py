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



def googleProblemThree(inpList):
   holderList = [x_ for x_ in xrange(100)]
   tempList=[]
   outList = []
   #print holderList[-1]
   for elem in holderList:
     if elem not in inpList:
        #print elem
        tempList.append(elem)
        #print tempList
     elif elem in inpList:
        outList.append(tempList)
        tempList= []
     if holderList[-1]==elem:
        #print "asi mama", tempList
        outList.append(tempList)
        tempList= []
   #print outList
   for subList in outList:
     f_ = subList[0]
     l_ = subList[-1]
     print "{}-{}".format(f_, l_)  
employeeDict={'AAA':['BBB', 'CCC', 'EEE'], 'CCC':['DDD']}
#googleProblemOne(employeeDict)
number_ = 6
lol= [[1, 2], [3, 4]]
out_ = googleProblemTwo(lol, number_)
#print out_


inputList=[3, 5, 51]
googleProblemThree(inputList)
