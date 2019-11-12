*******************
Manufacturing files
*******************

In the ``./gerbers`` folders you can find the plot files for the PCB and the plates.

Schematic
---------

:download:`Click here <https://github.com/Gondolindrim/SharkPCB/releases/download/Alpha/SharkPCB_schematic_Alpha.pdf>` for the schematic file of the Alpha version.

PCB manufacturing files
-----------------------

:download:`This zipped folder <https://github.com/Gondolindrim/SharkPCB/releases/download/Alpha/SharkPCB_Gerbers_Alpha.zip>` contains the Gerber files for the PCB Alpha version. Among them are probably more files than needed, including the files for the PCB edges and drill files.

:download:`Click here <https://github.com/Gondolindrim/SharkPCB/releases/download/Alpha/SharkPCB-pickNplace_Alpha.pos>` to download the component position file for the PCB.

.. Attention:: The `SharkPCB introduction page <./shark.html>`_ contains badges to show the last prototyped version of the PCB. I will release un-prototyped Gerbers in order to prototype them. Always check if the version you are downloading was prototyped!

Bill of Materials
-----------------

How to order components from LCSC
*********************************

:download:`This file <https://github.com/Gondolindrim/SharkPCB/raw/master/manuFiles/shark_BOM.csv>` contains the Bill of Materials -- all the components for the Shark PCB -- quoted in the LCSC site. It has all LCSC part numbers, quantities and descriptions. For exact instructions on how to order the components from LCSC using the sheet file, please see `this video <https://www.youtube.com/watch?v=eFgOC5_1VYU>`_.

If you don't want to order them from LCSC, the table below can be used.

BOM table
*********

:download:`Click here <https://github.com/Gondolindrim/SharkPCB/releases/download/Alpha/SharkPCB_BOM_Alpha.csv>` for the Bill of Materials file, or check the table below.

.. Hint:: Please note that some items may be out of stock when you are ordering them. Feel free to edit the BOM (making sure to substitute the components for compatible ones) if you know what you are doing. Also don't hesitate to hit me up, if you don't feel confident to change the components, so I can redo the list with available components.

.. Attention:: If you don't have experience with electronic design, do not attemp to swap or change the components in this table. Doing so may hinder some features of the PCB and even inutilize it!

+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| Designator          | Package            | Quantity | Value                 | Manufacturer           | Manufacturer Part No. | LCSC Part No. |
+=====================+====================+==========+=======================+========================+=======================+===============+
| L1                  | -                  | 1        | ACM2012-900-2P-T002   | TDK                    | ACM2012-201-2P-T002   | C76572        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| RVDD1               | R1206              | 1        | R010 1%               |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| L3                  | L1210              | 1        | CMI322513U1R0KT       | Guangdong Fenghua      | CMI322513U1R0KT       | C99412        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| CB10,CB9,CSO1       | C0805              | 3        | 1µ                    |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| RL1                 | R1206              | 1        | 620R                  |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| DL1                 | D0603              | 1        | 19-217/R6C-AL1M2VY/3T | Everlight Elec         | 19-217/R6C-AL1M2VY/3T | C72044        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| J1 :sup:`(1)`       | -                  | 1        | TYPE-C-31-M-12        | Korean Hroparts Elec   | TYPE-C-31-M12         | C165948       |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| U1                  | LQFP-48 :sup:`(3)` | 1        | STM32F072CBT6         | STMicroelectronics     | STM32F072CBT6         | C81720        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| L2                  | L0603              | 1        | MGFL1608F1R0MT-LF     | Microgate              | MGFL1608F1R0MT-LF     | C281108       |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| DF1                 | SOD-123F           | 1        | SMF9.0CA              | Microdiode Electronics | SMF9.0CA              | C123799       |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| RSO1,RSI1,RRST1     | R1206              | 3        | 100k                  |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| RPU1                | R1206              | 1        | 1k5                   |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| D1-63, D65          | SOD-123F           | 64       | 1N4148WL              |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| CB1,CB4,CB6         | C0402              | 3        | 1µ                    |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| CB2,CB3,CB5,CB7,CB8 | C0402              | 5        | 100n                  |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| CRST1               | C0805              | 1        | 10µ                   |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| CRST2,CSH1,CSH2     | C0805              | 3        | 4n7                   |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| CSI1,CUSB1          | C0805              | 2        | 100n                  |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| DRST1               | SOD-123            | 1        | B0520LW-7-F           | Diodes Incorporated    | B0520LW-7-F           | C155367       |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| DS1,DSH1            | SOD-123            | 2        | RB060M-60TR           | ROHM Semiconductor     | RB060M-60TR           | C114257       |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| F1                  | F1812              | 1        | 1A trip PTC:sup:`(2)` | BOURNS                 | MF-MSMF050-2          | C17313        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| QRST1               | SOT-23             | 1        | DTC123JKAT146         | ROHM Semiconductor     | DTC123JKAT146         | C111724       |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| RCC1,RCC2           | R1206              | 2        | 5k1                   |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| RSH1,RSH2           | R1206              | 2        | 1M                    |                        |                       |               |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| SWRST1              | 5.2x5.2mm          | 1        | K2-1187SQ-A4SW-06     | Korean Hroparts        | K2-1187SQ-A4SW-06     | C92584        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| U2                  | SOT-23-6           | 1        | USBLC6-2SC6           | STMicroelectronics     | USBLC6-2SC6           | C7519         |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
| U3                  | SOT-23             | 1        | MCP1700T-3302E/TT     | Microchip Tech         | MCP1700T-3302E/TT     | C39051        |
+---------------------+--------------------+----------+-----------------------+------------------------+-----------------------+---------------+
Notes on the BOM 
****************

