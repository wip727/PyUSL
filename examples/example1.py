# example 1 of pyusl
# simple USL curve fitting based on a few measurements

from pyusl import usl
u = usl()
x = [1,2,4,8,16,32,64,128]
y = [12,24,37,50,72,93,84,82]
u.fit(x,y)
