#!/bin/bash
# Test L4 for dim 40 to 200
ntest=10 #Number of test per dimension
echo "Test 1: Comparing L4 to LLL"
Start=40 #First dimension
End=50 #Last dimension
echo "Starting... "
for i in {$Start..$End..10}
do
	sage L4algorithm.py $i 0 $ntest
done
echo "Done. Making statistics..."
sage L4-statistics.py $Start $End
echo "Done. Writen in file"
echo "----------------------------"

