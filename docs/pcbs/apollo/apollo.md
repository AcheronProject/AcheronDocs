<p style="text-align:center">
  <a href="https://github.com/Gondolindrim/Apollo87H"><img src="https://img.shields.io/badge/GitHub%20Repo-gray.svg?style=for-the-badge&logo=GitHub" height="100" /></a>
  <img src="https://img.shields.io/badge/Latest%20Release-87H%20Delta%20RC1-blue.svg?style=for-the-badge" height="100" />
  <img src="https://img.shields.io/badge/Status-Rev%20Delta%20under%20testing-green.svg?style=for-the-badge" height="100" />
</p>

# Apollo

<figure>
  <img src="../../../images/apollo/apollo_logo.svg" width="600" align="middle"/>
</figure>


---

## Introduction

The Apollo is a family of tenkeyless (TKL) keyboard Printed Circuit Boards (PCB) which main feature is the per-key RGB lighting. There are two default layouts available: 87 and 88. The name comes from the default TKL ANSI layout which has 87 keys; adding an F13 key we have the 88 key layout. From these two layouts, variants arise:

- 87H (short convention for 87 keys Hotswap), features an 87-key layout with Kailh hotswap sockets and supports a "default" TKL layout, that is, a 6.25 units spacebar, no split backspace or right shift, and ANSI-only enter;
- 87H-T-SC for 87 layout, "H" for hotswap sockets, "T" for "Tsangan bottom", and "SC" for stepped caps lock;
- 88H-T-SC for 88 layout, "H" for hotswap sockets, "T" for "Tsangan bottom", and "SC" for stepped caps lock;

## Technical information (release Delta)

- Layout size: tenkeykess (TKL)
- Compatible switches: MX-like only, features hotswap sockets
- Lighting: per-key RGB through SK6812 mini-E reverse-mounted intelligent integrated controlled LEDs
- Support for RGB daughterboard through 4-pin JST
- Microcontroller: Joker64 multi-chip ARM compatibility topology compatible with:
    - STM32F401
    - STM32F072
    - STM32F303
- Connector: detachable USB Type C on the top side and JST connector for daughterboard support
- Firmware compatibility: QMK (with VIA support)
- Protection hardware:
    - USB data lines and power rail ESD suppressing
    - USB power overvoltage protection
    - Enclosure grounding pad
    - Overcurrent protection
    - LDO crowbar diode
    - EMI suppression (shielding ferrite bead)
- Current release: Release Delta (under prototyping assembly and tests as of january 2022)
- Designer: Gondolindrim
- License: Acheron Open-Source Hardware License version 1.4

## Keyboard compatibility

## Known compatibilities

- **Geonworks F1-8X and F1-6X:** confirmed by Geon, who tested the PCB 3D files against the case 3D files; live testing into a machined case confirms compatibility.

### Known incompatibilities

- **ai03 KBD8X MKII**: ai03 open-sourced the PCB files for his KBD8X. Although Apollo's edges do fit inside the original PCB's, its connector is more protruded than the original PCB's.

- **PrismA18**: different layouts on the function row.

- **MONOKEI x Hand Engineering Kage**: cutouts on 88H-T-SC are slightly misaligned with the ones on Kage's MNK88-T. It is possible to file down the 88H-T-SC to fit, but this is strongly not recommended.

## Acknowledgements

- The first prototypes of this PCB (revision Alpha) were paid for and tested by KeebsForAll, who also intends to make units of this PCB available for purchase;

- Geon, from GeonWorks, spent time helping design this PCB to fit his keyboards and for his thousand-dollar contribution to the Acheron Project;

- Xelus, who kindly volunteered to help write the QMK firmware;

- tzarc, who helped develop the "Joker" template for multi-STM microcontroller support.

## Releases and history

The Apollo family begun its development with 87H, which was designed in four incarnations from revision Alpha to revision Delta. Once 87H rev. Delta was prototyped and proven working, the other versions followed.

