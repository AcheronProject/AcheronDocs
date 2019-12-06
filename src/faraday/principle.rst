**********************
Principle of operation
**********************

This page describes the operation of the Faraday PCB in the details and inner workings. Some sections use heavily on applied mathematics (differential equations, Laplace transforms, transfer functions) and advanced electronics (high frequency signals, oscillators, filter design, high-speed signals processing). The writing is intended for any enthusiast to look at and understandm but nevertheless some time needs to be taken in order to check the ideas involved.

As always, feel free to contact me for questions.

The page is divided into six sections: the introduction; the capacitance AM-modulating circuit; the de-modulation circuit; the circuit used to simulate the behavior of electromechanical switches; the oscillator circuit and the filters used; and the power supply. Apart from the last section, all of the rest are well-founded with equations and SPICE simulations so they are very close to the real-world  behavior of the systems involved. Frequency and time domain plots are presented to validate the reasoning.

(0) Introduction
================

It has been a problem in the mechanical switch community that there are no custom keyboards that use the famous electro-capacitive Topre switches, which are different from the commonplace electromechanical switches generally used because they offer a very different tactile feeling and sound signature. There were some attempts, but they failed (as long as my researched has concluded). To my evaluation, this has three major factors:

- Topre switch parts are very difficult to come by. This has been changing in the past days but it is a common belief that, if you want Topre switch parts, you need to buy them from specific vendors;
- There are enough Topre switch OEM keyboards to satisfy the curious users who want a Topre experience: the KKHB Pro 2, the Leopold F660C and the Realforce line of keyboards. The HHKB Pro 2 can even be enhanced by using the famous Hasu controller, giving it bluetooth capabilities and programmability; the main issue being that these keyboards are generally expensive, ranging in the 200-dollar mark;
- The circuitry needed to deal with Topre switches is awfully complicated and difficult to implement; not only that, the available technology is very expensive, making it very hard to compete against the available OEM options. This is the main technical barrier: there are many smart and very intelligent makers in the mechanical keyboards hobby, but to my knowledge a hardware designer and specialist does not figure among them;
- In the attempts that were made to implement custom Topre keyboards, the end product was not QMK compatible. This one is a big no-no for most of the community as QMK is pretty much the backbone of this hobby.

The Faraday60 is my attempt to solve the third and fourth issues. This PCB is a QMK-compatible, custom PCB for a mechanical keyboard that uses Topre switches. Not only that, it uses simple and cheap circuitry, allowing for implementation in a myriad of layouts. 

I hope that, by having an easy-to-use and available custom option for Topre switches, these will spread in the community and parts will become more available.

(0.1) Design philosophy
-----------------------

The philosophy used for this design is a simple yet difficult one, for simplicity is the ultimate sophistication: designing circuitry for Topre switches that:

- Is cheap, using cheap and easy-to-find components;
- Can be explained in a simple yet precise way, so that aspiring designers can understand the principles of operations and eventually design their own implementations;

Also, while in the design process, the main requirements I had were:

- The tools I used to design, simulate and calculate the circuitry behavior are either free or plainly open-source;
- Documenting every single piece of information and every single thought that I had while designing. This way the design can be improved upon by other designers, creating new implementations for the community;
- Transparency is key. I was always very honest with the flaws in this design. Also, every single flaw has to be justified and understood; if the circuit has an unjustified flaw, I want to know why and how to suppress it;
- Performance requirements are reckless and necessary. While some of the features in this implementation might seem over-engineered, every single step has a justification to be and I always had very clear performance specifications, which I will detail in section **(0.3)**

(0.2) Basic principle of operation
----------------------------------

However complicated, the circuitry has a simple principle of operation. 

The Topre switch is basically a travel-to-capacitance transducer. The PCB has a metallic pad with two terminals; once the switch is pressed, a spring between the keycap and the PCB forms a capacitor with the PCB pads in such a way that, the farther the switch is pressed, the higher the capacitive effect sensed between the two terminals of the PCB pads.

In this sense, the PCB circuitry is not concerned with an electromechanical contact like with commonplace mechanical switches, but with the magnitude of the resulting capacitance of the PCB pad. This means that, in essence, Topre PCBs are capacitance sensors that take an action when the capacitance reaches a certain point.

For a common Topre switch, the actuation level is at :math:`2.2pF`, that is, the switch is considered pressed when the capacitance between the PCB pad terminals is :math:`2.2pF`. When the switch is bottomed-out, that capacitance is :math:`6pF`.

The first step is converting the capacitance value into an electrical signal. This is done in the circuitry by using an adaptive filter that outputs a sinusoidal wave. This wave has its amplitude modulated by the sensed capacitance, that is, the amplitude of the sine wave is proportional to the sensed capacitance. This is essentially an AM (Amplitude Modulation) modulator, codifying the signal (capacitance value) into the amplitude of a sinusoidal wave. The technique used for AM modulation is basically an operational-amplifier second-order filter; linear design techniques are employed (basically Laplace transform and Bode Plots).

Next is a circuit that transforms this amplitude into a smooth DC signal. This circuit is known as an AM de-modulator; more specifically, the one used here is a precision de-modulator. This circuit then outputs a DC signal which corresponds to the sensing capacitance. This part of the circuitry is the most delicate one and will be dealt with in a very technical manner, through SPICE simulations. A performance analysis of the system is carried out by means of simulation and statistical analysis.

After the demodulator is a circuit that simulates the activation of an electromechanical switch. This circuit is comprised of a comparator and an opto-coupler, and allows the whole design to be integrated with a switch matrix very similar to the ones generally used by electromechanical keyboards, while galvanically isolating the analog sensing circuitry from the digital keyboard circuitry. This comparator and optocoupler pair is also what enables QMK support.

(0.3) Performance parameters
----------------------------

The main difference from my implementation of a Topre PCB to the one that is generally used is that I employ analog precision sensing circuitry to determine the equivalent capacitance of the PCB pads in a given moment. This means that the majority of the circuitry I use is based upon applied electronic design and does not rely on software nor multiplexing techniques.

