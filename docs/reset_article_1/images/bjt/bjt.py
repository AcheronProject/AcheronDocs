# Python standard math/scientific libraries
import numpy as np
import csv

# Defining constants
pi = np.pi
e = np.e

# Defining math functions
inv = np.linalg.inv
transpose = np.transpose
array = np.array

# FSOLVE for nonlinear equation solving
import scipy.integrate as spi

# MatplotLib and PyPlot for plotting
import matplotlib.pyplot as pyplot
import matplotlib as mplot
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)

tspan = []
y1 = []
y2 = []
with open('scope_15.csv') as file:
	csv_reader = csv.reader(file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count < 2: line_count += 1 # Skips lines 1 and 2
		else:
			tspan.append(float(row[0]))
			y1.append(float(row[1]))
			y2.append(float(row[2]))
			line_count += 1

tspan = np.array(tspan)
y1 = np.array(y1)
y2 = np.array(y2)

fig1 = pyplot.figure()
ax1 = fig1.add_subplot(1,1,1)

ax1.plot(tspan, y1,linewidth=1 ,color="red",label="$V_o$")
ax1.plot(tspan, y2,linewidth=1 ,color="blue",label="$\delta$")

fig1.suptitle(r'PI-controlled nonlinear Ĉuk converter model simulation')

ax1.set_xlabel(r'Time (ms)')
ax1.set_ylabel(r'Output voltage $V_o$ (V)')
ax1.grid(True)

#ax2.set_xlabel(r'Time (ms)')
#ax2.set_ylabel(r'Control signal $\delta$ (-)')
#ax2.grid(True)

pyplot.show()
