# A multi-MCU approach to mechanical keyboard hardware design: the Joker template
*Because desperate times need creative measures*

**By Gondolindrim with contributos Tzarc and sigprof**

**First version** published in sptember, 1 2021

**Last revision** in october 22, 2021

---

## 1 Introduction

The worldwide pandemic has brought an unprecedented halt in many private sector fields, specially logistics and tourism, fields that were completely shut down in efforts to break the spread of the SARS-CoV-2 virus. One of such affected sectors was the semiconductor manufacturing, in a global phenomenon we agreed to call the "chip shortage", the "semiconductor shortage", or simply "electronics shortage" [1]. This shortage has been caused by a consurgence of factors, which include the US-China trade war in the Trump administration, the COVID-19 pandemic, the halting of factories in Europe, US and China ([2],[6]).

It is not the intent of this article to explain why this shortage is or what are its causes. See the references for deeper understanding.

This shortage has hit everyone by their guts at this point because in the digital humanity of the twenty-first century every single home appliance, handheld device, consumer electronics, and kids toy uses if not several at least one microcontroller (which we will, for better reading, abbreviate as MCUs for "Microcontroller Units"). The problem being that, due to the shortage, the supply of MCUs has been diminished to a point where even huge car manufacturers like Toyota, Honda and Ford announced that they are halting their manufacturing efforts simply because there are no MCUs available to manufacture their cars [3] .

As of the writing of this article (semtember of 2021), the semiconductor industry is still getting back on its feet, trying to match supply to demand. The void in supply is still huge, which brings us to the keyboard community. For us, this supply issue has hit hard. The thing is: not only demand is completely disproportionally small compared to demand, there are important industries in dire need of semiconductor devices, some of them deemed more urgent get priority, specially the car manufacturers and, for obvious reasons, the medical supplied and devices. In this zeitgeist, distributors like LCSC, Digikey and Mouser, who serve the general buyers like us mere keyboard mortals rarely get some stock of any MCUs at all. If there is stock, the microcontrollers are sold at ridiculous prices [4]. 

Just as an example: the microcontroller I use the most for keyboards is STM32F072C, be it the B (128kB flash) or 8 (64kB flash) versions. While in a normal setting I could get several thousand units for around two US dollars a piece, nowadays I can only get tens of them for twenty six US dollars each; and that's considering I can not *always* have them. This trend is not unique to this unit, as all others follow the same pattern. It's not surprising, then, to see that designing and manufacturing keyboard PCBs in this setting is a challenge. At a given time, one MCU is available, say F072, and in the next week it will become out of stock and another one, say, F411, will be available.

This article is an attempt to document a long and wide talk between:

- Me (Gondolindrim);
- **tzarc**, embedded systems engineer and known in the keyboard community through his work as a QMK developer
- **sigprof**, a member of the QMK community with significant contributions in hardware design, specially for the F4x1 family