The advantage of my implementation, as stated, is that it is cheap and easier to understand while also being able to be integrated into a common firmware environment such as QMK.

However, it obviously has downsides, the first of them being the intrinsic issue with all analog sensing circuitry: settling time. All sensors have a period of time to output their readings correctly and that sensing or settling time  must be respected. In this case, the settling time means the time interval between switch activation and the acknowledgement of that activation from the MCU; this time is the main factor contributing to input lag.

In common electromechanical switches, the settling time is virtually zero, owing some time interval only to the parasitic capacitances of the diodes generally employed. In my design, the settling time is significant.

The first performance goal is to achieve a 100 microsecond maximum sensing time; this means that, by design, the time between switch pressing and the MCU acknowledgind that press must be less than that. This value is not arbitrary: most keyboard firmwares (QMK included) use a 1kHz column sensing frequency; the theoretical input lag is rated at least a milisecond, which is the timeframe a column stays at a high state. 100 microseconds is a tenth of that value.

The second performance parameter of the sensing circuit is a 1% voltage precision. This guarantees that the circuit is reliable enough to be used safely as a capacitance-to-voltage transducer. In order to achieve this, all components use must have very tight tolerances -- for example, all resistors must be rated 1% or 0.5% and all capacitors 2% or 1%. This ensures that all simulations and calculations presented here are true to reality, that is, the design is close to what really happens.

The third performance parameter is that the system is robust to power supply voltage fluctuations. This is done by using specific operation amplifier topologies and filters.

Finally, the fourth performance parameter is that the analog sensing circuitry must be completely isolated from the digital and power circuitry, avoiding crosstalk and digital noises on analog circuits.

(0.4) Disclosure
----------------

While I am confident that all the design hereby documented is going to work and is very reliable, I cannot guarantee it will work. As of december of 2019, this design has not yet been tested nor prototyped.

(1) Capacitance sensing circuit: AM modulator
=============================================

(1.1) Transfer function and basic mechanism
-------------------------------------------

The heart of the whole system is a capacitance sensing circuit, in the form of a simple op-amp filter:

.. figure:: images/current_sensor.svg
        :align: center
        :width: 400px

In this filter, :math:`C_S` is the test capacitance which will be measured, while :math:`C_F` and :math:`R_F` are fixed, project-determined parameters. This filter circuit has transfer function given by

.. math:: G(s) = \dfrac{V_O(s)}{V_I(s)} = \dfrac{sC_S}{\dfrac{1}{R_F} + sC_F}

For the non-initiated in applied mathematics, this transfer function is a complex-valued function (that is, :math:`s \in \mathbb{C}`) that describes how the output voltage :math:`V_O` changes dynamically according to changes in the input voltage :math:`V_I`. For those not familiar with the concept, the Laplace Transform :math:`\mathcal{L}\left\{f\left(t\right)\right\}` is a mathematical transformation that associates a time signal :math:`f\left(t\right)` to a function in the space of complex frequency :math:`s \in \mathbb{C}`, given by

.. math:: F\left(s\right) := \mathcal{L}\left\{f\left(t\right)\right\}(s) = \int\limits_{-\infty}^{\infty} f\left(t\right)e^{-st}dt,\ F:\mathbb{C}\to\mathbb{C}

For Linear-Time-Invariant systems (linear systems that do not change with time, that is, dont "get older"), it can be shown that the time representation and the frequency-domain representation are interchangeable, a property we will use soon.

One of the many useful tricks allowed by this transformation is to analyse the response of an LTI system given a pure sine wave. Substituting :math:`s = j\omega` (:math:`j` being the imaginary unity that satisfyes :math:`j^2 = -1`) one can deduce the behavior of the system to pure-frequency sinusoidal signals. This means that, if the input signal is a pure-sine wave of frequency :math:`\omega`, the transfer function has an amplitude which is proportional to :math:`C_S`:

.. math:: \left\lvert G(j\omega) \right\rvert = \dfrac{\omega C_S}{\sqrt{\dfrac{1}{R_F^2} + \omega^2C_F^2}}

The main idea is then that, if :math:`V_I(t)` is a perfect sinusoidal wave with frequency :math:`\omega_0`, the output :math:`V_O(t)` will be a sinusoidal wave with frequency :math:`\omega_0` but which amplitude is proportional to :math:`C_S`:

.. math:: \dfrac{\left\lvert V_O(j\omega) \right\rvert}{\left\lvert V_I(j\omega)\right\rvert} = \dfrac{\omega C_S}{\sqrt{\dfrac{1}{R_F^2} + \omega^2C_F^2}} \Rightarrow C_S = \sqrt{\dfrac{1}{\omega^2R_F^2} + C_F^2}\dfrac{\left\lvert V_O(j\omega) \right\rvert}{\left\lvert V_I(j\omega)\right\rvert}

Hence, since :math:`\omega`, :math:`R_F` and :math:`C_F` are known, by measuring the output and input amplitudes one can obtain :math:`C_S`.

It is interesting and important to note that since the amplitude of the output sinusoidal wave will be proportional to the value of :math:`C_S`, then this circuit is actually an Amplitude Modulator which generates an Amplitude Modulated (AM) signal; as such, it is natural to think that after this circuit an AM de-modulator will be needed to complete the capacitance-to-voltage sensor; the frequency at which the carrier wave oscillates will be henceforth called :math:`\omega_0`.

(1.2) Determining filter parameters
-----------------------------------

Before doing any simulations, the parameters :math:`R_F` and :math:`C_F` must be determined. Topre switches cause a capacitance variation from 0 farads (or at least a very low quantity due to stray capacitances) to 6pF when bottomed out; the switch actuates at around 2.2pF. Then, let us adopt as a design parameter that at 6pF the transfer function must have a unitary gain at the carrier frequency :math:`\omega_0`, that is:

