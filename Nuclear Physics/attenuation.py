# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:06:12 2017

@author: ramir
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

def f(x,mu):
    return I_0*np.exp(mu*x)

with open("Attenuation_Data.csv") as infile:
    elements = ('Pb', 'Al')
    #for e in elements:
        
    df = pd.read_csv(infile)
    x_array = np.array(df['Pb thickness (mm)'])
    #x_array_2 = np.array(df['Al thickness (mm)'])
    y_array = np.array(df['Pb Counts'])
    #print(x_array,y_array)
    #y_array_2 = np.array(df['Al Counts'])
    y_error = np.array(df['Pb Counts Uncertainty'])
    #y_error_2 = np.array(df['Al Uncertainty'])
    I_0 = y_array[0]
    #I_0_Al = y_array_2[0]
    popt,pcov = curve_fit(f,xdata=x_array,ydata=y_array) # optimal, covariance
    #popt2,pcov2 = curve_fit(f,xdata=x_array_2,ydata=y_array_2) # optimal, covariance    
    mu = popt[0]
    print(mu)
    #a_2, mu_2 = popt2    
    fit_array = f(x_array,*popt)
    #fit_array_2 = f(x_array_2, *popt2)
    #plt.figure(1,figsize=(8,8))
    #plt.subplot(212)
    plt.errorbar(x_array, y_array, yerr=y_error, fmt='o',label="Data")
    plt.plot(x_array, fit_array,color='r',label="y = {}*exp({}*x)".format(I_0,round(mu,3)))
    plt.ylabel("Counts")
    plt.xlabel("Pb thickness (mm)")
    plt.title("Pb thickness (mm) vs. Counts")
    plt.legend(loc=1)
    plt.savefig("Pb_Attenuation_plot_2.pdf")    
    
    
    #plt.subplot(211)
    #plt.tight_layout(pad=1,h_pad=2)
    #plt.errorbar(x_array_2, y_array_2, yerr=y_error_2, fmt='o',label="Data")
    #plt.plot(x_array_2, fit_array_2,color='r',label="y = {}*exp({}*x)".format(I_0_Al,round(mu_2,3)))
    #plt.ylabel("Counts")
    #plt.xlabel("Al thickness (mm)")
    #plt.title("Al thickness (mm) vs. Counts")
    #plt.xlabel("test")
    plt.show()