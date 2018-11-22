import math 

def getDistance(point_tuple):
    calc = math.pow(point_tuple[0] - 0, 2) + math.pow(point_tuple[1] - 0, 2)
    return math.sqrt(calc)

def prob1(pt_list, topk):
    out_dic = {}
    out_lis = []
    final_list = []
    for pt_in in xrange( len( pt_list ) ):
        pt_dis = getDistance(pt_list[pt_in])
        out_dic[pt_dis] = pt_list[pt_in]
        out_lis.append(pt_dis)
    sorted_ = sorted(out_lis, reverse=True)
    for ind in xrange(topk):
        data_ = sorted_.pop()
        final_list.append(out_dic[data_])
    return final_list
    
class StreamHandler:
        def __init__(self, data_):
            self.data = data_



if __name__ =='__main__':
   the_pts = [(1, 2), (1, 0), (0, 3), (2, 4), (3, 1)]
   out = prob1(the_pts, 3)
   #print out 
   obj1 = StreamHandler(11111)
   print obj1.data 
   