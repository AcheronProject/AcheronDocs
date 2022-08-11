# Python standard math/scientific libraries
import numpy as np
import csv

from scipy.optimize import curve_fit

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

def sol_func(t,R1,R2,C,V): return R2/(R1+R2)*V*(1-np.exp( -t* (R1+R2)/(R2*R1*C)  ))

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

mint = 2.8
maxt = 15

t_lim = t_meas
b0_lim = b0_meas
remove = []

for i in range(len(t_lim)):
	if t_lim[i] > maxt or t_lim[i] < mint :
		remove.append(i)

t_lim = np.delete(t_lim,remove)
b0_lim = np.delete(b0_lim,remove)

t_init = t_lim[0]
t_lim_disloc = np.empty(len(t_lim))
t_meas_disloc = np.empty(len(t_meas))

for i in range(len(t_lim)):
	t_lim_disloc[i] = t_lim[i] - t_init

for i in range(len(t_meas)):
	t_meas_disloc[i] = t_meas[i] - t_init

print(t_lim_disloc)
popt, pcov = curve_fit(sol_func, t_lim_disloc, b0_lim,bounds=([300e3,900e3,7e-6,2],[400e3,1100e3,12e-6,3.3]),method='trf')
print(popt)


R1 = popt[0]
R2 = popt[1]
C = popt[2]
V = popt[3]

fig1 = pyplot.figure()
ax1 = fig1.add_subplot(1,1,1)

ax1.plot(t_meas, b0_meas,linewidth=1 ,color="red",label=r'Measured BOOT0')
ax1.plot(t_lim, b0_lim,linewidth=1 ,color="blue",label=r'Limited BOOT0')
ax1.plot(t_lim, [sol_func(i,R1,R2,C,V) for i in t_lim_disloc], linewidth=1 ,color="orange",label=r'Curve-fitted BOOT0')
ax1.plot(t_meas, [sol_func(i,R1,R2,C,V) for i in t_meas_disloc], linewidth=1 ,color="orange",label=r'Curve-fitted BOOT0')
ax1.legend()

fig1.suptitle(r'nRST-BOOT0 voltage signals curves: measured, nominal and parameter-fitted $\mathsf{{(V_{{3V3}} = {0:8.4f}, R_1 = {1:8.4f}k, R_2 = {2:8.4f}k, C = {3:8.4f}\mu) }}$'.format(V,R1/1000,R2/1000,C*1e6))

ax1.set_xlabel(r'Time (ms)')
ax1.set_ylabel(r'Signals (V)')
ax1.grid(True)

pyplot.show()
