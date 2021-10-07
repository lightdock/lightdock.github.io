---
permalink: /tutorials/0.9.1/rust
layout: splash
classes: wide
title: "LightDock-Rust"
---

<center><h1 style="margin-top:40px">LightDock-Rust</h1></center><br>

<center>
    <img src="/tutorials/0.9.1/rust/rust.png">
</center>

* table of contents
{:toc}


## 1. Introduction

LightDock-Rust is a new implementation of the LightDock software in the [Rust programming language](https://www.rust-lang.org/). Rust was designed for performance and reliability, and it is amazingly fast and memory-efficient (no runtime or garbage collector).

Not all LightDock has been rewritten in Rust, only the simulation part of the pipeline which is `lightdock3.py` Python script. Moreover, this new Rust version only has support for the DFIRE scoring function. However, **residue restraints, ANM and membrane beads are fully supported**.


## 2. Rust environment installation

For installing the Rust compiler and `cargo` we recommend the **rustup** way (an installer for
the Rust programming language):

Go to the [rustup](https://rustup.rs/) main website and follow the instructions or if you are in Linux or macOS, just type in your terminal:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

If you have any question about how to install and setup Rust and `cargo` it is very recommended to read the first chapter of the [Rust Programming Language Book](https://doc.rust-lang.org/book/ch01-00-getting-started.html).


## 3. Compilation

Source code of the LightDock-Rust software is available online in the [official GitHub repository](https://github.com/lightdock/lightdock-rust). Follow these instructions to compile it from source (this is the only way at the moment):

```bash
git clone https://github.com/lightdock/lightdock-rust
cd lightdock-rust
cargo build --release
```

First, we clone the repository from GitHub, then we move into the new repository and finally we let cargo download and compile the library dependencies for us with the most efficient target, which is `release`.

You may see an output like this:

```bash
Updating crates.io index
  Downloaded serde v1.0.110
  Downloaded ppv-lite86 v0.2.8
  Downloaded libc v0.2.71
  Downloaded serde_json v1.0.53
  Downloaded serde_derive v1.0.110
  Downloaded quote v1.0.6
  Downloaded proc-macro2 v1.0.17
  Downloaded syn v1.0.27
   Compiling libc v0.2.71
   Compiling proc-macro2 v1.0.17
   Compiling unicode-xid v0.2.0
   Compiling syn v1.0.27
   Compiling getrandom v0.1.14
   Compiling cfg-if v0.1.10
   Compiling byteorder v1.3.4
   Compiling serde v1.0.110
   Compiling ryu v1.0.4
   Compiling ppv-lite86 v0.2.8
   Compiling itoa v0.4.5
   Compiling lazy_static v1.4.0
   Compiling lib3dmol v0.3.2
   Compiling memchr v1.0.2
   Compiling quote v1.0.6
   Compiling nom v3.2.1
   Compiling rand_core v0.5.1
   Compiling npy v0.4.0
   Compiling rand_chacha v0.2.2
   Compiling rand v0.7.3
   Compiling serde_derive v1.0.110
   Compiling serde_json v1.0.53
   Compiling lightdock v0.1.0 (/path/to/lightdock-rust)
Finished release [optimized] target(s) in 1m 23s
```

The `lightdock-rust binary` will be generated at `target/release/lightdock-rust`. You may move or copy this binary to the path of your choice.

You may set an environment variable `LIGHTDOCK_DATA` to point to the data folder included in this repository to avoid copying it: `export LIGHTDOCK_DATA=/path/to/lightdock-rust/data`
{: .notice--info}


## 4. Usage and examples

You may test a real docking example:

```bash
cd example/1ppe
cp -R ../../data .
time ../../target/release/lightdock-rust setup_1ppe.json initial_positions_0.dat 100 dfire
```

If you execute the binary, you will get a description of the arguments needed:

```bash
./target/release/lightdock-rust 
Wrong command line. Usage: ./target/release/lightdock-rust setup_filename swarm_filename steps method
```

`lightdock-rust` is intended to be used per swarm. For example, if `lightdock3_setup.py` has genearted 10 swarms, you may need to run `lightdock-rust` for each of the swarms, from `swarm_0` to `swarm_9`.

We will show how to run `lightdock-rust` in a real example in the next section.


### 4.1. Running `lightdock-rust` for `1CZY` complex

* Create a new folder and download the necessary data:

 ```bash
 mkdir 1czy
 cd 1czy
 wget https://raw.githubusercontent.com/lightdock/lightdock-rust/master/example/1czy/1czy_protein.pdb
 wget https://raw.githubusercontent.com/lightdock/lightdock-rust/master/example/1czy/1czy_peptide.pdb
 wget https://raw.githubusercontent.com/lightdock/lightdock-rust/master/example/1czy/restraints.list
 ```

* Now run `lightdock3_setup.py`:

 ```bash
 lightdock3_setup.py 1czy_protein.pdb 1czy_peptide.pdb --noxt --noh -anm -rst restraints.list
 ```
 
 You will get an output like this:
 
 ```bash
[lightdock_setup] INFO: Ignoring OXT atoms
[lightdock_setup] INFO: Ignoring Hydrogen atoms
[lightdock_setup] INFO: Reading structure from 1czy_protein.pdb PDB file...
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue MET.335
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ASP.337
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue GLU.339
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue GLN.340
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue LYS.341
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue GLU.344
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue PRO.362
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ARG.403
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ARG.423
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue ARG.440
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue GLU.441
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue GLU.479
[pdb] WARNING: Possible problem: [SideChainError] Incomplete sidechain for residue LYS.481
[lightdock_setup] INFO: 1281 atoms, 168 residues read.
[lightdock_setup] INFO: Ignoring OXT atoms
[lightdock_setup] INFO: Ignoring Hydrogen atoms
[lightdock_setup] INFO: Reading structure from 1czy_peptide.pdb PDB file...
[lightdock_setup] INFO: 53 atoms, 7 residues read.
[lightdock_setup] INFO: Calculating reference points for receptor 1czy_protein.pdb...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Calculating reference points for ligand 1czy_peptide.pdb...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Saving processed structure to PDB file...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Saving processed structure to PDB file...
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Calculating ANM for receptor molecule...
[lightdock_setup] INFO: 10 normal modes calculated
[lightdock_setup] INFO: Calculating ANM for ligand molecule...
[lightdock_setup] INFO: 10 normal modes calculated
[lightdock_setup] INFO: Reading restraints from restraints.list
[lightdock_setup] INFO: Number of receptor restraints is: 1 (active), 0 (passive)
[lightdock_setup] INFO: Number of ligand restraints is: 0 (active), 0 (passive)
[lightdock_setup] INFO: Calculating starting positions...
[lightdock_setup] INFO: Generated 10 positions files
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: Number of swarms is 10 after applying restraints
[lightdock_setup] INFO: Preparing environment
[lightdock_setup] INFO: Done.
[lightdock_setup] INFO: LightDock setup OK
 ```

* If ANM is enabled (it is in this example), we should convert the ANM NumPy information from 3D to 1D data using the `lgd_flatten.py` script:

 ```bash
lgd_flatten.py lightdock_rec.nm.npy rec_nm.npy
lgd_flatten.py lightdock_lig.nm.npy lig_nm.npy
 ```

* Now we can test `lightdock-rust` simulating the first swarm:

 ```bash
cd swarm_0
cp ../lightdock_1czy_protein.pdb ../lightdock_1czy_peptide.pdb .
cp ../rec_nm.npy ../lig_nm.npy .
cp -R ../../../data .
time ../../../target/release/lightdock-rust ../setup.json ../init/initial_positions_0.dat 100 dfire
 ```
 
 Output should be similar to this:
 
 ```bash
Reading starting positions from "../init/initial_positions_0.dat"
Reading receptor input structure: lightdock_1czy_protein.pdb
Reading ligand input structure: lightdock_1czy_peptide.pdb
Loading DFIRE scoring function
Creating GSO with 200 glowworms
Starting optimization (100 steps)
Step 1
Step 2
Step 3
Step 4
Step 5
Step 6
Step 7
Step 8
Step 9
...
Step 98
Step 99
Step 100
real    0m5.152s
user    0m3.975s
sys     0m1.117s
 ```
 
We recommend to use `ant_thony.py` for parallelizing this execution. Copy the `lightdock-rust` binary to the current `1czy` folder:

```bash
cd 1czy
cp ../target/release/lightdock-rust .
```

Create a new `execution.sh` file with the following content:

```bash
#!/bin/bash

# Edit only the number of cores to use for this simulation
NUM_CORES=4

# LightDock setup
lightdock3_setup.py 1czy_protein.pdb 1czy_peptide.pdb --noxt --noh -anm -rst restraints.list

# Convert ANM data
lgd_flatten.py lightdock_rec.nm.npy rec_nm.npy
lgd_flatten.py lightdock_lig.nm.npy lig_nm.npy

# Calculate number of swarms
s=`ls -d swarm_* | wc -l`
swarms=$((s-1))

# Copy binary
cp ../../target/release/lightdock-rust .

# Create a task.list file for ant_thony
for i in `seq 0 $swarms`;do echo "cd swarm_${i}; cp ../lightdock_1czy_protein.pdb .; cp ../lightdock_1czy_peptide.pdb .;cp ../rec_nm.npy .;cp ../lig_nm.npy .;cp -R ../../../data .;../lightdock-rust ../setup.json ../init/initial_positions_${i}.dat 100 dfire; rm -rf lightdock_*.pdb *.npy data;" >> task.list; done

# Let ant_thony run
ant_thony.py --cores ${NUM_CORES} task.list

# Clean task.list
rm -rf task.list

```

Save it and then execute it (make sure you change the `NUM_CORES` variable according to your number of CPU cores available in your machine:

```bash
chmod u+x execution.sh
./execution.sh
```

After this, the docking simulation of the `1CZY` protein-peptide complex using the `A.PHE.377` as residue restraint should finish successfully.

```bash
$ find . -name gso_100.out | wc -l
10
```
