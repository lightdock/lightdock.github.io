---
permalink: /tutorials/membrane
layout: splash
classes: wide

---

<center><h1>Membrane-associated protein docking</h1></center><br>

This is a complete example of the LightDock docking protocol to model the [2HDI](https://www.rcsb.org/structure/2hdi) membrane-associated protein system with the use of an **implicit membrane representation** provided by the [MemProtMD](http://memprotmd.bioch.ox.ac.uk/) database.

**IMPORTANT** Please, make sure that you have the <code>python3</code> version of LightDock installed (<code>pip3 install lightdock</code>). We advise you to follow the basic tutorial about how to run a quick [LightDock simulation](https://lightdock.org/tutorials/2UUY)

Here, we provide a complete step-by-step guide to model the interaction between the Colicin I receptor Cir (beta-barrel) in complex with receptor binding domain of Colicin Ia.

## Copying the data
Create a directory and copy the sample data provided.

```bash
$ cd Desktop
$ mkdir test
$ cd test
wget https://raw.githubusercontent.com/haddocking/MemCplxDB/master/structures/2hdi/2hdi_unbound_A.pdb
wget https://raw.githubusercontent.com/haddocking/MemCplxDB/master/structures/2hdi/2hdi_unbound_B.pdb
wget MEMBRANE
```

Where *2hdi_unbound_A.pdb* corresponds to the beta-barrel structure, *2hdi_unbound_B.pdb* is the receptor binding domain and *MEMBRANE* the representative coarse-grained [snapshot]() of the 2HDI receptor.
