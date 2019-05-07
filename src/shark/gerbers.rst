************
Gerber files
************

In the ``./gerbers`` folders you can find the plot files for the PCB and the plates.

PCB Gerber files
----------------

:download:`This zipped folder <https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/SharkPCB.zip>` contains the Gerber files for the last (V3.1.6) PCB version. Among them are probably more files than needed, including the files for the PCB edges and drill files.

.. Attention:: The `SharkPCB introduction page <./shark.html>`_ contains badges to show the last prototyped version of the PCB. I will release un-prototyped Gerbers in order to prototype them. Always check if the version you are downloading was prototyped!

Plates Gerber and vector files
------------------------------

The gerbers folder also contains the plot files for the plates of both tall and short cases. There are basically two kinds of files for the plates: Gerbers and vectorized. 

Just to save on notation, "high plate" designates the plate for the tall (high-profile) case; the same goes for "short plate".

- The Gerber files are used to order plates in the very same way as you would a PCB. This is awesome because you can cheaply order plates made from FR4 (the same material as the PCBs).

- The vectorized files are more general files that can be used to order plates in all sorts of materials, as the machining shops don't use Gerbers. The aluminum plates offered in the group buys were ordered with these very same files. These shops usually use AutoCad ``*.dxf`` files, which can be downloaded below. The problem is that AutoCad is not open-source nor free, so I also offer ``*.svg`` files that can be used with Inkscape.

+---------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|  		|  **Gerber**												|	**.dxf** 											| **.svg**												|					
+---------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+	
|**High**	| :download:`Download<https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/highPlate.zip>`	| :download:`Download<https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/highPlate.dxf>`	| :download:`Download<https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/highPlate.svg>`	|
+---------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|**Low**	| :download:`Download<https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/lowPlate.zip>`	| :download:`Download<https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/lowPlate.dxf>`	| :download:`Download<https://github.com/Gondolindrim/SharkPCB/raw/master/gerbers/lowPlate.svg>`	|
+---------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
