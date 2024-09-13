# L4
L4 algorithm test library. Note that this code was mostly done for testing purpose and its runtime is
not optimized.

### Prerequisites

The things you need before installing the software.

* SageMath version 9.0 or higher.

The latest version can be downloaded on the sagemath.org website (link below)

https://www.sagemath.org/download.html

A set a of test lattices is given in the Data folder. They are generated with the Darmstadt Lattices generator
which can be found on the SVP challenge webpage (link below).

https://latticechallenge.org/svp-challenge/

To make this generator work you need to have the following libraries installed:

* GMP and NTL

### Matrix naming convention

All lattice bases must be saved on the Data folder using the following naming convention: dst-[dim]-[seed]
where [dim] is to be replaced by the dimension of the lattice and [seed] by the seed used in the generator.
For instance ``dst-40-0`` is a basis of a lattice of dimension 40 generated using 0 as the seed. We use the
seed as an index over the bases in the tests.

## Usage

### Comparison of L4 and LLL

To compare LLL and L4 run the following:

```
$ sage L4algorithm.py [dim] [start] [end]
```

where [dim] is the dimension of the lattice, [start] the first index [end] the last one. 
This will generate a csv file called L4-[dim].csv.
For each lattice ``dst-[dim]-[start]`` to ``dst-[dim]-[end]``  it gives you the approximation factor of LLL, the approximation factor of L4,
the number of time L4 calls LLL, and the runtime of L4.

For instance:

```
$ sage L4algorithm.py 80 0 100
```

will generate the L4-80.csv file which collects the aforementionned data for bases ``dst-80-0`` to ``dst-80-100``.


The script ``runL4.sh`` runs this test for dimension 40 to 200 with a step of 10 using 1000 lattice per dimensions. The dimensions and the number of tests
can be changed in the script.
Usage:

```
$ chmod +x runL4.sh
$ ./runL4.sh
```

### Testing randomization

To test the L4 with a fixed number of randomization run the following:

```
$ sage L4-Rand.py [dim] [start] [end] [nbRand]
```

where [dim] is the dimension of the lattice, [start] the first index [end] the last one and [nbRand] the number of randomizations.
For instance:

```
$ sage L4-Rand.py 80 0 100 10
```

generate the file TODO

To run test with the L4-Max2 and L4-Max4 randomization, run the following command:

```
$ sage L4-Max[k].py [dim] [start] [end]
```

where [k] is either 2 or 4.
For instance:

```
$ sage L4-Max4.py 80 0 100
```

generate the file TODO

The script ``runRandom.sh`` runs these test for dimension 40 to 200 with a step of 10 using 1000 lattice per dimensions. The dimensions, number of tests,
and number of randomizations can be changed in the script.
Usage:

```
$ chmod +x runRandom.sh
$ ./runRandom.sh
```

### Comparison of BKZ and L4+BKZ



## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...