.. math:: \left\lvert G(j\omega_0) \right\rvert = 1 = \dfrac{\omega_0 C_S}{\sqrt{\dfrac{1}{R_F^2} + \omega_0^2C_F^2}}

This design requirement is not arbitrary. The main issue associated with analog precision sensing circuitry are the second-order effects that op-amps introduce in the system, the most famous of which is the output saturation due to voltage rails. An operational amplifier will not output a voltage higher than :math:`V_{CC}` nor lower than :math:`V_{SS}`. In practicality, the limits of the output are even tighter; as a rule of thumb, we assume that the op-amp will clamp outputs higher than :math:`V_{CC}-2` and lower than :math:`V_{SS}+2`. While there are op-amps that have output limits very tight to the power rails (called rail-to-rail op-amps), these are generally more expensive and difficult to use than your everyday TL081s. For instance, the figure below shows the maximum output voltage of a TL08x operation amplifier as a function of operating frequency. Note that the maximum acievable output voltages are significantly lower than the power voltages supplied. (Image taken from the `TL08x datasheet <http://www.ti.com/lit/ds/symlink/tl082.pdf>`_).

.. _tl082_datasheet_graph :
.. figure:: images/tl082_voltage.svg
        :align: center
        :width: 400px

	. Datasheet plot showing the maximum output voltage for the TL081 opamp as a function of frequency.

The datasheet also denotes 

.. _tl082_datasheet_table :
.. figure:: images/tl082_datasheet_table.svg
        :align: center
        :width: 800px

	. Datasheet table showing the typical maximum output voltage for the TL081 opamp (image edited for clarity).


A value of :math:`V_{CC} = -V_{SS} = 15V` will be used; these voltages are easily generated from the USB power input through precision integrated buck-boost converters as the `TPS61040 <https://lcsc.com/product-detail/DC-DC-Converters_TI-Tex-as-Instruments_TPS61040DBVR_TI-Tex-as-Instruments-TI-TPS61040DBVR_C7722.html>`_ . The input voltage amplitude will be :math:`6.8V` (this value is also not arbitrary and its reason will be seen in the next section), which gives plenty headroom for the op-amps to work with without going into voltage saturation.

There is also the problem of choosing :math:`\omega_0`. This frequency should be in the kHz range, as PCB layout starts to get more and more complicated as MHz-range signals are used due to impedance effects. Also generating such high frequencies is no easy matter for your common solid state oscillators. The frequency of 100kHz was chosen, since it is both easy to generate and this value is very friendly to work with in PCB layouts.

There is also the problem of keyboard input lag. In the first designs, I used the 10kHz frequency, which is very easily generated and can be easily incorporated into PCB designs. The problem with this freqency at the end is that the AM demodulator project got too complicated, as this is a too low of a frequency to carry an AM signal and the AM demodulator dynamics got too slow; hence, the decay and charge times of the demodulator would range in the miliseconds range, which is noticeable. It also needs to be noted that the column and row sweep times of common keyboard firmwares (such as QMK) is generally 1kHz; because of this, having a milisecond-time dynamic for the demodulator will add input lag to the keyboard. 

In the second design, at 100kHz, it is very easy to design an AM demodulator with dynamics fast as to not add significant input lag. Also 100kHz is an easy to generate frequency and also easy to deal with, as most commonplace operational amplifiers can deal with that frequency range.

In this case, one can obtain a relation between :math:`R_F` and :math:`C_F`:

.. math:: 1 = \dfrac{2\pi\times 100\times 10^3\times C_S}{\sqrt{\dfrac{1}{R_F^2} + \left(2\pi\times 100\times 10^3\right)^2C_F^2}}

