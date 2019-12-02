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

V1.0
====

V1.0 :sub:`(10/05/2019)` 
----------------------------------

	- [:blue:`Feature`] **Initial version**. Initial version tagged.

`V1.1 <https://github.com/Gondolindrim/Austin/releases/tag/V1.1>`_ :sub:`(12/05/2019)`
--------------------------------------------------------------------------------------------

	- [:green:`Update`] **Toned down the Acheron Logo**. Maybe the Acheron logo was too big so we decide to tone it down a little bit.

	- [:green:`Update`] **Component footprints**. The U2 and U3 footprints were substituted for the Acheron Library SOT-23 and SOT-8 package footprints. These feature better markings to indicate which pin is the first and are optimized for manufacture.

	- [:green:`Update`] **Changed the LDO used**. The LDO used to converto the bus 5V into 3.3V for the microprocessor was the MCP1700-33; by the time of prototyping, it was not available on LCSC. I changed it for an LV1117-33, by Texas Instruments, which also features a better SOT-223 package.

`V1.2 <https://github.com/Gondolindrim/Austin/releases/tag/V1.2>`_ :sub:`(20/06/2019)`
--------------------------------------------------------------------------------------------

	- [:green:`Update`] **Plated Austin logo in the back**. Added a plated Ausin logo for the bling;
	
	- [:green:`Update`] **New 3D models**. New 3D models that contain the connector and all other components, for mechanical compliance checking.

`pre-Alpha <https://github.com/Gondolindrim/Austin/releases/tag/pre-Alpha>`_ :sub:`(29/06/2019)`
------------------------------------------------------------------------------------------------

	- [:green:`Update`] **Fixed courtyard problems.** The last version had some problems with the resistor placements. KiCad was not checking for courtyard crossings and some resistors came misplaced, to the point some of them would prevent some switches from correctly snapping into the PCB.

	- [:green:`Update`] **New label**. New plated label registering version.

	- [:green:`Update`] **Removed the split plus option**. There was a problem with the split plus options. This was because of two reasons:

		- To support split plus and LEDs, the 2U switch should be flipped 90 degrees so that the switch pads and LED pads would not superimpose. drifting decided that, for the sake of regularity, having a vertical switch should be better;
		
		- Not manyt people use the split plus;

	- [:green:`Update`] **Numpad plus rerouted.** Numpad plus was rerouted. Before, there were three switches to route differently; one was on row 3 (upper 1U switch) and two others (lower 1U and 2U switch) were on row 4. With the removal of the split option, the 2U switch was re-routed to row 3. 

	- [:red:`Fix`] **Silkscreen writings for he SWD pins.** In the last revision they were not rhere and that would surely be confusing. Markings were added to signal the pin functions.
		
	- [:orange:`Pre-release`] **Pre-release Alpha**. This version is the intended GB version and will be prototyped.

`Release Alpha <https://github.com/Gondolindrim/Austin/releases/tag/Alpha>`_ :sub:`(29/09/2019)`
------------------------------------------------------------------------------------------------

	- [:green:`Update`] **South facing stabilizers.** As 001anthony recommended in his stream, due to alignment and ease-of-maintenace reasons, the bottom space and numpad 0 stabs were changed to south-facing. To accomodate the stab holes, the PCB bottom edges were made a little bit further.

	- [:green:`Update`] **New silkscreen markings**. Some silkscreen markings were re-made to make building process further easier.

        - [:green:`Update`] **SWD pins reorganized**. The SWD pins are reorganized now to be compatible with SWD JTAG connectors.

        - [:pink:`Release`] **Alpha release**. This version is the final version that will be shipped with the boards. It has been prototyped, tested and its firmware built.
