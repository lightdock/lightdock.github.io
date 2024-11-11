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

### 2.1. The bread: 🍞

<p align="center">
    <img src="docking_challenge/images/bread.png">
</p>

### 2.2. The stuffing: 🥩🥬🍅

<p align="center">
    <img src="docking_challenge/images/stuffing.png">
</p>

### 2.3. The goal: 🌭

Is that a protein? Is that a star? No, it is the Turkish flag! 🇹🇷

<p align="center">
    <img src="docking_challenge/images/turkey_molecular_flag.gif">
</p>


## 3. Tips & tricks

1️⃣ Blind docking will probably not help a lot ([see a simulation](https://server.lightdock.org/job/run/d4431a1e054c43db83e1c2748b1f87a406dcec6f48d24bc3990fa650e607d843) we have prepared for you).

2️⃣ Docking simulations tend to maximize/minimize scoring functions by increasing the number of interactions. This usually favors larger binding interfaces, which is not the case for this challenge.

3️⃣ Residue restraints might definitely help to place our ligand in the good binding interface, but capturing this specific planar shape [is difficult](https://server.lightdock.org/job/run/8f6b5c739b6add17aa067a1a981395676a47650b928b454cb7daefe2cbce491e).

We have prepare two structures for you:

* <em>Bread</em> protein: [bread.pdb](docking_challenge/data/bread.pdb)

