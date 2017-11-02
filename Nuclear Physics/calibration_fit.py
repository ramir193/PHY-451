# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:06:12 2017

@author: ramir
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

def f(m,x,b):
    return m*x+b

with open("Spectrum_Data.csv") as infile:
    df = pd.read_csv(infile)
    x_array = np.array(df['Gamma peak (keV)'])
    y_array = np.array(df['HPGe Gamma Peak Channel No.'])
    y_error = np.array(df['HPGe R'])
    popt,pcov = curve_fit(f,xdata=x_array,ydata=y_array) # optimal, covariance
    #plt.scatter(x=x_array,y=y_array)
    fit_array = f(popt[0],x_array,popt[1])
    #print(popt,pcov)
    #print("y = {}x + {}".format(popt[0],popt[1]))
    #plt.scatter(x_array,y_array)
    plt.errorbar(x_array, y_array, yerr=y_error, fmt='o')
    #plt.vlines(661.7,ymin=min(y_array),ymax=max(y_array),label='137 Cs actual')
    #plt.scatter()
    plt.plot(x_array, fit_array,color='r',label="y = {}x + {}".format(round(popt[0],2),round(popt[1],2)))
    plt.ylabel("Channel No.")
    plt.xlabel("Gamma peak (keV)")
    plt.title("HPGe Gamma peak (keV) vs. Channel No.")
    plt.legend(loc=2)
    plt.savefig("gamma_channel_calibration_plot_hpge.pdf")    
    