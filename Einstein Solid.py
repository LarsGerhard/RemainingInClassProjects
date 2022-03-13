from random import randint, randrange
import matplotlib.pyplot as plt, numpy as np
from numpy import linspace,array,arange, log,exp,sin,cos,sqrt, pi, zeros, ones, arctan, full
from scipy.constants import k
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

# Part 2

# Function to simulate the exchange of energy over a given period of time

def exchange(solidin, Nin, Lin):  # iterate L times
    for i in range(Lin):

        while True:
            take = randint(0,Nin - 1) # random index of cell to take from
            give = randint(0,Nin - 1) # random index of cell to give to

            if solidin[take] != 0:
                break

        # Check if take has non-zero energy; if not select another take cell
        # Use a while loop to check and repeat

        # exchange energy
        solidin[take] = solidin[take] - 1
        solidin[give] = solidin[give] + 1
    return solidin


def sample(solidin, Nin):  # sample energy distribution
    qmax = int(np.max(solidin))
    pn = zeros(qmax)

    # Loop over q from 0 to qmax and count elements of solid that equal q
    #  use np.count_nonzero()

    for i in range(0,qmax):
        pn[i] = solidin[solidin==i].shape[0]

    error = np.sqrt(pn / Nin)  # statistical error
    return qmax, pn, error

# set up solid
K = 20                                  # grid dimension
qavg = 10                               # avg  units of energy per oscillator
N = K*K

# Create a list containing the N values of energy, initially qavg
solid = full(N, qavg)

# Simulate
Nint = 10**5 # number of interactions
L = Nint # number of times to interate
exchange(solid, N, L)         # thermalize, 100 interactions per oscillator
qmax, pn, error = sample(solid, N)

# analytic Boltzmann dist, qavg = 1/(exp(1/kT)-1), 1/kT=ln(1+1/qavg)

kT = 1 / log(1 + 1 / qavg)
C = max(pn)

En = np.arange(qmax)

pn_th =C * exp(-En /kT)

# Plot result
fig = plt.figure(1)
plt.plot(En, pn, 'o')
plt.errorbar(En, pn, error, ls='')
plt.plot(En, pn_th, '-r')  # theoretical result

plt.xlim(0, qmax)
plt.xlabel('Energy units')
plt.ylabel('Probability')
# plt.semilogy()        # semilog scale
plt.show()