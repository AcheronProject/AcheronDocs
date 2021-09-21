<p style="text-align:center">
  <a href="https://github.com/Gondolindrim/Apollo87H"><img src="https://img.shields.io/badge/GitHub%20Repo-gray.svg?style=for-the-badge&logo=GitHub" height="100" /></a>
  <img src="https://img.shields.io/badge/Latest%20Release-Pre%20Release%20Gamma-blue.svg?style=for-the-badge" height="100" />
  <img src="https://img.shields.io/badge/Status-Rev%20Delta%20under%20development-green.svg?style=for-the-badge" height="100" />
</p>

# Apollo87H



<figure>
  <img src="../../../images/apollo/apollo_logo.svg" width="600" align="middle"/>
</figure>


---

## Introduction

Apollo is a tenkeyless (TKL) keyboard Printed Circuit Board (PCB) which main feature is the per-key RGB lighting. This particular variant, 87H (short convention for 87 keys Hotswap), features an 87-key layout with Kailh hotswap sockets and supports a "default" TKL layout, that is, a 6.25 units spacebar, no split backspace or right shift, and ANSI-only enter.

## Technical information (release Gamma)

- Layout size: tenkeykess (TKL)
- Compatible switches: MX-like only, features hotswap sockets
- Lighting: per-key RGB through IS31FL3741A intelligent chip and common-annode RGB LEDs
- Support for WS2812 RGB underglow through 4-pin JST
- Microcontroller: multi-chip ARM compatibility including:
    - STM32F411 (CEU6/CET6)
    - STM32F401 (CEU6/CET6)
    - STM32F072 (CBT6/C8T6/CBU6/C8U6)
    - STM32F303 (CBT6/CBU6/CCT6/C8T6/C6T6)
- Connector: detachable USB Type C on the top side and JST connector for daughterboard support
- Firmware compatibility: QMK (with VIA support)
- Protection hardware:
    - USB data lines and power rail ESD suppressing
    - USB power overvoltage protection
    - Enclosure grounding pad
    - Overcurrent protection
    - LDO crowbar diode
    - EMI suppression (shielding ferrite bead)
- Current release: pre-release Gamma (has not been prototyped yet)
- Designer: Gondolindrim
- License: Acheron Open-Source Hardware License version 1.3

## Preliminary renders

<figure>
  <img src="../../../images/apollo/apollo87h_gamma_renders.png" width="1000" align="middle"/>
</figure>

## Keyboard compatibility

## Known compatibilities

- **Geonworks F1-8X and F1-6X:** confirmed by Geon, who tested the PCB 3D files against the case 3D files; live testing into a machined case confirms compatibility.

### Known incompatibilities

- **ai03 KBD8X MKII**: ai03 open-sourced the PCB files for his KBD8X. Although Apollo's edges do fit inside the original PCB's, its connector is more protruded then the original PCB's.

- **PrismA18**: different layouts on the function row.

## Acknowledgements

- The first prototypes of this PCB (revision Alpha) were paid for and tested by KeebsForAll, who also intends to make units of this PCB available for purchase;

- Geon, from GeonWorks, spent time helping design this PCB to fit his keyboards and for his thousand-dollar contribution to the Acheron Project;

- Xelus, who kindly volunteered to help write the QMK firmware;

- tzarc, who helped develop the "Joker" template for multi-STM microcontroller support.

## Releases and history

### [Alpha](https://github.com/Gondolindrim/Apollo87H/releases/tag/pre-Alpha)

The release alpha was commission-designed for [KeebsForAll](https://keebsforall.com/); they agreed to finance the project and open-source it. This PCB was always supposed to be fairly basic, using SK6812-mini-E LEDs for the per-key LEDs. It does not support RGB underglow, removable USB connector or daughterboard.

### [Beta](https://github.com/Gondolindrim/Apollo87H/releases/tag/v2.1.3%2Fv2.1.4)

Following the sucess of release Alpha, [Geon Works](https://geon.works/) also showed interest in Apollo to be used with his line of TKL keyboards; in this iteration, I decided to step it up a notch and rehaul the PCB with a more sophisticated IS31FL3741 RGB controller with common-anode RGB LEDs. This included the removable USBC connector, the RGB daughterboard support, USB daughterboard support and the "Apollo's head" logo.

Revision Beta was never prototyped; it is kept as an archive.

### [Gamma](https://github.com/Gondolindrim/Apollo87H/releases/tag/v3.1.23%2Fv3.1.20)

Mid-way through the prototyping stage of revision beta, factory Elecrow changed some of their manufacturing capabilities and enforced those upon Apollo. This meant that I had to completely redesign the PCB from the ground up using the new constraints.

Revision Gamma presents the same qualities and features as revision Beta but with new, more "manufacturable" constraints. Revision Gamma also features a [multi-STM-microcontroller design](../../../multimcu_article/multimcu_article) that allows for multiple STM32 parts to be used in the same design.

### Delta (under development)

Revision Gamma, albeit following factory constraints, is not mass-manufacturable due to the shortage in silicon chips, mainly the ISSI RGB controller used. Revision Delta is being designed with the same constraints as Gamma, but using the SK6812 mini-E reverse-mounted intelligent RGB LEDs of revision Alpha. Revision Delta will also feature the multi-STM-microcontroller design and all the features of revision Gamma (RGB and USB daughterboards support, removable USBC and so on).

## Copyright notice

This project is released under the [Acheron Open-Hardware License V1.4](../../../AOHL14.md)

The "apollo sun face" logo was licensed through purchase from the EnvatoMarket website; the source file and licensing proof can be found in ``./resources/apollo_logo``. The license was obtained in march 27, 2021 and allows the AcheronProject to redistribute the logo as open-source and allows anyone to sell the PCBs commercially, but it does not allow for reproduction, meaning that if you want to use the logo for your designs or products you will have to buy a license yourself.
