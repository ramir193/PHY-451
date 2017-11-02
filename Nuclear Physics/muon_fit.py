# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:21:40 2017

@author: ramir
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:06:12 2017

@author: ramir
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import expon

def f(t,tau,N0):
    return N0*np.exp(t/tau)

def g(m,x,b):
    return m*x+b
    
with open("muon_decays.csv") as infile:
    df = pd.read_csv(infile)
    t_array = np.array(df["time"],dtype=int)
    n_array = np.array(df["decay"],dtype=int)
    log_decay_array = np.array(df["log_decay"],dtype=float)
    log_time_array = np.array(df["log_time"],dtype=float)
    #popt_log, pcov_log = curve_fit(g,xdata=log_time_array,ydata=log_decay_array)
    plt.hist(x=n_array,bins=len(set(n_array)))
    
    hist, bin_edges = np.histogram(n_array,bins=len(set(n_array)))
    #print(len(hist))
    #plt.scatter(bin_edges,hist)
    #popt, pcov = curve_fit(f,xdata=)
    plt.xlabel("Time in between decays (ns)")
    plt.ylabel("Frequency")
    plt.savefig("muon_histogram_decaytimes.png")
    plt.title("Frequency of number of muon decays")
    #log_fit_array = g(popt_log[0],t_array,popt_log[1])
    #popt, pcov = curve_fit(f,xdata)
    #plt.plot(hist)
    #print(len(hist),len(t_array))
    #print(hist,bin_edges)
    #plt.plot(t_array,log_fit_array)
    #param=expon.fit(n_array)
    #print(param)
    #plt.plot(t_array,f(t_array,-param[1],param[0]))
    #pdf_fitted=norm.pdf(x,loc=param[0],scale=param[1])
    #popt, pcov = curve_fit(f,xdata=t_array,ydata=n_array)
    #print(popt)
    #plt.scatter(t_array,log_fit_array)
    #y_array_2 = np.array(df['Al Counts'])
    #y_error = np.array(df['Pb Counts Uncertainty'])
    #y_error_2 = np.array(df['Al Uncertainty'])
    #I_0 = y_array[0]
    #I_0_Al = y_array_2[0]
    #popt,pcov = curve_fit(f,xdata=t_array,ydata=n_array) # optimal, covariance
#    #popt2,pcov2 = curve_fit(f,xdata=x_array_2,ydata=y_array_2) # optimal, covariance    
    #tau,N0,delta = popt
    #print(popt)
    #plt.scatter(log_time_array,log_decay_array)
#    #a_2, mu_2 = popt2    
#    fit_array = f(t_array,*popt)
    #fit_array_2 = f(x_array_2, *popt2)
    #plt.figure(1,figsize=(8,8))
    #plt.subplot(212)
    #plt.errorbar(x_array, y_array, yerr=y_error, fmt='o',label="Data")
    #plt.plot(x_array, fit_array,color='r',label="y = {}*exp({}*x)".format(I_0,round(mu,3)))
    #plt.ylabel("Counts")
    #plt.xlabel("Pb thickness (mm)")
    #plt.title("Pb thickness (mm) vs. Counts")
    #plt.legend(loc=1)
    #plt.savefig("Pb_Attenuation_plot.pdf")    
    
    
    #plt.subplot(211)
    #plt.tight_layout(pad=1,h_pad=2)
    #plt.errorbar(x_array_2, y_array_2, yerr=y_error_2, fmt='o',label="Data")
    #plt.plot(x_array_2, fit_array_2,color='r',label="y = {}*exp({}*x)".format(I_0_Al,round(mu_2,3)))
    #plt.ylabel("Counts")
    #plt.xlabel("Al thickness (mm)")
    #plt.title("Al thickness (mm) vs. Counts")
    #plt.xlabel("test")
    #plt.show()