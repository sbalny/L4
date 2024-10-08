#!/bin/bash
ntest=99 #Number of tests per dimension
echo "Test Randomization"
Start=40 #First dimension
End=180 #Last dimension
rando=10 #Number of randomizations
echo "Starting with fixed number of randomization (randomize $rando times)..."
for (( i=$Start; i<=$End; i+=10 ))
do
	sage L4-Rand.py $i 0 $ntest $rando
done
echo "Done. Starting the L4-Max2..."
for (( i=$Start; i<=$End; i+=10 ))
do
	sage L4-Max2.py $i 0 $ntest
done
echo "Done. Starting the L4-Max4..."
for (( i=$Start; i<=$End; i+=10 ))
do
	sage L4-Max4.py $i 0 $ntest
done
echo "Done. Making statistics..."
sage L4-random-statistics.py $Start $End Rand$rando
sage L4-random-statistics.py $Start $End Max2
sage L4-random-statistics.py $Start $End Max4
echo "Done. Writen in files"

