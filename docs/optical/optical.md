# On the design of hardware and software for optical switches

*It's time custom keyboards use optical switches*

**By Gondolindrim**

**First version** published in may 5, 2022

---

## Introduction

The Alexandria Library is the symbol, footprint and 3D models library used on the Acheron Project, its printed circuit boards and documentation. This library is developed using a mixture of some originally-developed footprints and 3D models as well as some others obtained from other places.

### Supported software

Due to the open-source nature of Acheron and Alexandria, its libraries are developed with sole [KiCAD](https://www.kicad.org/) support. As of september 2021, Alexandria is developed using the developmental "nightly" versions of KiCAD; this is because, as part of the version 6.xx roadmap, the KiCAD developers decided to revisit file formats and the library system, which in turn forces Alexandria to comply to the new formats for future-proofing reasons.

This means that in order to use these symbols and footprints **you must update your KiCAD to the latest nightly release**. Since I (Gondolindrim) compile and update KiCAD daily directly from its [official development repository](https://gitlab.com/kicad), always assume the latest version is in use.

For discussion see [this GitHub issue](https://github.com/AcheronProject/AlexandriaLibrary/issues/11).

## Repository list

### [Custom keyboard switches](alexandria_switches.md)

Alexandria Library offers a wide variety of switch footprints, including support for MX, Alps, SMK and electrocapacitive switches.

## How to use

### Git usage

### KiCAD library management

### Show support

## How to contribute

## Acknowledgements

## License

Being a library, it does not make sense to license Alexandria under AOHL since it requires licensees to also open-source derivative works. Hence, Alexandria is released under a much more permissive BSD 3-clause which only requires users to have the same notice in case of redistribution.

*Copyright (c) 2019, Álvaro Augusto Volpato. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer;
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution;
- Neither the name of the nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.*
