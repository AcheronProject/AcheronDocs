.. figure:: images/acheronLong.svg

********
Overview
********

Introduction
============

The **Acheron Project** is a compendium of ECAD and MCAD resources for custom keyboards and audio equipment designed by Álvaro "Gondolindrim" Volpato with collaborators (except for some 3D models), that include

- Printed Circuit Boards (PCBs);

- KiCad footprints and symbols;

- Graphic resources like logos;

- 3D models

The aim of the project is to build a database of freely available resources for keyboard enthusiasts and audiophiles, focused primarily on PCBs that comply with Open-Source Hardware principles. Many features, characteristics, components are community-driven and feedback is highly appreciated.

Codenames and versioning
========================

Keyboard codenames
------------------

	Although each board has a codename to which it is commonly referred, each board in the Acheron project has a standard naming which comprises seven characteristics, which summarize each board's main features:

1. **Size**. The board size in percentage or abbreviation, e.g., 40, 50, 75, 100, WKL, (E) for ergo, (S) for split.

2. **Layout type**: staggered (S) or ortho (O).

3. **Microprocessor mounting type**. This is to differentiate between the "skeleton-type" boards I design, based on the Nori and the Gherkin. These usually use a THT platform (like the Proton C or the Pro Micro) and the components used (like diodes and LED resistors) are generally all THT. In this case, use a (TH) for "through hole". If otherwise, that is, the board has a surface-mounted microprocessor (which usually means SMD components) use (SM) for "suface-mount".

4. **Switch type:** can be (MX) for MX switches and clones, (AL) for alps switches, (KC) for kailh choc. This identifier can be a double; for instance, if the board supports both MX and Alps, use (MX/AL).

5. **Switch mount type:** hotswap (HS) or through-hole (TH).

6. **Wired**: if the keyboard is wired, use (WI). If it is a Bluetooth, use (BT).

Versioning
----------

	This naming system serves two purposes. First is identifying the boards in the Acheron Project, given that each board is a project on its own.

	Second is that these rules give us a criterion on when a change is a full version change or simply a minor revision. For example, the SharkPCB V3.1 (Acheron 40-O-STM32-MX-HS-WI) goes from MX support switches to MX-Alps compatible. Then this new Alps-compatible board will be V4.0.

	If, however, a change to the board did not change any of these listed parameters, than the sub-version changes. For example, again, if the SharkPCB V3.1 had a minor change to routing or edges, than the new version will be V3.2.

	Finally, if a minor change was made -- say one of the component silkscreen designators were changed, then the sub-subversion was changed, like going from V3.1.0 to V3.1.1.

	This process makes it easier to know if a change in versions was significant. It means that all commits have a version attached to them, making them easier to follow.

Project contributors
====================

- Raphael "BlindJoker" Nepomuceno

- Felipe "MrKeebs" Coury

- Raphael "ArcticFox" Hochheim

How to reach Gondolindrim
=========================

You can hit me up at:

- Email: ``alvaro.augusto.volpato@gmail.com``
- Discord: ``Gondolindrim#9738``
- reddit: ``u/gondolindrim_``
- Geekhack: ``Gondolindrim``

Feel free to ask me questions and interact!

About this documentation
========================

This documentation was built using Sphinx and the ReadTheDocs theme. The source files can be found at the Acheron Project `Github repository <https://github.com/Gondolindrim/AcheronProject>`_.

	The idea behind writing this documentation came from the other collaborators, not me particularly. Truth is I have never imagined that the Acheron Project and its components grew big enough for other people to use it, and hence I needed to document the design process.