From here the values must be matched from the feasible resistance and capacitance values and the values the component supplier can provide. Since this is a sensor circuit, the components used must have the lowest tolerances possible. 1% or even 0.5% resistors can be easily found, while low tolerance capacitors are harder to find. In this sense, it is better to first find a capacitor value that is available in a low tolerance and then find a matching resistor. For example, Murata Electronics' GRM0333C1H2R7WA01D is a :math:`2.7pF` resistor with :math:`\pm 0.05pF` tolerance, that is, :math:`\pm 1.85\%` tolerance, which is very good. Using :math:`C_F = 2.7pF` yields :math:`R_F = 297k\Omega`. One can easily use `Uniroyal Electric's 0603WAD3004T5E <https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_UNI-ROYAL-Uniroyal-Elec-0603WAD3004T5E_C423050.html>`_, which is a 300 kilo-Ohm resistor with 0.5% tolerance. Recalculating the gain at 100kHz yields

.. math:: \left\lvert G(j2\pi\times 100 \times 10^3) \right\rvert = \dfrac{2\pi\times 100\times 10^3 6\times 10^{-12}}{\sqrt{\dfrac{1}{\left(3\times 10^{6}\right)^2} + (2\pi\times 100\times 10^3)^2\left(2.7\times 10^{-12}\right)^2}} = 1.007944041

Which is very close to the intended unitary gain, validating the designed circuit.

(1.3) Dynamic response
----------------------

There is, however, a small problem with the calculations above: they are based on a steady-state analysis of how the amplitude of the output wave changes with respect to the capacitance value. In the realtime, dynamic behaviors exist: upon a change in the measured capacitance, even if that change is instant, the change in the amplitude of the output voltage is not. There is a transient that the amplitude faces before going to its intended value; if that transient is too slow, that means that the circuit takes too much time to register the capacitance change (that is, the circuit take too much time to register a keypress), rendering the keyboard unusable. Because of this, a thorough dynamical simulation of the key actuation and how the circuit behaves is salutar.

Let's use the circuit transfer function to simulate the output response of the circuit. Suppose that the input voltage is a sinusoidal wave with amplitude :math:`A` and :math:`\omega_0` frequency; then its Laplace Transform is given by

.. math:: V_I(t) = A\cos\left(\omega_0 t\right) \Rightarrow V_I(s) = \dfrac{As}{s^2 + \omega_0^2}

Let us also admit that the capacitance :math:`C_S` changes instantly from 0 to a value :math:`C` at instant zero, which is actually the instant at which the switch is pressed; hence, :math:`C_S` is modelled as a step of amplitude :math:`C`:

.. math:: C_S(t) = C\delta(t) \Rightarrow C_S(s) = \dfrac{C}{s}

In this situation, the output voltage transfer function is

.. math:: V_O(s) = \dfrac{CAs}{\left(s^2 + \omega_0^2\right)\left(\dfrac{1}{R_F} + sC_F\right)} = \dfrac{sCA}{s^3C_F + s^2\dfrac{1}{R_F} + sC_F\omega_0^2 + \dfrac{\omega_0}{R_F}}

Expanding this expression in partial fractions,

.. math:: V_O(s) = \dfrac{ACR_F}{C_F^2R_F^2\omega_0^2 + 1}\left(\dfrac{C_FR_F\omega_0^2 + s}{s^2 + \omega_0^2} - \dfrac{1}{s + \dfrac{1}{C_FR_F}} \right)

Taking the inverse Laplace transform yields

.. math:: V_O(t) = \dfrac{ACR_F}{C_F^2R_F^2\omega_0^2 + 1}\left[\left(\sqrt{C_F^2R_F^2\omega_0^4 + 1}\right)\cos\left(\omega_0 t + \theta\right) - e^{-\dfrac{t}{C_FR_F}}\right], tan\left(\theta\right) = \dfrac{1}{C_FR_F\omega_0^2}

Naturally, the first term -- the cosine --  is the steady-state response of :math:`V_O` while the exponential term accounts for the transient behavior aforementioned. It is interesting to note that such transient will be as fast as the time constant :math:`\tau_{trans} = R_FC_F`, meaning that the lower this constant, the faster the transient is.

As was determined in the last section, we will use :math:`C = 6pF`, :math:`A = 6.8V`, :math:`\omega_0 = 10kHz`, :math:`R_F = 300k\Omega`, :math:`C_F = 2.7pF`, yielding :math:`\tau_{trans} = 810ns`; in general the time for the exponential term to fade is considered to be three to fice times this constant, which would be at most 4 microsseconds. This means that the transient response seen is very fast and can be safely and ultimately neglected -- as for all intents and purposes the transient behavior can be considered null adter five to ten times the time constant, that is, between four and eight microsseconds.

Hence the final capacitance-to-AM modulator circuit adopted is given below.

.. figure:: images/current_sensor_real.svg
        :align: center
        :width: 400px

The plot below shows the step response of this system, as simulated in LTSpice (a dedicated integrated electronics simulation software). This simulation uses a transistor-level model for the operational amplifier, meaning it is very true to reality.

.. figure:: images/capSenseResponse.svg
        :align: center
        :width: 600px

As expected, the amplitude dynamic response is very fast, ranging in the 4 microsseconds we predicted, validating the design.


(2) AM signal de-modulator circuit
==================================

The AM-modulator circuit works in a very simple purpose: it codifies the measured capacitance into the amplitude of a sinusoidal wave. However useful, this information cannot be translated into a working circuit. The goal now is to design a circuit that measures the amplitude of a sine wave and outputs the amplitude of that wave in a DC voltage signal. Such circuit is called an AM-demodulator. Such circuit is shown in the figure below.

.. figure:: images/full_demodulator.svg
        :align: center
        :width: 600px

Note that the input voltage of this circuit is the output voltage of the AM modulator of the last section, meaning it is a sinusoidal wave which amplitude codifies the value of the measured capacitance. 

This circuit has a very intricate funcioning, which will be explained in detail below.

(2.1) Precision rectifier
-------------------------

First, consider the circuit immediately below, called a precision full-wave rectifier. Such circuit takes advantage of the high open-loop gain of operational amplifiers to remove the effects of the forward voltages of the diodes, rectifying the input sine wave to almost perfection.

.. figure:: images/precision_rectifier.svg
        :align: center
        :width: 600px

The rectifier does its job, transforming the sinusoidal wave into a pulsating DC voltage.

(2.2) Peak detector
-------------------

When :math:`C_1` is added to the rectifier, the circuit becomes what is called a peak detector, which outputs the highest registered level of the input voltage. This would be enough for us, because as the switch is pressed and the input sine wave rises, the peak detector would output the amplitude of that wine wave, which is exactly what we want. There is, however, a small problem with that: if the sine wave decreases its amplitude, the output voltage does not change accordingly. See the below figure for details. 

.. figure:: images/peak_detector.svg
        :align: center
        :width: 600px

In the figure, note how when the amplitude of the input voltage decreases, the output voltage does not decrese. In practicality, this means that if we active the switch, the demodulator will detect the activation, but when we release the switch, the demodulator will act as if the switch was held. To remedy this, a resistor is added in parallel to the capacitor.a

(2.3) Damped peak detector
--------------------------

Adding a discharge resistor to the capacitor allows it do discharge when the input voltage amplitude goes down. This circuit is known as a damped peak detector.

.. figure:: images/damped_peak_detector.svg
        :align: center
        :width: 700px

This is not the final circut, however. The issue with the damped peak detector is that, in order for the release detection to work fast enough, the RC filter is fast enough to discharge between the sinusoidal peaks, generating a distortion called ripple. So we want the lowest ripple possible. However, if we use too high of a resistance, the time the circuit takes to respond to a change in the voltage input amplitude becomes too high, meaning that the circuit will take too long to detec the switch activation or deactivation. The faster we want the circuit to react, the higher the ripple, making it a design tradeoff. In general, it is recommended that one chooses :math:`R_1` and :math:`C_1` such that the time constant :math:`R_1C_1` is ten times greater than the carrier wave period.

(2.4) Filtered demodulator
--------------------------

In order to filter the ripple, a low-pass filter is added to the circuit output, originating the final full demodulator circuit.

.. figure:: images/demodulator.svg
        :align: center
        :width: 800px

This circuit gives a smooth DC voltage in it output which corresponds to the amplitude of the input sine wave, which is what we wanted after all. It is important to note, however, that the addition of this lowpass filter will not totally remove ripple, but reduce it to very low levels. Not only that, it is important to have in mind that the addition of this circuit to the :math:`C_1R_5` circuit will add loading effect to the circuit, meaning that the design of both filters must be done at the same time, that is, you cannot design one after the other independently as they affect each other's behavior.

However it has another issue: due to the ripple filtering, the output voltage is not exactly the peak of the input voltage, but a diminished value -- see the arrow indications in the above picture. The output voltage is naturally higher the higher is the input voltage amplitude. Not only this, but the voltage drop is non-linear; the actual math is available (see for example Shade Graphs for rectifier design) but is way too complicated and unnecessary.

(2.5) The important stuff
-------------------------

Having given the step-by-step construction of the demodulator, one may find its project to be unecessarily difficult. The main issue is building a circuit which components can be easily found and cheaply bought. There are many ready-to-use modulators and demodulators, but these are generally expensive and difficult to find.

At the end of the day, however, all we need to know about our circuit are two things:

- (1) Is the demodulator fast enough to detect switch activation and deactivation without significant dynamic response time? And
- (2) What is the output of the demodulator at the exact capacitance of the switch activation?

The end result is almost entirely based off of electronic dynamic simulation, and the RC filters are designed in a very iteractive, back-and-forth basis due to the inherent nonlinearity of the process. I have determined the values for resistances and capacitances through LTSpice simulation; the resulting circuit is shown in :numref:`figure_demodulator_real`.

.. _figure_demodulator_real:
.. figure:: images/demodulator_real.svg
        :align: center
        :width: 800px
	
	. Schematic of the AM modulator and demodulator circuits with component ratings and opamp models.

The next plot shows the step time response of this circuit. In this plot, the sensed capacitor goes instantly (step function) to 6 picofarads at 20 microseconds.

.. figure:: images/demodulator_6p.svg
        :align: center
        :width: 1000px

The plot shows the important waveforms as well as a zoom-out on the waves in their steady-state form. It is important to see how the damped peak detector outputs a very rippled waveform and how the output filter is effective on making it a smooth DC signal. It is also important to note that the output signal is so smooth to the point that we can consider it basically a DC signal. The plot below shows the time responde of the system top various amplitudes of capacitance step.

(2.6) Evaluating the C2V converter performance
----------------------------------------------

So let us resume what we have so far.

First, a sinusoidal 100kHz signal is generated. This signal is then used with a capacitance sensor so that the output is a 100kHz sine wave which amplitude is proportional do the capacitance being sensed. This circuit is known as an Amplitude Modulation (AM) modulator.

Then, a de-modulator is used to convert the amplitude value of the generated sine wave to a smooth DC voltage. The modulator and de-modulator circuit form then what is called a Capacitance-to-Voltage converter (C2V). The image below shows a step time response of the whole modulator and demodulator circuit when the capacitor being sensed suffers a variety of amplitudes.

In this subsection I will dissert about the techniques and parameters I used to evaluate the C2V sensor performance.

The three parameters I used were:

- **Output signal linearity**. Ideally, a sensor will output a signal that is proportional to the quantity being sensed. Linearity is an amazing property that will greatly ease the measurement and signal processing. Since the output signal is not perfectly linear, we want to measure "how linear" the output signal is. This is done by measuring the average value of the output wave in its permanent behavior. In practical terms, this linearity means that the C2V output is well-behaved with respect to the switch travel distance, that is, the output signal is not too big or too low and doesn't change its behavior abruptly during the switch travel time.
- **Output signal distortion**. Also ideally, a C2V sensor will output a perfectly smooth DC voltage. We saw in the last graph that this is not true: the output wave is rippled, albeit by a little. Hence it is necessary to measure the ripple and compare it to the actual wave value. In practical terms, this ripple basically means the accuracy of the sensor, that is, the smoother the output wave is, the more accurate the measurement is.
- **Sensor rise time**. In the field of Control Theory, the rise time is defined as the amount of time that the system needs to attain 95% of the final output value. In practical terms, the rise time is a measurement of how fast the system reacts to the input signal. In practical terms, we want the system to have at most a 100 microsecond rise time, because that was one of the main performance requirements of the sensor, listed in the introduction.

The plot below shows the time response of the sensor to steps in the input (capacitance), which simulate a very fast switch press. The many capacitance values mean various level of keypress, to exemplify how the system behaves to various levels of input.

.. figure:: images/switch_values.svg
        :align: center
        :width: 1000px

The evaluation of these performance parameters applied to this circuit will be done in the following manner. This circuit was simulated six thousand times with six thousand different input capacitance values, from time zero to a milisecond (fairly enough to hit the static behavior). The output wave was cut for the last 20 microseconds and three parameters were measured: rise time of the curve since time zero; average and peak-to-peak values of the wave in the last 20 microseconds.

The parameter analysis will use a stochastic and discrete Minimum Least Squares method, which is basically a statistic time-fitting analysis of the discrete time response of the system.

(2.6.1) Output signal linearity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The plot below shows the average value of the C2V converter output voltage as a function of input capacitance.

.. figure:: images/C2V_linearity.svg
        :align: center
        :width: 600px

As it can be seen, the curve is extremely linear. A stochastic Minimum Squares fit will confirm these results:

.. math:: \overline{V} = \left(1.255 \pm 0.001366\right)C + \left(-0.1062 \pm 0.004738\right)  

Where :math:`\overline{V}` is the average output voltage in volts and ..math:`C` is the input capacitance in picofarads. The coefficient uncertainties are measured considering a 95% confidence interval. The measured R-squared coefficient is 0.99993, confirming that this is a very good approximation.

(2.6.2) Output signal ripple
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is also interesting to note that the ripple is very linear with capacitance (despite small spikes). The plot below shows the measured peak-to-peak voltaeg of the output C2V voltage as a function of input capacitance.

.. _C2V_peaktopeak :
.. figure:: images/C2V_peaktopeak.svg
        :align: center
        :width: 600px

	. Output voltage ripple amplitude as function of sensed capacitance.

.. math:: V_{pp} = \left(2.103  \pm 0.02874\right)C + \left(-0.015.76\times \pm 0.0009967 \right)  

Where :math:`\overline{V}` is the average output voltage in milivolts and ..math:`C` is the input capacitance in picofarads. The coefficient uncertainties are measured considering a 95% confidence interval. The measured R-squared coefficient is 0.99989, confirming again that this is a very good approximation.

It is then interesting to note that, since both ripple and average value are very linear to the capacitance, the average-to-ripple ratio is very good and can be calculated by using the Chain Rule and the Propagation of Uncertainty formula:

.. math:: \dfrac{\partial \overline{V}}{\partial V_{pp}} = \dfrac{\dfrac{\partial \overline{V}}{\partial C}}{\dfrac{\partial V_{pp}}{\partial C}} = 5.76.766524013 \pm 8.181351195

This means that, given a change in capacitance, we can assert that the output ripple will rise six hundred times slower than the average value, which is an amazing result for a capacitive sensor. More precisely, we can theoretically state with 95% confidence that this relation will be in the :math:`\left[588.585172818, 604.947875208\right]` interval.

(2.6.3) Output signal rise time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/C2V_risetime.svg
        :align: center
        :width: 660px

The risetime falls into the sub-100 microsecond category, maxing out at almost 70, which is very satisfactory.

(2.6.4) Results and discussion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The results show that the designed circuit passes the performance requirements with flying colors, attendind every requisite with much room to spare.

It is very important to note that the nonlinear, stochastic and simulatory analysis hereby presented is developed upon ideal conditions -- perfect components and no parasitic second-order effects. The main issue here is the tolerances of the components, which can greatly alter the time and frequency response of the system. The operational amplifiers guarantee that these tolerances will not have a significant effect to some extent, but nevertheless it is of the utmost importance to use precise components with at most 2% tolerance.

Also, there is a very difficult issue with implementation of this circuit which is PCB layout. Since all waves have a fundamental frequency of the modulator carrier (100kHz), a badly laid out PCB can generate parasitic capacitances and inductances that can simply destroy the circuit behavior and make all the analysis here useless, specially because of the fairly analog and high speeds involved. Hence, all these results require a very well laid-out PCB and circuit stability, which can be expected from USB-based PCBs.

The AM modulator and AM de-modulator circuit will henceforth be called a C2V (Capacitance-to-Voltage) converter.

(3) Switch simulation circuit
=============================

The C2V converter is a circuit that outputs a DC voltage correspnding to a sensed capacitance (the switch). Ultimately what we want is to simulate an emech switch activation on the MCU switch matrix, connecting a particular row to a particular column. This simulation, however, must be triggered only if the input capacitance hits a cretain level that corresponds to the Topre switch activation point, 2.2pF to be more exact. In our circuit, this means that this simulation must only be triggered when the C2V output voltage hits 2.389V.

The simulation circuit is then comprised of two stages:

-  **(1) A comparator (or voltage detector)**. The comparator stage detects a voltage level greater than 2.389V coming from the C2V, and triggers the actuator when that happens. The comparator used here also features a noise-filtering capability called *hystheresis*, which protects the circuit from the voltage ripples produced by the C2V.
- **(2) An actuator (or decoupler)**.  The actuator actuates on the MCU switch matrix when it is triggered, but there is a catch: it  must also meet performance requirements, the first requirement being that the actuator must offer n-key rollover and anti-ghosting capabilities to the matrix. The second requirement being that this actuator must isolate the sensing circuitry from the digital MCU part, in order to make the sensing circuit more reliable. Finally, this circuit must be again cheap, easy to understand and easily available.

(3.1) Simulating an emech-switch behavior
-----------------------------------------

In order to understand how the actuator circuit simulates an electromechanical switch and diode pair, let us first understand how a keyboard switch matrix works. During normal operation, a Microprocessor Unit (MCU) has its pins connected to rows and columns; the rows and columns are connected by switches. Electrically, switches are nothing more than simple electromechanical short-circuits activated when the switch is pressed. This short-circuit is generally comprised by two leaf contacts that are pressed against each other.

All the rows are set as input (most commonly open-drain) and all columns are set as outputs (most commonly push-pulls). At a given moment only one column can be at high state; in that moment, the MCU senses for voltage in the row pins. If a given row pin receives a high state, that is because the switch corresponding to that particular column and row was pressed.

After some time (generally a milisecond) that particular row is turned off and the next row receives a high state; the MCU then scans for actions on the rows.i This cycle runs endlessly until the MCU is turned off, and constitutes the main loop of a keyboard firmware.

The problem with switches, however, is that since they are short circuits, current can flow in both directions. Say that at a particular time the column 1 is at high state, and the switch at column 1 and row 2 is pressed. If another switch is also pressed in the same column, say, switch at row 2 column 3, then columns 1 and 3, as well as row 2, are short-circuited. This may cause many effects from damaging the MCU to causing very high currents; the most known phenomena and common is **ghosting**, where this situation makes the MCU register *ghost* keys that were not pressed.

To remedy this, diodes are generally used in series with the switches; these diode, presenting assymetrical conduction, will prevent currents from flowing back to the switches and causing unintended issues. This way we can press any combination of switches in the keyboard and the MCU will register the right keypresses; this feature is known as *n-key rollover* or nKRO. Also this technique enables the MCU to not detech ghost keypresses, that is, this implementation prevents ghosting, a feature called *anti-ghosting* or AGh.

Komar, the designer of the famous GH60 PCB, has an amazing explanation in `his blog <http://blog.komar.be/how-to-make-a-keyboard-the-matrix/>`_, definitely worth the reading for any PCB designer worth their salt.

