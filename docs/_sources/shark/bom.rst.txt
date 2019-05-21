*****************
Bill of Materials
*****************

How to order components from LCSC
---------------------------------

:download:`This file <https://github.com/Gondolindrim/SharkPCB/raw/master/bom/shark_LCSC.xlsx>` contains the Bill of Materials -- all the components for the Shark PCB -- quoted in the LCSC site. It has all LCSC part numbers, quantities and descriptions. For exact instructions on how to order the components from LCSC using the sheet file, please see `this video <https://www.youtube.com/watch?v=eFgOC5_1VYU>`_.

If you don't want to order them from LCSC, the table below can be used.

BOM table
---------

.. Hint:: Please note that some items may be out of stock when you are ordering them. Feel free to edit the BOM (making sure to substitute the components for compatible ones) if you know what you are doing. Also don't hesitate to hit me up, if you don't feel confident to change the components, so I can redo the list with available components.

.. Attention:: If you don't have experience with electronic design, do not attemp to swap or change the components in this table. Doing so may hinder some features of the PCB and even inutilize it!

+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: Description           | .. centered:: Value                 | .. centered:: Package           | .. centered:: Quantity   |
+=====================================+=====================================+=================================+==========================+
| .. centered:: J1                    |                                     | .. centered:: 31-M-12 :sup:`(2)`| .. centered:: 1          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: CX1 and CX2           | .. centered:: 22pF                  | .. centered:: 0805              | .. centered:: 2          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: C7, C9, CRST2         | .. centered::  4.7nF                | .. centered:: 0805              | .. centered:: 3          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: CRST1                 | .. centered::  10uF                 | .. centered:: 0805              | .. centered:: 1          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: (Poly)Fuse :sup:`(3)` |  .. centered:: 1.5A trip            | .. centered:: 0805              | .. centered:: 1          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: R5 and R6             | .. centered:: 1MOhm                 | .. centered:: 1206              | .. centered:: 2          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: CSin                  |                                     |                                 |                          |
| .. centered:: CSout                 |                                     |                                 |                          |
| .. centered:: CVB1-3                |                                     |                                 |                          |
| .. centered:: CA, CB                | .. centered:: 100nF                 | .. centered:: 0805              | .. centered:: 7          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: Q1                    | .. centered:: AO4406AL              | .. centered:: SOIC8             | .. centered:: 1          |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: CVB4                  | .. centered:: 1uF                   | .. centered:: 0805              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: CVB5                  | .. centered:: 4.7uF                 | .. centered:: 0805              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: DF1                   | .. centered:: RB060M-60TR           | .. centered:: SOD-123           | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: QRST                  | .. centered:: DTC123J-KAT146        | .. centered:: SOT-23            | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RCC                   | .. centered:: 5.1kOhm               | .. centered:: 1206              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RD+ and RD-           | .. centered:: 22ROhm                | .. centered:: 1206              | .. centered::  2         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RD+Up                 | .. centered:: 1.5kOhm               | .. centered:: 1206              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RB1/2, RA1/2          |                                     |                                 |                          |
| .. centered:: RPGate                | .. centered:: 10kOhm                | .. centered:: 1206              | .. centered::  5         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RRST                  | .. centered:: 100kOhm               | .. centered:: 1206              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RSGate                | .. centered:: 100 Ohm               | .. centered:: 1206              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: SWRST                 | .. centered:: SMD Push Button       |                                 | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: U1                    | .. centered:: STM32F303CCT6         | .. centered:: LQFP48 :sup:`(4)` | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: U2                    | .. centered:: MCP1700-330 LDO       | .. centered:: SOT23             | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: Y1                    | .. centered:: 8MHz 4 pin            | .. centered:: 5032              | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RGB                   | .. centered:: WS2812B               |                                 | .. centered::  8         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: RL1-48                | .. centered:: 360 Ohm               | .. centered:: 1206              | .. centered::  50        |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: DS1                   |                                     |                                 |                          |
| .. centered:: DRST                  |                                     |                                 |                          |
| .. centered:: D1-48                 | .. centered:: 1N4148W               | .. centered:: SOD-123           | .. centered::  52        |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: DESD                  | .. centered:: 1N4007W               | .. centered:: SOD-123           | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+
| .. centered:: ROT1                  | .. centered:: ALPS EC11Ex :sup:`(1)`|                                 | .. centered::  1         |
+-------------------------------------+-------------------------------------+---------------------------------+--------------------------+

Notes on the BOM 
----------------

**(1)** The rotary encoder was chosen because it was available at LCSC, Digikey and Mouser electronics. Its cheap, readily available and easu to solder. It also offers mechanical endurance through auxiliary legs that are soldered into the PCB. 

The encoder series EC11Ex looks to be a very versatile encoder in the sense that any rotary encoder in the series fits the footprint and has the sae pinout, as the models differ only on shaft shape and size but their footprints are the same. In the render I used the ALPS EC11E 15244G1.

**(2)** This connector seems to not be available in the european or american markets, only asian. It was chosen because, while being USBC, it has simplified pins and can easily be handsoldered. I have yet to find a good substitute for this connector that can be bought worldwide.

**(3)** Any fuse that fits the footprint will work, but I personally prefer polyfuses. Make sure that is has a minimum 1.5A trip current, as the LEDs and the high current microprocessor can sum 1A current easily.

**(4)** Please make sure that you order this exact package, since the footprint will not support anything different than this.
