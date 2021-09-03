# A multi-MCU approach to mechanical keyboard hardware design
*Because desperate times need creative measures*

---

## 1 Introduction

The worldwide pandemic has brought an unprecedented halt in many private sector fields, specially logistics and tourism, fields that were completely shut down in efforts to break the spread of the SARS-CoV-2 virus. One of such affected sectors was the semiconductor manufacturing, in a global phenomenon we agreed to call the "chip shortage", the "semiconductor shortage", or simply "electronics shortage" [MM1]_. This shortage has been caused by a consurgence of factors, which include the US-China trade war in the Trump administration, the COVID-19 pandemic, the halting of factories in Europe, US and China :sup:`(` [MM2]_ :sup:`,` [MM6]_ :sup:`)`.

It is not the intent of this article to explain why this shortage is or what are its causes. See the references for deeper understanding.

This shortage has hit everyone by their guts at this point, because, in the digital humanity of the twenty-first century, every single home appliance, handheld device, consumer electronics device and kids toy, uses, if not several, at least one microcontroller (which we will, for better reading, abbreviate as MCUs for "Microcontroller Units"). The problem being that, due to the shortage, the supply of MCUs has been diminished to a point where Toyota, Honda and Ford announced that they are halting their manufacturing efforts simply because there are no MCUs available to manufacture their cars [MM3]_ .

As of the writing of this article (semtember of 2021), the semiconductor industry is still getting back on its feet, trying to match supply to demand. The void in supply is still huge, which brings us to the keyboard community. For us, this supply issue has hit hard. The thing is: since there are important industries in dire need of semiconductor devices, the ones deemed more urgent get priority, specially the car manufacturers and, for obvious reasons, the medical supplies and devices manufacturers. In this zeitgeist, distributors like LCSC, Digikey and Mouser, who serve the general buyers, rarely get some stock of any MCUs at all. If there is stock, the microcontrollers are sold at ridiculous prices [MM4]_. 

The biggest example being the microcontroller I use the most for keyboards: STM32F072C, be it the B (128kB flash) or 8 (64kB flash) versions. While in a normal setting I could get several thousand units for around two US dollars a piece, nowadays I can only get tens of them for twenty six US dollars each; and that's considering I can not *always* have them. This trend is not unique to this unit, as all others follow the same pattern. It's not surprising, then, to see that designing and manufacturing keyboard PCBs in this setting is a challenge. At a given time, one MCU is available, say F072, and in the next week it will become out of stock and another one, say, F411, will be available.

This article is an attempt to document a long and wide talk between me (Gondolindrim) and **tzarc**, embedded systems engineer and known in the keyboard community through his work as a QMK developer, where we achieved a template design that allows for multiple STM microcontroller units to be used in the same design, only needing tweaking in the bill of materials. This should make the manufacture of the PCBs *easier* in the context of the pandemic (because of course no one can't make it easier than it was before, with availability and prices) while giving the PCB designer some insight insight in such approach.

### 1.1 The STM approach

The STM family of microprocessors is industry-wide known for their cross-compatibility, that is, the ability to *replace one microcontroller type by another one in the same product series* [MM5]_ . It is nice to know that the STM microcontrollers are designed for *some level* of cross-compatibility from the get-go, but one must wonder what are the needed changes to port a design from one microcontroller or another; STM has many :sup:`(` [MM8]_ :sup:`,` [MM9]_ :sup:`,` [MM10]_ :sup:`)` references on such operations. However, to the best of my knowledge there is not an application note on a *multi-microcontroller* approach, that is, how to design an appliance to support multiple microcontroller families.

References _[8]