(3.3) Comparator circuit
------------------------

We know from our C2V simulations that  when it outputs a voltage grater than 2.389 volts, we can consider that the switch is activated. Fortunately, there is a very handy circuit in electronics called a comparator, shown in the figure below, that can be used as a voltage level detection circuit.

.. figure:: images/comparator_circuit.svg
        :align: center
        :width: 300px

The comparator works in a very simple manner: if :math:`V_P > V_N`, the output is ideally :math:`V_{CC}` (remember that this only happens with a special kind of opamp called rail-to-rail; a common opamp will input only approximately :math:`V_{CC}-2`); if :math:`V_P < V_N` then the output voltage is VSS (then again, normal opamps will output approximately :math:`V_{SS}+2`). 

A very common technique is to generate a reference signal through a voltage resistor divider from VCC, as denoted in :numref:`comparator_circuit_ideal`. The figure also shows the output response of the system: :math:`V_o = V_H` if :math:`V_I > V_F` and :math:`V_o = V_L` if :math:`V_I < V_F`. :math:`V_H` and :math:`V_L` are the maximum and minimum peak voltages of the opmp at :math:`V_{CC}`; as :numref:`tl082_datasheet_table` shows, for the TL08x at 15V, those are :math:`\pm 13.5V`. It is interesting to note that since the opamp has a very high input impedance, one can calculate :math:`V_F` as

