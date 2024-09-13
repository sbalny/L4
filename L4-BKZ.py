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
from copy import deepcopy


#input
n = int(argv[1])
#seeds
first = int(argv[2])
last = int(argv[3])
#BKZ block size
block = int(argv[4])
#file header
with open("L4-BKZ-"+str(n)+".csv", 'a') as file:
    file.write("dimension,seed,BKZ,time BKZ,L4,L4 time,L4-BKZ,time L4-BKZ\n")

for seed in range(first, last+1):
    results = {"LLL" : [0], "BKZ" : [0, 0], "L4" : [0, 0], "L4-BKZ" : [0, 0]}
    #Basis input
    path = "datas/dst-"+str(n)+"-"+str(seed)
    B = IntegerMatrix.from_matrix(convert(path))
    #LLL reduction
    B = LLL.reduction(B)
    countLLL = 1
    S = Sample_Init(B)
    S = sorted(S, key = lambda vec : vec.sq_length)
    results["LLL"][0] = S[0].sq_length
    gaussian_heuristic = gh(B)
    #running BKZ algorith
    results["L4"][0] = S[0].sq_length
    Bbkz = deepcopy(B)
    t_BKZ = time()
    BKZ.reduction(Bbkz, o=BKZ.Param(block_size=block))
    results["BKZ"][1] = time() - t_BKZ
    results["BKZ"][0] = Bbkz[0].norm()**2
    #running L4-BKZ algorithm
    t = time()
    S, _ = Sample_L4(B)
    results["L4"][1] = time() - t
    results["L4"][0] = S[0].sq_length
    m = len(S)
    B = IntegerMatrix(m, n)
    for i in range(m):
        for j in range(n):
            B[i, j] = int(S[i].vec[j])
    B = LLL.reduction(B)
    B_temp = IntegerMatrix(n, n)
    for i in range(n):
        for j in range(n):
            B_temp[i, j] = B[i+m-n, j]
    BKZ.reduction(B_temp, o=BKZ.Param(block_size=block))
    results["L4-BKZ"][1] = time() - t
    results["L4-BKZ"][0] = B_temp[0].norm()**2
    #output file
    with open("L4-BKZ-"+str(n)+".csv", 'a') as file:
        file.write(str(n)+",")
        file.write(str(seed)+",")
        file.write(str(round(results["BKZ"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["BKZ"][1], 4))+",")
        file.write(str(round(results["L4"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["L4"][1], 4))+",")
        file.write(str(round(results["L4-BKZ"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["L4-BKZ"][1], 4))+"\n")
    
    
    