### [87H Alpha-RC1](https://github.com/Gondolindrim/Apollo87H/releases/tag/pre-Alpha)

The release alpha was commission-designed for [KeebsForAll](https://keebsforall.com/); they agreed to finance the project and open-source it. This PCB was always supposed to be fairly basic, using SK6812-mini-E LEDs for the per-key LEDs. It does not support RGB underglow, removable USB connector or daughterboard.

### [87H Alpha-RC1](https://github.com/Gondolindrim/Apollo87H/releases/tag/v2.1.3%2Fv2.1.4)

Following the sucess of release Alpha, [Geon Works](https://geon.works/) also showed interest in Apollo to be used with his line of TKL keyboards; in this iteration, I decided to step it up a notch and rehaul the PCB with a more sophisticated IS31FL3741 RGB controller with common-anode RGB LEDs. This included the removable USBC connector, the RGB daughterboard support, USB daughterboard support and the "Apollo's head" logo.

Revision Beta was never prototyped; it is kept as an archive.

### [87H Gamma-RC1](https://github.com/Gondolindrim/Apollo87H/releases/tag/v3.1.23%2Fv3.1.20)

Mid-way through the prototyping stage of revision beta, factory Elecrow changed some of their manufacturing capabilities and enforced those upon Apollo. This meant that I had to completely redesign the PCB from the ground up using the new constraints.

Revision Gamma presents the same qualities and features as revision Beta but with new, more "manufacturable" constraints. Revision Gamma also features a [multi-STM-microcontroller design](../../../multimcu_article/multimcu_article) that allows for multiple STM32 parts to be used in the same design.

### [87H Delta-RC1](https://github.com/Gondolindrim/Apollo87H/releases/tag/delta-rc1) (under testing)

Revision Gamma, albeit following factory constraints, is not mass-manufacturable due to the shortage in silicon chips, mainly the ISSI RGB controller used. Revision Delta is being designed with the same constraints as Gamma, but using the SK6812 mini-E reverse-mounted intelligent RGB LEDs of revision Alpha and a 64-pin microcontroller topology due to the current shortage prices and availability constraints. Revision Delta will also feature a multi-STM-microcontroller design and all the features of revision Gamma (RGB and USB daughterboards support, removable USBC and so on).

### [87H-T-SC Alpha-RC1](https://github.com/Gondolindrim/Apollo87H-T-SC) (under development)

### [88H-T-SC Alpha-RC1](https://github.com/Gondolindrim/Apollo88H-T-SC) (under development)

## Copyright notice

This project is released under the [Acheron Open-Hardware License V1.4](../../AOHL14.md)

The "apollo sun face" logo was licensed through purchase from the EnvatoMarket website; the source file and licensing proof can be found in ``./resources/apollo_logo``. The license was obtained in march 27, 2021 and allows the AcheronProject to redistribute the logo as open-source and allows anyone to sell the PCBs commercially, but it does not allow for reproduction, meaning that if you want to use the logo for your designs or products you will have to buy a license yourself.

## Pictures (revision Delta, credits by Geon from Geon.Works)

<figure>
  <img src="../../../images/apollo/delta-pictures/delta1.jpeg" width="1000" align="middle"/>
</figure>

<figure>
  <img src="../../../images/apollo/delta-pictures/delta2.jpeg" width="1000" align="middle"/>
</figure>

<figure>
  <img src="../../../images/apollo/delta-pictures/delta3.jpeg" width="1000" align="middle"/>
</figure>

<figure>
  <img src="../../../images/apollo/delta-pictures/delta4.jpeg" width="1000" align="middle"/>
</figure>

<figure>
  <img src="../../../images/apollo/delta-pictures/delta5.jpeg" width="1000" align="middle"/>
</figure>

<figure>
  <img src="../../../images/apollo/delta-pictures/delta6.jpeg" width="1000" align="middle"/>
</figure>
