<p style="text-align:center">
  <a href="https://github.com/AcheronProject/Raphael"><img src="https://img.shields.io/badge/GitHub%20Repo-gray.svg?style=for-the-badge&logo=GitHub" height="100" /></a>
  <img src="https://img.shields.io/badge/Latest%20Release-Not%20yet%20released-red.svg?style=for-the-badge" height="100" />
  <img src="https://img.shields.io/badge/Status-Rev%20Alpha%20under%20prototyping-orange.svg?style=for-the-badge" height="100" />
</p>

# Raphael

<figure>
  <img src="../../../images/apollo/apollo_logo.svg" width="600" align="middle"/>
</figure>


---

## Introduction

The Raphael is a 60% PCB aimed at gummy mount applications like the Singa Unikorn and the Bakeneko. It features the common layouts in 60%s:

- Split backspace, right and left shifts
- ISO and ANSI enter
- 6.25 and 7 units spacebar

Below is an image of the supported layouts.

<figure>
  <img src="../../../images/raphael/raphael_kle.png" width="1000" align="middle"/>
</figure>

Additionally, Raphael also supports both on-board USB connector and a JST connector for USB daughterboard usage.

## Technical information

### Release Alpha
- Layout size: 60%
- Compatible switches: MX-like only, solderable
- Lighting: per-key single-color LEDs
- Microcontroller: [Joker48 multi-chip ARM compatibility topology](../../joker_mcus/joker.md)
- Connector: detachable USB Type C on the top side and JST connector for daughterboard support
- Firmware compatibility: QMK (with VIA support)
- Protection hardware:
    - USB data lines and power rail ESD suppressing
    - USB power overvoltage protection
    - Enclosure grounding pad
    - Overcurrent protection
    - LDO crowbar diode
    - EMI suppression (shielding ferrite bead)
- Designer: Gondolindrim
- License: Acheron Open-Source Hardware License version 1.4

## Keyboard compatibility

## Known compatibilities

- **Dark's ex-Visa**
- **Dark's Guga**

### Known incompatibilities

- **Any tray-mount** 60% cases like the TOFU, the TINA and the Klippe as Raphael does not feature screw holes.

## Acknowledgements

- Dark, who contributed with developing the outlines and tested the 3D files onto his keyboards models to see if they are fit.

## Releases and history

### [Alpha RC-1](https://github.com/Gondolindrim/Apollo87H/releases/tag/pre-Alpha)

The release alpha was made in efforts with Dark as supporting PCBs for his Guga and ex-Visa projects.

## Pictures (renders)

<figure>
  <img src="../../../images/raphael/raphael_alpha-rc1_renders.png" width="1000" align="middle"/>
</figure>
