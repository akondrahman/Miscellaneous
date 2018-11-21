def prob1(contact_list):
    temp_dict = {}
    out_lis = []
    for contact in contact_list:
        cID, cEmail = contact
        if cEmail not in temp_dict:
            temp_dict[cEmail] = cID 
    for k_, v_ in temp_dict.iteritems():
        out_lis.append((v_, k_))
    return out_lis


def prob2(digit):
    digitStrDict = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', 
                    '9': 'Nine', '10': 'Ten'}
    labelStrDict = {3: 'Thousand', 2: 'Hundred', 1: 'ty'}
    dig_str = str(digit)
    dig_len = len(dig_str)
    full_str = ''
    ind_str  = ''
    for cha_ind in xrange(len(dig_str)):
        char = dig_str[cha_ind]
        label_ind = dig_len - (cha_ind + 1)
        if label_ind >= 2:
           ind_str = digitStrDict[char] + ' ' + labelStrDict[label_ind]
        else:
            if label_ind == 1:
              ind_str = digitStrDict[char] + labelStrDict[label_ind]
            else:
              ind_str = digitStrDict[char]
        full_str = full_str + ' ' + ind_str
        ind_str = ''
    print full_str
    


if __name__=='__main__':
   inp_con_lis = [('A1', 'a@q.com'), ('A2', 'a@z.com'), ('A3', 'x@b.com'), ('A4', 'a@b.com'), ('A5', 'a@b.com')]
   out_con = prob1(inp_con_lis)
   #print out_con
   digit = 7429
   prob2(digit)

