#!/bin/bash
# Test L4 
ntest=10 #Number of tests per dimension
echo "Test 1: Comparing L4 to LLL"
Start=40 #First dimension
End=50 #Last dimension
Block=24
echo "Test 3: Comparing L4+BKZ to BKZ - blocksize $Block"
echo "Starting..."
for (( i=$Start; i<=$End; i+=10 ))
do
	sage L4-BKZ.py $i 0 $ntest $Block
done 
echo "Done. Making statistics..."
sage L4-BKZ-statistics.py $Start $End
