**************************
Frequently Asked Questions
**************************

How do I know the designs are funcional and tested?
---------------------------------------------------

Each project in Acheron has an Introduction page, where are located three badges: PCB version, Prototype Version, and Firmware.

- PCB Version means the latest release or pre-release, which will probably be the current PCB version on the repository master branch;
- Prototype Version means the latest prototyped version;
- Firmware passing/not passing indicates if the current firmware works on the latest prototype.

.. Attention:: To stay on the safe side, for fabrication and commercial purposes, be sure to use the latest prototyped version, as I can endorse its proper functioning.

Will you profit from this project?
----------------------------------

I won't profit from it myself, although I may retain a little portion of the gains to fund further projects, that is, to maintain prototyping, components and overall design costs. A famous brazilian writer, Millôr Fernandes, once said: "never trust an idealist that profits from his ideals".

On the other hand, in order to make international GBs possible I will generally partner with a collaborator who of course permission to use the design commercially, so I'm not entitled to tell that collaboratorif he should profit and how much.

Nevertheless I will keep in close contact and it is, obviously, in the best interest of us (me and the collaborator) and the community that the prices are kept affordable and as low as possible.

Who is funding this project?
----------------------------

I am, with some collaborators. My *modus operandi* is generally this: a collaborator comes with an idea he wants me to try or design. I will make the design for free if the collaborator agrees to open-source the design; all I ask is that the collaborator pays for prototypes. If the collaborator does not wish to publish the design as open-source, I will ask for a small donation.

This is for two reasons. First is that parts and equipment availability in Brazil are limited, and I need some help for the prototypes. The small donation is used to fund my other projects, including the Acheron itself.

Can anyone contribute to this project?
--------------------------------------

Anyone is welcome to contribute, be it through feature requests, opinions or criticisms. This can be done through the GeekHack posts, issues and questions on GitHub or even through my Discord (#Gondolindrim#9738). If you want to actively contribute to the design, feel free to contact me and we'd be glad to have you. 

Why open-source?
----------------

As I don't intend to profit from this, there is no reason to keep the design closed. I also have the opportunity to contribute to the open-source way of thinking: many heads are better than one. Following these steps I use only open-source stuff to design the keyboards: the ECAD design is made with KiCad, the renders and animations in Blender, the logo design in Inkscape. All these software are run on Arch Linux, which is a Linux distro heavily based on the OSS and KISS principles.

By adopting free OSS tools any newbie makers can take a look and learn from these designs, that is, I also have an educational reason in mind. In this regard, I also have a transparency principle, that is, anyone in the community can contact me and ask questions about the project and the design decisions or the design process. Any maker can also check my designs and points its flaws.

Second, there is also the KISS (Keep It Simple, Stupid!) principle in mind. Since this project is completely un-ambicious, I try to keep it as simple as possible, so that the design and community processes are fluid.

And why publish the design under a share-alike license?
-------------------------------------------------------

This is to prevent any modifications to be closed-source, effectively nullifying the open-source principle of the Project.

What resources and software do you use?
---------------------------------------

All the footprints and symbols are available wither on the KiCad libraries or my MX library, which contains footprints and symbols for some components not available on KiCad.

The design, footprints and symbols are made through KiCad. The 3D models are obtained in sites where the content is free and widely available like 3D Content Central and GrabCad Community, and to edit them I use FreeCAD.

The logos were designed in Inkscape.

The Shark base image was taken from `this page <https://www.vectorportal.com/StockVectors/Animals/SHARK-ILLUSTRATION/15844.aspx>`_ (last access: 26 feb, 2019). Although stated in the Vector Portal site that the designs are freely available to be used in commercially, I tried to contact the uploader, who goes by the name of "Yohan Plantec" with no success.

The renders and animations are made in Blender.

The cases were designed in Fusion360.

Why not use Blender for the cases?
----------------------------------

The case was designed in Fusion360, which is not open-source but is freely available. I had a hard time with 3D modelling in Blender, specially because it was not designed to interact with CAD and parts manufacturing; for example, it does not output its files in the STEP format, which is a major problem since that is the standard file extension used in the industry. Ultimately, Blender was not designed for CAD and parts fabrication, but for graphical animations.

Fusion, on the other hand, was designed specifically for the manufacturing process, specially machining and 3D printing, so its features are much more part-oriented and less modelling-oriented.

Since Fusion is not open-source, I will always release the case files in three extensions: an F3D file (Fusion's proprietary file) along with STEP and STL files, which can be opened in any free modelling software like FreeCAD and Blender.

How can I follow your design process and learn from this project?
-----------------------------------------------------------------

I try to stream the design process when I can. I generally do it at tuesdays and thursdays at 3PM PST (8PM BRT). In the streams I answer general electronics questions, and show how the board is designed. I stream at my `Twitch channel <http://twitch.tv/gondolindrim_>`_. The past streams can be seen in my Youtube channel.
