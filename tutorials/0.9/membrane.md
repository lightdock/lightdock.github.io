---
permalink: /tutorials/0.9/membrane
layout: splash
classes: wide

---

<center><h1 style="margin-top:40px">Membrane-associated protein docking</h1></center><br>

* table of contents
{:toc}

<hr>

## 1. Introduction
This tutorial demonstrates the use of [LightDock](https://lightdock.org) for predicting the structure of membrane receptor–soluble protein complex using the topological information provided by the membrane to guide the modeling process. We will be following the protocol described in [Roel-Touris *et al*, 2020](https://www.nature.com/articles/s41467-020-20076-5).

Membrane proteins are among the most challenging systems to study with experimental structural biology techniques, thus computational techniques such as docking might offer invaluable insights on the modeling of those systems.

<center>
    <img src="3x29_membrane.png">
    <br>
    <b>Fig.1</b> 3X29 complex in a lipid bilayer as simulated by <a href="http://memprotmd.bioch.ox.ac.uk/_ref/PDB/3x29" target="_blank">MemProtMD</a>.
    <br><br>
</center>

In this tutorial we will be working with the crystal structure  of *Mus musculus* [Claudin-19](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR006187/) transmembrane protein (PDB code [3X29](https://www.ebi.ac.uk/pdbe/entry/pdb/3x29), chain A) in complex with the unbound C-terminal fragment of the *Clostridium perfringens* [Enteroxin](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR003897/) (PDB code [2QUO](https://www.ebi.ac.uk/pdbe/entry/pdb/2quo), chain A). The PDB code of the complex is [3X29](https://www.ebi.ac.uk/pdbe/entry/pdb/3x29) (chains A and B).

3X29 complex is one of the cases covered in the [MemCplxDB](https://github.com/haddocking/MemCplxDB) membrane protein complex benchmark ([Koukos _et al_, 2018](https://www.sciencedirect.com/science/article/pii/S0022283618308222)). Despite not being one of the most challenging cases covered in the benchmark in terms of flexibility, its relatively small size will help us describing the complete modeling protocol in the short time intended for a tutorial.

<hr>

For this tutorial we will make use of the [LightDock software](https://lightdock.org/) and the [LightDock server](https://server.lightdock.org/) (which is currently under open beta version).

The integrative approach followed in this tutorial is described here:

* J. Roel-Touris, B. Jimenez-Garcia and A.M.J.J. Bonvin. [Integrative modeling of membrane-associated protein assemblies](https://www.nature.com/articles/s41467-020-20076-5). *Nat. Commun.*, **11**, 6210 (2020).

LightDock docking framework is described in the following publications:

* J. Roel-Touris, A.M.J.J. Bonvin and B. Jimenez-Garcia. [LightDock goes information-driven](https://doi.org/10.1093/bioinformatics/btz642). *Bioinformatics*, **36**:3 950-952 (2020).

* B. Jimenez-Garcia, J. Roel-Touris, M. Romero-Durana, M. Vidal, D. Jimenez-Gonzalez, J. Fernandez-Recio. [LightDock: a new multi-scale approach to protein-protein docking](https://doi.org/10.1093/bioinformatics/btx555). *Bioinformatics*, **34**:1 49-55 (2018).


## 2. General concepts

LightDock is a macromolecular docking software written in the Python programming language, designed as a framework for rapid prototyping and test of scientific hypothesis in structural biology. It was designed to be easily extensible by users and scalable for high-throughput computing (HTC). LightDock is capable of modeling backbone flexibility of molecules using anisotropic model networks ([ANM](https://en.wikipedia.org/wiki/Anisotropic_Network_Model)) and the energetic minimization is based on the [Glowworm Swarm Optimization](https://dx.doi.org/10.1007/978-3-319-51595-3) (GSO) algorithm.

LightDock protocol is divided in two main steps: **setup** and **simulation**. On setup step, input PDB structures for receptor and ligand partners are parsed and prepared for the simulation. Moreover, a set of *swarms* is arranged around the receptor surface. Each of these swarms represents an independent simulation in LightDock where a fixed number of agents, called *glowworms*, encodes for a possible receptor-ligand pose. During the simulation step, each of these glowworms will sample a given region of the energetic landscape depending on its neighboring glowworms. 

<center>
    <img src="4g6m_restraints.png">
    <br>
    <b>Fig.2</b> A receptor surface showing only two swarms. Each swarm contains a set of glowworms representing a possible receptor-ligand pose.
    <br><br>
</center>

Swarms on the receptor surface can be easily filtered according to regions of interest. Figure 2 shows an example where only two swarms have been calculated to focus on two residues of interest on the receptor partner (depicted in <span style="color:orange">orange</span>). **On this tutorial we will explore this capability in order to filter out incompatible transmembrane binding regions in membrane complex docking**.

For more information about LightDock, please visit the [tutorials section](https://lightdock.org/tutorials/).

<hr>

## 3. Setup/Requirements

In order to run this tutorial you will need to have the following software installed: [LightDock][link-lightdock], [pdb-tools][link-pdbtools] and [PyMOL][link-pymol].

### 3.1. Installing LightDock

LightDock is distributed as a Python package through the [Python Package Index](https://pypi.org/project/lightdock/) (PyPI) repository.

#### 3.1.1. Command line
Installing LightDock is as simple as creating a virtual environment for **Python 3.6+** and running `pip` command (make sure your instances of `virtualenv` and `pip` are for Python 3.6+ versions). We will install the version *0.9.0* of LightDock which is the first released version with support for the membrane protocol and execution in [Jupyter Notebooks](https://jupyter.org/) (see next section):

```bash
virtualenv venv
source venv/bin/activate
pip install numpy && pip install lightdock==0.9.0
```

If the installation finished without errors, you should be able to execute LightDock in the terminal:

```bash
lightdock3.py -v
```

and to see an output similar to this:

```bash
lightdock3 0.9.0
```

#### 3.1.2. Jupyter Notebook and Google Colab

Another option to use LightDock is through [Google Colaboratory](https://colab.research.google.com) ("Colab" for short) which allows you to write and execute Python in the browser using *notebooks*. In case of choosing this option, simply execute in a new notebook in the first cell the following command:

```
!pip install lightdock==0.9.0
```

### 3.2. Installing PDB-Tools

PDB-Tools is a set of Python scripts for manipulating PDB files following the philosophy of *one script, one task*. For different manipulating tasks on a PDB file, the procedure would be to *pipe* the different PDB-Tools scripts to accomplish the different tasks. 

PDB-Tools is distributed as a PyPI package. To install it, simply:

```bash
pip install pdb-tools
```

or alternatively in a Google Colab notebook:

```
!pip install pdb-tools
```

### 3.3. Tutorial Notebook

We have prepared a Colab Notebook ready to be imported. Download it: [tutorial.ipynb](data/tutorial.ipynb)

In case of using the provided Colab notebook, go to the [Colab site](https://colab.research.google.com) and upload the provided notebook (see A):

<center>
    <img src="colab.png">
    <br>
</center>

Once imported, click on the icon pointed in (B) and upload the required files as marked in (C) by the orange arrow. The two required files ([3x29_receptor_membrane.pdb](data/3x29_receptor_membrane.pdb) and [3x29_ligand.pdb](data/3x29_ligand.pdb)) should appear now as in (D). 

Then, run one by one each of the code cells as several libraries will be installed in the first code cells.

<hr>



[link-pymol]: https://www.pymol.org/ "PyMOL"
[link-lightdock]: https://lightdock.org "LightDock"
[link-pdbtools]: https://github.com/haddocking/pdb-tools/ "PDB-Tools"