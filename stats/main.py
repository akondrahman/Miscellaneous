import stat_stuff
import numpy as np
print "Automation technique usage ratio 'H' vs. 'L' "
auto_High = [ 0.8571428571, 0.2142857143, 0.5714285714 ]
auto_Low=[0.2857142857, 0.8571428571, 0.1428571429, 0.8571428571]
print "stat summary: auto_high: (mean, median, std. Dev): {}, {}, {}".format(np.mean(auto_High), np.median(auto_High), np.std(auto_High))
print "stat summary: auto_low: (mean, median, std. Dev): {}, {}, {}".format(np.mean(auto_Low), np.median(auto_Low), np.std(auto_Low))
print "result (t, p): {}".format(stat_stuff.performWilcoxonRankSumTest(auto_High, auto_Low))
print "Software security practice usage ratio 'H' vs. 'L' "
sec_High = [ 0.7272727273, 0.8181818182, 0.6363636364]
sec_Low=[0.6363636364, 1, 0.3636363636, 0.9090909091]
print "stat summary: sec_high: (mean, median, std. Dev): {}, {}, {}".format(np.mean(sec_High), np.median(sec_High), np.std(sec_High))
print "stat summary: sec_low: (mean, median, std. Dev): {}, {}, {}".format(np.mean(sec_Low), np.median(sec_Low), np.std(sec_Low))
print "result (t, p): {} ".format(stat_stuff.performWilcoxonRankSumTest(sec_High, sec_Low))
