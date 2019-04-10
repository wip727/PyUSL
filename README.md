# pyusl
Universal Scalability Law in Python

## Required packages
* matplotlib (for result plotting)
* numpy (for numeric computation)
* scipy (for curve fitting)

## Required test package
* nose (for unit testing)

## To install the package
```
sudo pip install pyusl
```

## To run a quick demo
```
cd examples
python example1.py
```

## To run tests
```
python setup.py test
```
or if you have nose installed, simply call
```
nosetests
```
in the project folder.

## Instructions for pyusl
You can create a pyusl instance with no input:
```
from pyusl import usl
u = usl()
```
It has three public properties, and their default values are:
* (Concurrency) gamma = 1
* (Contention) alpha = 0
* (Coherency) beta = 0

You can create a model by assigning the parameter values through the constructor, for example:
```
u = usl(3, 4, 5)
```
You can evaluate the USL model by the "compute" method:
```
x = [1,2,3,4,7]
y = u.compute(x)
```
You can plot `x` and `y` to get a rough sketch of the USL curve. 
