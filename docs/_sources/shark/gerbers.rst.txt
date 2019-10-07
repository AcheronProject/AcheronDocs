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

+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| Designator               | Package            | Quantity | Value                        | LCSC part number | Manufacturer        | Manufacturer Part No. |
+==========================+====================+==========+==============================+==================+=====================+=======================+
| RCC2, RCC1               | 1206               | 2        | 5.1k                         | C352054          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| Q1                       | SOIC-8             | 1        | AO4406AL                     | C35349           | Alpha Omega Semicon | AO4406AL              |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| DRST1,D1-48              | SOD-123            | 49       | 1N4148W                      | C181134          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| DESD1, DLDO1             | SOD-123            | 2        | 1N4007W                      | C108803          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RGB1-8                   | 5050               | 8        | WS2812B                      | C114585          | Worldsemi           | WS2812B               |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RSH1,RESD1               | 1206               | 2        | 1M                           | C308486          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RDP1,RDM1                | 1206               | 2        | 22R                          | C17958           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RPU1                     | 1206               | 1        | 1.5k                         | C212489          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RPG1,RA1,RA2,RB1,RB2     | 1206               | 5        | 10k                          | C328409          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RRST1                    | 1206               | 1        | 100k                         | C212480          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RSG1                     | 1206               | 1        | 100R                         | C319959          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| RL1-48                   | 1206               | 48       | 360R                         | C25376           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| DF1                      | SOD-123            | 1        | RB060M-60TR                  | C114257          | ROHM Semicon        | RB060M-60TR           |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| SRST1                    | SPST-NO            | 1        | K2-1187SQ-A4SW-06            | C92584           | Korean Hroparts     | K2-1187SQ-A4SW-06     |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CX2,CX1                  | 0805               | 2        | 22p                          | C1804            |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CSH1,CESD1,CRST2,CUSB1   | 0805               | 4        | 4.7n                         | C77063           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| F1 :sup:`(3)`            | 0805               | 1        | 1.5A trip PTC fuse           | C20979           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CRST1                    | 0805               | 1        | 10u                          | C15850           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CSI1,CSO1,CVB1,CVB2,CVB3 | 0805               | 5        | 100n                         | C111492          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CVB5,CB1,CA1             | 0805               | 3        | 10n                          | C58456           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| U2                       | SOT-23             | 1        | MCP1700-3302E                | C39051           | Microchip Tech      | MCP1700T-3302E/TT     |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| QRST1                    | SOT-23             | 1        | DTC123JKAT146                | C111724          | ROHM Semicon        | DTC123JKAT146         |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CVB4                     | 0805               | 1        | 1u                           | C141772          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| CVB6                     | 0805               | 1        | 4.7u                         | C37818           |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| J1                       |                    | 1        | TYPE-C-31-M12                | C165948          | Korean Hroparts     | TYPE-C-31-M12         |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| U1                       | LQFP-48 :sup:`(2)` | 1        | STM32F303CCT6                | C81523           | ST Microelectronics | STM32F303CCT6         |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| Y1                       | 5032 4Pin          | 1        | 8MHz                         | C251594          |                     |                       |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| U3                       | SOT-23-6           | 1        | USBLC6-2SC6                  | C7519            | STMicroelectronics  | USBLC6-2SC6           |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+
| ROT1, ROT2               |                    | 1        | ALPS EC11E15244G1 :sup:`(1)` | C370970          | ALPS Electric       | EC11E15244G1          |
+--------------------------+--------------------+----------+------------------------------+------------------+---------------------+-----------------------+

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
