|pcbBadge|
|protoBadge|
|firmwareBadge|

.. figure:: images/faraday_logo.svg
        :align: center
        :width: 600px

************
Introduction
************

Overview
========

The Faraday PCB was conceived as a take on the Topre swiches for keyboards from the Acheron Project. Topre custom PCBs are pretty much nonexistant in this hobby (apart from some initiatives here and there); this is mainly due to the complicated and difficult to handle capacitive switch technology.

Topre switches work basically by measuring the capacitance difference of a spring-loaded rubber dome system. In this regard, it has always boggled me on how the Leopold FC660C, Realforce and HHKB Pro keyboards implemented the capacitor sensing technology, through a rather complicated and overly sophisticated multiplexation circuitry. The FaradayPCB instead uses an analog capacitance-to-voltage (C2V) analog sensing circuitry, which is detailedly explained in the `principle section <section_>`_ .

Current state
=============

The Faraday60 is still under development and is not yet released. The simulations are stil being perfected and the sensing circuitry designed. However, one-off prototypes of the switches were already made and the system is proven to work; there were some implementation flaws, however.

The roadmap for this first version is to be an HHKB Pro 2 replacement PCB. This will also include a replacement for the USB hub daughterboard that the HHKB has. In its first intended stage, the Faraday60 will feature a USB mini-B connector, no bluetooth connection, and a USB2.0 hub. The main feature, however, is integrating QMK compatibility with the famous electrocapacitive Topre switches.

Pages
=====

The initial IC page for the Faraday60 was made in a `GeekHack post <https://geekhack.org/index.php?topic=105035>`_ . Some feedback from the community was taken and suggestions ensued. After this IC, the design was revamped in some of its features.

As of may 2020 there is still no way to obtain a Faraday PCB.

Contributors
============

- Upas, from CannonKeys, who helped immensely by giving feedback and tips for this PCB.

.. _section : principle.html

.. |pcbBadge| image:: https://img.shields.io/badge/PCB%20Version-Not%20AvailableAlpha-gray.svg?style=flat
.. |protoBadge| image:: https://img.shields.io/badge/Prototype%20Version-Not%20Available-gray.svg?style=flat
.. |firmwareBadge| image:: https://img.shields.io/badge/Firmware-Not%20Available-gray.svg?style=flat
