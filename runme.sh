#!/bin/bash
# Test L4 
ntest=99 #Number of tests per dimension
echo "Test 1: Comparing L4 to LLL"
Start=40 #First dimension
End=180 #Last dimension
echo "Starting... "
for (( i=$Start; i<=$End; i+=10 ))
do
	sage L4algorithm.py $i 0 $ntest
done
echo "Done. Making statistics..."
sage L4-statistics.py $Start $End
echo "Done. Writen in file"
echo "----------------------------"
#Test Randomization
echo "Test 2: Randomization"
rando=10 #Number of randomizations
echo "Starting with fixed number of randomization (randomize $rando times)..."
for i in {$Start..$End..10}
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
echo "----------------------------"
#Test L4+BKZ
ntestB=99 #Number of tests per dimension
StartB=40 #First dimension
EndB=150 #Last dimension
Block=24
echo "Test 3: Comparing L4+BKZ to BKZ - blocksize $Block"
echo "Starting..."
for (( i=$StartB; i<=$EndB; i+=10 ))
do
	sage L4-BKZ.py $i 0 $ntestB $Block
done 
echo "Done. Making statistics..."
sage L4-BKZ-statistics.py $StartB $EndB