.. math:: V_F = V_{CC}\dfrac{R_1}{R_1 + R_2}

.. _comparator_circuit_ideal :
.. figure:: images/comparator_circuit_ideal.svg
        :align: center
        :width: 800px

	. Ideal voltage-divider-fed comparator circuit

This is the key: if we assume :math:`V_N = 2.289V` and hook up the AM de-modulator circuit to :math:`V_P` then we will achieve the very result we want: the output signal will be approximately VCC-2 when the PCB pads sensed capacitance is greater than 2.2pF (key is activated) and VSS+2 when it is not pressed. Producing a 2.389V level is easy, it can be done by using a resistive divider with 11.1k and 2.10k resistors, which will input a 2.389V into :math:`V_N`, which is very close to the 2.43V we seek. See the circuit below for the real implementation. Capacitor :math:`C_1` is used to prevent spikes on the 15V supply to interfere with the sensing action.

.. _comparator_circuit_real :
.. figure:: images/comparator_circuit_real.svg
        :align: center
        :width: 400px

	. Voltage-divider-fed comparator circuit using TL081, designed to trigger at the 2.389V (2.2pF) voltage mark.

(3.4) Comparator circuit with hystheresis
-----------------------------------------

The circuit in figure :numref:`comparator_circuit_real` has a problem, however: it reacts very wildly to flickering or rippled voltages. :numref:`comparator_nonhystheresis_response` shows the time response of that circuit given a flickering input voltage.

