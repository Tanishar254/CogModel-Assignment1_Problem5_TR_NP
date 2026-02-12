from simulation import SEIRParameters, SEIRInitialConditions, simulate_seir
from viz import plot_results
import matplotlib.pyplot as plt




if __name__ == "__main__":


    parameters = SEIRParameters(beta=3.0, sigma=0.5, gamma=0.5)

    # S0, E0, I0, R0
    inits = SEIRInitialConditions(s0=9999.0, e0=1.0, i0=0.0, r0=0.0)

    ### Your code here
    s, e, i, r = simulate_seir(parameters, inits, days=100)

    ### Expected result
    fig = plot_results(i)
    plt.show()
