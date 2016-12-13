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



def googleProblemFour(circleParam):
  for ind1_ in xrange(len(circleParam)):
    for ind2_ in xrange(len(circleParam)):
        if ind2_ != ind1_:
            comparer_center = circleParam[ind1_][0]
            comparer_radius = circleParam[ind1_][1]
            comparee_center = circleParam[ind2_][0]
            dist_ = abs(comparer_center - comparee_center)
            if dist_ < comparer_radius:
                print "Circle#{} intersects with circle#{}".format(ind2_, ind1_)
def googleProblemFive(arrayParam):
 pivotIndex = -999
 for ind_ in xrange(len(arrayParam)):
   fHalf = ind_
   lHalf = fHalf + 1
   firstHalf  = arrayParam[0:fHalf]
   secondHalf = arrayParam[lHalf:]
   #print "f:{}, l:{}".format(firstHalf, secondHalf)
   if (sum(firstHalf)==sum(secondHalf)):
     pivotIndex = ind_
 return pivotIndex




def googleProblemSix(arrayList):
  output_ = []
  l_ = len(arrayList) + 1
  handler_ = [0]*l_
  for elem_ in arrayList:
    handler_[elem_] = handler_[elem_] + 1
  for ind_ in xrange(len(handler_)):
    if handler_[ind_] > 1:
        output_.append(ind_)
  return output_
def googleProblemSeven(theStrParam):

employeeDict={'AAA':['BBB', 'CCC', 'EEE'], 'CCC':['DDD']}
#googleProblemOne(employeeDict)
number_ = 6
lol= [[1, 2], [3, 4]]
out_ = googleProblemTwo(lol, number_)
#print out_


inputList=[3, 5, 51]
googleProblemThree(inputList)
print "*"*100
print "Circle problem"
circleStuff = [(1.00, 0.75), (2.00, 1.75), (3.00, 0.50), (4.00, 1.00), (0.00, 2.00)]
googleProblemFour(circleStuff)
print "*"*100
print "Pivot problem"
arrList=[2, 5, 4, 2, 7, 4]
pivotIndex=googleProblemFive(arrList)
print "Pivot index:", pivotIndex
print "*"*100
print "Duplicate in O(n)"
list_ = [4, 1, 3, 5, 5]
dupl_ = googleProblemSix(list_)
print dupl_
print "*"*100
theStr='2-4a0r7-4k'
outpu_ = googleProblemSeven(theStr)