The goal of this documentation is: **achieving a template design that allows for multiple STM microcontroller units to be used in the same design, only needing tweaking in the bill of materials.** This should make the manufacture of the PCBs *easier* by generalizing the design process and making the designed PCBs recyclabe, especially in the context of the pandemic (because of course no one can't make it easier than it was before, with availability and prices) while giving the PCB designer some insight insight in such approach.

### 1.1 Objective and constraints

The end objective of this article is to develop a template design consisting of a microcontroller footprint and several ancillary components (EEPROM, clock crystal and its load capacitors, USB resistors, bypass capacitors); this template design is intended as a "wildcard" or "joker" (whence the name) design that can support multiple STM32 microcontrollers, with the following parameters:

- **Firmware compatibility**: target MCUs must be QMK-supported;
- **Availability**: target MCUs must also be available for purchase for the general public (there are versions restricted to military or industrial use);
- **Design licensing**: the Joker template should be KiCAD-compatible and open-source;
- **Manufacturability**: the design must be manufacturable through a wide myriad (if not all) of the PCB manufacturers out there. There are some MCU versions that use BGA, UBGA and WLCSP packages which are only manufacturable in specialized fab houses. In this article we will focus on 48 and 64-pin variants, specifically UFQFPN-48 and LQFP-48 packages for the 48-pin variants and LQFP-64 packages for 64-pin variants.

### 1.2 The STM approach and how we make use of it

The STM family of microprocessors is industry-wide known for their cross-compatibility, that is, the ability to *replace one microcontroller type by another one in the same product series* [5] . It is nice to know that the STM microcontrollers are designed for *some level* of cross-compatibility from the get-go, but one must wonder what are the needed changes to port a design from one microcontroller or another; STM has many ([8], [9], [10]) references on such operations. However, to the best of my knowledge there is not an application note on a *multi-microcontroller* approach, that is, how to design an appliance to support multiple microcontroller families.

References [8] through [10] show official STM documents that specifically target the migrating capabilities of the STM32 family, allowing us to get a better grip on how it works.

## 2. How the template works

The core mechanic of the joker template is the fact that in the STM32F family MCUs some specific peripherals and the power inputs are kept at the same pins throughout multiple chip models, hence allowing us to fix those pins and maintain some keyboard features (RGB, LEDs and so on) attached to the same pin of the footprint. In other words, the way this works is that the pins we use for RGBs, LEDs, OLED control and so on can be the same across multiple chips; this in turn allows us to make a design that can receive a variety of different chips and configure their pins through QMK or a realtime operating system.

This is not to say, however, that all the STM32 microcontrollers are the same. For instance, STM32F07x is a microcontroller line aimed at connectivity in cost-sensitive applications; hence it integrates a solid-state oscillator with a USB 2.0 and CAN bus, meaning you have a high degree of possibilities in a small and cheap package with resistorless USB connectivity and crystal-less operation. However, its peripherals are very basic; the STM32F30x family, on the other hand, is a more sophisticated family with operational amplifiers, ultra-fast comparators, 12-bit ultra-fast ADCs but they need an USB pullup resistor and an oscillator crystal while being more expensive.

Hence, even though the F0x and F30x have the SPI and I2C peripherals at the same pins, those peripherals might not be the same (with a high chance of the F30x peripherals being better and faster). This gives rise to a second layer of the ingenuity of the joker template: ultimately, keyboards are not the pinnacle of human technology. No one needs a ultra-fast ADC to run a keyboard; a simple ADC will do the trick. Hence, both the "lighter" peripherals of the F07x and the "better" ones on F30x will work.

The second layer of abstraction the template uses is the way 

#### I2C

The I2C1 peripheral is generally at pins 42 and 43 (PB9 and PB10) in the 48-pin variants and ; this peripheral is used by QMK for:

- Some RGB controlling chips, mostly Lumissil chips like IS31FL3741A;
- OLED screens;
- External EEPROM memory which is used by VIA to store the user options non-volatilly.

#### PWM

The channel 1 of TIM3 is generally at pin 15 (PA6); this peripheral can be used by QMK to control the WS2812 RGB LEDs and for the backlight LEDs (also called "in-switch" LEDs); in the case of this template, we use it mainly for the backlight.

#### SPI

The SPI2 peripheral is generally located at pins 28, 27 and 26 (in that order, MOSI, MISO and SCK pins). This peripheral is used by the template to control integrated-controlled RGB LEDs (WS2812, SK6812 and derivatives), which can be used for RGB underglow and per-key RGB lighting.

#### Reset pins

- All MCUs supported by the template have a BOOT0 pin, located at pin 44, and an nRST pin located at pin 7;
- For those MCUs that have BOOT1, it is located at pin 20;

### 2.2 Understanding the generality of the circuit

It must be understood that the final circuit of figure 2 is supposed to work with multiple STM units, some of which either don't make use or do not need some of the peripherals needed. For instance, in QMK the STM32F072 units can make use of an EEPROM simulation algorithm that allocates some flash memory to act as EEPROM; STM32L072 and STM32L051 have integrated EEPROM. This means that these units do not need the external EEPROM, and this in turn means that if the PCB in question is being manufactured using one of those microcontrollers one can omit the EEPROM and its bypass capacitor (and if no other I2C devices are being used, the I2C pullup resistors as well) from the Bill of Materials, thus informing the factory that, albeit the footprints being there, these components are not to be soldered. This situation is most commonly referred to as leaving these footprints or sites *unpopulated*.

There are, however, some components that are implemented specifically for a certain family of STM32. For instance, resistor R5 for the USB fullspeed pullup, is integrated in most STM32 MCUs; according to [15], all MCUs in the STM32F303 family need that external resistor.

## 3 The final circuits and the KiCAD files

###  3.1 Final circuits

Figures 1a and 1b show a schematic of the Joker48 template while figures 2a and 2b show a schematic of the Joker64 template. The circuits are denoted in two versions, a colored version denoting some pin functionalities and a black and white version for better readability.

!!! note "Joker templates schematics"
    === "Joker 48 B/W"
        <figure>
            <img src="../../images/joker_article/joker48_bw.svg" width="1000" align="middle"/>
            <figcaption><b> Figure 1a. </b>  "Joker48" 48-pin STM32 MCU circuit topology (black and white version). </figcaption>
        </figure>
    === "Joker48 colored"
        <figure>
            <img src="../../images/joker_article/joker48_colored.svg" width="1000" align="middle"/>
	    <figcaption><b> Figure 1b. </b>  "Joker48" 48-pin STM32 MCU circuit topology (colored version). </figcaption>
        </figure>
    === "Joker64 B/W"
        <figure>
            <img src="../../images/joker_article/joker64_bw.svg" width="1000" align="middle"/>
            <figcaption><b> Figure 2a. </b>  "Joker64" 64-pin STM32 MCU circuit topology (black and white version). </figcaption>
        </figure>
    === "Joker64 colored"
        <figure>
            <img src="../../images/joker_article/joker64_colored.svg" width="1000" align="middle"/>
	    <figcaption><b> Figure 2b. </b>  "Joker64" 64-pin STM32 MCU circuit topology (colored version). </figcaption>
        </figure>

### 3.2 Notes on the final circuits

#### A brief discussion on external crystals versus internal RC oscillators

In microcontrollers, a quartz crystal is generally used to generate the clock signal -- basically the microcontroller's hearbeat, dictating the frequency at which commands are undertaken in the digital logic. In a very summarized explanation, the clock signal dictates at what speed the microcontroller runs. The problem being that certain operations in the microcontroller require ultra-precision timing; for instance, USB communication at 2.0 full speed requires a 480MHz signal with a very tight tolerance. If the signal sent by the microcontroller is not inside this narrow limit, then the host device (or whoever the MCU is talking to) will not recognize the communication and your system will simply not work. Clock timing is also very important for timed functions in the microcontroller; keeping the real-time clock precise, like in digital watches, is one of such functions. Hence, precise and consistent clock timing is paramount. Quartz crystals are known to be excellently precise in generating clock, with tolerances in the parts-per-milion (that's 0.0001%). Hence most microcontrollers will employ such a device to generate their clock signals.

