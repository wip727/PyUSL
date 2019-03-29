import numpy as np

class USL:
    # Attributes:
    # Concurrency
    gamma = 1
    # Contention
    alpha = 0
    # Coherency
    beta = 0

    # Initializer, with initial guess as optional inputs
    def __init__(self, gamma0=1, alpha0=0, beta0=0):
        self.gamma = gamma0
        self.alpha = alpha0
        self.beta = beta0
