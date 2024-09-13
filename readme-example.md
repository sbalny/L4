
##Datas
Some lattices are available in the data folder

You can use the Darmsadt lattice generator to generate more lattices.
in folder [...] run the following:

 make

 ./generate_random --dim [dim] --seed [seed] >> dst-[dim]-[seed]

Example dim: 80 seed 100
./generate_random --dim 80 --seed 100 >> [Path]/dst-80-100

You will need to have the GMP and NTL library installed beforehand. 


##Comparison of LLL and L4

To compare LLL and L4 on one dimension run the following:

[...]

You will obtain a file called L4-dim.csv.
For each lattice it gives you the approximation factor of LLL, the approximation factor of L4,
the number of time L4 calls LLL, and the runtime of L4.

To generate the tables that compare LLL and L4 from dimension [...] to [...]:

##Randomization

Test per dimension:

Test global:

##L4+BKZ comparison.


##Full test:
the runme.sh runs all the test.


