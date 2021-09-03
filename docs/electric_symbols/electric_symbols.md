# Electrical Template Symbol Library

## Introduction

Electrical Templates is a symbol library used to make good-looking and uniformized electrical circuit schematics in a vectorized software. The original source is from Inkscape and all sources are developed in Inkscape SVG format which should be natively supported by most vector editors like Illustrator, CorelDRAW *et cetera*.

The main purpose of these symbols are to be freely available in a vectorized format so they can be modified, adapted, scaled and documented in any way needed. The tool used to draw and edit them is [Inkscape](https://inkscape.org/), a free and open-source vector editor.

## General information

- GitHub repository: [click here](https://github.com/AcheronProject/electrical_template)
- Status: actively maintained, under construction but usable
- Licensing: [modified BSD-3](https://github.com/AcheronProject/electrical_template/blob/main/LICENSE.md)

## Uses

This library was first intended for the writing of circuit and hardware design documentation, which needs thorough and detailed drawing of the schematics involved. The initial versions were used in the [Acheron project documentation, aka Acheron Docs](http://acheronproject.com). As such, the library can be used whenever detailed circuit schematic characteristics are needed:

- Software documentation, specially embedded firmware;
- Scientific papers and articles;
- Learning material, courseware

## Standards

This symbol library follows the [IEEE/ANSI standard 315-1975](https://standards.ieee.org/standard/315-1975.html) for its references as to how to draw the symbols.

Since the standard does not indicate grid or sizes, some liberties were taken to better reflect the symbols in the standard to digital form.

## Development conventions

In order to ensure scalability and reproductibility, certain aspects are enforced and uniformized throughout the symbols:

- Points use a 1mm grid with thicker lines at every 1cm. All points should snap to the grid. It is recommended to use grid-snapping;
- In order for the images to be compatible throughout all systems, the font used is *sans-serif* which is an open-source adaptation of Helvetica;
- Line thickess was kept as 1mm throughout symbols;
- All documents have four layers:
	- **Values** for values (in the case of passives, their nominal values like 10k Ohm or 100nF)
	- **Designators** for the designators (R1, C3, U3 etc)
	- **Anchors** for graphics anchors such as circle centers
	- **Drawings** for the drawings themselves

![Grid example](./readme/bjt_example_1.png)

![Grid example zoom](./readme/bjt_example_2.png)

In order to keep the grid fixed, the page size is set to A4 size and **should not be changed**, as doing so will move the grid and mess with the formatting of the symbols.

## How to use

If you want to add a component to your drawing, simply copy the drawing from the source file and paste into your circuit file or import the source file SVG. Avoid modifying the source drawings.

### How to deal with the layers

The layers are an important aspect of the symbols because they allow the user to hide and show important pieces of information like anchors, centers, image documentation. None of those will likely make it into the final image, but it is nonetheless important and useful to have them there for maintainability of the images later on. It is recommended that all objects in all layers be copied over to the final circuit; one can hide or un-hide certain layers to keep unwanted objects out of the final drawing.

### About anchors

Since these symbols are graphic tools first and foremost, there needs to be some graphical convention as to what is a symbol "center", so that the concepts of alignment and linkage can be understood. The anchors (red crosses in 0.5mm traces) are just that, conventions to what are the symbols "centers" as graphical reference points. It is highly recommended to keep the anchors fixed in their position relative to their symbols.

In most symbols the anchors are conveniently placed in notable points like geometrical centers. Nevertheless, all anchors are snapped to the 1mm grid and should be kept like that.

## Background colors

Some might find it easier to differentiate between parts of the circuit, or easier to visualize the circuit, if certain components are filled with a background color.

The colors used should be fairly light and translucent, so as not to diverge attention from the circuit itself. In ``./readme/example_background.svg`` there can be found several examples of such colors, used for this documentation, called "electric colors". These electric colors are given in RGBA or HEX codes as:

- Electric light blue: (0,180,250,40) or 0x00b4fa66;
- Electric dark blue: (0,0,250,50) or 0x0000ff80;
- Electric purple: (150,0,250,40) or 0x9600fa66;
- Electric pink: (250,0,100,50) or 0xfa006480;
- Electric green: (0,200,0,40) or 0x00x800066;
- Electric yellow: (250,180,0,50) or 0xfab40080.

The light and translucent nature of such colors is very well pictured in the image below, where they are used in an open-drain-output comparator which needs a transistor symbol internal to the amplifier symbol. Due to the light colors, it is easy to see the transistor.

![Background colors example](./readme/example_background.svg)

Additionally, for proper differentiation between circuits or functions, one might want to avoid using two close colors in the same schematic, like the light and dark blue colors or the purple and pink.

## Licensing

This library is licensed under a slightly modified BSD "three clause" license, which means it is free to use even commercially (credits are appreciated, however), but redistributions must follow the copyleft principle.