However, there are some drawbacks to quartz crystals, two of which are the most cited. First, the crystal requires load capacitors to work, adding three more components to the bill of materials; second, and more important that the former, is that due to the very high frequency the crystal outputs, tracing that signal is perhaps the worst task in the microcontroller routing process: the crystal needs to be expertly close to the controller, as well as its capacitors, and the traces need to be short and unbroken.

Most (if not all) STM32F microcontrollers have an integrated RC (short for Resistor-Capacitor) oscillator, which is a solid-state device able to generate clock, generally based on a transistorized oscillator topology like an astable operationally-amplified multivibrator. These devices tend to be very, very imprecise (sometimes their generated frequency can swing as much as 10% of their rated frequency!) because they are semiconductor-based, so thermal and fabrication variances are immense (see [16,17] for further details on thermal and parameter spreading effects on conductance of transistors and [18] for details on the effect of parameter uncertainty in some transistors). One might ask why then is that such internal oscillators are not quartz-based, and the answer is very simple: despite it being easy to miniaturize and integrate transistors, resistors and capacitors, the same case cannot be made for miniaturizing crystals because, due to their piezoelectric nature, their size is a major factor in their oscillating frequency. For all of these reasons, the internal RC oscillators in these microcontrollers are generally used for very limited functions, especially the early booting procedures like starting the program stack pointer and enabling basic buses; from very early in the process, the external oscillator kicks in.

However, there are some microcontrollers that embed a somewhat decently precise RC oscillator; not exactly *crystal-precision-precise*, but under a 0.5% tolerance achieved through a laser-trimming process. Due to this precision, these microcontrollers have a "crystal-less USB" feature, or "xtalless USB", that is, the capability of operating USB fullspeed communications and timed oeprations without a crystal oscillator. In custom keyboards, an important example is STM32F072 which is widely used because of this feature; remember that F072 was designed for cost-sensitive applications, so it makes sense that it integrates a precise solid-state oscillator.

Hence, in some units like F072, the crystal unit is not needed albeit most (if not all) STM32F microcontrollers having an internal RC oscillator.

#### Peripheral usage and notes

#### Template pin colors

The colored versions of the circuits shows five pin types:

- **Blue pin type or "MCU function pins":** these are used by the microcontroller for specific functions like booting options, In-System-Programming SWD or voltage regulating capacitors (VCAP pins). Blue pins should not be changed or edited in any way whatsoever as they are crucial for the compatibility of the Joker templates:
    - **Crystal pins:**
    - **nRST, BOOT0 and BOOT1:** BOOT0 and BOOT1 are sampled during reset which happens when nRST is pulled low or a software reset is issued. BOOT0 is present in all STM32F MCUs and is used to select between DFU (if high state) and main memory boot (if low state). BOOT1, on the other hand, is also used for boot selection but is not available in all families. However, in the ones it is, if BOOT1 is pulled down, the BOOT0 pin works like it does in the MCUs that don't have BOOT1 (DFU is BOOT1 is sampled high, main memory if sampled low). For clarification on this, read the [part 2 of the reset circuit article](../reset_article_2/reset_article_2.md). Hence, the idea is to pull BOOT1 down through a 10k ohm pullup and operate BOOT0 the same way in both cases; the signals for nRST or BOOT1 can be chosen at the discretion of the designer. The ones available in [part 1 of the reset circuit article](../reset_article_1/reset_article_1.md) are advised;
    - **SWD pins SWDIO and SWCLK:** used for in-system-programming. These have very particular topologies, some have pullup or pulldown resistors. Expose them with a pin header and leave them be;
    - **USB pins USB_D+ and USB_D-:** used for USB communication;
    - **Pin PB2 or VCAP**: used by some MCU units for regulating ADC reference voltage and internal regulators voltages. According to [13], this should be hooked to an external 4.7 microfarads ceramic capacitor and should not be used for anything else.
