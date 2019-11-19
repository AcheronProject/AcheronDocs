**********************
Principle of operation
**********************

===========================
Capacitance sensing circuit
===========================

-------------------------------------
Transfer function and basic mechanism
-------------------------------------

The heart of the whole system is a capacitance sensing circuit, in the form of a simple op-amp filter:

.. figure:: images/current_sensor.svg
        :align: center
        :width: 400px

In this filter, :math:`C_S` is the test capacitance which will be measured, while :math:`C_F` and :math:`R_F` are fixed, project-determined parameters. This filter circuit has transfer function given by

.. math:: G(s) = \dfrac{V_O(s)}{V_I(s)} = \dfrac{sC_S}{\dfrac{1}{R_F} + sC_F}

This means that the transfer function has an amplitude which is proportional to :math:`C_S`:

.. math:: \left\lvert G(j\omega) \right\rvert = \dfrac{\omega C_S}{\sqrt{\dfrac{1}{R_F^2} + \omega^2C_F^2}}

The main idea is then that, if :math:`V_I(t)` is a perfect sinusoidal wave with frequency :math:`\omega_0`, the output :math:`V_O(t)` will be a sinusoidal wave with frequency :math:`\omega_0` but which amplitude is proportional to :math:`C_S`:

.. math:: \dfrac{\left\lvert V_O(j\omega) \right\rvert}{\left\lvert V_I(j\omega)\right\rvert} = \dfrac{\omega C_S}{\sqrt{\dfrac{1}{R_F^2} + \omega^2C_F^2}} \Rightarrow C_S = \sqrt{\dfrac{1}{\omega^2R_F^2} + C_F^2}\dfrac{\left\lvert V_O(j\omega) \right\rvert}{\left\lvert V_I(j\omega)\right\rvert}

Hence, since :math:`\omega`, :math:`R_F` and :math:`C_F` are known, by measuring the output and input amplitudes one can measure :math:`C_S`.

-----------------------------
Determining filter parameters
-----------------------------

Before doing any simulations, the parameters :math:`R_F` and :math:`C_F` must be determined. Topre switches cause a capacitance variation from 0 farads (or at least a very low quantity due to stray capacitances) to 6pF when bottomed out; the switch actuates at 2pF. Then, let us adopt as a design parameter that at 6pF the transfer function must have a unitary gain at the frequency :math:`\omega_0`, that is:

.. math:: \left\lvert G(j\omega_0) \right\rvert = 1 = \dfrac{\omega_0 C_S}{\sqrt{\dfrac{1}{R_F^2} + \omega_0^2C_F^2}}

This design requirement is not arbitrary. The main issue associated with precision sensing are the second-order effects that op-amps introduce in the system, the most famous of which is the output saturation due to voltage rails. An operational amplifier will not output a voltage higher than :math:`V_{CC}` nor lower than :math:`V_{SS}`. In practicality, the limits of the output are even tighter; as a rule of thumb, we assume that the op-amp will clamp outputs higher than :math:`V_{CC}-2` and lower than :math:`V_{SS}+2`. While there are op-amps that have output limits very tight to the power rails (called rail-to-rail op-amps), these are generally more expensive and difficult to use than your everyday TL081s.

There is also the problem of choosing :math:`\omega_0`. This frequency should be in the kHz range, as PCB layout starts to get more and more complicated as MHz-range signals are used due to impedance effects. Also generating such high frequencies is no easy matter for your common solid state oscillators. The frequency of 10kHz was chosen, since it is both easy to generate and this value is very friendly to work with in PCB layouts.

A value of :math:`V_{CC} = -V_{SS} = 10V` will be used; these voltages are easily generated from the USB power input through precision integrated buck-boost converters as the TPS61040. The input voltage amplitude will be :math:`5V`. which gives plenty headroom for the op-amps to work with without going into voltage saturation.

In this case, one can obtain a relation between :math:`R_F` and :math:`C_F`:

.. math:: 1 = \dfrac{2\pi\times 10k \times C_S}{\sqrt{\dfrac{1}{R_F^2} + \left(2\pi\times 10k\right)^2C_F^2}}

