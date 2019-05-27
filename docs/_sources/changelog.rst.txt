.. raw:: html

    <style> .red {color:#f21717; font-weight:bold; font-size:16px} </style>

.. role:: red

.. raw:: html

    <style> .green {color:#009933; font-weight:bold; font-size:16px} </style>

.. role:: green

.. raw:: html

    <style> .blue {color:#1777f2; font-weight:bold; font-size:16px} </style>

.. role:: blue

.. raw:: html

    <style> .orange {color:#dc7633; font-weight:bold; font-size:16px} </style>

.. role:: orange

.. raw:: html

    <style> .pink {color:#cc00cc; font-weight:bold; font-size:16px} </style>

.. role:: pink

**************************************
How to read and write The Acheron Docs
**************************************

======================
Why keep documentation
======================

Documentation in hardware projects is classically scarce because, for a long time, the hardware designers did not know how to use version management software; this was mainly due to the fact that harware design was always tied to big corporations that held their own way of documenting cases, generally trough internal channels like engineering logs.

As time passes, free and open-source tools like KiCad and FreeCAD made hardware design affordable to hobbyists. Also hardware designers were pushed closer to software with the widespread of microcontroller prototype boards like the Arduino and Blue Pill, forcing hardware specialists to know how to write firmware --- putting them closer to the open-source software world. This taught hardware designers how important it is to keep documentation, and they borrowed some methods from the software community.

When it comes to hardware, documentation is important for basically three things:

- **Maintenance**. Documenting what has changed in the project goes a long way in keeping a record of the process and the knowledge gained throughout it. 
- **Licensing and code of conduct**. This is imperative for any Open-Source project.
- **Deployment**. The documentation is generally where the design and manufacuring files are released.

Each one is explained detailedly below.

Licensing, publishing and the code of conduct
---------------------------------------------

It is common for open-source projects to have a conde of conduct: a document that contains guidelines and rules for its participants to work together and make the project happen. While all condes of conduct do have "civility" clauses --- no harsh language, hate speech, demeanor towards fellow contributors or users, kindness and so on --- they will generally also contain general guidelines of contribution and approach to development. This will involve project-defining rules like who belong to which part of hardware, to technical stuff like the size of indenting and branching before committing.

Hence the code of conduct is generally a big part of a documentation in the sense that it guides the methods by which the team will cooperate and make it happen.

For the Acheron Project, the first basic rule is: **learn Git and how it works**. The methods I use to devise, deliver, publish and manage the Acheron Project were all based on the Git software. Technical details consist of basic rules and design constraints given primarily by the manufacturing capabilities of the PCB manufacturers. These constraints are blatantly stated in the design files and should be taken into consideration every time the contributor wishes to use the files.

Maintenance and the nature of hardware design
---------------------------------------------

Throughout the development of the Acheron Project, I found that the most critical part of the documentation (at least when it comes to hardware projects) is the Changelog. This boils down to two problems: the very nature of hardware design --- hardware will punish you for mistakes --- and because there is no specialized tool to deal with versioning in hardware design projects.

Hardware will punish you for mistakes means that design errors in hardware will generally take a toll of considerable amounts of money and time. Hardware is not as forgiving as software; whilst deploying and maintaining software (generally) does not incur prices, fees and times, when hardware is designed the prototyping process takes weeks because it includes manufature, shipping, assembly and testing time --- and every step incurs costs and timeframes. Also the prototyping process depends on a basic knowledge of the manufacturing process, assembly (soldering) skills, specialized tools and experience, and so on. This means that hardware testing generally follows an interactive process of changes and learning; a first-timer will take months to deploy a single functioning prototype, and even years for fairly sophisticated systems. This is what I generally call the "nature of hardware projects", a term to describe those particular difficulties in deploying hardware projects.

There is another critical part of keeping a Changelog. Since version management tools for software projects have existed for a long time, the software guys have devised a very clever way of keeping track of changes: the delta approach. For instance, when you deploy a piece of software to GitHub, it is able to show exactly which lines of code were changed, added or removed. But there is no tool that does the same thing for hardware projects; this means that while the delta approach is useful, it still needs to be done manually, that is, through a descriptive text that thoroughly describes the changes done. This cannot be done through the simple texts of git commits, and through the simple texts that the Markdown platform gives. Hence the need to keep a dedicated documentation of the whole project.

Deployment: prototyping and releasing
-------------------------------------

Because of the nature of hardware projects, the cycle of pre-releasing, prototyping and releasing is generally very well defined, inflexible and strict. A lot of care is taken for the words "functional", "ready", "commercial", "end version". There is no absolute way to guarantee a hardware design is functional, ready, or commercial if no prototypes were made and tested; in the same way, no feature is complete without proper prototyping.

The problem is that due to the nature of hardware design, deployment of such prototypes is costly and takes weeks to happen. This means that there is no way to properly design a hardware project without proper funding; in some cases the needed amounts figure in the hundreds of dollars.

In this regard, I take the issue very seriously. For every component of the Acheron Project there is an **Introduction** page where three badges are kept;

- **PCB Version** is the version of the master branch of the main repository; this badge is :blue:`blue` if that version is supposed to be a functional version and :red:`red` if not.
- **Prototype Version** is the version of the last prototype. This badge is :green:`green` if the last prototype was functional and fully tested and :orange:`orange` if the last prototype was ordered but not yet fully tested.
- **Firmware** can be "not available", "passing" or "not passing", describing the state of the firmware for the last prototype.

**Always** keep in mind that the only way to be certain that a particular version will work is if it was prototyped.

============================================
Using git and the purpose of the AcheronDocs
============================================

The Acheron Docs
----------------

When I first designed the KeebsPCB and the ArcticPCB --- the first boards of what would later become the Acheron Project --- I was very familiar with git and software versioning. Hence all the PCB versioning was done through git's commit system, wherein for each commit you write a simple sentence to describe the changes. Due to the nature of hardware project versioning described in the last section, these small texts were not enough to describe the changes involved. Also the deltas from a commit to another were shown in the form of he hard coded files, and not the parctical changes in the PCBs schematics or their modifications --- making it really harder to acknowledge those changes.

Hence I devised a structure to adapt the hardware design process to git:

- The changelog is written in PCB versions --- being them functional or not --- that describe a particular set of changes. Each version can contain more than one commit. The problem here is that since all changes must be detailedly specified, commits are not a satisfatory way to keep track of changes in hardware projects because their descriptions are supposed to be small texts. I also find it very hard to refer to changes by the commit hash, and prefer human-readable names that mean a particular version in a set timeframe.
- Adopting a codename and a versioning convention. What classifies a new version, sub-version and revision need to be really clear for the changelog to make sense. The adopted convention grew over time, and the final one can be read in the next section of this page (codenames_).
- Writing very detailed changelog, describing the changes and their reason in a manner such that each change is well-founded and clear.
- Writing an Open-Source Hardware license adapted to the mechanics of git (push-pull, commiting, pull requests and so on).

The Acheron Project documentation, which I later named the Acheron Docs, was a way of adapting the hardware design process to git, allowing for a steeper learning curve of hardware design both for me and whoever wishes to contribute to or use the project.

Facilitating readability
------------------------

In order for the user to have access to each version and state or test the changes made, each commit (version) will be labeled as a `git tag <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_ and the Changelog must contain the web address (link) to that particular tag. This feature makes the link between the documentation and the git repository, where the files are stored.

Writing good and clean changelog through tags
---------------------------------------------

The convention used for the changelogs is as follows. Each version has a significant change that should be commited; the changes were divided into three categories, earning colored tags.

Features
^^^^^^^^

The tag [:blue:`Feature`] **Means a new feature was added.** The feature and its qualities should be described, as well as its functionalities so that its addition is well-founded. A "feature" in a hardware project means a underlying or functional quality of the project that may or may not manifest as a fuctionality in the end product.

Updates
^^^^^^^
[:green:`Update`] **Means a previous feature was updated.** A change qualifies as an update if the past feature was not a bug, that is, it was completely funcional and not a problem or difficulty. Updates are generally improvements to the design. The description of an update must contain the problem with the past feature, why and how it was modified and how the final result improves upon the past implementation.

Fixes
^^^^^

[:red:`Fix`] **Means a bug was fixed.** Mind that hardware bugs are different from software bugs: hardware ones are generally design features that hinder funcionality or make deployment more difficult. For instance, a trace that was in the wrong pin is a bug because in all likelihood that trace will impossibilitate a functionality of the PCB. Bugs also may be features that are not designed wrongly, but badly --- for example a trace too thin or too close to a pad that makes it hard to manufacture. What differs a fix from an update is that, while a fix is the revision of faulty or bad design, updates are better implementations of a functioning design. A description of a bug fix must contain what the bug was, how it hindered functionality, how it was fixed and the pretended outcome of the new implementation.

The expression "throrough description" means accounting for changes in the lowest level possible, that is, trace and component-wise, citing which traces were changed (example: "the ones around component X or Y" or "the power lines for the microprocessor").

Releases and pre-releases
^^^^^^^^^^^^^^^^^^^^^^^^^

The deployment of a version follows a three-step process. First, if a certain version is intended as the target final release, it is flagged as :orange:`Pre-release`, prototypes are ordered and a greek letter codename is adopted to designate that pre-release; thence a tag for pre-releases was made:

- [:orange:`Pre-release`] **Means that a particular version was flagged as a pre-release.** This means that prototypes were ordered and tests are pending.

The prototypes are manufactured and sent to me or the PCB designer. Since prototypes are done in small quantities (2-5 units) it is generally the designer that assembles the board (solders all components into it) and builds the firmware. The prototype will induce new changes that will also be changelogged. If the changes were significant, a new prototype will be ordered; if they were minor, then the changes will be applied to the design only.

If the pre-release (modified or not) is deemed a fully-fledged completely working version, then it is released, inducing a new tag:

- [:pink:`Release`] **Means that the prototypes were tested and deemed functional.** Releases are denoted with greek letters (*ist est* "rev. Alpha").

.. _codenames:

========================
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

This process makes it easier to know if a change in versions was significant. It means that all commits have a version attached to them, making them easier to follow and their changes more understandable.