- **Pink pin type or "keyboard feature pins":** these pins are used by certain keyboard features.
    - The I2C pins SDA and SCL are used for the EEPROM (needed for VIA). It is recommended to not use these pins for anything else as some MCUs in the compatibility list need EEPROM and designing your PCB without EEPROM support will make features like VIA not work with these MCUs in particular. In the case of MCUs with embedded EEPROM or EEPROM-simulation capabilities one can just leave the EEPROM circuit unpopulated;
    - The LED PWM can be any pin with PWM capability (avoid TIM2 pins as that is used by ChibiOS for OS tick). If your keyboard does not have backlight this pin can be used for anything else or left floating;
    - The RGB_3V3 pin used can be any SPI-capable pin; the RGB LEDs output signal is delivered by the SPIx_MOSI pin. The default port used in Joker48 is SPI2. Remember however that once SPI is enabled, the SPIx_CLK pin is locked and cannot be used for anything else; this is denoted by an X on the schematics figures. You can still use the SPIx_MISO pin for rows and columns. If your keyboard does not need to use this feature these pins can be freely used for anything else or left floating.
- **Black pin type or "general use pins":** these pins are, as the name suggests, ideal for general use, preferable rows and columns in your keyboard matrix;
- **Green pin type or "special case pins":** read below.
    - **PA9**: in microcontrollers with the USB OTG capability, this pin is used as VBUS sensing and has an embedded strong pullup resistor which impedes it from being used for anything else. On the template this is left with a 0R resisor (essentially a jumper) which can be populated in case this feature is not usable.
    - **PA10**: in MCUs with this capability, this pin is used by the DFU to update firmware using the USART peripheral; if left floating or with a long enough copper trace this pin can pickup signals and the USART DFU can trigger, which makes the MCU give USB errors. A weak pullup (51k on the schematic) is used to avoid  this. This pin can be used as a general input-output; the recommended use is as row or column pin in the switch matrix.
