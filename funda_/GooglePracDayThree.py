'''
Akond, Dec 14, Day 3
'''

def GoogleProbOne(arrayP):
  for i_ in xrange(len(arrayP)):
    for j_ in xrange(len(arrayP)):
      if j_ > i_:
        subArray = arrayP[i_: j_+1]
        sumOfSub=sum(subArray)
        if ((sumOfSub>=i_) and (sumOfSub<=j_)):
           print "Eligible sub-array:",subArray
arra_=[5, 1, 3, 4, 7, 6, 1, 2]
GoogleProbOne(arra_)
