### Playground to test various modules

from two_column_text_read_12 import two_column_text_read

data = two_column_text_read("volumes_energies.dat")

print("DATA")
print(data)
print("")

from univariate_statistics_12 import univariate_statistics

statistics = univariate_statistics(data)

print("STATISTICS")
print(statistics)
print("")

from quadratic_fit_12 import quadratic_fit

quadratic_coefficients = quadratic_fit(data)

print("QUADRATIC_COEFFICIENTS")
print(quadratic_coefficients)
print("")

from fit_curve_array_12 import fit_curve_array

fit_curve = fit_curve_array(quadratic_coefficients, statistics[2], statistics[3], 100)

print("FIT_CURVE")
print(fit_curve)
print("")

from plot_data_with_fit_12 import plot_data_with_fit

plot_data_with_fit(data, fit_curve, 0, 0)  # data_format & fit_format can be anyone of 1=R, 2=B, or 3=Y


from lowest_eigenvectors_12 import square_matrix, lowest_eigenvectors

square_matrix_test = square_matrix()
eigenvalues, eigenvectors = lowest_eigenvectors(square_matrix_test, 5)
print("lowest_eigenvectors")
print(eigenvalues)
print(eigenvectors)