- **Yellow pins or power pins:** there are basically three types of power pins: VBAT for battery sensing, VDD for digital power, VDDA for analog power and VDDUSB for the USB peripheral power in MCUs that feature this (in the ones that don't these are just VDDIO pins). Figure 3 shows a schematic of the power supply scheme recommended by ST. Note the 10 microfarad tantallum capacitor, used for the particularity of thermal, age and electric reliability of tantallums.
    - Pin 1 has a battery sensing pin; this is used mostly for the realtime clock (RTC) peripheral to keep the time counter ticking while the microcontroller is not operating. According to **[11-13]**, if not external battery is present then this pin should be connected to VDD with a 100nF capacitor.
    - Pins 8 and 9 are the analog power supply and analog voltage reference for the ADC and DAC peripherals, reset blocks, oscillator PLLs and the internal HSI and LSI buses. The references recommend using two capacitors: a 100 nF ceramic with a 1uF ceramic or tantallum. Additionally, for digital noise filtering, it is also recommended to connect VDDA to VDD using through a ferrite bead;
    - Pins 23 and 24, 35 and 36, 47 and 48 are digital supply pin pairs (VDD and VSS respectively for each pair). These should be connected with a single tantallum or ceramic capacitor of minimum 4.7uF (10uF typical recommended) and a 100nF ceramic capacitor for each pin.

<figure>
  <img src="../../images/joker_article/stm32f0x1x2x8_power.svg" width="600" align="middle"/>
  <figcaption><b> Figure 3. </b>  STM32F0x1/x2/x8 power supply schematic as recommended by STM. Source: [12].</figcaption>
</figure>

It must be noted that in the 48-pin version, counting all general-purpose pins (with PA10), the template has 22 pins supporting up to 121 keys (11 rows by 11 colums) or 96 keys in a six-row by sixteen-columns design, meaning it can be used to support up to a TKL keyboard matrix.

### 3.3 Ready-to-use KiCAD files
     
In order to speed up development using these templates, the Acheron Project made available KiCAD template files that can be readily used through the [AcheronSetup keyboard creator script](../acheron_setup/acheron_setup.md) or by simply copying the target files. These files already have constraints and tolerances used by the AcheronProject to achieve somewhat factory-agnostic manufacturable PCB tolerances (like minimum copper trace widths, copper clearances *et cetera*), as documented in the AcheronSetup page.

## 4 Joker48 MCU compatibility list

Here are listed the known compatible or incompatible MCUs and some description of their workings, with the populate and don't populate list of components for each family.

### How to check if an MCU is supported by the Joker48 template
- It is available in a 48-pin version, in either LQFP-48 (package code "CxT") or UFQFPN (package code "CxU") packages;
- There is an I2C peripheral on pins 42 and 43;
- There is an SPI peripheral on pins 26 through 28;
- There is a PWM (timer) peripheral on pin 15 (avoid using timer TIM2 as it is used by ChibiOS for the OS tick);
- There is an USB peripheral on pins 32 and 33;
- The BOOT0 is at pin 44 and nRST at pin 7;
- For those units that have BOOT1, it's located at pin 20;
- For those units that do not have an internal RC oscillator, the oscillator crystal pins are 5 and 6;
- For those units that need a capacitor for the voltage regulators, the VCAP pin is located at pin 22;
- There are VDD and VSS (digital power and digital ground) at pins 23/24, 35/36, 47/48
- There are VDDA and VSSA (analog power and analog ground) at pins 8 and 9;
- There is a VBAT battery sense at pin 1;
- There are USB D+ and D- at pins 33 and 32 respectively;

Additionally, one must also make sure that all the power pins check. The MCUs compatible have VDD and VSS pins at pins 23/24, 35/36, 47/48; analog voltage reference pins are 8 and 9. Pins 1 is used as a battery voltage sensing and should be connected to VDD.

### 4.1 Known compatible families

#### F0x2

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32f0x2.html)
- **Compatible units**: this family has two sub-families.
    - *[STM32F042](https://www.st.com/resource/en/datasheet/stm32f042c4.pdf)*: STM32F042C(X)(Y) where (X) can be either 4 or 6 for 16 or 32 kB of flash and (Y) can be T or U for LQFP or UFQFPN package. 
    - *[STM32F072](https://www.st.com/resource/en/datasheet/stm32f072c8.pdf)*: STM32F072C(X)(Y) where (X) can be either 8 or B for 64 or 128kB of flash and (Y) can be T or U for LQFP or UFQFPN packages.
- **General notes:** these microcontrollers are very nice to use because they need minimal external components: no EEPROM, no crystal, no USB resistor. The only populated components needed are the I2C pullup resistors R2 and R3 if any I2C device beyond the EEPROM is needed, like an ISSI RGB controller. Both STM32F072C8 and STM32F072CB versions are compatible and provenly work but the lower flash on the 8 version might be a problem specially with VIA. It should however prove to be enough for most keyboards with no fancy custom code.
    - **Avoid F042 and favour F072**: avoid using F042 for its very, very low flash sizes (16kB for STM32F042x4 and 32kB for STM32F042x6) which will not be enough for a firmware with VIA; in truth, the F042 series is just a toned-down version of F072 but with no price or availability counterpart. Highly favour the F072 series MCU as it tends to be cheaper and more available than most (in non-pandemic times at least...);
    - **XTAL-less USB and integrated "EEPROM"**: QMK implements an EEPROM-simulating algorithm, hence essentially it has an integrated EEPROM. This MCU also integrates as solid-state oscillator with crystal-less USB capabilities, so it also does not need a crystal oscillator. 
- **Leave unpopulated**
    - Crystal oscillator Y1 and load capacitors C2 and C3 (has internal oscillator);
    - External EEPROM (simulates internal EEPROM in its flash). The I2C pullup resistors R2 and R3 can be also unpopulated if no other I2C devices are needed;
    - Pullup resistor R2 (integrated);
    - Voltage sense resistor R4 (has no voltage sensing in that pin);
    - BOOT1 pulldown resistor R1 (has no BOOT1);
    - VCAP capacitor C9 (does not have a VCAP pin);

#### F303

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32f303.html#overview)
- **Compatible units**: this family has basically three sub-families: *[STM32F303xD/xE](https://www.st.com/resource/en/datasheet/stm32f303re.pdf)*, *[STM32F303x6/x8](https://www.st.com/resource/en/datasheet/stm32f303c6.pdf)* and *[STM32F303xB/xC](https://www.st.com/resource/en/datasheet/stm32f303cb.pdf)* of which only the latter is supported; compatible devices then are STM32F303(X)T where (X) can be either B or C for 128 or 256 kB flash. Only the LQFP package is available for this sub-family.
- **General notes: DO NOT USE** x6 or x8 devices as they lack USB interfaces. Also, xD and xE variants are not available in 48-pin packages.
- **Leave unpopulated**
    - Voltage sense resistor R4 (has no voltage sensing in that pin);
    - BOOT1 pulldown resistor R1 (has no BOOT1);
- **Populate**
    - Crystal oscillator Y1 and load capacitors C2 and C3;
    - External EEPROM and I2C pullup resistors;
    - USB pullup resistor R5;
    - VCAP capacitor C9 (does not have a VCAP pin);

!!! warning

    **DO NOT, ABSOLUTELY DO NOT** use the x6 or x8 sub-families: despite available in LQFP-48 package, they lack USB interfaces. Also xD or xE versions are not available in 48-pin packages.

#### F411

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32f411.html#overview)
- **Compatible units**: has a [single sub-family](https://www.st.com/resource/en/datasheet/stm32f411ce.pdf). Compatible units are STM32F411C(X)(Y) where (X) can be C or E for 256 or 512 kB of flash and (Y) can be either T or U for LQFP or UFQFPN packages.
- **General notes**:
    - **F4x1 families**: the F411 and F401 families are, for our purposes, drop-in replacemets of one another. Therefore the same notes, observations and populate/not populate lists are the same.
    - **Clock and PLL**: this family had its use widely established through the [Black Pill MiniF4 featherboard](https://github.com/WeActTC/MiniSTM32F4x1) which is cheaply available on AliExpress, Alibaba and so on. The problem with the Black Pill, however, is that its designers decided to use too high a crystal frequency (25MHz) and that makes the firmware developed unreliable. Stick with the 8MHz of the template and adjust the PLL M,Q,N,P multiplicators as well as setting the ``STM32_HSECLK`` macro to 8000000. For an example on how to do this on QMK, check the [Mode M65S PCB firmware on QMK](https://github.com/qmk/qmk_firmware/tree/master/keyboards/mode/m65s);
    - **USB VBUS OTG sensing**: this family has what is called a "on-the-go fullspeed" USB, or "USB OTG FS" for short; this allows the device to act both as USB master and slave roles, stablishing a communication link between two devices. On this device, pin A9 (pin 30 on the 48-pin versions) has a USB OTG VBUS sensing, which would not be a big deal were it not for an undocumented integrated pulldown resistor on that pin which prevents it from being used for pretty much anything else on a keyboard, even column or row keys. If this peripheral is needed one can connect this pin to VBUS by the 0R resistor, but for most (almost all, really) applications this resistor should be left un-populated.
- **Leave unpopulated**
    - Voltage sense resistor R4 (populate if voltage sensing is needed);
    - USB pullup resistor R5;
- **Populate**
    - Crystal oscillator Y1 and load capacitors C2 and C3;
    - External EEPROM and I2C pullup resistors;
    - BOOT1 pulldown resistor R1;
    - VCAP capacitor C9;

#### F401

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32f401.html#overview)
- **Compatible units**: this family has two sub-families, *[STM32F401xB/xC](https://www.st.com/resource/en/datasheet/stm32f401cb.pdf)* and *[STM32F401xD/xE](https://www.st.com/resource/en/datasheet/stm32f401re.pdf)*, the difference between them being insignificant for our purposes, so any of those two sub-families can be used. Hence compatible units are STM32F401C(X)U where (X) can be B, C, D or E for 128, 256, 384 or 512 kB of flash. The 48-pin versions are only available in UFQFPN package.
- **General notes**:
    - **F4x1 families**: the F411 and F401 families are, for our purposes, drop-in replacemets of one another. Therefore the same notes, observations and populate/not populate lists are the same.
    - **Clock and PLL**: this family had its use widely established through the [Black Pill MiniF4 featherboard](https://github.com/WeActTC/MiniSTM32F4x1) which is cheaply available on AliExpress, Alibaba and so on. The problem with the Black Pill, however, is that its designers decided to use too high a crystal frequency (25MHz) and that makes the firmware developed unreliable. Stick with the 8MHz of the template and adjust the PLL M,Q,N,P multiplicators as well as setting the ``STM32_HSECLK`` macro to 8000000. For an example on how to do this on QMK, check the [Mode M65S PCB firmware on QMK](https://github.com/qmk/qmk_firmware/tree/master/keyboards/mode/m65s);
    - **USB VBUS OTG sensing**: this family has what is called a "on-the-go fullspeed" USB, or "USB OTG FS" for short; this allows the device to act both as USB master and slave roles, stablishing a communication link between two devices. On this device, pin A9 (pin 30 on the 48-pin versions) has a USB OTG VBUS sensing, which would not be a big deal were it not for an undocumented integrated pulldown resistor on that pin which prevents it from being used for pretty much anything else on a keyboard, even column or row keys. If this peripheral is needed one can connect this pin to VBUS by the 0R resistor, but for most (almost all, really) applications this resistor should be left un-populated.
- **Leave unpopulated**
    - Voltage sense resistor R4 (populate if voltage sensing is needed);
    - USB pullup resistor R5;
- **Populate**
    - Crystal oscillator Y1 and load capacitors C2 and C3;
    - External EEPROM and I2C pullup resistors;
    - BOOT1 pulldown resistor R1;
    - VCAP capacitor C9;

#### L4x2

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32l4x2.html#overview)
    - *[STM32L412xxx](https://www.st.com/resource/en/datasheet/stm32l412c8.pdf)*
    - *[STM32L422xxx](https://www.st.com/resource/en/datasheet/stm32l422cb.pdf)*
- **Compatible units**: STM32L4(Z)2C(X)(Y), where:
    - (X) can be B for 128kB of flash or 8 for 64kB of flash;
    - (Y) can be T for LQFP-48 package or U for UFQFPN-48;
    - (Z) can be either 1 or 2;
- **General notes**:
    - **No PWM on pin 16**: do not have a timer channel output on pin 16 so the LED backlight feature will not be available; hence this unit is only supported if this feature is not needed or can be disabled;
    - **Crystal-less USB**: these do not need a crystal to run the oscillator because they have an internal solid state oscillator;
- **Leave unpopulated**
    - Voltage sense resistor (has no voltage sensing);
    - USB pullup resistor R5 (integrated);
    - BOOT1 pulldown resistor R1 (has no BOOT1);
    - VCAP capacitor C9 (has no VCAP pin);
    - Crystal oscillator Y1 and load capacitors C2 and C3 (has internal RC oscillator);
- **Populate**
    - External EEPROM and I2C pullup resistors;

#### L4x2

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32l4x2.html#overview)
- **Compatible units**: this family has six sub-families:
   - *[STM32L422xx](https://www.st.com/resource/en/datasheet/stm32l422cb.pdf)*: pin 16 does not have a timer channel, hence it cannot output a PWM signal, meaning single-color backlight is unavailable with this MCU. No BOOT1 pin nor VCAP. Pin 36 is used for VDDUSB, for USB transceivers.
    - **Leave unpopulated**: voltage sense resistor R4 (populate if voltage sensing is needed), BOOT1 pulldown resistor R1 (has no BOOT1), VCAP capacitor C9 (has no VCAP pin);
    - **Populate**: crystal oscillator Y1 and load capacitors C2 and C3, external EEPROM and I2C pullup resistors, pullup resistor R2;
    - *[STM32L412xx](https://www.st.com/resource/en/datasheet/stm32l412c8.pdf)*
    - *[STM32L462xE](https://www.st.com/resource/en/datasheet/stm32l462ce.pdf)*
    - *[STM32L452xx](https://www.st.com/resource/en/datasheet/stm32l452cc.pdf)*
    - *[STM32L432Kx](https://www.st.com/resource/en/datasheet/stm32l432kb.pdf)*
    - *[STM32L442KC](https://www.st.com/resource/en/datasheet/stm32l442kc.pdf)*

#### L433

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32l4x3.html)
- **Compatible units**: sub-family from the L4x3 family: *[STM32L443xC](https://www.st.com/resource/en/datasheet/stm32l443cc.pdf)*.

#### L443

- **Link**: [family website](https://www.st.com/en/microcontrollers-microprocessors/stm32l4x3.html)
- **Compatible units**: sub-family from the L4x3 family: *[STM32L433xx](https://www.st.com/resource/en/datasheet/stm32l433cc.pdf)*.

### 4.2 Known incompatibilities

#### F103

The template lacks the USB termination resistors needed for proper operation of the USB peripheral on this family. The 103 family is very old and has a serious flaw when it comes to keyboard PCBs: despite having a USB peripheral on pins 32 and 33, they do not have a stock USB DFU bootloader, meaning that one has to flash firmware through the SWD pins which is highly end-user unfriendly as  one must have an ST-Link flasher device and access the PCB directly. There are third-party bootloaders with USB DFU capability but in order to flash those one must still use the SWD pins; also flashing a bootloader should only be done by someone that knows what they are doing because it can brick the microcontroller unit.

#### F417

Not available in 48-pin version.

#### F407

Not available in 48-pin version.

#### F415

Not available in 48-pin version.

#### F405

Not available in 48-pin version.

#### F446

Not available in 48-pin version.

#### F303 (x6, x8, xD, xE)

- **xE and xD sub-families:** not available in 48-pin version;
- **x6 and x8 sub-families:** lack an USB peripheral, hence they do not communicate over USB at all.

## 5 Joker64 MCU compatibility list

### 5.1 Known compatible families

#### F4x1

#### L431

#### L151

#### L071

### 5.1 How to check if an MCU is supported by the Joker64 template
- It is available in a 64-pin version, in LQFP-64 package which package code is "R";
- There is an I2C peripheral on pins 42 and 43;
- There is an SPI peripheral on pins 26 through 28;
- There is a PWM (timer) peripheral on pin 15 (avoid using timer TIM2 as it is used by ChibiOS for the OS tick);
- There is an USB peripheral on pins 32 and 33;
- The BOOT0 is at pin 44 and nRST at pin 7;
- For those units that have BOOT1, it's located at pin 20;
- For those units that do not have an internal RC oscillator, the oscillator crystal pins are 5 and 6;
- For those units that need a capacitor for the voltage regulators, the VCAP pin is located at pin 22;
- There are VDD and VSS (digital power and digital ground) at pins 23/24, 35/36, 47/48
- There are VDDA and VSSA (analog power and analog ground) at pins 8 and 9;
- There is a VBAT battery sense at pin 1;
- There are USB D+ and D- at pins 33 and 32 respectively;

Additionally, one must also make sure that all the power pins check. The MCUs compatible have VDD and VSS pins at pins 23/24, 35/36, 47/48; analog voltage reference pins are 8 and 9. Pins 1 is used as a battery voltage sensing and should be connected to VDD.

# References

- **[1]** *Why is there a chip shortage?*. Written by Chris Baraniuk for the BBC, published in august 26, 2021. Available at [this link](https://www.bbc.com/news/business-58230388). Last accessed september 1, 2021.

- **[2]** *The 2020-2021 global chip shortage*. Available in Wikipedia at [this link](https://en.wikipedia.org/wiki/2020%E2%80%932021_global_chip_shortage). Last accessed september 1, 2021.

- **[3]** *The Car Semiconductor Shortage Is Persisting. What It Means for Auto Stocks*. Written by Al Root for Barron's and published in august 27, 2021. Available at [this link](https://www.barrons.com/articles/chip-shortage-auto-stocks-tesla-51630077387). Last accessed september 1, 2021.

- **[4]** *Coping with the auto-semiconductor shortage: Strategies for succes*. Written by Ondrej Burkacky, Stephanie Lingemann, and Klaus Pototzky for McKinsey and Company and published in  may 27, 2021. Available in [this link](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/coping-with-the-auto-semiconductor-shortage-strategies-for-success) . Last accessed september 1, 2021.

- **[5]** *Application Note AN3364: Migration and compatibility guidelines for STM32 microcontroller applications*. Available at [this link](https://www.st.com/resource/en/application_note/an3364-migration-and-compatibility-guidelines-for-stm32-microcontroller-applications-stmicroelectronics.pdf). Last accessed september 1, 2021.

- **[6]** *The China-US trade war*. Available in Wikipedia at [this link](https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war). Last accessed september 1, 2021.

- **[7]** *How and When the Chip Shortage Will End, in 4 Charts: Fabs using older process nodes are the key*. By Samuel K. Moore and published in the IEEE Spectrum website in 29 of june, 2021. Available at [this link](https://spectrum.ieee.org/chip-shortage). Last accessed september 1, 2021.

- **[8]** *Application note AN4088: Migrating between STM32F1 and STM32F0 series microcontrollers*.  Available at [this link](https://www.st.com/resource/en/application_note/dm00052530-migrating-between-stm32f1-and-stm32f0-series-microcontrollers-stmicroelectronics.pdf). Last accessed september 1, 2021.

- **[9]** *Application note AN3422: Migration of microcontroller applications from STM32F1 to STM32L1 series*.  Available at [this link](https://www.st.com/resource/en/application_note/an3422-migration-of-microcontroller-applications-from-stm32f1-to-stm32l1-series-stmicroelectronics.pdf). Last accessed september 1, 2021.

- **[10]** *Application note AN3427: Migrating a microcontroller application from STM32F1 to STM32F2 series*.  Available at [this link](https://www.st.com/resource/en/application_note/an3427-migrating-a-microcontroller-application-from-stm32f1-to-stm32f2-series-stmicroelectronics.pdf). Last accessed september 1, 2021.

- **[11]** *Application note AN4206: Getting started with STM32F3 series hardware development*. Available at [this link](https://www.st.com/resource/en/application_note/dm00070391-getting-started-with-stm32f3-series-hardware-development-stmicroelectronics.pdf). Last accessed october 2, 2021.

- **[12]** *Application note AN4080: Getting started with STM32F0x1/x2/x8 hardware development*. Available at [this link](https://www.st.com/resource/en/application_note/dm00051986-getting-started-with-stm32f0x1x2x8-hardware-development-stmicroelectronics.pdf). Last accessed october 2, 2021.

- **[13]** *Application note AN4488: Getting started with STM32F4xxx hardware development*. Available at [this link](https://www.st.com/resource/en/application_note/dm00115714-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf). Last accessed october 2, 2021.

- **[14]** *USB On-The-Go Wikipedia article*. Available at its [Wikipedia page](https://en.wikipedia.org/wiki/USB_On-The-Go). Lasta ccessed october 3, 2021.

- **[15]** *USB hardware and PCB guidelines using STM32 MCUs*. Available at [this link](https://www.st.com/resource/en/application_note/dm00296349-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf). Last accessed october 12, 2021.

- **[16]** *Avalanche Breakdown Wikipedia page*. Available at [this link](https://en.wikipedia.org/wiki/Avalanche_breakdown). Last accesses october 23, 2021.

- **[17]** *Frequency response of theoretical models of junction transistors*. By R.L. Pitchard, published in the IRE Transactions on Circuit Theory, vol.2, no.2, pp. 183-191 in june 1995. Available at [this link](https://ieeexplore.ieee.org/abstract/document/6373424). Last accessed october 23, 2021.

- **[18]** *Uncertainty-added S-parameters of high power transistors*. By Ceylan, Osmar, Buber, Tekamul and Esposito Giampiero, published in IEEE Data Port Open-Access in july, 2020. Available at [this link](https://ieee-dataport.org/open-access/uncertainty-added-s-parameters-high-power-rf-transistors). Last accessed october 23, 2021.