.. _comparator_nonhystheresis_response :
.. figure:: images/comparator_nonhystheresis_response.svg
        :align: center
        :width: 400px

	. Time response (top plot) of the circuit of :numref:`comparator_circuit_real` given a flickering input voltage (bottom plot).

In keyboard practical terms, this means that the comparator will trigger the switch simulation circuit uninterruptly, which will make the MCU register the same key countless times inside a very small time space, an unwanted behavior we generally call "key chattering". A very effective way to solve this issue is to add a feedback resistor, which generates a feature called **hystheresis**. :numref:`comparator_circuit_hystheresis_ideal` shows the circuit schematic and its input-output response.

.. _comparator_circuit_hystheresis_ideal :
.. figure:: images/comparator_circuit_hystheresis_ideal.svg
        :align: center
        :width: 800px

	. Voltage-divider-feedback-ed comparator ideal circuit.

What is interesting about this circuit is that it adds a sort of "conditional response". Applying the Kirchoff Current Law yields

.. math:: \dfrac{V_0 - V_F}{R_F} + \dfrac{V_F}{R_2} = \dfrac{V_{CC} - V_F}{R_1} \Leftrightarrow V_F = \dfrac{\dfrac{V_{CC}}{R_1} - \dfrac{V}{R_F}}{\dfrac{1}{R_1} + \dfrac{1}{R_2} - \dfrac{1}{R_F}}

Suppose that the circuit is working with a very low input voltage and it keeps growing. The output voltage is :math:`V_L`, so the feedback voltage is given by

.. math:: V_{FH} = \dfrac{\dfrac{V_{CC}}{R_1} - \dfrac{V_L}{R_F}}{\dfrac{1}{R_1} + \dfrac{1}{R_2} - \dfrac{1}{R_F}}

Meaning that the output voltage will only rise when the input voltage is :math:`V_{FH}`. Similarly, if the input voltage is too high and keeps getting lower, the feedback voltage is given by

.. math:: V_{FL} = \dfrac{\dfrac{V_{CC}}{R_1} + \dfrac{V_H}{R_F}}{\dfrac{1}{R_1} + \dfrac{1}{R_2} - \dfrac{1}{R_F}}

And then the output voltage will only lower when the input voltage is :math:`V_{FL}`.

The magical thing about this circuit is that it has a small amplitude :math:`V_A`, around a central voltage :math:`V_C`, in the input thresholds that prevent it from reacting to flickering signals:

.. math:: A = V_{FH} - V_{FL} = \dfrac{ \dfrac{V_H - V_L}{R_F}}{\dfrac{1}{R_1} + \dfrac{1}{R_2} - \dfrac{1}{R_F}}

.. math:: V_C = \dfrac{\dfrac{V_{CC}}{R_1} - \dfrac{V_L + V_H}{2R_F}}{\dfrac{1}{R_1} + \dfrac{1}{R_2} - \dfrac{1}{R_F}}

:numref:`comparator_circuit_hystheresis_ideal_response` shows the input-output-response of the comparator with hystheresis consiering the central voltage and voltage amplitude.