**(1)** The rotary encoder was chosen because it was available at LCSC, Digikey and Mouser electronics. Its cheap, readily available and easy to solder. It also offers mechanical endurance through auxiliary legs that are soldered into the PCB. 

The encoder series EC11Ex looks to be a very versatile encoder in the sense that any rotary encoder in the series fits the footprint and has the sae pinout, as the models differ only on shaft shape and size but their footprints are the same. In the render I used the ALPS EC11E 15244G1.

**(2)** This connector seems to not be available in the european or american markets, only asian. It was chosen because, while being USBC, it has simplified pins and can easily be handsoldered. I have yet to find a good substitute for this connector that can be bought worldwide.

**(3)** Any fuse that fits the footprint will work, but I personally prefer polyfuses. Make sure that is has a minimum 1.5A trip current, as the LEDs and the high current microprocessor can sum 1A current easily.

**(4)** Please make sure that you order this exact package, since the footprint will not support anything different than this.

Plates Gerber and vector files
------------------------------

The gerbers folder also contains the plot files for the plates of both tall and short cases. There are basically two kinds of files for the plates: Gerbers and vectorized. 

Just to save on notation, "high plate" designates the plate for the tall (high-profile) case; the same goes for "short plate".

- The Gerber files are used to order plates in the very same way as you would a PCB. This is awesome because you can cheaply order plates made from FR4 (the same material as the PCBs).

- The vectorized files are more general files that can be used to order plates in all sorts of materials, as the machining shops don't use Gerbers. The aluminum plates offered in the group buys were ordered with these very same files. These shops usually use AutoCad ``*.dxf`` files, which can be downloaded below. The problem is that AutoCad is not open-source nor free, so I also offer ``*.svg`` files that can be used with Inkscape.

+----------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
|          | **Gerber**                                                                                               | **DXF**                                                                                                  | **SVG**                                                                                                  |
+----------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **High** | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/highPlate.zip>` | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/highPlate.dxf>` | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/highPlate.svg>` |
+----------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Low**  | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/lowPlate.zip>`  | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/lowPlate.dxf>`  | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/lowPlate.svg>`  |
+----------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Base** | :download:`Download<https://github.com/Gondolindrim/SharkHardware/releases/download/V1.0/basePlate.zip>` |                                                                                                          |                                                                                                          |
+----------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
