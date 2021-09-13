# A multi-MCU approach to mechanical keyboard hardware design: the Joker template
*Because desperate times need creative measures*

---

## 1 Introduction

The worldwide pandemic has brought an unprecedented halt in many private sector fields, specially logistics and tourism, fields that were completely shut down in efforts to break the spread of the SARS-CoV-2 virus. One of such affected sectors was the semiconductor manufacturing, in a global phenomenon we agreed to call the "chip shortage", the "semiconductor shortage", or simply "electronics shortage" [1]. This shortage has been caused by a consurgence of factors, which include the US-China trade war in the Trump administration, the COVID-19 pandemic, the halting of factories in Europe, US and China ([2],[6]).

It is not the intent of this article to explain why this shortage is or what are its causes. See the references for deeper understanding.

This shortage has hit everyone by their guts at this point because in the digital humanity of the twenty-first century every single home appliance, handheld device, consumer electronics, and kids toy uses if not several at least one microcontroller (which we will, for better reading, abbreviate as MCUs for "Microcontroller Units"). The problem being that, due to the shortage, the supply of MCUs has been diminished to a point where even huge car manufacturers like Toyota, Honda and Ford announced that they are halting their manufacturing efforts simply because there are no MCUs available to manufacture their cars [3] .

As of the writing of this article (semtember of 2021), the semiconductor industry is still getting back on its feet, trying to match supply to demand. The void in supply is still huge, which brings us to the keyboard community. For us, this supply issue has hit hard. The thing is: not only demand is completely disproportionally small compared to demand, there are important industries in dire need of semiconductor devices, some of them deemed more urgent get priority, specially the car manufacturers and, for obvious reasons, the medical supplied and devices. In this zeitgeist, distributors like LCSC, Digikey and Mouser, who serve the general buyers like us mere keyboard mortals rarely get some stock of any MCUs at all. If there is stock, the microcontrollers are sold at ridiculous prices [4]. 

Just as an example: the microcontroller I use the most for keyboards is STM32F072C, be it the B (128kB flash) or 8 (64kB flash) versions. While in a normal setting I could get several thousand units for around two US dollars a piece, nowadays I can only get tens of them for twenty six US dollars each; and that's considering I can not *always* have them. This trend is not unique to this unit, as all others follow the same pattern. It's not surprising, then, to see that designing and manufacturing keyboard PCBs in this setting is a challenge. At a given time, one MCU is available, say F072, and in the next week it will become out of stock and another one, say, F411, will be available.

This article is an attempt to document a long and wide talk between me (Gondolindrim) and **tzarc**, embedded systems engineer and known in the keyboard community through his work as a QMK developer, where we achieved a template design that allows for multiple STM microcontroller units to be used in the same design, only needing tweaking in the bill of materials. This should make the manufacture of the PCBs *easier* in the context of the pandemic (because of course no one can't make it easier than it was before, with availability and prices) while giving the PCB designer some insight insight in such approach.

### 1.1 Objective and constraints

The end objective of this article is to develop a template design consisting of a microcontroller footprint and several ancillary components (EEPROM, clock crystal and its load capacitors, USB resistors, bypass capacitors); this template design is intended as a "joker" design that can support multiple STM32 microcontrollers, with the following parameters:

#### Firmware compatibility

Target MCUs must be QMK-supported;

#### Availability

Target MCUs must also be available for purchase for the general public (there are versions restricted to military or industrial use);

#### Design licensing
The Joker template should be KiCAD-compatible and open-source;

#### Manufacturability

The design must be manufacturable through a wide myriad (if not all) of the PCB manufacturers out there. There are some MCU versions that use BGA, UBGA and WLCSP packages which are only manufacturable in specialized fab houses. In this article we will focus on 48-pin variants, specifically UFQFPN-48 and LQFP-48 packages.

### 1.2 The STM approach and how we make use of it

The STM family of microprocessors is industry-wide known for their cross-compatibility, that is, the ability to *replace one microcontroller type by another one in the same product series* [5] . It is nice to know that the STM microcontrollers are designed for *some level* of cross-compatibility from the get-go, but one must wonder what are the needed changes to port a design from one microcontroller or another; STM has many ([8], [9], [10]) references on such operations. However, to the best of my knowledge there is not an application note on a *multi-microcontroller* approach, that is, how to design an appliance to support multiple microcontroller families.

References [8] through [10] show official STM documents that specifically target the migrating capabilities of the STM32 family, allowing us to get a better grip on how it works.

## 2. How the template works

The core mechanic of the joker template is the fact that for the majority of the STM32 MCUs, some specific peripherals and the power inputs are kept at the same pins throughout multiple chip models, hence allowing us to fix those pins and maintain some keyboard features (RGB, LEDs and so on) attached to the same pin of the footprint. In other words, the way this works is that the pins we use for RGBs, LEDs, OLED control and so on can be the same across multiple chips; this in turn allows us to make a design that can receive a variety of different chips and configure their pins through QMK or a realtime operating system.

This is not to say, however, that all the STM32 microcontrollers are the same. For instance, STM32F07x is a microcontroller line aimed at connectivity in cost-sensitive applications; hence it integrates a solid-state oscillator with a USB 2.0 and CAN bus, meaning you have a high degree of possibilities in a small and cheap package with resistorless USB connectivity and crystal-less operation. However, its peripherals are very basic; the STM32F30x family, for instance, is a more sophisticated family with operational amplifiers, ultra-fast comparators, 12-bit ultra-fast ADCs but they need a pullup resistor and an oscillator crystal while being more expensive.

Hence, even though the F0x and F30x have the SPI and I2C peripherals at the same pins, those peripherals might not be the same (with a high chance of the F30x peripherals being better and faster). This gives rise to a second layer of the ingenuity of the joker template: ultimately, keyboards are not the pinnacle of human technology. No one needs a ultra-fast ADC to run a keyboard; a simple ADC will do the trick. Hence, both the "lighter" peripherals of the F07x and the "better" ones on F30x will work.

#### I2C

The I2C1 peripheral is generally at pins 42 and 43 (PB9 and PB10); this peripheral is used by QMK for some RGB controlling chips (ISSI chips mostly) and to control OLED screens;

#### PWM

The channel 1 of TIM3 is generally at pin 15 (PA6); this peripheral can be used by QMK to control the WS2812 RGB LEDs and for the backlight LEDs (also called "in-switch" LEDs); in the case of this template, we use it mainly for the backlight.

#### SPI
The SPI2 peripheral is generally located at pins 28, 27 and 26 (in that order, MOSI, MISO and SCK pins).

## 1.3 The final circuit

Figure 1 shows a schematic of the "joker template" developed. 

<figure>
  <img src="../../images/multimcu_article/joker.svg" width="800" align="middle"/>
  <figcaption><b> Figure 1. </b>  "Joker" 48-pin STM32 MCU circuit topology.</figcaption>
</figure>

This template can be used by using the [keyboard creator tool](../acheron_setup/acheron_setup.md) script or by simply copying the [target files](https://github.com/AcheronProject/AcheronSetup/tree/main/keyboard_creator/joker_template). Figure 2 shows the KiCAD schematic implementation of these files.

<figure>
  <img src="../../images/multimcu_article/kicad_schematic.svg" width="800" align="middle"/>
  <figcaption><b> Figure 2. </b>  "Joker" 48-pin STM32 MCU circuit KiCAD template schematic.</figcaption>
</figure>

## 1.4 How the 


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
