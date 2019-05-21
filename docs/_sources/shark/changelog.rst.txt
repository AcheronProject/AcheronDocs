.. raw:: html

    <style> .red {color:#f21717; font-weight:bold; font-size:16px} </style>

.. role:: red

.. raw:: html

    <style> .green {color:#009933; font-weight:bold; font-size:16px} </style>

.. role:: green

.. raw:: html

    <style> .blue {color:#1777f2; font-weight:bold; font-size:16px} </style>

.. role:: blue



*********
Changelog
*********

How to read the changelog
=========================

My commits follow a little convention I like to use. The commit messages are usually concise. I use tags to describe better what the commit is about:

- [:blue:`Feature`] Means a new feature was added
- [:green:`Update`] Means a previous feature was improved or updated
- [:red:`Fix`] Means a bug was fixed


----

V3.0
====

V3.0.1 :sub:`(01/12/2019)` 
----------------------------------

	- [:green:`Update`] **Started MCU porting**. Started porting the version 2 from the ATMEGA32U4 processor to a more modern ARM Cortex M4 STM32F303CCT6 processor.

V3.0.2 :sub:`(01/13/2019)`
--------------------------

	- [:green:`Update`] **Added USBC connector.**

V3.0.3 :sub:`(2019/01/14)`
--------------------------
	
	- [:blue:`Feature`] **Added RGB underglow**.

V3.0.4 :sub:`(2019/01/15)`
--------------------------
	
	- [:green:`Update`] **Changed grid**. Changed the grid used from the standard 19.05mm to the 19mm used in the Planck.

V3.0.5 :sub:`(2019/01/21)`
--------------------------

	- [:red:`Fix`] **Fixed wiring**. Solved a problem with connector wiring and added a nice render to the README.

V3.0.6 :sub:`(2019/01/26)`
--------------------------
	
	- [:green:`Update`] **Changed components to SMD.**

	- [:blue:`Feature`] **Added Blender renders.**

	- [:green:`Update`] **Updated preview.**

V3.0.7 :sub:`(2019/02/13)`
--------------------------

	- [:blue:`Feature`] **Added US and BR flags to the design.**

	- [:green:`Update`] **Corner radius were made larger**.

	- [:green:`Update`] **Adjusted models**. Adjusted 3D models of crystal and Push Button.

----

V3.1
====

V3.1.0 :sub:`(2019/02/20)`
--------------------------

	- [:blue:`Feature`] **Added rotary encoder support.**

V3.1.1 :sub:`(2019/02/27)`
--------------------------
	
	- [:red:`Fix`] **Fixed EdgeCuts problem**. Fixed a little problem with the Edge Cuts. Somehow for a reason only God knows KiCad messed up the starting and finish point coordinates of the lines and arcs in this layer. This has now been fixed manually. Really small (less than 5 mil) modifications were made on the edges of the PCB.

V3.1.2 :sub:`(2019/03/12)`
--------------------------

	- [:green:`Update`] **Incorporated feedback**. We incorporated some feedback we got from the IC and GB posts on GeekHack and Reddit.

	- [:green:`Update`] **Added second position for the encoder**. A second position for the Rotary Encoder was added; some users noted that the previous position, bottom left, was where the arrow keys were located and as such this was an important position. So an extra possible position was added, the bottom right. The problem is that this position is where the CTRL key is located, and is also an important position. I deemed it was not worthy to add encoder positions on the top left or right corners, as those are the ESC and BKSPC keys, which are of utmost importance. So this means that it is up to the user where the rotary encoder goes: either bottom left or bottom right. Note that although both positions are offered, *the user must choose only one of them, that is, do not use two rotary encoder positions at the same time* as this will probably not work because both positions share the same microprocessor pins.

V3.1.3 :sub:`(2019/03/13)`
--------------------------

	- [:green:`Update`] **New switch plate cutout**. The switch plate cutout was revamped to allow users to take the switch top while the switch is mounted on the plate.

	- [:blue:`Feature`] **Added I2C pins.** Added I2C communication pins, as suggested by user equalunique from Geekhack. The user can use the holes or solder a four-pin JST BM04B-ASRS-TF connector that is in the BOM. If the user does not want to buy the connector, he or she can use the THT pads right next to the connector pads.

V3.1.4 :sub:`(2019/03/16)`
--------------------------

	- [:green:`Update`] **Changed the connector of I2C pins.** The I2C connector was changed to a common 4-pin header.

	- [:blue:`Feature`] **Broken out more pins.** Added extra header pins for the remaining not used pins of the microcontroller. With these pins the user will be able to expand the keyboard by adding off-board devices.

V3.1.5 :sub:`(2019/03/19)`
--------------------------

`V3.1.5 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.1.5>`_ :sub:`(2019/03/19)`
--------------------------------------------------------------------------------------------

	- [:blue:`Feature`] **Moved some components to the bottom layer**. Some components, like the LDO and its network, as well as the reset network, were moved to the bottom layer to ensure no component would get in the way of the switches when mounting them.

V3.1.6 :sub:`(2019/03/21)`
--------------------------

	- [:green:`Update`] **Changed package of some capacitors**. Capacitor CVBus1, which was a 1uF 0406, was changed to 1uF 0805 to match the other CVBus'es. Now all capacitors are 0805 packages, and all resistors are 1206.

	- [:red:`Fix`] **Fixed problems in the BOM**. The BOM had minor problems like components out of stock and incongruent information (e.g., 0805 resistors when they should be 1206). This has all been fixed and checked. Double checked. I dare you to find a problem. I double dare you, MFer.

V3.1.6 :sub:`(2019/05/07)`
--------------------------

	- [:green:`Update`] **Adjusted plate files**. The plate files were adjusted to fit the custom case.

	- [:green:`Update`] **Added plate DXF files.** Added plate DXF files so that they can be ordered from a shop that does laser cutting and CNC. The first versions of these files, that were imported from KiCad directly, did not have any screw holes -- strange, yes. I fixed this by exporting the plate files to SVG, and from Inkscape exporting to AutoCad 14 DXF files, which worked. For this I used the Front Silkscreen layer, which is why in the plate KiCad files there are rings on these layers that coincide with the screw holes.

V3.1.6 :sub:`(2019/05/09)`
--------------------------

	- [:red:`Fix`] **Fixe problems with plate files**. The plate files had a problem where the middle hole was 4mm wide, when it should be 2mm. This was fixed.

	- [:red:`Fix`] **Fixed issues with cases**. The case files also had two issues.

		- First, the USB cutouts were wide enough to acomodate some connectors, but not wide enough to accomodade the wider connectors. The cutouts were made wider and taller to accomodate those big connectors.

		- Second, the SharkPCB has a little protrusion to support the USB connector, but the SharkPCB USB cutout was not tall enough to acocomodade that protrusion; this was such that the protrusion touched the case, making the PCB and the plate not align perfectly on the mounting holes. This was fixed making the USB cutout taller to accomodate for the protrusion.

`V3.1.7 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.1.7>`_ :sub:`(2019/05/09)`
--------------------------------------------------------------------------------------------

	- [:green:`Update`] **Enlarged case pegs**. The mounting pegs for the PCB and plates were made larger in both cases. The PCB pegs are now 6mm wide and the plate pegs are 5mm (they were 4mm wide, both). This was done after some mechanical stress simulations were done, and I found 5mm to be the best radius for the plate pegs. 

	- [:green:`Update`] **Enlarged PCB peg holes**. Following the wider pegs in the case, the PCB has three holes for these mounting pegs of the plates. Such holes were made larger - they had 2.8mm radius and now have 3mm. This was done in order to free up space so the pegs can be made wider.

`V3.1.7 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.1.7>`_ :sub:`(2019/05/09)`
--------------------------------------------------------------------------------------------

	- [:green:`Update`] **Larger case fillets**. I changed the fillets of the USB cutouts of both cases to 1.5mm. This was done because, according to the manufacturer, the cutout was deep and a 1mm radius was difficult to machine. In order to make those fillets larger, the cutout was also needed to be made a little larger: 1mm for each dimension.

----

V3.2
====

`V3.2.0 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.2.0>`_ :sub:`(2019/10/19)`
--------------------------------------------------------------------------------------------

Although technically the modifications for this version do not qualify as a new sub-version, the changes were too big to consider them part of the V3.1 series. This is why this new series jumped to V3.2 .

	- [:green:`Update`] **Tracing overhaul**. There was a general overhaul of the tracing.

		- First, around the microprocessor. There were too many dangerous traces, specially near the power pins, that were now removed. This does not mean the previous versions would not work, but it does mean they could be more prone to fabrication defects, specially due to fabrication tolerances;

		- Second, around the USB connector. Through hard lessons I learned that one should not trust the solder mask as electrical isolator. The problem was that there were too many traces under the USB connector, presenting potential short-circuits. All those were removed and re-routed outside the connector.

	- [:green:`Update`] **Reassigned of some cols and rows in the MCU**. In order to make possible the re-routing around the microprocessor, some columns and rows were reassigned in the microcontroller:

		- Row2 and Row1 exchanged places: Row2 was reassigned from pin 39 to pin 38, and Row1 vice-versa;
		- EncA and EncB were respectively moved to pins 42 and 43, from 41 and 20;
		- Col12 was moved from pin 34 to pin 19; pin 34 is SWDIO and should not be attached to row or column to allow for SWD;
		- Col7 and Col8 exchanged places: Col7 was reassigned to pin 14 from 15, and Col8 vice-versa;
	
	- [:blue:`Feature`] **Exposed SWD pins**. Even though the STM32F303 being used does have a stock USB DFU bootloader, I took some advice from **pelrun** and exposed the SWD pins anyway. This is done as a backup plan should the user mess up the bootloader and need to reflash it. Pins BOOT0 and NRST were also exposed, just in case they are needed. In order to expose these pins, RGB5 had to be slightly moved.

	- [:green:`Update`] **Renamed some components for clarity**. The CVBus capacitors were renamed to CVB, for clarity. Also C1 and C2 were renamed to CX1 and CX2 to denote they are XTAL load capacitors;

	- [:blue:`Feature`] **Re-implemented ESD inrush current protection**. Incorporated case ESD current inrush protection. This was for three motives:

		- In previous versions, the case ESD problem was dealt with by means of a dedicated pad that should be connected to the case via a wire. Then I realized that, being this PCB supposed to be used with tray mount devices, the case and PCB were galvanically conected by the screws, so instead of the dedicated pin I neded only use one of the mounting pads. So I simply connected the ESD discharge net to one of those pads;

		- There was a small problem with my past implementation. The ESD net was directly connected to GND, meaning that current could come from the USB connector to the case, provoking an electrical shock to the user. This was dealt with by adding a 1N4007 diode, blocking current from the USB to the case, but allowing the other way around. The choice of component was because this diode has high peak rush current and high reverse voltage -- the most needed qualities when ESD is concerned. Nevertheless this diode has two problems. First is it is slow, meaning that, theoretically, in the case of an ESD discharge, the high voltage could spread to the PCB as the diode would not be able to absorb it in time. This should be mitigated by isolating the mounting pads, which are the sites of galvanic connection, from any copper traces. This was done by adding a 1 mm clearance to all those mounting pads. The second problem with the 1N4007 is that it has a rather high forward voltage when compared to more sophisticated alternatives like Schottky diodes. However this may not be a problem, as in an ESD discharge event, involved voltages will most certainly figure among the tenths of volts, if not more, so this problem would not be such a concern. Further testing is required.

		- The past implementation also relied on the ground plane to deliver the unwanted inrush current to its proper destination -- the USB connector. The problem here is that, in the way the ground copper pour was configured, that inrush current would most certainly need to pass through the microcontroller, which could fry it. The ESD testings in the V3.1.1 prototypes did not yield any damage to the chip, meaning that this hypothetical event is possible but not certain, but it is better to avoid this problem. The new implementation deals with this by delivering the inrush current directly at the connector, avoiding that such current pass through delicate components.

	- [:green:`Update`] **New logo!**. The old Acheron logo was replaced for the newer one.

`V3.2.1 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.2.1>`_ :sub:`(2019/10/20)`
--------------------------------------------------------------------------------------------

	- [:red:`Fix`] **Fixed potential problems in the reset network**. The reset network used had two issues, pointed out by **ishtob**.

		- First, the CRST capacitor, which was rated 4.7nF, should actually be 10uF. This problem would cause the high voltage not to be held for long enough, most probably causing a issue in the prototypes where the reset pin needed to be pressed several times before the microcontroller would finally achieve bootloader mode.

		- Second, the transistor used, BC548, did not have a base resistor to bias it. Although it worked fine in the prototypes, this causes a too high of a current on the base-emitter junction, which would probably deteriorate the transistor over time. To fix this two options were available: either insert a discrete resistor between the transistor base and the push button, or use a "self-bias" transistor package, that is, a package that contained a transistor with a resistive net (including a resistor on the base). The latter solution was the one adopted, replacing the BC548 for a DTC123J self-bias transistor.

`V3.2.2 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.2.2>`_ :sub:`(2019/10/21)`
--------------------------------------------------------------------------------------------

	- [:green:`Update`] **Changed some texts for readability**. Some silkscreen texts were changed for more clarity. In the latest prototype (V3.1.6), I used the height value of 0.5mm for the silkscreen character height, which was readable in my opinion but not for Steve -- reasonably so. All sikscreen text charaters now should be at least 0.6mm tall and more readable.

	- [:green:`Update`] **Re-positioned RGB5**. The positioning of RGB5 was changed. It was slightly off-centered in version V3.2.0 to accomodate the pins for SWD, BOOT0 and NRST. The LED was now put in its original place, because I realized the pins can be accessed via wires should the user need.

`V3.2.3 <https://github.com/Gondolindrim/SharkPCB/releases/tag/V3.2.3>`_ :sub:`(2019/10/21)`
--------------------------------------------------------------------------------------------

	- [:red:`Fix`] **Fixed DRC "errors"**. When I run the DRC (Design Rule Check) on KiCad, lots of errors pop out. Those are normally due to overlapping holes and pads -- a consequence of the multi-layout support, as the holes and pads of close switches will inevitably overlap. The problem is that, this time around, more than 200 error popped out, the majority of them being "Parallel lines being too close" and "Two tracks end too close". It is a known issue in KiCad that when a trace is "broken", that is, composed of many traces, these errors will appear. I knew this, but it had never happened to me. There's a first time to everything I guess. So I redid all traces that had this problem. This is more of an :blue:`Update` than a fix, because the traces were fine as they were, but I wanted to remove those errors and check them one by one because you never know -- some of them could actually be legitimate errors.