.. _comparator_circuit_hystheresis_ideal_response :
.. figure:: images/comparator_circuit_hystheresis_ideal_response.svg
        :align: center
        :width: 600px

	. Voltage-divider-feedback-ed comparator ideal circuit input-output-response.

The formulas, however, are pretty difficult, specially because they contain three resistance parameters to tune. What is generally done is to consider :math:`R_F` much greater than :math:`R_1` or :math:`R_2`, which is generally true. Under this assumption, we can approximate

.. math:: A \approx \dfrac{1}{R_F}\dfrac{ V_H - V_L}{\dfrac{1}{R_1} + \dfrac{1}{R_2}}

.. math:: V_C \approx \dfrac{\dfrac{V_{CC}}{R_1}}{\dfrac{1}{R_1} + \dfrac{1}{R_2}}

What we want ultimately is that the amplitude voltage be bigger than the ripple amplitude, avoiding that the circuit respond too rapidly due to the ripple. As a security, measure, we generally adopt the amplitude as twice the maximum ripple. From :numref:`C2V_peaktopeak` we can assume that, at the desired actuation point (2.2pF), the ripple is almost 4mV; hence we want a hystheresis amplitude of 8mV. Using the same resistances from the non-hysteresis comparator yields

.. math:: R_F \approx \dfrac{1}{8\times 10^{-3}}\dfrac{ 13.5 - \left(-13.5\right) }{\dfrac{1}{11.1\times 10^3} + \dfrac{1}{2.01\times 10^3}} = 5.743678489702517M\Omega

Adopting the nearest value, :math:`5.76M\Omega`. If you feel uncomfortable with the approximations, you can use the non-approximated formulas:

.. math:: A = \dfrac{ \dfrac{13.5 - \left(-13.5\right)}{5.76\times 10^6}}{\dfrac{1}{11.1\times 10^3} + \dfrac{1}{2.01\times 10^3} - \dfrac{1}{5.76\times 10^6}} = 8.207749 mV

.. math:: V_C = \dfrac{\dfrac{15}{11.1\times 10^3} - \dfrac{13.5-\left(-13.5\right)}{2\times 5.76\times 10^6}}{\dfrac{1}{11.1\times 10^3} + \dfrac{1}{2.01\times 10^3} - \dfrac{1}{5.76\times 10^6}} = 2.294971102V

Which are values close to the ones wanted: :math:`8mV` and :math:`2.389V`, but not quite there. We can adjust :math:`R_1` and :math:`R_2` slightly to :math:`R_1 = 10.7k\Omega` and :math:`R_2 = 2k\Omega`, and keeping :math:`R_F = 5.76M\Omega`, 

.. math:: A = \dfrac{ \dfrac{13.5 - \left(-13.5\right)}{5.76\times 10^6}}{\dfrac{1}{10.7\times 10^3} + \dfrac{1}{2\times 10^3} - \dfrac{1}{5.76\times 10^6}} = 7.900933mV

.. math:: V_C = \dfrac{\dfrac{15}{10.7\times 10^3} - \dfrac{13.5 - \left(-13.5\right)}{2\times 5.76\times 10^6}}{\dfrac{1}{10.7\times 10^3} + \dfrac{1}{2\times 10^3} - \dfrac{1}{5.76\times 10^6}} = 2.407013612V

:numref:`comparator_hystheresis_response` shows the output of this circuit to a flickering input signal. Comparing this response to :numref:`comparator_nonhystheresis_response` makes clear how the hystheresis makes the circuit much more well-behaved, making it much more well-suited to a rippled voltage like the one that the C2V outputs.

.. _comparator_hystheresis_response :
.. figure:: images/comparator_hystheresis_response.svg
        :align: center
        :width: 400px

	. Time response (top plot) of the circuit of :numref:`comparator_circuit_real` given a flickering input voltage (bottom plot).

And those are much closer results.

http://www.ti.com/lit/ug/tidu020a/tidu020a.pdf

(3.2) Actuator circuit
----------------------

For now, what I want to emphasize is: the circuit used for simulating the switch and diode behavior has to provide the same features -- namely, nKRO and AGh. What is interesting to note is that a switch plus diode pair is basically an electrical contact that only conducts current in one way.

If you know electronics at an enough high level, a lighbulb might have popped in your head: a current conductor that conducts current in a single way when an electrical signal is input is simply a saturated bipolar transistor; a simple common collector or common drain topology will serve as an electronically controlled switch that conducts current in a single way. And that is perfectly correct. However, those topologies have a major flaw: not only they need a power supply, they also need biasing components. These two requirements will make the circuit significantly bigger and complex. Also, it is known that the behavior of these topologies is extremely dependant on the tolerances of those components and the parameter variation of the transistor, which is huge for commonplace BC548s.

A far easier solution to this task is using an **opto-coupler**. This device is made of an LED (generally infra-red emitter) and a transistor with an open gate (a phototransistor); when the LED conducts light directly into the transistor's base, the base is overflown with carriers due to photon recombination at the energy band level, making the transistor conduct current too. This topology uses only a single component, does not need a dedicated power supply, and will provide the assymetrical conductance we need for the AGh and nKRO.

Another advantage of this device is that it galvanically isolates the diode matrix and the capacitor sensing circuit. Whereas the switch matrix uses the USB or LDO-provided 5 or 3.3V for its operation, the capacitance sensing uses 15V generated by a voltage source. Not only that, mixing the digital power rails and analog sensing power rails can be disastrous to the sensing circuit, because it relies on very precise measurements to work. Hence, not only the opto-coupler does the job of being an actuator, it also promotes isolation between digital processing circuit and analog sensor, greatly enhancing the reliability of the circuit.


(5) Carrier wave generator oscillator
=====================================

.. figure:: images/oscillator_dft.svg
        :align: center
        :width: 60px

(6) Power supply and noise isolation
====================================
