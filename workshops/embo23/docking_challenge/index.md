---
permalink: /workshops/embo23/docking_challenge
layout: splash
classes: wide
title: "Docking Challenge"
---

<center><h1 style="margin-top:40px">Docking Challenge 🏆</h1></center>

<br>

<p align="center">
    <img style="height:350px;" src="docking_challenge/images/docking_challenge.png">
</p>

* table of contents
{:toc}


## 1. Introduction

**Integrative structure modeling** (ISM) computationally combines data from multiple sources of information with the aim of obtaining structural insights that are not revealed by any single approach alone ([Braitbard, Schneidman-Duhovny & Kalisman, 2019](https://doi.org/10.1146/annurev-biochem-013118-111429)).

With the aim of practicing and testing the ISM capabilities of the LightDock software, we propose the following challenge:

<center><h3>Are you ready to model the <em>molecular</em> Turkish 🇹🇷 flag?</h3></center>


## 2. The challenge


### 2.1. The moon ☾

For the first component, we got inspired by the *[Say it with proteins: an alphabet of crystal structures](https://www.nature.com/articles/nsmb.3011)* article. We found a C-shaped protein a good candidate to model the moon on the Turkish flag.

The crystal structure of the porcine ribonuclease inhibitor (PDB code: [2bnh](https://www.rcsb.org/3d-view/2bnh)) will be the receptor on our docking simulations. We have already prepared the structure for you, ready to use in LightDock: [TUR.pdb](docking_challenge/data/TUR.pdb).

<p align="center">
    <img src="docking_challenge/images/2bnh.png">
</p>


### 2.2. The star ☆

The second component is a ⭐-shaped molecule that we built, without any biological context or chemical validation. Indeed, we are pretty sure that it would explode in any serious modeling software. But we are here just for the fun and the glory 🏴‍☠️!

The structure ready to use in LightDock can be downloaded here: [KEY.pdb](docking_challenge/data/KEY.pdb).

<p align="center">
    <img style="height:450px;" src="docking_challenge/images/star.png">
</p>

Any coincidence with Patrick 𓇼 from SpongeBob is that, just a coincidence.


### 2.3. The goal 🇹🇷

Is that a protein? Is that a star? No, it is the Turkish flag! 🇹🇷

<p align="center">
    <img src="docking_challenge/images/turkey_molecular_flag.gif">
</p>


## 3. Tips & tricks

1️⃣ Blind docking will probably not help a lot ([see a simulation](https://server.lightdock.org/job/run/d4431a1e054c43db83e1c2748b1f87a406dcec6f48d24bc3990fa650e607d843) we have prepared for you).

2️⃣ Docking simulations tend to maximize/minimize scoring functions by increasing the number of interactions. This usually favors larger binding interfaces, which is not the case for this challenge.

3️⃣ Residue restraints might definitely help to place our ligand in the good binding interface, but capturing this specific planar shape [is difficult](https://server.lightdock.org/job/run/8f6b5c739b6add17aa067a1a981395676a47650b928b454cb7daefe2cbce491e).

4️⃣ Adding a fake bead membrane might really help. See a simulation [here](https://server.lightdock.org/job/run/414b89a1bfcb60eff1557ccfc207315ad77b9834464d40aca3b071f8663db785).

<p align="center">
    <img src="docking_challenge/images/complex_mmb_beads.gif">
</p>

We have prepare two structures for you:

* C-shaped protein prepared to be used in [Membranator](https://server.lightdock.org/membranator): [TUR2.pdb](docking_challenge/data/TUR2.pdb)
* C-shaped protein with a fake membrane: [TUR3.pdb](docking_challenge/data/TUR3.pdb)
