*******************
Manufacturing files
*******************

This page was last updated since the `pre-Release Alpha <https://github.com/Gondolindrim/Doddle60/releases/tag/preAlpha>`_ .

Gerbers
-------

:download:`Click here <https://github.com/Gondolindrim/Doddle60/releases/download/preAlpha/doddle60_preAlpha_Gerbers.zip>` to download the latest release gerber files. These can be used to order the PCBs either assembled or un-assembled.

Schematic
---------

:download:`Click here <https://github.com/Gondolindrim/Doddle60/releases/download/preAlpha/doddle60_preAlpha_Schematic.pdf>` for the schematic file of the Alpha version.

PCB manufacturing files
-----------------------

:download:`This zipped folder <https://github.com/Gondolindrim/Doddle60/releases/download/preAlpha/doddle60_preAlpha_Gerbers.zip>` contains the Gerber files for the PCB pre-revision Alpha version. Among them are probably more files than needed, including the files for the PCB edges and drill files.

:download:`Click here <https://github.com/Gondolindrim/Doddle60/releases/download/preAlpha/doddle60_preAlpha_positionFile.pos>` to download the component position file for the PCB.

.. Attention:: The `introduction page <./intro.html>`_ contains badges to show the last prototyped version of the PCB. I will release un-prototyped Gerbers in order to prototype them. Always check if the version you are downloading was prototyped!

Bill of Materials
-----------------

BOM table
*********

:download:`This file <https://github.com/Gondolindrim/Doddle60/releases/download/preAlpha/doddle60_preAlpha_BoM.csv>` contains the Bill of Materials -- all the components for the PCB -- quoted in the LCSC site. It has all LCSC part numbers, quantities and descriptions. For exact instructions on how to order the components from LCSC using the sheet file, please see `this video <https://www.youtube.com/watch?v=eFgOC5_1VYU>`_.

If you don't want to order them from LCSC, the table below can be used.

.. Hint:: Please note that some items may be out of stock when you are ordering them. Feel free to edit the BOM (making sure to substitute the components for compatible ones) if you know what you are doing. Also don't hesitate to hit me up, if you don't feel confident to change the components, so I can redo the list with available components.

.. Attention:: If you don't have experience with electronic design, do not attemp to swap or change the components in this table. Doing so may hinder some features of the PCB and even inutilize it!


+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| Designator          | Package            | Quantity | Value                  | Manufacturer           | Manufacturer Part No. | LCSC Part No. |
+=====================+====================+==========+========================+========================+=======================+===============+
| L1                  |                    | 1        | ACM2012-900-2P-T002    | TDK                    | ACM2012-201-2P-T002   | C76572        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| RVDD1               | R1206              | 1        | R010 1%                |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| L3                  | L1210              | 1        | CMI322513U1R0KT        | Guangdong Fenghua      | CMI322513U1R0KT       | C99412        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| CB10,CB9,CSO1       | C0805              | 3        | 1µ                     |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| RL1                 | R1206              | 1        | 620R                   |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| DL1                 | D0603              | 1        | 19-217/R6C-AL1M2VY/3T  | Everlight Elec         | 19-217/R6C-AL1M2VY/3T | C72044        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| J1 :sup:`(1)`       |                    | 1        | TYPE-C-31-M-12         | Korean Hroparts Elec   | TYPE-C-31-M12         | C165948       |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| U1                  | LQFP-48 :sup:`(3)` | 1        | STM32F072CBT6          | STMicroelectronics     | STM32F072CBT6         | C81720        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| L2                  | L0603              | 1        | MGFL1608F1R0MT-LF      | Microgate              | MGFL1608F1R0MT-LF     | C281108       |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| DF1                 | SOD-123F           | 1        | SMF9.0CA               | Microdiode Electronics | SMF9.0CA              | C123799       |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| RSO1,RSI1,RRST1     | R1206              | 3        | 100k                   |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| RPU1                | R1206              | 1        | 1k5                    |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| D1-63, D65          | SOD-123F           | 64       | 1N4148WL               |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| CB1,CB4,CB6         | C0402              | 3        | 1µ                     |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| CB2,CB3,CB5,CB7,CB8 | C0402              | 5        | 100n                   |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| CRST1               | C0805              | 1        | 10µ                    |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| CRST2,CSH1,CSH2     | C0805              | 3        | 4n7                    |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| CSI1,CUSB1          | C0805              | 2        | 100n                   |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| DRST1               | SOD-123            | 1        | B0520LW-7-F            | Diodes Incorporated    | B0520LW-7-F           | C155367       |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| DS1,DSH1            | SOD-123            | 2        | RB060M-60TR            | ROHM Semiconductor     | RB060M-60TR           | C114257       |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| F1                  | F1812              | 1        | 1A trip PTC :sup:`(2)` | BOURNS                 | MF-MSMF050-2          | C17313        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| QRST1               | SOT-23             | 1        | DTC123JKAT146          | ROHM Semiconductor     | DTC123JKAT146         | C111724       |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| RCC1,RCC2           | R1206              | 2        | 5k1                    |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| RSH1,RSH2           | R1206              | 2        | 1M                     |                        |                       |               |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| SWRST1              | 5.2x5.2mm          | 1        | K2-1187SQ-A4SW-06      | Korean Hroparts        | K2-1187SQ-A4SW-06     | C92584        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| U2                  | SOT-23-6           | 1        | USBLC6-2SC6            | STMicroelectronics     | USBLC6-2SC6           | C7519         |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
| U3                  | SOT-23             | 1        | MCP1700T-3302E/TT      | Microchip Tech         | MCP1700T-3302E/TT     | C39051        |
+---------------------+--------------------+----------+------------------------+------------------------+-----------------------+---------------+
Notes on the BOM 
****************

**(1)** This connector seems to not be available in the european or american markets, only asian. It was chosen because, while being USBC, it has simplified pins and can easily be handsoldered. I have yet to find a good substitute for this connector that can be bought worldwide.

**(2)** Any fuse that fits the footprint will work, but I personally prefer polyfuses. Make sure that is has a minimum 1.5A trip current, as the LEDs and the high current microprocessor can sum 1A current easily.

**(3)** Since there are many versions of this MCU, please make sure that you order this exact package since the footprint will not support anything different than this.
