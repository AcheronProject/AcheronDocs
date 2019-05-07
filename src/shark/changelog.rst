*********
Changelog
*********

How to read the changelog
=========================

My commits follow a little convention I like to use. The commit messages are usually concise. I use tags to describe better what the commit is about:

- [Feature] Means a new feature was added
- [Update] Means a previous feature was improved or updated
- [Fix] Means a bug was fixed

V3.0
====

V3.0.1 :sub:`(01/12/2019)` 
----------------------------------

	- [Update] Started porting the version 2 from the ATMEGA32U4 processor to a more modern ARM Cortex M4 STM32F303CCT6 processor.

V3.0.2 :sub:`(01/13/2019)`
--------------------------

	- [Update] Added USBC connector.

V3.0.3 :sub:`(2019/01/14)`
--------------------------
	
	- [Feature] Added RGB underglow with the WS2812B.

V3.0.4 :sub:`(2019/01/15)`
--------------------------
	
	- [Update] Changed the grid used from the standard 19.05mm to the 19mm used in the Planck.

V3.0.5 :sub:`(2019/01/21)`
--------------------------

	- [Fix] Solved a problem with connector wiring and added a nice render to the README.

V3.0.6 :sub:`(2019/01/26)`
--------------------------
	
	- [Update] Changed components to SMD.

	- [Feature] Added Blender renders.

	- [Update] Updated preview.

V3.0.7 :sub:`(2019/02/13)`
--------------------------

	- [Feature] Added US and BR flags to the design.

	- [Update] Rounded corners to fit the Planck Low-Pro case (as suggestged by garbo from Geekhack).

	- [Update] Adjusted 3D models of crystal and Push Button.

V3.0.8 :sub:`(2019/02/20)`
--------------------------

	- [Feature] Added rotary encoder support.

V3.1
====

V3.1.1 :sub:`(2019/02/27)`
--------------------------
	
	- [Fix] Fixed a little problem with the Edge Cuts. Somehow for a reason only God knows KiCad messed up the starting and finish point coordinates of the lines and arcs in this layer. This has now been fixed manually. Really small (less than 5 mil) modifications were made on the edges of the PCB.

V3.1.2 :sub:`(2019/03/12)`
--------------------------

	- [Update] We incorporated some feedback we got from the IC and GB posts on GeekHack and Reddit:

	- [Update] A second position for the Rotary Encoder was added; some users noted that the previous position, bottom left, was where the arrow keys were located and as such this was an important position. So an extra possible position was added, the bottom right. The problem is that this position is where the CTRL key is located, and is also an important position. I deemed it was not worthy to add encoder positions on the top left or right corners, as those are the ESC and BKSPC keys, which are of utmost importance. So this means that it is up to the user where the rotary encoder goes: either bottom left or bottom right. Note that although both positions are offered, *the user must choose only one of them, that is, do not use two rotary encoder positions at the same time* as this will probably not work because both positions share the same microprocessor pins.

V3.1.3 :sub:`(2019/03/13)`
--------------------------

	- [Update] The switch plate cutout was revamped to allow users to take the switch top while the switch is mounted on the plate.

	- [Feature] Hi profile plates were added, as suggested by user sam278 from Geekhack.

	- [Feature] Added I2C communication pins, as suggested by user equalunique from Geekhack. The user can use the holes or solder a four-pin JST BM04B-ASRS-TF connector that is in the BOM. If the user does not want to buy the connector, he or she can use the THT pads right next to the connector pads.

V3.1.4 :sub:`(2019/03/16)`
--------------------------

	- [Update] The I2C connector was changed to a common 4-pin header.

	- [Feature] Added extra header pins for the remaining not used pins of the microcontroller. With these pins the user will be able to expand the keyboard by adding off-board devices.

V3.1.5 :sub:`(2019/03/19)`
--------------------------

	- [Feature] Some components, like the LDO and its network, as well as the reset network, were moved to the bottom layer to ensure no component would get in the way of the switches when mounting them.

V3.1.6 :sub:`(2019/03/21)`
--------------------------

	- [Update] Capacitor CVBus1, which was a 1uF 0406, was changed to 1uF 0805 to match the other CVBus'es.

	- [Update] The BOM had minor problems like components out of stock and incongruent information (e.g., 0805 resistors when they should be 1206). This has all been fixed and checked. Double checked. I dare you to find a problem. I double dare you, MFer.

V3.1.7 :sub:`(2019/05/07)`
--------------------------

	- [Update] The plate files were adjusted to fit the custom case.

	- [Fix] Added plate DXF files so that they can be ordered from a shop that does laser cutting and CNC. The first versions of these files, that were imported from KiCad directly, did not have any screw holes -- strange, yes. I fixed this by exporting the plate files to SVG, and from Inkscape exporting to AutoCad 14 DXF files, which worked. For this I used the Front Silkscreen layer, which is why in the plate KiCad files there are rings on these layers that coincide with the screw holes.
