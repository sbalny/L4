#!/bin/bash
#Compare L4 to LLL
ntest=10 #Number of tests per dimension
echo "Comparing L4 to LLL"
Start=40 #First dimension
End=50 #Last dimension
echo "Starting... "
for (( i=$Start; i<=$End; i+=10 ))
do
	sage L4algorithm.py $i 0 $ntest
done
echo "Done. Making statistics..."
sage L4-statistics.py $Start $End
echo "Done. Writen in file"

