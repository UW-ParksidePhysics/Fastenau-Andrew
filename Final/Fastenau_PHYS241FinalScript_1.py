'''
Program to run volume, energy data set via Vinet method
'''

# Import built-in modules
from numpy import linspace
import matplotlib.pyplot as mp
# Import custom modules
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from univariate_statistics import univariate_statistics
from two_column_text_read import two_column_text_read
from quadratic_fit import quadratic_fit

# Parses the filename into its substituent parts
def parse_file_name(filename):
    p = filename.split(".")
    ChSym = p[0]
    SySym = p[1]
    Acr = p[2]
    return ChSym, SySym, Acr

filename = "Ag.Fm-3m.GGA-PBE.volumes_energies.dat"
ChSym, SySym, Acr = parse_file_name(filename)


# Reads and processes the data set
data_set = two_column_text_read("Ag.Fm-3m.GGA-PBE.volumes_energies.dat")
quadratic_coefficients = quadratic_fit(data_set)
statistics = univariate_statistics(data_set)


# Converts the 2D-array to a nice list of volumes and energies - Credit to Julia, Paul, and Andrew in Final Review
unzipped_data = zip(*data_set)
data = list(unzipped_data)

# Fits the data into the correct equation of state (Vinet)
# NOTE: There is an issue with the given vinet function in the equations_of_state module
#       as both murnaghan and birch-murnaghan work whereas vinet does not work.
eos_fit_curve, bulk_modulus = fit_eos(data[0], data[1], quadratic_coefficients, eos='birch-murnaghan', number_of_points=50)

# Defined function to annotate graph - Permission granted by Dr. Parker during Collaborative Ultra session on the
#                                      date of 5/14/2020. Code invented by Dr. Parker and Paul Rizzo.
def annotate_graph(ChSym, SySym):
    graph.annotate(ChSym, xy=(min(data[0]) - (min(data[0]) * 0.05), max(data[1]) + max(data[0]) * 0.00005))

    graph.annotate(r'$ {}\overline{{{}}} {}$'.format(SySym[0:2], SySym[3], SySym[1]), xy=(EQ,
                                                 (max(data[1]) + min(data[1])) / 1.99996))

    graph.annotate('V_0={:.3f}Å^3/atom'.format(EQ), xy=(EQ, (max(data[1]) + min(data[1])) / 1.99992))
    mp.axvline(EQ - data[0][data[1].index(min(data[1]))] * 0.01, color="black", linestyle='--')

    mp.title("{} Equation of State for {} in DFT {}".format('Vinet', ChSym, Acr))
    mp.text(91.453, -287.333, "Created by Andrew Fastenau 2020-05-12")
    return

# Driver code to annotate graph
EQ = data[0][data[1].index(min(data[1]))]

# Allows the graph to have both the eos_fit_curve and data plotted
fig = mp.figure()
graph = fig.add_subplot()

# Plotted data points
DAT = graph.plot(data[0], data[1], 'o')

# Plotted eos_fit_curve
fit_x = linspace(min(data[0]), max(data[0]), len(eos_fit_curve))
CUR = graph.plot(fit_x, eos_fit_curve, color="black")

# Labels the axes via LaTeX
mp.xlabel(r'$ \mathit{Å^3/atom}\ $')
mp.ylabel(r'$ \mathit{eV/atom}\ $')

# Driver code to annotate the graph (make it pretty)
annotate_graph(ChSym, SySym)

# Scales the x-axis by 10% dynamically
x_min = (min(data[0]) - (min(data[0]) * 0.10))
x_max = (max(data[0]) + (max(data[0]) * 0.10))
y_min = (min(data[1]) - (min(data[0]) * 0.00007)) # Scaled by the magnitude of the volume (via trial and error)
y_max = (max(data[1]) + (max(data[0]) * 0.00007)) # Scaled by the magnitude of the volume
mp.xlim(x_min, x_max) # Changes the graph's limits
mp.ylim(y_min, y_max)


# Boolean statement regarding if the program will output PNG or display graph
display_graph = True
if display_graph == True:
    mp.show(display_graph)
elif display_graph == False:
    mp.savefig("Fastenau.Ag.Fm-3m.GGA-PBE.volumes_energies.dat")





















