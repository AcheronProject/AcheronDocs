# A single-push reset circuit for STM32

*Making the complex a simple thing is (paradoxically!) complex*

**By Gondolindrim with contributor ishtob**

**First version** published in august 12, 2019

**Last revision** in september 2, 2021

---

The STM32 family of microcontrollers offers a wide good variety of options when it comes to boot selection. The majority of STM32 devices are flashed at factory with a bootloader that is very permissive and complete; it allows for a wide variety of options when it comes to booting options, boot behaviors, in-system programming through I2C, SPI, serial communication and very good debug features.

One of the most interesting aspects of working with these devices is the way STM tackled the boot selection process, that is, what portion of the memory is used for the stack pointer start. In STM32F0xx devices, there are basically four ways you can boot the MCU: main flash memory, main system memory, embedded SRAM memory, and an "empty check" option only available to STM32F04x and STM32F09x devices.

This articule is written for the STM32F072 MCU that I use mainly in my boards. The [part 2](../reset_article_2/reset_article_2.md) will discuss the adaptation for other families of STM32 microcontrollers; however, all of those will take over from the principles, calculations and simulations in this article.

In this article I will detail the many possibilities there are for handling these boot options, and the design of a reset circuit that can reset the MCU simply or drive it to bootloader, using a single push button.

## 1 Introduction

Embedded Engineering is fairly complicated shenanigans. It involved dominating technologies and procedures so complex that they need higher education to be fully mastered, and then make those very same technologies and procedures available and accessible to the general public which is very unkowledgeable about technology. Customers generally want a very simple solution to a very complex problem and, sometimes, the best product does not always win if it is not user-friendly -- Apple products being the master example for me, being much less powerful than the competitors in the same price range but light-years ahead in terms of user experience and usability.

One of such problems is handling the reset event in an MCU. A microcontroller generally has several memory options, all of which can be invoked, operated, written and erased at runtime and all of which containing their particular use and place. From and end user's perspective, *we want it to just work*, but that's not how it goes in research and development. R&D is a very nonlinear process that requires full mastery of the system being worked on, which is again completely incompatible with user experience due to the general unkowledgeability of the end user.

In this article I will detail the three possibilities we have to handle that problem in STM32F07x MCUs; each of the three ways have their pros and cons and, just like almost everything in PCB development, design choices have to be made.


### 1.1 But what exactly is the problem?

Of course, no one develops a solution in search of a problem. So, first of all, before tackling hardware and firmware specifics, we need to state **"what exactly is the problem?"** and work from there.

The problem is twofold. First, the STM32 MCUs have several boot options and we need to know which ones does what, so that we can limit those options to the ones the end user will effectively use, and how to access them individually. Second, we need to minimize user interaction to such a degree that designers are comfortable knowing the end user can operate the product with zero knowledge about how it works.

In STM32 MCUs, the user will basically use two boot regions. The first is the **main system memory**, which starts at address 0x1FFF in STM32F07x devices (see [1], section 6.3.14 for the addresses of the other devices in the family). The main system memory contains the bootloader program that is flashed by STM at the factory. One of the main reasons for the adoption of the STM32F072/071 devices is the USB DFU capability of their bootloader, that is, the possibility of upgrading the flash program memory from the USB peripheral. Devices without this capability need a dedicated communication, called In-System Programming or Serial Wire Debug for STM (SWD for short), to have their flash memory upgraded. This boot option is used when the user want to re-flash their keyboard, which is not often but still needed very seldomly.

The second boot region that the end user willl need is the **main flash memory**, located at 0x08000000, where the operating firmware like QMK is to be flashed. Resetting the MCU into this are is what you would expect from the word *reset*. It stops execution and re-starts it from the beggining of the program, which can be needed in many cases such as if the keyboard firmware has stopped due to a bug or if the keyboard is simply showing erratic behavior, or after flashing the keyboard.

Booting from SRAM or the empty check are primarily development options which the end user will much, much rarely use; hence, we want to limit the boot options to system memory and flash memory. The problem then becomes: **how to develop a user-friendly way to make available the flash memory and system memory choices into an end product, which requires minimal knowledge about the system's intricacies and can still be reliable enough?**

### 1.2 How boot selection works on STM32F0xx

The way we select the boot region in STM32F0xx devices are through external pins and certain registers. In those devices there are two external pins, **nRST** and **BOOT0**, and two memory registers **nBOOT1** and **nBOOT0** which are set in software. **nRST** is the hardware reboot pin: when this pin is pulled low, all but some registers in the MCU are reset (it has a low logic, hence the "n" in "nRST"). When it gets back to normal high the MCU starts from memory address 0x00000000 and the bootloader program takes over. At the fourth rising edge of the system clock the **BOOT0**, **nBOOT0** and **nBOOT1** values are sampled and the boot option is determined according to the table at figure 1.

<figure>
  <img src="../../images/reset_article/reset_table.svg" width="600" align="middle"/>
  <figcaption><b> Figure 1. </b> Table of boot options for STM32F0xx devices. Source: [2].</figcaption>
</figure>

First of all, we can ignore the three bottom options as those are only available to STM32F04x and STM32F09x devices. Then for the three top options, we can ignore **BOOT_SEL** that is 1 for all these options and **nBOOT0** which is marked as an **x** meaning its value does not matter for these options. As for **nBOOT1**, we have to remember it comes factory-set as zero, meaning that if we simply don't mess with it, we can do both the options we wanted -- boot from system memory or boot from flash -- at the expense of not being able to start from SRAM which is very, very rare on an end-product occasion so not a big deal anyways.

