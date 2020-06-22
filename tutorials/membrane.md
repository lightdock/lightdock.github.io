---
permalink: /tutorials/membrane
layout: splash
classes: wide

---

<center><h1>Membrane-associated protein docking</h1></center><br>

This is a complete example of the LightDock docking protocol to model the [2HDI](https://www.rcsb.org/structure/2hdi) membrane-associated protein system with the use of an **implicit membrane representation** provided by the [MemProtMD](http://memprotmd.bioch.ox.ac.uk/) database.

**IMPORTANT** Please, make sure that you have the <code>python3</code> version of LightDock installed (<code>pip3 install lightdock</code>). We advise you to follow the basic tutorial about how to run a quick [LightDock simulation](https://lightdock.org/tutorials/2UUY)

Here, we provide a complete *step-by-step* guide to model the interaction between the Colicin I receptor Cir (*beta*-barrel) in complex with receptor binding domain of Colicin Ia.

## Copying the data
Create a directory and copy the sample data provided.

```bash
$ cd Desktop
$ mkdir test
$ cd test
wget https://raw.githubusercontent.com/haddocking/MemCplxDB/master/structures/2hdi/2hdi_unbound_A.pdb
wget https://raw.githubusercontent.com/haddocking/MemCplxDB/master/structures/2hdi/2hdi_unbound_B.pdb
wget https://raw.githubusercontent.com/lightdock/lightdock.github.io/master/tutorials/examples/2HDI/2hdi-coarsegrain.pdb
```

Where *2hdi_unbound_A.pdb* corresponds to the *beta*-barrel receptor structure, *2hdi_unbound_B.pdb* is the receptor binding domain and *2hdi-coarsegrain.pdb* the representative coarse-grained [snapshot](http://memprotmd.bioch.ox.ac.uk/_ref/PDB/2hdi/_sim/2hdi_default_dppc/) of the 2HDI receptor.

## Pre-processing of input structures
Next, we need to prepare the input structures.

- (1) Remove all CG beads except those representing the phospate beads

```bash
$ grep -v "C4B" 2hdi-coarsegrain.pdb | grep -v "C3B" | grep -v "C2B" | grep -v "C1B" | grep -v "C4A" | grep -v "C3A" | grep -v "C2A" | grep -v "C1A" | grep -v "GL2" | grep -v "GL1" | grep -v "NC3" >> 2hdi-phosphate.pdb
```

- (2) Remove all ions and water molecules since these are not parametrized in the scoring function

```bash
$ grep -v "ION" 2hdi-phosphate.pdb | grep -v " W " | grep -v "CONECT" >> 2hdi-phosphate-clean.pdb
```

- (3) Rename CG backbone beads to CA atoms in order to superimpose the atomistic structure

```bash
$ sed "s/B... /CA   /g" 2hdi-phosphate-clean.pdb | sed "s/5B.. /CA   /g" | sed "s/0BTN/CA  /g" | sed "s/0BEN/CA  /g" | sed "s/0BHN/CA  /g" >> 2hdi-phosphate-clean-CA.pdb
```

- (4) Rename phosphate beads

```bash
$ sed "s/ PO4/BJ /g" 2hdi-phosphate-clean-CA.pdb | sed "s/DPPC/ MMB /g >> 2hdi-phosphate-clean-CA-BJ.pdb
```

- (5) Replace CG transmembrane domain by the atomistic one

Open *2hdi_unbound_A.pdb* and *2hdi-phosphate-clean-CA-BJ.pdb* with [PyMol](https://pymol.org/2/) and run the following command <br>
<code> align 2hdi_unbound_A and name CA, 2hdi-phosphate-clean-CA-BJ and name CA </code> <br> <br>
Now, do save both molecules as *2hdi_unbound_A_aligned.pdb* and *2hdi-phosphate-clean-CA-BJ_aligned.pdb* to combine both files

```bash
$ grep -v "MMB" 2hdi-phosphate-clean-CA-BJ_aligned.pdb >> membrane.pdb
$ cat 2hdi_unbound_A_aligned.pdb membrane.pdb >> receptor_membrane.pdb
```

- (6) Remove all remaining files

```bash
$ rm 2hdi-phosphate.pdb 2hdi-phosphate-clean.pdb 2hdi-phosphate-clean-CA.pdb 2hdi-phosphate-clean-CA-BJ.pdb 2hdi_unbound_A_aligned.pdb 2hdi-phosphate-clean-CA-BJ_aligned.pdb membrane.pdb
```
