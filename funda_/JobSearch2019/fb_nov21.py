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


if __name__=='__main__':
   inp_con_lis = [('A1', 'a@q.com'), ('A2', 'a@z.com'), ('A3', 'x@b.com'), ('A4', 'a@b.com'), ('A5', 'a@b.com')]
   out_con = prob1(inp_con_lis)
   print out_con