In the end, we can reset into flash or go into DFU USB by only setting the value of the pin **BOOT0**: if it is high, the MCU goes into DFU and if it is low, it resets into flash.

### 1.3 The vanilla reset circuit

The least complicated reset circuitry we can use is actually very simple. It has only two interactions required from the user: setting BOOT0 to either low or high logic levels and pressing a button to trigger the hardware reset process through pin nRST. Reference [2] in page 30 shows a very simple yet effective way to achieve this in the reference design. This vanilla circuit is depicted in figure 2 .

<figure>
  <img src="../../images/reset_article/vanilla_reset.svg" width="400" align="middle"/>
  <figcaption><b> Figure 2. </b> Vanilla reset circuit recommended by ST in [2].</figcaption>
</figure>

This circuit is very simple and only needs a couple components. The pulling of nRST is done by a simple push button and a capacitor to avoid weird transients; the BOOT0 selection is done by a selector switch. In some custom keyboards like [the Sagittarius](https://geekhack.org/index.php?topic=107023>), this employs an SPDT switch:

<figure>
  <img src="../../images/reset_article/sagittarius_reset.svg" width="600" align="middle"/>
  <figcaption><b> Figure 3. </b> Implementation of the vanilla reset circuit in the Sagittarius keyboard using an SPDT switch and a push button.</figcaption>
</figure>

On these boards, to flash the MCU, the user changes the SPDT to position one and presses the push button, forcing the MCU to DFU. After the MCU is flashed, the user changes the SPDT back to the 0 position and presses the button again. 

On BluePill boards, this is done through a simple jumper selector.

<figure>
  <img src="../../images/reset_article/bluepill_reset.svg" width="400" align="middle"/>
  <figcaption><b> Figure 4. </b> Implementation of the vanilla reset circuit in the Blue Pill feathboards using a jumper and a push button.</figcaption>
</figure>

The vanilla circuit of figure 1 can be modified just a little bit to make it more reliable, by addding a 100R resistor in series with the nRST button to avoid fast voltage changes in its capacitor and adding a little 100n capacitor to BOOT0 to avoid any fast transients, since it is a CMOS-type input.

<figure>
  <img src="../../images/reset_article/vanilla_reset_gondo.svg" width="400" align="middle"/>
  <figcaption><b> Figure 5. </b> Slight modification from the vanilla reset circuit recommended by ST.</figcaption>
</figure>

### 1.4 The problems with the vanilla circuit

There are two problems with the vanilla circuit of figures 1 and 5. First, it requires way too many operations from the user. Turn SPDT to high, push button, flash, turn SPDT back to low, push button again. This can confuse some people and, ultimately, can make the flashing experience hard for people not tech-savvy.

The second one is that it's a *double-action*. Since the hardware reset rests on the PCB, and to access the PCB one must open the case (unscrew, remove gaskets...) which takes a lot of time, some makers in the community like to have their keyboard plates with a small hole so that the push button can be accessed with a small tool like a pencil, hence allowing the user to reset the microcontroller easily. This vanilla circuit does not allow for that because it is double-action.

## 2 A new reset circuit

In middle development of the SharkPCB, a user by the name of ishtob blessed me with a piece of his knowledge and shared a reset circuit he was working on. A version of this circuit is depicted in figure 6.

<figure>
  <img src="../../images/reset_article/reset1.svg" width="600" align="middle"/>
  <figcaption><b> Figure 6. </b> ishtob's original reset circuit for STM32.</figcaption>
</figure>

The circuit is pretty clever; the idea is that the user will need to interact with the PCB only once to get it to work. When the push button is pressed, the transistor will drive nRST to ground immediately; the reset and capacitor by BOOT0 will store voltage. By the time the user lets go of the button, BOOT0 is charged up and nRST is low. The MCU then goes into bootloader mode.

There are two caveats with this circuit. The first is that the diode is absolutely needed; without it, the charged voltage across the BOOT0 capacitor can maintain the transistor conducting and the MCU will not reset before BOOT0 loses its voltage to resistor decay. The second is that the transistor used has to have a base resistor, or else the base and emitter will be shorted -- a bipolar transistor is basically two diodes back-to-back -- and the circuit will never work; using a pre-biased transistor (also known as digital transistor) like the DTC123JK helps to keep component count lower due to the integrated resistors.

One might point out that this circuit only does half the job -- it is able to get the MCU into DFU, but not able to reset the program. Well, as it turns out, resetting the MCU is not needed *per se*. See, QMK has software reset capabilities, so once the MCU is flashed it automatically resets. The user is also able to reset the MCU through a key combination, making use of the Boot Magic features of QMK.

The circuit works wonders. It is fairly simple, does the job and requires few components; revisions Alpha of the SharkPCB and ArcticPCB use it. Still, it is not good practice to rely solely on software reset and, as it turns out, it can be pretty catastrophic because locking the hardware reset can brick the MCU by getting it into a buggy state where software reset does not respond.

### 2.1 Improving over ishtob's circuit

In order to add a reset-and-DFU capability to the circuit, I had to turn my eyes to the BOOT0 branch. The nRST branch was pretty much figured out, so what I had to do was invent a way to modulate wether BOOT0 will be low or high at the time instant the user releases the push button, which is when nRST gets back to one and the BOOT0 pin is sampled and the boot option decided.

What I did was simple, yet complex. The addittion of a resistor between the diode and the BOOT0 branch will enable the RC circuit of BOOT0 to act as a timed charge RC circuit which voltage rises across time as the push button is maintained pressed.

<figure>
  <img src="../../images/reset_article/reset2.svg" width="600" align="middle"/>
  <figcaption><b> Figure 6. </b> Improvement over ishtob's original reset circuit.</figcaption>
</figure>

Hence, the idea here is that the MCU boot option will be determined by how much time the user keeps the push button pressed. If for a short amount of time, the BOOT0 RC circuit will not have time to charge up enough to be considered high and the MCU will simply reset. If the button is held long enough, then BOOT0 will charge enough voltage to be considered high and the MCU will enter DFU.

The form and charge/decay rates of the BOOT0 pin are given by the R1, R2 and C1 components. The bigger the R2 over R1 proportion, the faster the circuit charges and the bigger will be the steady-state voltage. The higher the capacitance, the slower the voltage charges. The challenge then becomes to finely tune the values so that the times needed are convenient. For instance, if the charge is too fast, the user will not be able to press and release the circuit fast enough to reset it, and the MCU will always bootload. If the charge is too slow, then the user will need to keep the button pressed for too long a time.

To determine the exact times, first we need to know the logig level thresholds of the BOOT0 pin. In the MCU datasheet [3]_ one can see the following table:

<figure>
  <img src="../../images/reset_article/thresholds_table.svg" width="600" align="middle"/>
  <figcaption><b> Figure 7. </b> Datasheet table of minimum and maximum voltage logic level thresholds.</figcaption>
</figure>

The table shows that using a feeding voltage of 3.3b,  BOOT0 is considered low for voltages lower than 0.3 x 3.3 - 0.3 = 0.69V and high for voltages higher than 0.2 x 3.3 + 0.95 = 1.61V. The circuit of fogire 6 was simulated usin LTSpice XVII; the simulation results are detailed below.

<figure>
  <img src="../../images/reset_article/nominal_reset_plot.svg" width="800" align="middle"/>
  <figcaption><b> Figure 8. </b> Time simulation of the circuit in figure 6.</figcaption>
</figure>

The simulation shows that as the button is kept pressed, the voltage of BOOT0 crosses the low logic level maximum threshold at approximately 1 second and the high logic level minimum threshold at approximately 3.5 seconds. In other words, if the button is kept pressed for shorter than a second, the MCU will reset and, if kept pressed more then 3.5 seconds, the MCU will enter DFU mode. There is no telling what happens in between the 1s and 3.5s, as the logic level interpretation is not certain in that voltage zone.

### 2.2 Considering components tolerances

There is, however, an inherent flaw wih the design of the  the components used have tolerances which have to be accounted for; since these tolerances are considerable, the press timings will change with the real component values.

Let us define that the resistors have a 5% tolerance and capacitors have a 20% tolerance. First of all, since the nRST branch of the circuit is just pulling nRST to the ground and very fast, there is not much analysis to do with component tolerances here. The real problem lies with the RC charginf circuit of BOOT0.

Consider then the three comparison cases:

- (1) Nominal case. All components are at their nominal values;
- (2) "Slow" case. C1 and R1 are at their highest possible value of 120µF and 34.65kΩ and R2 is at its lowest of 95kΩ; hence this variation is the one that takes the longest to charge;
- (3) "Fast" case. Pretty much the opposite of the slow case: C1 and R1 are at the lowest values 80µF and 31.35kΩ and R1 is at its highest 105kΩ, which is the fastest charging possible variation.

<figure>
  <img src="../../images/reset_article/variance_reset_plot.svg" width="800" align="middle"/>
  <figcaption><b> Figure 9. </b> Time simulation of the circuit in figure 6 considering component tolerance-added "slow" and "fast" cases.</figcaption>
</figure>

Figure 9 shows the simulation of the three cases. The simulations show that the fastest time the circuit will cross the low logic levle maximum threshold is at approximately 0.75s, while the longest time the circuit will take to cross the high logic level minimum voltage is approximately 4.5 seconds. This means that by using the circuit of figure 7`, if the user presses the button for no more than 0.75 seconds the MCU is guaranteed to reset, and if he or she presses the button for longer than 4.5 seconds the MCU is guaranteed to DFU.

These times are, however, not to my liking. As can be seen in figure 11, the spread of timings between the curves is way too high. In order to solve that, I changed the tolerances of the resistors to 1% and the tolerance of the capacitor to 5%. 

<figure>
  <img src="../../images/reset_article/reset2_tighter.svg" width="600" align="middle"/>
  <figcaption><b> Figure 10. </b> Improved reset circuit with tighter tolerances.</figcaption>
</figure>

Figure 10 shows the simulation of the same circuit with the tighter tolerances, which is much, much better: now the needed times for guaranteed low and high levels are 0.94 seconds (which can be considered 1s for a human reaction time) and 3.8 seconds.

<figure>
  <img src="../../images/reset_article/variance_reset_plot_tight.svg" width="800" align="middle"/>
  <figcaption><b> Figure 11. </b> Time simulation of the circuit in figure 10 which has tighter component tolerances.</figcaption>
</figure>

The choice of tighter or normal components is really a designer choice, but I highly recommend the use of this tighter circuit since the price raise is really not much (maybe a dollar?) and the circuit becomes much, much more reliable.


## 3 Handling the discharge issue

### 3.1 Describing the discharge issue

The circuit of figure 7, both in its nominal "looser" and in the "tighter" version, still has an issue: the discharge of the BOOT0 circuit. The charging of the circuit sure does serve our purpose, but what happens *after* the MCU has reset or entered DFU mode? Of course, the BOOT0 circuit discharges -- the energy charged in the C1 capacitor makes its way to ground with R2. However, the discharge rate of this circuit is way too slow.

Figure 12 shows the simulation of the reset circuit during and after the push button is pressed. This simulation shows that, after the button is released, the BOOT0 takes 10 seconds to fall back to the low logic level threshold. Picture the following situation: the user holds the button and gets the MCU into DFU mode, only to realize that that was not the intention, they wanted really only to reset the circuit. Well, now they give the button a fast press and, surprise: the MCU still goes to DFU when the user didnt hold the button. Since the BOOT0 pin was charged, they must now wait 20 seconds to press again.

A vendor might see the disaster this situation can become: the user now thinks they have a faulty PCB and proceed to rage on the vendor website about how the PCB does not work as intended and they want a refund. 

<!-- .. _discharge_simulation : -->
<figure>
  <img src="../../images/reset_article/nominal_falltime.svg" width="800" align="middle"/>
  <figcaption><b> Figure 12. </b> Simulation of the reset circuit of figure 7 during and after the pushbutton is pressed.</figcaption>
</figure>

### 3.2 Using the MUN533

In order to fast discharge the BOOT0 pin, an additional PNP transistor is used, generating the circuit in Figure 13. The use of the MUN5335DW1T1G integrated circuit makes it possible to integrate both the pre-biased NPN transistor for the nRST pin as well as the PNP transistor for the BOOT0 discharge in the same SOT-23-6 package, keeping component count the same as the old circuit without the discharge.

The idea here is that when the push button is relased, the PNP transistor will conduct and drive BOOT0 immediately to zero, therefore dis-charging the BOOT0 pin and making it possible to re-activate the circuit.

<!-- .. _reset3 : -->
<figure>
  <img src="../../images/reset_article/reset3.svg" width="600" align="middle"/>
  <figcaption><b> Figure 13. </b> Yet another improvement over the reset circuit, this time with a discharge transistor to ensure voltage fallback discharge.</figcaption>
</figure>

Figure 13 shows the BOOT0 and NRST voltages as the push button is pressed and released. The keen reader will however be able to find the issue with this circuit: the added PNP transistor does what it was supposed to; the BOOT0 pin with the MUN component indeed discharges way faster than without it. However, the addition of this PNP transistor also comes with the addition of two transistors that bias it, both internal to the MUN device.

These transistors have two detrimental effects.

- First, the 47k resistor and the 2.3k act in parallel with the 33k resistor, making a much lower parallel resistance and interfering with the charge pattern of the BOOT0 pin in such a way that it charges way faster than the nominal case, making it impossible for the user to release the button before BOOT0 is charged, effectively removing the circuit's capability to reset the MCU;
- Second, the internal PNP resistors also make a path that bypasses the D1 diode which was supposed to keep the BOOT0 from maintaining the base of the NPN transistor charged. With this new path, the voltage and the NPN base is maintained, causing the NRST voltage to not rise immediately, but takes near a second more to rise again.

<!-- .. _mun_simulation : -->
<figure>
  <img src="../../images/reset_article/mun_simulation.svg" width="800" align="middle"/>
  <figcaption><b> Figure 14. </b> Time simulation of the circuit in figure 13 during a 5 second press of the push button and release, comparing NRST and BOOT0 signals for this case and the nominal circuit of figure 7 </figcaption>
</figure>

### 3.3 Using the UMF5N

The apparent solution to this problem would be to adopt a PNP transistor that does not integrate the biasing resistors. [ROHM Semiconductors' UMF5N](https://www.rohm.com/products/transistors/complex-transistors/umf5n-product) is a device which houses a pre-biased NPN and a non-biased PNP, that is, a NPN that has the internal transistors but a PNP that does not.

<!-- .. _reset5 : -->
<figure>
  <img src="../../images/reset_article/reset5.svg" width="600" align="middle"/>
  <figcaption><b> Figure 15. </b> PNP-discharged circuit of figure 13 using the UMF5N, which contains a non-biased PNP transistor. </figcaption>
</figure>

Figure 15 shows the time simulation of the circuit. Since the UMF5N does not have the biasing resistors, hence does not make a current path that bypasses the diode D1, the charging profile of BOOT0 is kept the same as the nominal case. The PNP transistor does the job of discharging the circuit much faster than the nominal case, and the NRST voltage rises as fast as the nominal case.

<!-- .. _umf5n_simulation : -->
<figure>
  <img src="../../images/reset_article/umf5n_simulation.svg" width="800" align="middle"/>
  <figcaption><b> Figure 16. </b> Time simulation of the circuit in figure 15 using the UMF5N device comparing the BOOT0 voltage against the nominal case of figure 7. </figcaption>
</figure>

### 3.4 Using a JFET

I still was not *quite happy* with how the UMF5N device solves the issue. As can be seen from the simulation in figure 16, the BOOT0 voltage does fall profusely in the first seconds after the push button is released, but adter some time it still looks like it holds some voltage (approximately 0.3V). That is due to the bipolar transistor's circuit characteristics. In simple terms, a bipolar transistor is fundamentally two diodes constructed back-to-back; this means the bipoalr transistor has an exponential characteristic such that the lower the base voltage, the collector current is diminished exponentially. After a while, when the BOOT0 circuit is already discharged, the PNP transistor cannot conduct current fast enough to make the BOOT0 discharge completely to zero volts.

The solution I found was to use a JFET transistor, which are known to be unparalleled analog switches. The circuit with the JFET as an analog discharge switch is shown in figure 17.

<!-- .. _reset7 : -->
<figure>
  <img src="../../images/reset_article/reset7.svg" width="600" align="middle"/>
  <figcaption><b> Figure 17. </b> Schematic of the discharged-reset circuit using a J270 JFET instead of a bipolar transistor for the BOOT0 discharge. </figcaption>
</figure>

<!-- .. _jfet_simulation : -->
<figure>
  <img src="../../images/reset_article/jfet_discharge_simulation.svg" width="800" align="middle"/>
  <figcaption><b> Figure 18. </b> Schematic of the discharged-reset circuit using a J270 JFET instead of a bipolar transistor for the BOOT0 discharge. </figcaption>
</figure>

As the simulation shows, the JFET does the job perfectly: it *instantly* grounds BOOT0, discharging it immediately. The problem now is... it does the job way too well. FIgure 19 shows the zoomed-in version of the plot in figure 18. The plot shows that the JFET discharges BOOT0 so fast that the pin reaches its low threshole even before nRST reaches its high, meaning that the when the MCU samples BOOT0 -- after nRST has reached high logic -- BOOT0 will already be at low state. This means that the circuit will never go into DFU mode, only reset to flash!

<!-- .. _jfet_simulation_zoom : -->
<figure>
  <img src="../../images/reset_article/jfet_discharge_simulation_zoom.svg" width="800" align="middle"/>
  <figcaption><b> Figure 19. </b> Zoomed-in exceprt of the plot in figure 18 showing the rise and falltimes of BOOT0 and nRST and their thresholds during the simulation of the JFET-discharged circuit of figure 17. </figcaption>
</figure>

### 3.5 JFET reset with delayed discharge

To delay the JFET discharge time, all that is needed is to add a resistor to the JFET, as shown in figure 20. The time simulation of this circuit to a press, hold and release of the push button is shown in figure 21.

<!-- .. _reset4 : -->
<figure>
  <img src="../../images/reset_article/reset4.svg" width="800" align="middle"/>
  <figcaption><b> Figure 20. </b> Schematic of the reset circuit using a delayed-discharge JFET mechanism. </figcaption>
</figure>

<!-- .. _delayed_discharge_simulation : -->
<figure>
  <img src="../../images/reset_article/jfet_delayed_discharge_simulation.svg" width="800" align="middle"/>
  <figcaption><b> Figure 21. </b> Time simulation of the delayed-discharge JFET mechanism circuit of figure 20. </figcaption>
</figure>

This circuit is simple but ingenious. What is happening here is quite sophisticated yet so simple. The JFET acts as a switch that commutes the BOOT0 RC circuit charge and discharge, as seen in figure 22.

<!-- .. _reset4_simple : -->
<figure>
  <img src="../../images/reset_article/reset4_simple.svg" width="800" align="middle"/>
  <figcaption><b> Figure 22. </b> Simplification of the schematic of the reset circuit using a delayed-discharge JFET mechanism showing the JFET as a discharge resistor switch. </figcaption>
</figure>

When the push button is pressed and the BOOT0 circuit is charging, the JFET does not conduct current and the 1MΩ resistor is used to charge the circuit slowly, abiding by the designed cross times we seen before; as a matter of fact, the JFET conducts so little current that the 10kΩ resistor is almost non-existant. When the push button is released, the JFET starts conducting current and the 10kΩ resistor is shorted to ground, making a parallel resistance with the 1MΩ. Since the former is so much smaller than the latter, the resulting parallel resistance is very close to 10kΩ.

So at the end the JFET acts as a switch that commutes the resistors; when the push button is pressed, the circuit charges with the bigger 1MΩ and hence charges slowly. When the button is released the circuit "changes" the RC resistance to 10kΩ, which makes it discharge swiftly.

The 10kΩ value was not chosen randomly. It was chosen to be much smaller than 1MΩ, bringing the charge/discharge commutation effect yes, but it was also chosen such that the discharge of the JFET was delayed in such a way that the nRST pin would have time to reach high logic before BOOT0 completely discharged. Figure 23 shows the time plot of the time simulation of the delayed-discharge JFET circuit with a 10kΩ resistor.

<!-- .. _reset4_simulation_zoom : -->
<figure>
  <img src="../../images/reset_article/jfet_delayed_discharge_simulation_zoom.svg" width="800" align="middle"/>
  <figcaption><b> Figure 23. </b> Simplification of the schematic of the reset circuit using a delayed-discharge JFET mechanism showing the JFET as a discharge resistor switch. </figcaption>
</figure>

As the plot shows, the delayed discharge allows the circuit an approximate 25 milisecond time between nRST reaching high logic and BOOT0 discharging to the high logic threshold, which is far more than enough. Remember that, according to the datasheet, the BOOT0 pin is sampled on the fourth rise of the clock signal of the MCU once nRST is high; since the MCU works at 72 megahertz, a 25 milisecond time is very reasonable.

Finally, as far as the R4 value goes, almost any value between 2kΩ and 10kΩ will give a plausible result. The next plot shows a simulation of the falltime of BOOT0 on the circuit given several values of R4, ranging from 0 to 10kΩ in 1kΩ steps. Naturally, the bigger the R4 value, the slower the discharge is and the more available time the MCU has to sample BOOT0 at high time.

<!-- .. _reset4_simulation_stepped : -->
<figure>
  <img src="../../images/reset_article/jfet_delayed_discharge_simulation_stepped.svg" width="800" align="middle"/>
  <figcaption><b> Figure 24. </b> Parametric plots of the time simulation of the JFET-delayed-discharge circuit of figure 21 with multiple discharge resistor values. </figcaption>
</figure>

Figure 25 shows a parametric plot of the available time that the MCU has to sample BOOT0 as high level, that is, the time difference between the instant nRST voltage rises to its high logic level threshold and the time instant BOOT0 voltage falls back to its high logic threshold, as a function of the R4 resistance. As we seen before, at 0kΩ, the available time is negative, that is, BOOT0 falls below high logic level before nRST hits its high logic level. This is counterbalanced at approximately 1kΩ (1.021kΩ to be more precise) where the available time is zero, that is, BOOT0 and nRST hit their high level thresholds at the same time. At 2kΩ the available time is 2.8559 miliseconds -- enough on its own. The reason I chose 10kΩ is because it gives a very nice headroom to work with component tolerances and is a good value to find with tighter tolerances.

<!-- .. _nrst_available_time : -->
<figure>
  <img src="../../images/reset_article/nrst_available_time.svg" width="800" align="middle"/>
  <figcaption><b> Figure 25. </b> Parametric plot showing the available time the MCU has to sample a high logic level BOOT0 once nRST is sampled high as a function of the discharge resistor. </figcaption>
</figure>


## 5 MOSFET version

There are two small problem with the reset circuits hereby discussed. First is that some people might see the use of a JFET a little bit complicated, because it is a weird part (even though its use as a voltage-controlled switch is solid). Second, and this is the most important, both the pre-biased NPN transistor and the JFET used are extended parts in the [JLCPCB assembly service](https://jlcpcb.com/smt-assembly). Let's make a brief explanation why that might be a problem.

The JLCPCB service is known as a quick and cheap prototyping tool. Their assembly service works like this: where most PCB assemblers will source parts from distributors when you supply them a Bill of Materials, JLCPCB has a [parts library](https://jlcpcb.com/parts) wherefrom the needed parts will be sourced. In this library, there are two types of parts: "basic" and "extended" ones.

- Basic parts are components that are very often used by designers so JLCPCB has a line of pick-and-place machines with these parts pre-loaded and ready to be used. Using these parts is fairly simple and inexpensive and no fee is charged besides the part cost and the soldering fee;
- Extended parts are ones that albeit figuring in the parts roster are not pre-loaded into machines, meaning that a JLC employee must load them into the machines; hence for extended parts JLC charges a 3 USD fee on top of the parts cost and soldering fee (this is per unique extended parts, so if you have say two extended components on the same PCB that are the same part number, the 3 USD fee will be charged only once).

As one might imagine, both the JFET and the pre-biased bipolar transistor used in the reset circuits are extended parts, and there are no basic parts that directly substitute them. Or, until now at least.

### 5.1 Substituting the BJT

Substituting a bipolar transistor as a switch is easy; one can use a 2N7002 MOSFET with a couple resistors. The 10k ohm resistor can be ommitted but it is recommended that it is left as the extra cost is negligible. The advantage here being, of course, the 2N7002 is a basic part and costs cents a piece.

<figure>
  <img src="../../images/reset_article/mos_biaspnp.svg" width="800" align="middle"/>
  <figcaption><b> Figure 26. </b>  MOSFET equivalent to the pre-biased bipolar transistor used.</figcaption>
</figure>

Using this MOSFET, the resulting "improved reset" circuit would be as depicted in figure 27.

<figure>
  <img src="../../images/reset_article/mos_reset.svg" width="800" align="middle"/>
  <figcaption><b> Figure 27. </b> "Improved reset" circuit using a MOSFET equivalent to the pre-biased bipolar transistor.</figcaption>
</figure>

### 5.2 Substituting the JFET

Now to the big issue: substituting the JFET. As mentioned before, the big advantage of using a P-channel JFET is that it acts almost like a perfect switch while working with an active-low logic, that is, conducts when its gate input is zero, which is a little hard to replicate. Not even a PNP or a P-channel MOS will work the same way, as both need some connection from bridge to emitter (in the case of the BJT) or gate and source (in the case of the MOS), which will inevitably disbalance the circuit much like the MUN533 and the UMF5N did. The only way to replicate that behavior is to use a *driver circuit*, that is, an ancillary circuit intended to drive the PMOS or the PNP transistor; in its simplest forms, this driver circuit generally manifests as an inverting amplifier (common source or common emitter) with some protection circuitry.

As one might imagine this is not ideal. We already have a good bunch of components in the circuit and adding many more would not be ideal. However, we are in luck: one can identify that the MOSFET used to drive the nRST is already an inverting amplifier; in order to give the BOOT0 and the nRST circuits some isolation we use a high value resistor, which in turn culminates in a "double-MOSFET improved delayed discharge" reset circuit (that's a mouthful) depicted in figure 28. As always, blue components are not essential but recommended. 

<figure>
  <img src="../../images/reset_article/double_mos_reset.svg" width="800" align="middle"/>
  <figcaption><b> Figure 28. </b> "Double-MOSFET improved delayed discharge" reset circuit.</figcaption>
</figure>

The question now is: *how well* does the MOSFET approximate the analog switch of the JFET? Figure 29 shows a time simulation of both circuits using variable discharge resistor values (R4 in both figures 28 and 20). The values are range from $1\text{k}\Omega$ to $100\text{k}\Omega$ in 21 logarithmically spaced steps.

<figure>
  <img src="../../images/reset_article/double_mos_reset_comparison.svg" width="800" align="middle"/>
  <figcaption><b> Figure 29. </b> Time simulation comparison between the "double-MOSFET-delayed" and the "JFET-delayed" reset circuits.</figcaption>
</figure>

As the figure shows, the simulation performances of both circuits are so close that they are almost indistinguishable; this leads us to keep the same value of discharge resistor, $10\text{k}\Omega$.

## 6 Conclusion

The article presents the development and simulation of various possible reset circuits, of which four are viable, meaning they can reliably drive the MCU both to reset and to DFU mode. The tabs below show these reset circuits in comparison to one another.

!!! note ""
    === "Vanilla reset"
        <!-- .. _reset4_simulation_zoom : -->
        <figure>
            <img src="../../images/reset_article/vanilla_reset_final.svg" width="800" align="middle"/>
        </figure>	
    === "Improved reset (MOS)"
        <figure>
    	    <img src="../../images/reset_article/improved_reset_final.svg" width="800" align="middle"/>
        </figure>
    === "Improved reset (BJT)"
        <figure>
    	    <img src="../../images/reset_article/improved_reset_BJT_final.svg" width="800" align="middle"/>
        </figure>
    === "Delayed-discharge reset"
        <figure>
    	    <img src="../../images/reset_article/delayed_discharge_reset_final.svg" width="800" align="middle"/>
        </figure>

### 6.1 Which circuit should I use?

First of all, the price and availability of the 27000 is a great reason to just adopt those variants. They are cheaper, easier to implement, and the 2N7002 MOSFET is available by the hundreds of thousands in many manufacturers around; the only downside is real-estate because where the DTC123JKAT146 had integrated resistors, the 2N7002 needs external ones to work. Since these resistors do not carry power current, you can safely use small packages like 0402 resistors.

That being said, four possibilities arise: the "vanilla" reset, the "improved reset" (both MOSFET version of figure 27 and the BJT version of figure 10)  and the "double-MOSFET" of figure 28. Confronted with these many possibilities one might ask which is the best or which should they use. Although I do not know if there is a "better" or "worse" circuit, there are adtanvages and disadvatages with every single one of them:

- The "vanilla reset" circuit is by far the simplest one. It is the most reliable and simple to implement and requires few simple components. However, the fact that it requires a rather complicated routine to flash and reset makes it non-ideal for user usability; reestated, the fact that it is not single-action and requires several steps to work may be a problem in troubleshoot and operation for the common non-experienced users;
- The "improved reset" circuit is the initial implementation of the BOOT0 charging mechanism where a short button press is a reset and a long button press drives the MCU to DFU mode.  It is fairly complicated and requires precision 1% resistors and a 5% tolerance capacitor on the BOOT0 circuit to be reliable, but delivers the single-action proposal of this article with cheap and simple enough components. The problem here being that each activation of this circuit should be approximately 30 seconds apart, due to the fact that the BOOT0 circuit takes time to discharge. There are two variants of this circuit:
	- The MOSFET version (figure 27) is a preferred choice due to the price and availability of the MOSFET versus the pricey and more limited pre-biased BJT; this is specially true if one is using the JLCPCB prototyping service, where the 2N7000 is a basic part while all pre-biased BJTs are extended parts (hence more expensive to use)
	- The BJT version might be just a tad pricey and less available, but has a huge advantage when it comes to variety. There are tons of different pre-biased BJT transistors in varying packages; not only it integrates the biasing resistors (which you have to add discretely to the MOSFET circuit), the 27000 component is only available in a SOT-23 package whereas one can find pre-biased BJTs in the tinies of packages;
	- Both versions are perfectly interchangeable performance-wise, so use them at your discretion; myself (Gondolindrim) I highly favour the BJT version as I solder my prototypes at home, meaning I don't need to solder extra resistors. 
- The "double MOSFET" circuit of figure 28 is the most user-friendly, because it implements the discharge needed for reliable re-operation of the BOOT0 charge-and-discharge mechanism -- the fact that the delayed discharge is performed means that the circuit is immediately discharged after button release, meaning the user can press the button rapidly and the circuit will work every time without problems, delivering the promise of a "truly single" action. This circuit substitutes the JFET circuit of figure 20; honestly, don't use these. JFETs are very particular components used in a small number of designs where they are absolutely needed; they are difficult to source and fairly expensive. Just don't.
	- A big warning here is that, albeit the "improved reset" circuit having two interchangeable variants (BJT and MOSFET), this is not the case here. The fact of the matter is that the MOSFET is a much better electronic switch than the BJT is because the BJT is slow and needs a base current to work; this means that if a BJT is used, be it in the BOOT0 or the nRST portions of the circuit, the timins get messed up and it does not work as well.

The usage of each circuit is of course at the discretion of the designer; my personal experience and opinion is that the vanilla circuit is fine for prototyping reasons or if the PCB you are designing is a personal project and not intended for mass production and selling. If the objective is user friendliness and mass selling, I definitely recommend using the JFET delayed discharge circuit. For 20 cents more you get a reliable single-action circuit that works as intended every time, as opposed to the "improved reset" that, albeit being single-action, can be misused if the user is not patient enough to wait 30 seconds for each action or is simply ignorant of its functioning. It is my opinion that a product should not be designed while supposing that the user knows its inner workings, hence why I recommend the delayed-discharge circuit.

### 6.2 Tighter tolerance components

Another possible question that arises is: are the tighter tolerance components on the BOOT0 charge circuit *really* needed? The true answer is no. The time plot of figure 9  shows that it's perfectly possible to reset and DFU the MCU without the special tighter tolerance components. The *real* only thing that changes from a circuit that uses common-tolerance components and a circuit that uses tighter tolerance components is simply the guaranteed times needed. For instance, with normal tolerances, the MCU is guaranteed to reset if the button is released under 0.7 seconds after being pressed and guaranteed to DFU is the button is held for at least 4.6 seconds.

The usage of tighter component tolerances gives you two advantages.

First, that the times tom reset and DFU are a little bit more reasonable -- to reset release under a second of press and to DFU hold for at least 3.8 seconds. The curse of the exponential growth characteristic of the charging circuit means that if you try to make the reset timing larger -- to a second, for instance -- the DFU timing will also be *much* longer; if you try to make the DFU timing shorter, the reset timing will be *much* shorter. This means that, with common tolerances, it is very difficult to adjust the reset and DFU timings because trying to adjust one will *exponentially* (literally) affect the other. With tighter tolerances, however, the change is still exponential; but since the parameter uncertainty is that much smaller, the effect is not that great.

To illustrate this advantage, imagine a common serial RC circuit with a constant voltage source $V_S$. Then the charge timing of the capacitor voltage is given by

$$ v_C(t) = V_S\ e^{-\left(\dfrac{t}{RC}\right)} $$

Hence, the time $T$ the capacitor takes to reach a voltage $V$ is given by

$$ T = - RC\ln\left(1 - \dfrac{V}{V_S}\right) $$

Imagine now that $R$ and $C$ vary with uncertainties $\Delta R$ and $\Delta C$ that is,

$$ R = R_0 \pm \Delta R,\ C = C_0 \pm \Delta C $$

Call $T_0$ the nominal time to reach voltage $V$, that is, the capacitor would reach that voltage if the components were perfect:

$$ T_0 = - R_0 C_0\ln\left(1 - \dfrac{V}{V_S}\right) $$

Then through the propagation of uncertainty formulas, the uncertainty of $T$, that is, $\Delta T$, is given by

$$ \dfrac{\Delta T}{T_0} = \sqrt{\left(\dfrac{\Delta R}{R}\right)^2 + \left(\dfrac{\Delta C}{C}\right)^2} $$

The keen reader might indetify this as a elliptic parabolloid in the $\Delta T$, $\Delta R$ and $\Delta C$ variables. This means that the time uncertainty $\Delta T$ grow *parabolically* with the resistor and capacitor uncertainties, which goes to show that the time uncertainty is very, very sensible to these quantities.

The interested reader might also calculate the partial derivatives of the sensibilities of $\Delta T$ with respect to $\Delta R$ and $\Delta C$, which will prove the parabolic growth of the sensibility.

If the reader is still incredulous, let us calculate the time sensibility in the terms of this last formula. If we are using common tolerances, that is, 

$$ \dfrac{\Delta R}{R} = 0.05,\ \dfrac{\Delta C}{C} = 0.2 $$

Then the normalized time uncertainty equals 20.62%. If the tighter tolerances are used, that is, 

$$ \dfrac{\Delta R}{R} = 0.01,\ \dfrac{\Delta C}{C} = 0.05 $$

Then the time uncertainty equals 5.10%.

These calculations motivate the second advantage that this circuit gives you; this advantage is deeper and less visible, but much more important: reliability. Suppose that you are using the circuit with common tolerances in a 1000-unit production run. Since every PCB has different capacitanca and resistance values, each PCB has a different time charging curve; what I can guarantee is that this curve is at all times located between the "fast case" yellow curve and the "slow case" pink curve of figure figure 9, and that the charging times between PCBs will vary in a 20.62% margin. This means that the actual timings to reser and DFU can vary wildly between PCBs. On the other hand, if you use tighter tolerances, the charging curve will be confined between the fast and slow curves of figure figure 10, which are much closer together; hence the actual timings of each PCB will vary mildly (inside a 5.1% margin, which is much more tolerable), as opposed to the large variations you would get if you used the more common tolerances. The fact that the circuit is more predictable and less variable -- hence, more **reliable** -- means that the behavior of the circuit will be more uniform across all production units, that is, while the normal tolerance components will give each unit a very different timing, the tighter tolerance will make sure all PCB units will be under a very strict margin. This, in turn, makes sure that your product is much closer to specifications.

My opinion and experience on this matter are this: use component footprints so that the common tolerance and the tighter tolerance components share the same footprints; for instance, use a 1206 resistor and a 0805 capacitor footprint, as there are both 5% and 1% 1206 resistors just like 20% and 5% 0805 capacitors. That way you can keep prototype costs down by using the more common tolerances and, on the final more polished product, you use the tighter tolerances components because, at a large scale, the price per PCB will be increased marginally while the circuit will be much more reliable and user-friendly.

## References

**[1]** *STM32F0x1/STM32F0x2/STM32F0x8 advanced ARM-based 32-bit MCUs series reference manual*. Available at [this link](https://www.st.com/resource/en/reference_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf). Last accessed june 22, 2020.

**[2]** *Getting started with STM32F0x1/x2/x8 hardware development*. Available at [this link](https://www.st.com/resource/en/application_note/dm00051986-getting-started-with-stm32f0x1x2x8-hardware-development-stmicroelectronics.pdf). Last accessed june 22, 2020.

**[3]** *STM32F072xB / STM32F072x8 MCUs datasheet*. Available at [this link](https://www.st.com/resource/en/datasheet/stm32f072rb.pdf). Last accessed june 22, 2020.
