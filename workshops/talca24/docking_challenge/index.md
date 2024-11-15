---
permalink: /workshops/talca24/docking_challenge
layout: splash
classes: wide
title: "Docking Challenge"
---

<center><h1 style="margin-top:40px">Docking Challenge 🏆</h1></center>

<br>

<p align="center">
    <img style="height:350px;" src="docking_challenge/images/docking_challenge.jpg">
</p>

* table of contents
{:toc}


## 1. Introduction

**Integrative structure modeling** (ISM) computationally combines data from multiple sources of information with the aim of obtaining structural insights that are not revealed by any single approach alone ([Braitbard, Schneidman-Duhovny & Kalisman, 2019](https://doi.org/10.1146/annurev-biochem-013118-111429)).

With the aim of practicing and testing the ISM capabilities of the LightDock software, we propose the following challenge:

<center><h3>Are you ready to model the <em>molecular</em> completo mojado?</h3></center>


## 2. The challenge

We will model a ***molecular completo mojado*** by using a camelid nanobody-peptide complex as scaffold. The PDB of the complex is [6I2G](https://www.rcsb.org/3d-view/6I2G).

<p align="center">
    <img style="width:800px" src="docking_challenge/images/6i2g.png">
</p>

### 2.1. The bread: 🍞

We have prepared for you the scaffold receptor structure: [6i2g_nanobody.pdb](docking_challenge/data/6i2g_nanobody.pdb)

<p align="center">
    <img style="width:800px" src="docking_challenge/images/6i2g_nanobody.png">
</p>

### 2.2. The stuffing: 🥩🥬🍅

You will need to model a T-A-L-C-A peptide:

<p align="center">
    <img src="docking_challenge/images/talca_peptide.gif">
</p>

You may use [pyPept](https://github.com/Boehringer-Ingelheim/pyPept) Python package for building the peptide. Secondary structure is just a proposal!

If you don't manage to build the peptide, you may download the one we have already prepared: [talca_peptide.pdb](docking_challenge/data/talca_peptide.pdb)

### 2.3. The goal: 🌭

Is that a <em>completo</em>? Is it <em>mojado</em>? Oh, wait, it is our ***completo molecular mojado***!

<p align="center">
    <img style="width:800px" src="docking_challenge/images/challenge.png">
</p>

## 3. Tips & tricks

1️⃣ Blind docking will probably help since we are able to recover a similar interface ([see a simulation](https://server.lightdock.org/job/run/97308c2b7be4279d2283417e65ac5fde3761fb98fbc44b4087a8ebe5d1e112e7) we have prepared for you).

2️⃣ Docking simulations tend to maximize/minimize scoring functions by increasing the number of interactions. This usually favors larger binding interfaces, it might be the case for this challenge.

3️⃣ Residue restraints might definitely help to place our ligand in the good binding interface, but this is a totally new interaction compared to the native complex.

We have prepared a notebook ready to run on Google Colab. Have fun!

* [Talca24_LightDock_Completo_Mojado.ipynb](docking_challenge/data/Talca24_LightDock_Completo_Mojado.ipynb)