From here the values must be matched from the feasible resistance and capacitance values and the values the component supplier can provide. Since this is a sensor circuit, the components used must have the lowest tolerances possible. 1% or even 0.5% resistors can be easily found, while low tolerance capacitors are harder to find. In this sense, it is better to first find a capacitor value that is available in a low tolerance and then find a matching resistor. For example, Murata Electronics' GRM0333C1H2R7WA01D is a 2.7pF resistor with +- 0.05pF tolerance, that is, +- 1.85% tolerance, which is very good. Using :math:`C_F = 2.7pF` yields :math:`R_F = 2.97M\Omega`. One can easily use Uniroyal Electric's 0603WAD3004T5E, which is a 3 mega-Ohm resistor with 0.5% tolerance. Recalculating the gain at 10kHz yields

.. math:: \left\lvert G(j20k\pi) \right\rvert = \dfrac{20k\pi\times 6\times 10^{-12}}{\sqrt{\dfrac{1}{\left(3\times 10^{6}\right)^2} + (20k\pi)^2\left(2.7\times 10^{-12}\right)^2}} = 1.007944041

Which is very close to the intended unitary gain.

----------------
Dynamic response
----------------

There is, however, a small problem with the idea: upon a change in the measured capacitance, even if that change is instant, the change in the amplitude of the output voltage is not. There is a transient that the amplitude faces before going to its intended value; if that transient is too slow, that means that the circuit takes too much time to register the capacitance change (that is, the circuit take too much time to register a keypress), rendering the keyboard unusable. Because of this, a thorough dynamical simulation of the key actuation and how the circuit behaves is salutar.

 Let's use the circuit transfer function to simulate the output response of the circuit. Suppose that the input voltage is a sinusoidal wave with amplitude :math:`A` and :math:`\omega_0` frequency:

.. math:: V_I(t) = A\cos\left(\omega_0 t\right) \Rightarrow V_I(s) = \dfrac{As}{s^2 + \omega_0^2}

Let us also admit that the capacitance :math:`C_S` changes instantly from 0 to a value :math:`C` at instant zero, which is actually the instant at which the switch is pressed; hence, :math:`C_S` is modelled as a step of amplitude :math:`C`:

.. math:: C_S(t) = C\delta(t) \Rightarrow C_S(s) = \dfrac{C}{s}

In this situation, the output voltage transfer function is

.. math:: V_O(s) = \dfrac{CAs}{\left(s^2 + \omega_0^2\right)\left(\dfrac{1}{R_F} + sC_F\right)} = \dfrac{sCA}{s^3C_F + s^2\dfrac{1}{R_F} + sC_F\omega_0^2 + \dfrac{\omega_0}{R_F}}

Expanding this expression in partial fractions,

.. math:: V_O(s) = \dfrac{ACR_F}{C_F^2R_F^2\omega_0^2 + 1}\left(\dfrac{C_FR_F\omega_0^2 + s}{s^2 + \omega_0^2} - \dfrac{1}{s + \dfrac{1}{C_FR_F}} \right)

Taking the inverse Laplace transform yields

.. math:: V_O(t) = \dfrac{ACR_F}{C_F^2R_F^2\omega_0^2 + 1}\left[\left(\sqrt{C_F^2R_F^2\omega_0^4 + 1}\right)\cos\left(\omega_0 t + \theta\right) - e^{-\dfrac{t}{C_FR_F}}\right], tan\left(\theta\right) = C_FR_F^2\omega_0^2

Naturally, the first term -- the cosine --  is the steady-state response of :math:`V_O` while the exponential term accounts for the transient behavior aforementioned. It is interesting to note that such transient will be as fast as the time constant :math:`\tau_{trans} = R_FC_F`, meaning that the lower this constant, the faster the transient is.

As was determined in the last section, we will use :math:`C = 6pF`, :math:`A = 5V`, :math:`\omega_0 = 10kHz`, :math:`R_F = 3M\Omega`, :math:`C_F = 2.7pF`, yielding :math:`\tau_{trans} = 8.1\mu s`, meaning that the transient response seen is very fast and can be safely and ultimately neglected. 
