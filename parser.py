# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:49:46 2017

@author: ramir
"""

infile_1 = open("getwfm1.txt")
infile_2 = open("getwfm2.txt")
outfile = open("getwfm1_parsed.txt", "w")

with open("getwfm1.txt", "r") as ch1, open("getwfm2.txt", "r") as ch2, open("getwfm_parsed.txt", "w") as outfile:
    lines = len(ch1.readlines()) 
    result_string = ""
    for i in range(lines):
        ch_1_line = ch1.readline()
        ch_2_line = ch2.readline()
        v1, t1 = ch_1_line.strip("\"\n").split(",")
        dv1 = float(v1) * 0.02
        v2, t2 = ch_2_line.split("\t")
        dv2 = float(v2) * 0.02        
        result_string += "{}\t{}\t{}\t{}\n".format(v1,dv1,v2,dv2)
    outfile.write(result_string)