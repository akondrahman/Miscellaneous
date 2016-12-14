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


def GoogleProbTwo(arrayP):
   for x_ in xrange(len(arrayP)):
    fHalf = arrayP[0:x_+1]
    lHalf = arrayP[x_+1:]
    if (sum(fHalf)==sum(lHalf)):
        print "The index is:", x_

arra_=[5, 1, 3, 4, 7, 6, 1, 2]
GoogleProbOne(arra_)
