'''
Dec 04, 2016: Akond, Radix Sort
'''

def performRadixSort(inpList):
    dict_ = {}
    for cnt_ in xrange(10):
        dict_[cnt_]=[]
    for elem in inpList:
        indexToPut = elem % (10**1)
        tmp_ = dict_[indexToPut]
        updated = tmp_ + [elem]
        dict_[indexToPut] = updated
    newDict={}
    for cnt_ in xrange(10):
        newDict[cnt_]=[]
    for k_, v_ in dict_.iteritems():
       for elem_ in v_:
         indexToPut = elem_ / (10**1)
         tmp_ = newDict[indexToPut]
         updated_ = tmp_ + [elem_]
         newDict[indexToPut] = updated_
    return newDict

def performCountingSort(inpParam):
    m = max(inpParam) + 1
    temp_holder=[0]*m
    output = []
    print "orig:{}, temp:{}".format(len(inpParam), len(temp_holder))
    for elem in inpParam:
        temp_holder[elem] = temp_holder[elem] + 1
    total= 0
    for ind_ in xrange(len(temp_holder)):
        oldCount = temp_holder[ind_]
        total = total + oldCount
        temp_holder[ind_] = total
    k = len(inpParam) - 1
    output = [0]*m
    while k >= 0:
        elem_ = inpParam[k]
        indexToPut =  temp_holder[elem_]
        output[indexToPut] = elem_
        k = k - 1
    return output
input_=[23, 1, 2, 11, 7, 50, 19]
radix_answer = performRadixSort(input_)
#print radix_answer
counting_answer = performCountingSort(input_)
print counting_answer
