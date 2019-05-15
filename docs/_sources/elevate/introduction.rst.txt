************
Introduction
************

History
=======

	The Elevate is a joint project between me (Gondolindrim), MrKeebs and Tesletron from Framework; I am the PCB designer, MrKeebs is the runner and Tesletron the case designer. Although the case is not open-source, I really wanted to open-source the PCB so I could improve it for next revisions with feedback from the community.

	My intention with this board is to make a Bluetooth keyboard 

	The keyboard consists of a 50% bluetooth board, supporting three layouts, among them a split spacebar.

Here's a list of the board's features:

- AVR ATMEGA32U4 processor;

- QMK firmware compatible;

- USBC type connector;

- RGB underglow through intelligent integrated controller WS2812B LEDs;

- Three layout support:

- Hardware reset through a push button and reset network;

- Overcurrent and overvoltage input protection through a fuse and schottky diode;

- Case Electrical Static Discharge (ESD) protection through a discharge net;

- ESD protection for the USB connection -- GND, VCC and data pins.

- 4-bit DIP switch:

	- Battery on/off control;

	- Bluetooth on/off control;
	
	- Keyboard on/off control;

	- And a bit connected to the MCU for programmability (changing layouts, for example);

- Bluetooth through a MDBT40 module;

- In switch LEDs;

- Three status indicator LEDs: battery, bluetooth and VCC.
