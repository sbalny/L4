#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# Created By  : Sébastien BALNY
# Created Date: 01/09/2024
# version ='1.0'
# ---------------------------------------------------------------------------
from fpylll import IntegerMatrix, LLL, BKZ, GSO
from time import time
from L4 import *
from sys import argv


#input
n = argv[1]
#seeds
first = argv[2]
last = argv[3]
#file header
with open("L4-"+str(n)+".csv", 'a') as file:
    file.write("dimension,seed,LLL,L4,time\n")

#running L4 algorithm
for seed in range(first, last+1):
    results = {"LLL" : [0], "1run" : [0, 0]}
    #Basis input
    path = "datas/dst-"+str(n)+"-"+str(seed)
    B = IntegerMatrix.from_matrix(convert(path))
    #LLL reduction
    B = LLL.reduction(B)
    S = Sample_Init(B)
    S = sorted(S, key = lambda vec : vec.sq_length)
    results["LLL"][0] = S[0].sq_length
    gaussian_heuristic = gh(B)
    t = time()
    S = Sample_L4(B)
    results["1run"][1] = time() - t
    n = len(S[0].vec)
    v_min = S[0]
    results["1run"][0] = S[0].sq_length
    
    #output file
    with open(str(n)+".csv", 'a') as file:
        file.write(str(n)+",")
        file.write(str(seed)+",")
        file.write(str(round(results["LLL"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["1run"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["1run"][1], 4))+"\n")
    
    
    
