# 2. superconductivity/oscope
#
# CSV = time in seconds, voltage in volts
# ch1 file = volts out of FG = (current through R)*(5000 ohms)
# ch2 file = volts out of preamp = (voltage across R)*(-1000)
#
# - plot voltage across R vs. current across R
# - assume 2% uncertainty for both the voltage and current across R
# - fit to line
# - get resistance R (should be about 1 ohm) and offset (should be 0) and
# uncertainties


import SpinlabCF as cf
import csv
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(m,x,b):
    return m*x+b

with open("Data Sets/Superconductivity/9-26/ch1.csv") as ch1, \
     open("Data Sets/Superconductivity/9-26/ch2.csv") as ch2, \
     open("Data Sets/Superconductivity/9-26/VI.csv", "w") as out:
    ch1reader = csv.reader(ch1)
    ch2reader = csv.reader(ch2)
    v_array = []
    i_array = []
    for line_1, line_2 in zip(ch1reader, ch2reader):
        try:
            v,i = float(line_1[1]), float(line_2[1])
            v_array.append(v)
            i_array.append(i)
            out.write(','.join([line_1[1],line_2[1]]) + '\n')

        except IndexError:
            pass
    v_array = np.array(v_array)
    i_array = np.array(i_array)
    #std = np.std(vi_array)
    popt,pcov = curve_fit(f,xdata=v_array,ydata=i_array) # optimal, covariance
    plt.plot(v_array,i_array, 'b-', label='data')
    plt.plot(v_array, f(v_array, *popt), 'r--', label='fit')
    plt.xlabel("V (v)")
    plt.ylabel("I (A)")
    plt.legend()
    plt.savefig('fit-plot.pdf')






