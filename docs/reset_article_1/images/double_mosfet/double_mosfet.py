# Python standard math/scientific libraries
import numpy as np
import csv

import scipy
import scipy.signal

# Defining constants
pi = np.pi
e = np.e

# Defining math functions
inv = np.linalg.inv
transpose = np.transpose
array = np.array

# MatplotLib and PyPlot for plotting
import matplotlib.pyplot as pyplot
import matplotlib as mplot
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# for Palatino and other serif fonts use:

rc('text', usetex=True)
rc('text.latex',preamble=r'\usepackage{newtxtext,newtxmath,sansmath}')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

t_meas = []
b0_meas = []
nrst_meas  = []
with open('scope_8.csv') as file:
	csv_reader = csv.reader(file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count < 2: line_count += 1 # Skips lines 1 and 2
		else:
			t_meas.append(float(row[0]))
			b0_meas.append(float(row[1]))
			nrst_meas.append(float(row[2]))
			line_count += 1

for i in [t_meas, b0_meas, nrst_meas]: i = np.array(i)

fig1 = pyplot.figure()
ax1 = fig1.add_subplot(1,1,1)

b, a = scipy.signal.butter(3, 0.05)
f_nrst_meas = scipy.signal.filtfilt(b, a, nrst_meas) #Filtered version
f_b0_meas = scipy.signal.filtfilt(b, a, b0_meas) #Filtered version

#ax1.plot(tspan, Fy1,linewidth=1 ,color="red",label=r'$\mathsf{V_o}$')

#--------------------------------------------------------------------
tspan = []
b0_mod = []
b0_nom = []
nrst_nom = []
nrst_mod = []
with open('reset.csv') as file:
	csv_reader = csv.reader(file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count < 2: line_count += 1 # Skips lines 1 and 2
		else:
			tspan.append(float(row[0]))
			b0_mod.append(float(row[1]))
			b0_nom.append(float(row[2]))
			nrst_mod.append(float(row[3]))
			nrst_nom.append(float(row[4]))
			line_count += 1

for i in [tspan, b0_mod, b0_nom, nrst_mod, nrst_nom]: i = np.array(i)


ax1.plot(t_meas, b0_meas,linewidth=1 ,color="red",label=r'Measured BOOT0')
ax1.plot(t_meas, nrst_meas,linewidth=1 ,color="blue",label=r'Measured nRST')
ax1.plot(tspan, b0_nom,linewidth=1 ,color="green",label=r'Nominal BOOT0')
ax1.plot(tspan, b0_mod,linewidth=1 ,color="orange",label=r'Fitted BOOT0')
ax1.plot(tspan, nrst_mod,linewidth=1 ,color="pink",label=r'Fitted nRST')
ax1.plot(tspan, nrst_nom,linewidth=1 ,color="purple",label=r'Nominal nRST')
ax1.legend()

fig1.suptitle(r'nRST-BOOT0 voltage signals curves: measured, nominal and parameter-fitted $\mathsf{(V_{3V3} = 3.28V, R_1 = 365k, R_2 = 940k, C = 6.5\mu)}$')

ax1.set_xlabel(r'Time (ms)')
ax1.set_ylabel(r'Signals (V)')
ax1.grid(True)

pyplot.show()
