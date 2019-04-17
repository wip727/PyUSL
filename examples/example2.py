# example 2 of pyusl
# Fit the USL curve based on four measurements
# Then plot the predicted curve from 1 to 20

from pyusl import usl;
import numpy as np;
u = usl(1, 2, 0)
x = [1,2,3,4]
y = [1,2.1,2.9,3.5]
u.fit(x, y, requires_plot = False)
xgrid = np.linspace(1,20,200)
u.plot(xgrid)
