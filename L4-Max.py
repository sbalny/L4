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
n = int(argv[1])
#seeds
first = int(argv[2])
last = int(argv[3])
# nb of randomizations
max_rand = int(argv[4])
#file header
with open("L4-Max"+str(max_rand)+"-"+str(n)+".csv", 'a') as file:
    file.write("dimension,seed,nbLLL,LLL,L4,time L4, L4-Rand"+str(max_rand)+",time L4-Rand"+str(max_rand)+"\n")

#running L4 algorithm
for seed in range(first, last+1):
    results = {"LLL" : [0], "1run" : [0, 0], "rand" : [0, 0]}
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
    t = time()
    S, cLLL = Sample_L4(B)
    results["1run"][1] = time() - t
    n = len(S[0].vec)
    v_min = S[0]
    countLLL += cLLL
    results["1run"][0] = S[0].sq_length
    i_rand = 0
    while i_rand < max_rand:
        m = len(S)
        B = IntegerMatrix(m, n)
        for i in range(m):
            for j in range(n):
                B[i, j] = int(S[i].vec[j])
        B = LLL.reduction(B)
        S = [Vector(n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                S[i][j] = B[i+m-n, j]
        B = basis_reduction(S, density = 148)
        S, cLLL = Sample_L4(B)
        countLLL += cLLL
        if S[0] < v_min:
            v_min = S[0]
            i_rand = 0
        else:
            i_rand += 1
    results["rand"][1] = time() - t
    results["rand"][0] = v_min.sq_length
    #output file
    with open("L4-Max"+str(max_rand)+"-"+str(n)+".csv", 'a') as file:
        file.write(str(n)+",")
        file.write(str(seed)+",")
        file.write(str(countLLL)+",")
        file.write(str(round(results["LLL"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["1run"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["1run"][1], 4))+",")
        file.write(str(round(results["rand"][0]**0.5/gaussian_heuristic, 4))+",")
        file.write(str(round(results["rand"][1], 4))+"\n")
    
    
    
