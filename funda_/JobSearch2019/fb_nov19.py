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

if __name__=='__main__': 
   lis1 = [5, 6, 3]
   lis2 = [8, 4, 2] 
   out_prob1 = prob1(lis1, lis2)
   print out_prob1