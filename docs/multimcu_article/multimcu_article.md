# A multi-MCU approach to mechanical keyboard hardware design
*Because desperate times need creative measures*

---

## 1 Introduction

The worldwide pandemic has brought an unprecedented halt in many private sector fields, specially logistics and tourism, fields that were completely shut down in efforts to break the spread of the SARS-CoV-2 virus. One of such affected sectors was the semiconductor manufacturing, in a global phenomenon we agreed to call the "chip shortage", the "semiconductor shortage", or simply "electronics shortage" [1]. This shortage has been caused by a consurgence of factors, which include the US-China trade war in the Trump administration, the COVID-19 pandemic, the halting of factories in Europe, US and China ([2],[6]).

It is not the intent of this article to explain why this shortage is or what are its causes. See the references for deeper understanding.

This shortage has hit everyone by their guts at this point, because, in the digital humanity of the twenty-first century, every single home appliance, handheld device, consumer electronics device and kids toy, uses, if not several, at least one microcontroller (which we will, for better reading, abbreviate as MCUs for "Microcontroller Units"). The problem being that, due to the shortage, the supply of MCUs has been diminished to a point where Toyota, Honda and Ford announced that they are halting their manufacturing efforts simply because there are no MCUs available to manufacture their cars [3] .

As of the writing of this article (semtember of 2021), the semiconductor industry is still getting back on its feet, trying to match supply to demand. The void in supply is still huge, which brings us to the keyboard community. For us, this supply issue has hit hard. The thing is: since there are important industries in dire need of semiconductor devices, the ones deemed more urgent get priority, specially the car manufacturers and, for obvious reasons, the medical supplies and devices manufacturers. In this zeitgeist, distributors like LCSC, Digikey and Mouser, who serve the general buyers, rarely get some stock of any MCUs at all. If there is stock, the microcontrollers are sold at ridiculous prices [4]. 

The biggest example being the microcontroller I use the most for keyboards: STM32F072C, be it the B (128kB flash) or 8 (64kB flash) versions. While in a normal setting I could get several thousand units for around two US dollars a piece, nowadays I can only get tens of them for twenty six US dollars each; and that's considering I can not *always* have them. This trend is not unique to this unit, as all others follow the same pattern. It's not surprising, then, to see that designing and manufacturing keyboard PCBs in this setting is a challenge. At a given time, one MCU is available, say F072, and in the next week it will become out of stock and another one, say, F411, will be available.

This article is an attempt to document a long and wide talk between me (Gondolindrim) and **tzarc**, embedded systems engineer and known in the keyboard community through his work as a QMK developer, where we achieved a template design that allows for multiple STM microcontroller units to be used in the same design, only needing tweaking in the bill of materials. This should make the manufacture of the PCBs *easier* in the context of the pandemic (because of course no one can't make it easier than it was before, with availability and prices) while giving the PCB designer some insight insight in such approach.

### 1.1 The STM approach

The STM family of microprocessors is industry-wide known for their cross-compatibility, that is, the ability to *replace one microcontroller type by another one in the same product series* [5] . It is nice to know that the STM microcontrollers are designed for *some level* of cross-compatibility from the get-go, but one must wonder what are the needed changes to port a design from one microcontroller or another; STM has many ([8], [9], [10]) references on such operations. However, to the best of my knowledge there is not an application note on a *multi-microcontroller* approach, that is, how to design an appliance to support multiple microcontroller families.

References [8] through [10] show

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
