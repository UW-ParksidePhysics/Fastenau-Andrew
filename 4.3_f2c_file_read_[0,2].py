### Program to extract Temperature from data file.
infile = open('temperature_data.dat', 'r')

# Data extraction code
z = []
for line in infile:
    z1 = line.split()
    z.append(z1)
infile.close()
z = z[3][2]
z = float(z)

# Function code
def T(z):
    T = (5 / 9) * (z - 32)
    return T

# Driver code
print("Temperature in Celsius degrees =", T(F))

