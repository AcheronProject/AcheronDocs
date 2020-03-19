.. raw:: html

    <style> .red {color:#f21717; font-weight:bold; font-size:16px} </style>

.. role:: red

.. raw:: html

    <style> .green {color:#009933; font-weight:bold; font-size:16px} </style>

.. role:: green

.. raw:: html

    <style> .blue {color:#1777f2; font-weight:bold; font-size:16px} </style>

.. role:: blue

.. raw:: html

    <style> .orange {color:#dc7633; font-weight:bold; font-size:16px} </style>

.. role:: orange

.. raw:: html

    <style> .pink {color:#cc00cc; font-weight:bold; font-size:16px} </style>

.. role:: pink

*********
Changelog
*********

`V1.0 <http://github.com/Gondolindrim/ArcticPCB/releases/tag/V1>`_  :sub:`(02/28/2019)`
=======================================================================================

	- This verion can be found at its `release page <https://github.com/Gondolindrim/ArcticPCB/releases/tag/V1>`_. It was a preliminary version made for prototype and testing purposes; despite being functional, it had dimension issues and was absolutely not usable with any case. **Avoid using this version by all means**.

`pre-Release Alpha <http://github.com/Gondolindrim/ArcticPCB/releases/tag/pre-Alpha>`_  :sub:`(09/23/2019)`
===========================================================================================================

	- [:red:`Fix`] **Revised dimensions and mounting points**. PCB dimensions now fit a universal 60% case. Screw mounting points also fit these cases now.
	- [:green:`Update`] **New ARM MCU**. Changed used microprocessor from Atmega32U4 to STMicroelectronics STM32F072CBT6, which is faster, cheaper, smaller and has lots of flash memory.
	- [:blue:`Feature`] **USB Type C connector**. USB connector changed from USB mini to USB type C;
	- [:blue:`Feature`] **ESD protection**. USB data lines are now ESD protected with a dedicated chip. Voltage suppression is also available through a schottky diode on the USB power rails.
	- [:blue:`Feature`] **Case grounding and shield protection**. Metallic case is now grounded through the screw points. Connector shield is now grounded through a grounding snubber net.
	- [:blue:`Feature`] **Relief cuts**. "Relief" or "flex" cuts added to allow for more malleability, enhancing the "flex" sensation. These cuts consist on the removal of PCB material in strategic places, isolating vibrations on the PCB at specific spots, making a more pleasant typing experience.
	- [:blue:`Feature`] **Extra pins**. The unused PCB pins were broken out into header distances; they can further be used to enhance the PCB with more features.
	- [:blue:`Feature`] **In-System Programming SWD pins**. The pins used for the ARM MCU ISP, called SWD protcol, were broken out in the ARM 10-pin JTAG pattern. This allows for debugging and futureproofing, as the user can take total control of the MCU in case drastic measures are needed, such as re-programming the bootloader or erashing the EEPROM.
	- [:orange:`Pre-release`] **Pre-release Alpha**. The prototypes for this release were gracefully provided by PCBWay. The files can be checked at the release page in the title.

`Release Alpha <http://github.com/Gondolindrim/ArcticPCB/releases/tag/Alpha>`_  :sub:`(03/18/2019)`
===================================================================================================

	- [:red:`Fix`] **USB data lines swapped**. For some reason I swapped the D+ and D- in the pre-Alpha USB connector and had to make a little hack for them to work. The pins are now in their right positions and work just dandy.
	- [:red:`Fix`] **Split right shift keys swapped**. Also for some unknown reason I swapped the split right shift keys (1U Fn key and 1.75U RShift key); in the original Tsangan layout, the Fn key was at the right and RShift at the left, whereas Arctic pre-Alpha I did the opposite. I swapped these keys just now and the layout is correct.
	- [:green:`Update`] **Changed stabilizer orientation**. In pre-Alpha, the left Shift and Enter key stabilizers were both south-facing. This is not a problem *per se* --- since I tested the PCB with both C3 and original Cherry stabs and everything works fine; however the stab pieces and wires get close enough that I fear the stabs might collide in further versions of these stabs of with another manufacturer or brands. To make this less of an issue, I reverted the Enter key stab to north-facing so that the wires and pieces get some distance.
	- [:green:`Update`] **Split right shift keys connections**. In pre-Alpha, the Fn key and 1.75U RShift key for split right shift were connected; now the Fn key has its own single place in the switch matrix and the 2.75U RShift and 1.75U RShift keys are connected. This makes writing the firmware easier because a single key position is used for both RShift's, and a single file can contemplate single RShift and split RShift layouts, whereas in the pre-Alpha implementation (where Fn and 1.75RShift were connected) a file was needed for the default ANSI RShift and another one for split right shift.
	- [:pink:`Release`] **Release Alpha**. The pre-Alpha prototypes were modified according to this changelog and Alpha version was released. This version is completely functional with no hardware bugs.
