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
input=[23, 1, 2, 11, 7, 50, 19]
answer = performRadixSort(input)
print answer
