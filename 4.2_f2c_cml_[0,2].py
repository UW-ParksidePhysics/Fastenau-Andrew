### Program to convert Farenheit to Celcius via the command line
import sys
# Command line user input
F = int(sys.argv[1])  # 4.2_f2c_cml_[02].py 300 

# Function code
def T(F):
    T = (5 / 9) * (F - 32)
    return T


print("Temperature in Celsius degrees =", C(F))