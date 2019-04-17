import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class usl:
    # Attributes:
    # Concurrency
    gamma = 1
    # Contention
    alpha = 0
    # Coherency
    beta = 0

    # Raw data to fit
    rawx = 0
    rawy = 0

    # Initializer, with initial guess as optional inputs
    def __init__(self, gamma0 = 1, alpha0 = 0, beta0 = 0):
        self.gamma = gamma0
        self.alpha = alpha0
        self.beta = beta0

    # Fit command, estimate the parameters of USL using nonlinear least square
    def fit(self, x = None, y = None, init_guess = None, requires_plot = True):
        if (x is not None) and (y is not None):
            if (len(x) != len(y)):
                raise AssertionError('x and y must have same lengths')
            # store a copy in class instance
            self.rawx = x
            self.rawy = y

            if init_guess is None:
                init_guess = [self.gamma, self.alpha, self.beta];
            # Fit the data
            popt, pcov = curve_fit(self._uslfunc, x, y, p0 = init_guess, bounds = (0, np.inf))
            self.gamma = popt[0]
            self.alpha = popt[1]
            self.beta = popt[2]

            print("Optimized parameters: ", popt)
            print("Estimated covariance: ", pcov)

            if requires_plot:
                self._plotfittedresult()

    def compute(self, x = None):
        if x is None:
            x = self.rawx
        x = np.array(x)
        return self._uslfunc(x, self.gamma, self.alpha, self.beta)

    def _plotfittedresult(self):
        plt.plot(self.rawx, self.rawy, 'b*', label = 'measured data')
        xgrid = np.linspace(min(self.rawx), max(self.rawx), len(self.rawx) * 2)
        plt.plot(xgrid, self.compute(xgrid),
        'r-', label = 'fitted USL curve: gamma=%3.2f, alpha=%3.2f, beta=%3.2f'
        % (self.gamma, self.alpha, self.beta))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def plot(self, x = None):
        if x is None:
            x = self.rawx
        y = self.compute(x)
        plt.plot(x, y, 'r-',
        label = 'USL curve: gamma=%3.2f, alpha=%3.2f, beta=%3.2f'
            % (self.gamma, self.alpha, self.beta))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def _uslfunc(self, x, gamma, alpha, beta):
        return gamma * x / (1 + alpha * (x - 1) + beta * x * (x - 1))
