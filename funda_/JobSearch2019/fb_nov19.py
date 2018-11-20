'''
Akond Rahman 
Just practising 
'''

def prob1(ls_1, ls_2):
    out_ls  =  []
    len_ls  = len(ls_1)
    divisor = 0 
    for k1_ in reversed(ls_1):
        ind_ = ls_1.index(k1_)
        k2_  = ls_2[ind_] 
        sum_ = divisor + k1_ + k2_
        reminder = sum_ % 10 
        divisor  = sum_ / 10 
        out_ls.append(reminder)
    if divisor == 1: 
       out_ls.append(divisor)
    out_ls = list(reversed(out_ls))
    return out_ls

def prob2(ls1, ls2):
    out_lis = []
    last_elem_lis = []
    for e in ls1:
        last_elem_lis.append(e[1])
    for e in ls2:
        last_elem_lis.append(e[1])
    for elem in ls1:
      diff = elem[1] - elem[0]
      if (elem[0]==1) and (diff==1):
         out_lis.append(elem)
      else:
          tmp_lis = [x_ for x_ in out_lis]
          prev = tmp_lis.pop()
          if prev[1] < elem[0]:
            data = [x_ for x_ in last_elem_lis if x_ - elem[1] ==1 ][0]
            out_lis.append((elem[0], data))
    return out_lis
         
if __name__=='__main__': 
   lis1 = [5, 6, 3]
   lis2 = [8, 4, 2] 
   out_prob1 = prob1(lis1, lis2)
   #print out_prob1
   lis1 = [(1, 2), (3, 9)]
   lis2 = [(4, 5), (8, 10), (11, 12)]    
   out_prob2 = prob2(lis1, lis2)
   print out_prob2