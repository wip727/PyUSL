import numpy as np
import matplotlib.pyplot as pyplot
from scipy.optimize import curve_fit

class USL:
    # Attributes:
    # Concurrency
    gamma = 1
    # Contention
    alpha = 0
    # Coherency
    beta = 0

    # Raw data to fit
    rawx = None
    rawy = None

    # Initializer, with initial guess as optional inputs
    def __init__(self, gamma0 = 1, alpha0 = 0, beta0 = 0):
        self.gamma = gamma0
        self.alpha = alpha0
        self.beta = beta0

    # Fit command, estimate the parameters of USL using nonlinear least square
    def fit(self, x = None, y = None):
        if (x is not None) && (y is not None):
            self.rawx = x
            self.rawy = y

            # Fit the data
            xgrid = np.linspace(min(self.rawx), max(self.rawx), len(rawx))
