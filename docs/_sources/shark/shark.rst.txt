|pcbBadge|
|protoBadge|
|firmwareBadge|

.. figure:: ../images/shark.svg

************
Introduction
************

Overview
========

The SharkPCB was conceived as an alternative 40% ortho keyboard that could be easily built and sold in difficult-to-reach markets like Brazil. 

When I was some years into the Mechanical Keyboard hobby, I wanted to try a 40% ortho layout. Unfortunately none were available in the Brazilian market; the Planck was (and still is) pretty much the only option in the market when it comes to that layout, and it was only available in the US market and EU through Massdrop.

Due to the proxy prices, PayPal fees and importing taxes, I would not be able to get a Planck since I simply did not have the money. So I set myself to design a keyboard that I could easily build and customize. My idea was to use a Blue Pill breakout board, using simple THT components for diodes and resistors.

In the next weeks, Steve from WoodCables came along and funded the project. We made a little revision of the design plan as a default SMD-component based PCB was needed to compete on the market. And thus Shark was born.

The name comes from a dear friend of mine, Gustavo, who at the time did not have a nickname. I suggested the nickname "Shark" because he used a shark image for his avatar; after much thinking, he decided to adopt the Undecided Shark alias, from whence the Shark PCB was named.

Features
========

The SharkPCB is a freely available, open-source 40% keyboard Printed Circuit Board (PCB) supporting three layouts: full grid, 1x2U spacebar and 2x2U spacebar. All resources and software used to design this board are open-source and/or freely available.

Here's a list of the board's features:

- ARM Cortex M4-based STM32F303 processor;

- QMK firmware compatible;

- USBC type connector;

- RGB underglow through intelligent integrated controller WS2812B LEDs;

- Three layout support: full-grid (FG), 1 centered spacebar (1S) and double spacebar (2S);

- Rotary encoder support;

- Hardware reset through a push button and reset network;

- Overcurrent and overvoltage input protection through a fuse and schottky diode;

- Electrical Static Discharge (ESD) protection through a discharge net.

Additionally, plate gerber files are also available so that the user can order them made from the same manufacturer as the PCBs and out of the same material (FR4, a fiberglass enhanced resin laminate). This makes production cheaper and faster.

There are four plate designs available: one for each supported layout and a universal one that supports all three of them.

The idea to make a Open-Sourcea Hardware compliant board was that it could be widely customizable from the start, so anyone could take a SharkPCB, give their thoughts, feedback and even modify it to their liking. It was designed for that purpose.

In that sense, the Shark uses an STM32 microprocessor that can be programmed in many ways, be it through the QMK firmware, Arduino IDE or any ensemble of software able to flash an STM32.

Also, following the customizable principle, all unused pins were exposed so that the user can add anything hardware-wise he or she wishes.

.. |pcbBadge| image:: https://img.shields.io/badge/PCB%20Version-3.2.5-blue.svg?style=flat
.. |protoBadge| image:: https://img.shields.io/badge/Prototype%20Version-3.2.4-orange.svg?style=flat
.. |firmwareBadge| image:: https://img.shields.io/badge/Firmware-not%20available-inactive.svg?style=flat
