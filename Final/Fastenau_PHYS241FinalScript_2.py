'''
Program to calculate the eigenvectors and eigenvalues of volume, energy data set
'''

# Imports built it modules
import matplotlib.pyplot as mp
from numpy import linspace

# Imports custom modules with their functions
from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors

# Initial parameters given
N_dim = 90
potential_parameter = 300
potential_name = "Sinusoidal"

generated_matrix = generate_matrix(-10, 10, N_dim, potential_name, potential_parameter)
eigenvalues, eigenvectors = lowest_eigenvectors(generated_matrix, 3, 6) # The 3 and the 6 correspond to the indices

# Creates x-axis in terms of N_dim
x = linspace(-10, 10, len(eigenvectors[2][0:N_dim]))

# Plots the eigenvectors
PlotA, = mp.plot(x, eigenvectors[0][0:N_dim], color = "red")
PlotB, = mp.plot(x, eigenvectors[1][0:N_dim], color = "lightblue")
PlotC, = mp.plot(x, eigenvectors[2][0:N_dim], color = "teal")

# Sets the horizontal and vertical axis limits
mp.axis([min(eigenvectors[0] - 2), max(eigenvectors[0] + 2), min(eigenvectors[1] - 2), max(eigenvectors[1]) + 2])

# Creates a black horizontal line on the x-axis
mp.axhline(color="black")

# Decorates the graph with science jargon
mp.title("Sinusoidal 2, 3, 4 Grid")
mp.legend((PlotA, PlotB, PlotC), ('ψ1, Ε1 = 0.18851101 a.u.', 'ψ2, Ε2 = 0.29428517 a.u.', 'ψ3, Ε3 = 0.42330764 a.u.'))
mp.xlabel("x [a.u.]")
mp.ylabel("ψ n (x) [a.u.]")
mp.text(-1.8, -1.8, "Yeeted by Andrew Fastenau 2020-05-12")

# Boolean statement regarding if the program will output PNG or display graph
display_graph = True
if display_graph == True:
    mp.show(display_graph)
elif display_graph == False:
    mp.savefig("Andrew.Sinusoidal.Eigenvector2, 3, 4.png")

