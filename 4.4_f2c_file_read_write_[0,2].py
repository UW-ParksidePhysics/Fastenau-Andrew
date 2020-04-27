from numpy import array, asarray
infile = open('Fdeg.dat', 'r')

z = []
for line in infile:
    z1 = line.split()
    z.append(z1)
infile.close()

F = []
count = 3
while count <= 8:
    F.append(float(z[count][2]))
    count += 1
F = asarray(F)
C = (5 / 9) * (F - 32)

infile = open('FdegCdeg.dat', 'w')
print (C)
count = 1
while count <= len(C):
    infile.write(str(F[count])), infile.write(' ')
    infile.write(str(C[count])), infile.write('\n')
    count += 1
infile.close()