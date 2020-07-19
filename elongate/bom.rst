*****************
Bill of Materials
*****************

How to order components from LCSC
---------------------------------

:download:`This file <https://github.com/Gondolindrim/Elongate/raw/master/manuFiles/elongate_BOM.csv>` contains the Bill of Materials -- all the components for the Shark PCB -- quoted in the LCSC site. It has all LCSC part numbers, quantities and descriptions. For exact instructions on how to order the components from LCSC using the sheet file, please see `this video <https://www.youtube.com/watch?v=eFgOC5_1VYU>`_.

If you don't want to order them from LCSC, the table below can be used.

BOM table
---------

.. Hint:: Please note that some items may be out of stock when you are ordering them. Feel free to edit the BOM (making sure to substitute the components for compatible ones) if you know what you are doing. Also don't hesitate to hit me up, if you don't feel confident to change the components, so I can redo the list with available components.

.. Attention:: If you don't have experience with electronic design, do not attemp to swap or change the components in this table. Doing so may hinder some features of the PCB and even inutilize it!

+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: Designator | .. centered:: Package         | .. centered:: Quantity | .. centered:: Value              | .. centered:: LCSC Part Number        |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: X1         | .. centered:: 4 pin 5032      | .. centered:: 1        | .. centered:: 16MHz              | .. centered:: C242216                 |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: RDM1       | .. centered:: 0805            | .. centered:: 2        | .. centered:: 22R                |                                       |
| .. centered:: RDP1       |                               |                        |                                  |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: D1-54      | .. centered:: Axial (THT)     | .. centered:: 54       | .. centered:: 1N4148             | .. centered:: C261233                 |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: U3         | .. centered:: TQPF-44         | .. centered:: 1        | .. centered:: ATMEGA32U4         | .. centered:: C44854                  |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: U2         | .. centered:: SOT-23-6        | .. centered:: 1        | .. centered:: USBLC6-2SC6        | .. centered:: C323793                 |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: SW_RST1    | .. centered:: SMD Push Button | .. centered:: 1        | .. centered:: K2-1187SQ-A4SW-06  | .. centered:: C92584                  |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: RSH1       | .. centered:: 0805            | .. centered:: 1        | .. centered:: 1M                 |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: RRST2      | .. centered:: 0805            | .. centered:: 1        | .. centered:: 330R               |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: RRST1      | .. centered:: 0805            | .. centered:: 1        | .. centered:: 4.7k               |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: RHWB1      | .. centered:: 0805            | .. centered:: 2        | .. centered:: 10k                |                                       |
| .. centered:: RF1        |                               |                        |                                  |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: J1         |                               | .. centered:: 1        | .. centered:: Hirose UX60-MB-5S8 | .. centered:: (not available on LCSC) |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: F1         | .. centered:: 1812            | .. centered:: 1        | .. centered:: 1.5A trip          |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: DF1        | .. centered:: SOD-123         | .. centered:: 1        | .. centered:: RB060M-60TR        | .. centered:: C114257                 |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: CX2,CX1    | .. centered:: 0805            | .. centered:: 2        | .. centered:: 8.2pF              |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: CUSB1      | .. centered:: 0805            | .. centered:: 8        | .. centered:: 100nF              |                                       |
| .. centered:: CSH1       |                               |                        |                                  |                                       |
| .. centered:: CRST1      |                               |                        |                                  |                                       |
| .. centered:: CB2-6      |                               |                        |                                  |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+
| .. centered:: CU1        | .. centered:: 0805            | .. centered:: 3        | .. centered:: 1uF                |                                       |
| .. centered:: CB1        |                               |                        |                                  |                                       |
| .. centered:: CF1        |                               |                        |                                  |                                       |
+--------------------------+-------------------------------+------------------------+----------------------------------+---------------------------------------+

Notes on the BOM 
----------------

**(1)** The rotary encoder was chosen because it was available at LCSC, Digikey and Mouser electronics. Its cheap, readily available and easy to solder. It also offers mechanical endurance through auxiliary legs that are soldered into the PCB. 

The encoder series EC11Ex looks to be a very versatile encoder in the sense that any rotary encoder in the series fits the footprint and has the sae pinout, as the models differ only on shaft shape and size but their footprints are the same. In the render I used the ALPS EC11E 15244G1.

**(2)** This connector seems to not be available in the european or american markets, only asian. It was chosen because, while being USBC, it has simplified pins and can easily be handsoldered. I have yet to find a good substitute for this connector that can be bought worldwide.

**(3)** Any fuse that fits the footprint will work, but I personally prefer polyfuses. Make sure that is has a minimum 1.5A trip current, as the LEDs and the high current microprocessor can sum 1A current easily.

**(4)** Please make sure that you order this exact package, since the footprint will not support anything different than this.
