---
permalink: /tutorials/0.9.1/dna_docking
layout: splash
classes: wide
title: "Protein-DNA Docking"
---

<center><h1 style="margin-top:40px">Protein-DNA docking prediction</h1></center><br>

* table of contents
{:toc}

This is a complete example of the LightDock docking protocol to model the [1AZP](https://www.rcsb.org/structure/1azp) protein-DNA complex with the use of **residue restraints**.

<br>

<p align="center">
    <img src="dna_docking/1azp.png">
</p>


## 1. Copying the data

Create a directory and copy the sample data provided.

```bash
mkdir 1azp
cd 1azp
curl -O https://raw.githubusercontent.com/lightdock/lightdock.github.io/master/tutorials/0.9.1/dna_docking/data/1AZP_A.pdb
curl -O https://raw.githubusercontent.com/lightdock/lightdock.github.io/master/tutorials/0.9.1/dna_docking/data/1AZP_B.pdb
```

## 2. Specifying residue restraints

LightDock is able to use information derived from either experimental information and/or bioinformatic predictions to drive the docking at several levels. This information is used in the form of **residue restraints**.

To do it so, we first need to create a `restraints.list` file. For the sake of simplicity, we will use a list of residue restraints (3) already formatted for you:

```bash
curl -O https://raw.githubusercontent.com/lightdock/lightdock.github.io/master/tutorials/0.9.1/dna_docking/data/restraints.list
```

The file `restraints.list` contains three residue restrains on the receptor (protein partner):

```
R A.TRP.24
R A.VAL.26
R A.ARG.42
```

Residue restraints might also be defined at the nucleic ligand level.
{: .notice--info}

**NOTE** For a detailed description of the exact implications of ACTIVE and PASSIVE restraints in LightDock, please refer to [LightDock goes information-driven](https://doi.org/10.1093/bioinformatics/btz642).
{: .notice--warning}

## 3. Protonation

### 3.1. Protein
First of all, we need the protein partner to have the correct hydrogen atoms as parametrized in our `dna` scoring function (`dna` scoring function is based in the AMBER94 force-field). To do it so, we will use the software `reduce` which can be downloaded from [GitHub](https://github.com/rlabduke/reduce).

We remove the previous hydrogens and them rebuild them according to reduce.

```bash
reduce -Trim 1AZP_A.pdb > 1AZP_A_noh.pdb
reduce -BUILD 1AZP_A_noh.pdb > 1AZP_A_h.pdb
```

We have renumbered the atoms of the protein receptor partner using the PDB-Tools ([web server](https://bianca.science.uu.nl/pdbtools/) or [Python Package](https://github.com/haddocking/pdb-tools/)):

```bash
pdb_reatom 1AZP_A_h.pdb > protein.pdb
```

You can find this file already generated for you here: [protein.pdb](data/protein.pdb)


### 3.2. DNA
We do the same as in previous section for the DNA partner (ligand):

```bash
reduce -Trim 1AZP_B.pdb > 1AZP_B_noh.pdb
reduce -BUILD 1AZP_B_noh.pdb > 1AZP_B_h.pdb
```

The problem is that hydrogen atoms produced by `reduce` for nucleic acids are not 100% name-compatible with the AMBER94 force-field. We have prepared a simple Python script to rename and/or remove incompatible atom types: [reduce_to_amber.py](data/reduce_to_amber.py)

You can execute it on the previous `reduce` output:

```bash
./reduce_to_amber.py 1AZP_B_h.pdb dna.pdb
```

This script is not covering at the moment all the non-compatible hydrogen atoms, but you can easily adapt it to your needs. **For an exhaustive list of atoms supported by the `dna` scoring function check this file: [amber.py](https://github.com/lightdock/lightdock/blob/master/lightdock/scoring/dna/data/amber.py)**

Finally, we provide the DNA PDB structure ready for LightDock here: [dna.pdb](data/dna.pdb)


## 4. Setup

First, we need to run the setup step. We will leave the number of swarms and glowworms by default, but we will enable the flexibility and use restraints:

```bash
lightdock3_setup.py protein.pdb dna.pdb -anm -rst restraints.list
```

You will see an output similar to this:
```
@> ProDy is configured: verbosity='none'
[lightdock3_setup] INFO: Reading structure from protein.pdb PDB file...
[lightdock3_setup] INFO: 1094 atoms, 66 residues read.
[lightdock3_setup] INFO: Reading structure from dna.pdb PDB file...
[lightdock3_setup] INFO: 506 atoms, 16 residues read.
[lightdock3_setup] INFO: Calculating reference points for receptor protein.pdb...
[lightdock3_setup] INFO: Reference points for receptor found, skipping
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Calculating reference points for ligand dna.pdb...
[lightdock3_setup] INFO: Reference points for ligand found, skipping
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Saving processed structure to PDB file...
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Saving processed structure to PDB file...
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Calculating ANM for receptor molecule...
[lightdock3_setup] INFO: 10 normal modes calculated
[lightdock3_setup] INFO: Calculating ANM for ligand molecule...
[lightdock3_setup] INFO: 10 normal modes calculated
[lightdock3_setup] INFO: Reading restraints from restraints.list
[lightdock3_setup] INFO: Number of receptor restraints is: 3 (active), 0 (passive)
[lightdock3_setup] INFO: Number of ligand restraints is: 0 (active), 0 (passive)
[lightdock3_setup] INFO: Calculating starting positions...
[lightdock3_setup] INFO: Generated 21 positions files
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Number of calculated swarms is 21
[lightdock3_setup] INFO: Preparing environment
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: LightDock setup OK
```


## 5. Simulation

We can run this simulation in a local machine or in a HPC cluster. For the first option, simply run the following command.

```bash
lightdock3.py setup.json 100 -s dna -c 8
```

Where the flag `-c 8` indicates LightDock to use 8 available cores. For this example we will run `100` steps of the protocol and using a scoring function with support for nucleic acids: `-s dna`.

To run a LightDock job on a HPC cluster, a Portable Batch System (PBS) file can be generated. This PBS file defines the commands and cluster resources used for the job. A PBS file is a plain-text file that can be easily edited with any UNIX editor. 

For example, create a new `submit_job.sh` file containing:

```bash
#PBS -N LightDock-1AZP
#PBS -q medium
#PBS -l nodes=1:ppn=16
#PBS -S /bin/bash
#PBS -d ./
#PBS -e ./lightdock.err
#PBS -o ./lightdock.out

lightdock3.py setup.json 100 -s dna -c 16
```

This script tells the PBS queue manager to use 16 cores of a single node in a queue with name `medium`, with job name `LigthDock-1AZP` and with standard output to `lightdock.out` and error output redirected to `lightdock.err`.

To run this script you can do it as:

```
qsub < submit_job.sh
```

## 6. Clustering and Filtering

Once the simulation has finished (it takes around 6-7 min per 100 steps per swarm), we need to generate the structures of the predictions, cluster them per swarm and finally filtering them.

**Attention!** In order to get realistic simulations results it is critical to always cluster intra-swarm structures and to filter them for restraints compatibility.
{: .notice--danger}


Here there is a PBS script to do all steps at once:

```bash
#PBS -N 1AZP-post
#PBS -q medium
#PBS -l nodes=1:ppn=8
#PBS -S /bin/bash
#PBS -d ./
#PBS -e ./postprocessing.err
#PBS -o ./postprocessing.out

### Calculate the number of swarms ###
s=`ls -d ./swarm_* | wc -l`
swarms=$((s-1))

### Create files for Ant-Thony ###
for i in $(seq 0 $swarms)
  do
    echo "cd swarm_${i}; lgd_generate_conformations.py ../protein.pdb ../dna.pdb  gso_100.out 200 > /dev/null 2> /dev/null;" >> generate_lightdock.list;
  done

for i in $(seq 0 $swarms)
  do
    echo "cd swarm_${i}; lgd_cluster_bsas.py gso_100.out > /dev/null 2> /dev/null;" >> cluster_lightdock.list;
  done

### Generate LightDock models ###
ant_thony.py -c 8 generate_lightdock.list;

### Clustering BSAS (rmsd) within swarm ###
ant_thony.py -c 8 cluster_lightdock.list;

### Generate ranking files for filtering ###
lgd_rank.py $s 100;

### Filtering models by >40% of satisfied restraints ###
lgd_filter_restraints.py --cutoff 5.0 --fnat 0.4 -lnuc rank_by_scoring.list restraints.list A B

```

**Attention!** Do not forget to include the flag `-lnuc` when executing the `lgd_filter_restraints.py` command since this enables searching for restraints in nucleic acid partners.
{: .notice--danger}


**NOTE:** You can also run the previous commands locally in a sequential way.
{: .notice--info}

Once the post-processing is finished, a new folder called `filtered` has been created, which contains any predicted structure which satisfies the given 40% filtering. Inside of this directory, there is a file with the ranking of these structures by LightDock `dna` score (the more positive the better) `rank_filtered.list`.

We provide for this example a complete [simulation.tgz](data/simulation.tgz) compressed file of the complete run.

<br>


# 7. References
For a more complete description of the algorithm as well as different tutorials, please refer to [LightDock](https://lightdock.org/), or check the following references:

- **Integrative Modeling of Membrane-associated Protein Assemblies**<br>
Jorge Roel-Touris, [Brian Jiménez-García](https://bjimenezgarcia.com) & Alexandre M.J.J. Bonvin<br>
*Nat Commun* **11**, 6210 (2020); doi: [https://doi.org/10.1038/s41467-020-20076-5](https://doi.org/10.1038/s41467-020-20076-5)

- **LightDock goes information-driven**<br>
Jorge Roel-Touris, Alexandre M.J.J. Bonvin and [Brian Jiménez-García](https://bjimenezgarcia.com)<br>
*Bioinformatics*, Volume 36, Issue 3, 1 February 2020, Pages 950–952, doi: [https://doi.org/10.1093/bioinformatics/btz642](https://doi.org/10.1093/bioinformatics/btz642)

- **LightDock: a new multi-scale approach to protein–protein docking**<br>
[Brian Jiménez-García](https://bjimenezgarcia.com), Jorge Roel-Touris, Miguel Romero-Durana, Miquel Vidal, Daniel Jiménez-González and Juan Fernández-Recio<br>
*Bioinformatics*, Volume 34, Issue 1, 1 January 2018, Pages 49–55, doi: [https://doi.org/10.1093/bioinformatics/btx555](https://doi.org/10.1093/bioinformatics/btx555)
