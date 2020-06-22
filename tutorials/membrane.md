---
permalink: /tutorials/membrane
layout: splash
classes: wide

---

<center><h1>Membrane-associated protein docking</h1></center><br>

This is a complete example of the LightDock docking protocol to model the [2HDI](https://www.rcsb.org/structure/2hdi) membrane-associated protein system with the use of an **implicit membrane representation** provided by the [MemProtMD](http://memprotmd.bioch.ox.ac.uk/) database.

**IMPORTANT** Please, make sure that you have the <code>python3</code> version of LightDock installed (<code>pip3 install lightdock</code>). We advise you to follow the basic tutorial about how to run a quick [LightDock simulation](https://lightdock.org/tutorials/2UUY)

Here, we provide a complete *step-by-step* guide to model the interaction between the Colicin I receptor Cir (*beta*-barrel) in complex with receptor binding domain of Colicin Ia.

## 1. Copying the data
Create a directory and copy the sample data provided.

```bash
cd Desktop
mkdir test
cd test
curl -O https://raw.githubusercontent.com/haddocking/MemCplxDB/master/structures/2hdi/2hdi_unbound_A.pdb
curl -O https://raw.githubusercontent.com/haddocking/MemCplxDB/master/structures/2hdi/2hdi_unbound_B.pdb
curl -O https://raw.githubusercontent.com/lightdock/lightdock.github.io/master/tutorials/examples/2HDI/2hdi-coarsegrain.pdb
```

Where `2hdi_unbound_A.pdb` corresponds to the *beta*-barrel receptor structure, `2hdi_unbound_B.pdb` is the receptor binding domain and `2hdi-coarsegrain.pdb` the representative coarse-grained [snapshot](http://memprotmd.bioch.ox.ac.uk/_ref/PDB/2hdi/_sim/2hdi_default_dppc/) of the **2HDI** receptor.


## 2. Pre-processing of input structures
Next, we need to prepare the input structures.

1. Remove all CG beads except those representing the phospate beads

 ```bash
grep -v "C4B" 2hdi-coarsegrain.pdb | grep -v "C3B" | grep -v "C2B" | grep -v "C1B" | grep -v "C4A" | grep -v "C3A" | grep -v "C2A" | grep -v "C1A" | grep -v "GL2" | grep -v "GL1" | grep -v "NC3" >> 2hdi-phosphate.pdb
 ```

2. Remove all ions and water molecules since these are not parametrized in the scoring function

 ```bash
grep -v "ION" 2hdi-phosphate.pdb | grep -v " W " | grep -v "CONECT" >> 2hdi-phosphate-clean.pdb
 ```

3. Rename CG backbone beads to CA atoms in order to superimpose the atomistic structure

 ```bash
sed "s/B... /CA   /g" 2hdi-phosphate-clean.pdb | sed "s/5B.. /CA   /g" | sed "s/0BTN/CA  /g" | sed "s/0BEN/CA  /g" | sed "s/0BHN/CA  /g" >> 2hdi-phosphate-clean-CA.pdb
 ```

4. Rename phosphate beads

 ```bash
sed "s/ PO4/BJ /g" 2hdi-phosphate-clean-CA.pdb | sed "s/DPPC/ MMB /g" >> 2hdi-phosphate-clean-CA-BJ.pdb
 ```

5. Replace CG transmembrane domain by the atomistic one

 Open `2hdi_unbound_A.pdb` and `2hdi-phosphate-clean-CA-BJ.pdb` with [PyMol](https://pymol.org/2/) 

 ```bash
pymol 2hdi_unbound_A.pdb 2hdi-phosphate-clean-CA-BJ.pdb
 ```

 and run the following command:

 ```
align 2hdi_unbound_A and name CA, 2hdi-phosphate-clean-CA-BJ and name CA
 ```
 
 Now, do save each of the molecules as `2hdi_unbound_A_aligned.pdb` and `2hdi-phosphate-clean-CA-BJ_aligned.pdb` (PyMOL>File>Export Molecule...).

 **IMPORTANT**: Select the proper PDB file extension <code> PDB (*\.pdb *\pdb.gz) </code> <br>

 Finally, combine both files

 ```bash
grep -v "MMB" 2hdi-phosphate-clean-CA-BJ_aligned.pdb >> membrane.pdb
cat 2hdi_unbound_A_aligned.pdb membrane.pdb >> receptor_membrane.pdb
 ```

6. Remove all remaining files

 ```bash
rm 2hdi-phosphate.pdb 2hdi-phosphate-clean.pdb 2hdi-phosphate-clean-CA.pdb 2hdi-phosphate-clean-CA-BJ.pdb 2hdi_unbound_A_aligned.pdb 2hdi-phosphate-clean-CA-BJ_aligned.pdb membrane.pdb
 ```

An animation of the receptor embedded into the bead bilayer can be found below:

<p align="center">
  <img src="../assets/images/2hdi_membrane.gif">
</p>

## 3. Setup
First, we need to run the setup step. We will specify a number of 400 initial swarms and 200 glowworms. We will exclude the terminal oxygens and **ALL** hydrogens (not parametrized in `fastdfire` scoring function).

At this step we will enable the **membrane mode**. `(-membrane)`

```bash
lightdock3_setup.py receptor_membrane.pdb 2hdi_unbound_B.pdb 400 200 --noxt --noh -membrane

[lightdock_setup] INFO: Ignoring OXT atoms
[lightdock_setup] INFO: Ignoring Hydrogen atoms
[lightdock_setup] INFO: Reading structure from receptor_membrane.pdb PDB file...
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ARG.111
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue LYS.212
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ARG.643
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ASN.649
[lightdock_setup] INFO: 5155 atoms, 1056 residues read.
[lightdock_setup] INFO: Ignoring OXT atoms
[lightdock_setup] INFO: Ignoring Hydrogen atoms
[lightdock_setup] INFO: Reading structure from 2hdi_unbound_B.pdb PDB file...
[lightdock_setup] INFO: 810 atoms, 103 residues read.
[lightdock_setup] INFO: Calculating reference points for receptor receptor_membrane.pdb...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Calculating reference points for ligand 2hdi_unbound_B.pdb...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Saving processed structure to PDB file...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Saving processed structure to PDB file...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Calculating starting positions...
[lightdock_setup] INFO: Generated 115 positions files
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Number of swarms is 115 after applying restraints
[lightdock_setup] INFO: Preparing environment
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: LightDock setup OK
```

At first glance, we see that the initial number of specified swarms (400) has been reduced to 115. This means that 285 swarms have been removed as they are incompatible with the topological information provided by the membrane.

Please note, that while we have not specified any residue restraint for the current example, the **membrane mode** `(-membrane)` is totally compatible with this feature. For more info, please check our [antibody](https://lightdock.org/tutorials/4G6M) example.

An animation of the `setup`, with the geometrical centers of the `swarms` depicted in blue, can be found below:

<p align="center">
  <img src="../assets/images/2hdi_setup.gif">
</p>
