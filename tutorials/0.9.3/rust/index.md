---
permalink: /tutorials/0.9.3/rust
layout: splash
classes: wide
title: "LightDock-Rust"
---

<center><h1 style="margin-top:40px">LightDock-Rust</h1></center><br>

<center>
    <img src="/tutorials/0.9.3/rust/rust.png">
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
   Compiling proc-macro2 v1.0.78
   Compiling unicode-ident v1.0.12
   Compiling autocfg v1.1.0
   Compiling thiserror v1.0.58
   Compiling libm v0.2.8
   Compiling memchr v2.7.1
   Compiling semver v1.0.22
   Compiling cfg-if v1.0.0
   Compiling crossbeam-utils v0.8.19
   Compiling libc v0.2.153
   Compiling ucd-trie v0.1.6
   Compiling once_cell v1.19.0
   Compiling proc-macro2 v0.4.30
   Compiling num-traits v0.2.18
   Compiling byteorder v1.5.0
   Compiling getrandom v0.1.16
   Compiling num-bigint v0.4.4
   Compiling aho-corasick v1.1.2
   Compiling regex-syntax v0.8.2
   Compiling serde v1.0.197
   Compiling rayon-core v1.12.1
   Compiling crc32fast v1.4.0
   Compiling unicode-xid v0.1.0
   Compiling quote v1.0.35
   Compiling syn v2.0.52
   Compiling regex-automata v0.4.6
   Compiling rustc_version v0.4.0
   Compiling heapless v0.7.17
   Compiling crossbeam-epoch v0.9.18
   Compiling num-integer v0.1.46
   Compiling hash32 v0.2.1
   Compiling crossbeam-deque v0.8.5
   Compiling stable_deref_trait v1.2.0
   Compiling utf8parse v0.2.1
   Compiling adler v1.0.2
   Compiling miniz_oxide v0.7.2
   Compiling anstyle-parse v0.2.3
   Compiling regex v1.10.3
   Compiling num-complex v0.4.5
   Compiling thiserror-impl v1.0.58
   Compiling serde_derive v1.0.197
   Compiling rand_core v0.5.1
   Compiling quote v0.6.13
   Compiling smallvec v1.13.1
   Compiling equivalent v1.0.1
   Compiling either v1.10.0
   Compiling serde_json v1.0.115
   Compiling log v0.4.21
   Compiling hashbrown v0.14.3
   Compiling colorchoice v1.0.0
   Compiling ppv-lite86 v0.2.17
   Compiling anstyle v1.0.6
   Compiling pest v2.7.9
   Compiling anstyle-query v1.0.2
   Compiling anstream v0.6.13
   Compiling rand_chacha v0.2.2
   Compiling env_filter v0.1.0
   Compiling indexmap v2.2.6
   Compiling rayon v1.9.0
   Compiling rstar v0.11.0
   Compiling doc-cfg v0.1.0
   Compiling flate2 v1.0.28
   Compiling humantime v2.1.0
   Compiling ryu v1.0.17
   Compiling pest_meta v2.7.9
   Compiling itoa v1.0.10
   Compiling env_logger v0.11.3
   Compiling rand v0.7.3
   Compiling lazy_static v1.4.0
   Compiling pest_generator v2.7.9
   Compiling pest_derive v2.7.9
   Compiling py_literal v0.4.0
   Compiling npyz v0.8.3
   Compiling pdbtbx v0.11.0
   Compiling lightdock v0.3.1 (/Users/bjimenez/workspaces/lightdocking/lightdock-rust)
    Finished release [optimized] target(s) in 11.75s
```

The `lightdock-rust binary` will be generated at `target/release/lightdock-rust`. You may move or copy this binary to the path of your choice.

### 3.1. Set environment 
To avoid copying the `data` folder containing scoring function parameters, set an environment variable pointing to this folder in this repository:

```bash
export LIGHTDOCK_DATA=/path/to/lightdock-rust/data
```

## 4. Usage and examples

You may test a real docking example:

```bash
cd example/1ppe
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
 lightdock3_setup.py 1czy_protein.pdb 1czy_peptide.pdb --noxt --noh -anm -rst restraints.list -spr 10
 ```
 
 You will get an output like this:
 
```bash
[lightdock3_setup] INFO: Ignoring OXT atoms
[lightdock3_setup] INFO: Ignoring Hydrogen atoms
[lightdock3_setup] INFO: Reading structure from 1czy_protein.pdb PDB file...
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
[lightdock3_setup] INFO: 1281 atoms, 168 residues read.
[lightdock3_setup] INFO: Ignoring OXT atoms
[lightdock3_setup] INFO: Ignoring Hydrogen atoms
[lightdock3_setup] INFO: Reading structure from 1czy_peptide.pdb PDB file...
[lightdock3_setup] INFO: 53 atoms, 7 residues read.
[lightdock3_setup] INFO: Calculating reference points for receptor 1czy_protein.pdb...
[lightdock3_setup] INFO: Reference points for receptor found, skipping
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Calculating reference points for ligand 1czy_peptide.pdb...
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
[lightdock3_setup] INFO: Number of receptor restraints is: 1 (active), 0 (passive)
[lightdock3_setup] INFO: Number of ligand restraints is: 0 (active), 0 (passive)
[lightdock3_setup] INFO: Calculating starting positions...
[lightdock3_setup] INFO:   * Surface density: TotalSASA/50.00
[lightdock3_setup] INFO:   * Swarm radius: 10.00 Å
[lightdock3_setup] INFO:   * 180° flip of 50% of starting poses: False
[lightdock3_setup] INFO:   * Ligand Max Diameter: 18.79 Å
[lightdock3_setup] WARNING: Ligand radius is below the cutoff, using default swarm radius 10.0 as surface distance
[lightdock3_setup] INFO:   * Surface distance: 10.00 Å
[lightdock3_setup] INFO: Swarms after incompatible filter: 303
[lightdock3_setup] INFO: Swarms after interior points filter: 165
[lightdock3_setup] INFO: Swarms after occlusion filter: 165
[lightdock3_setup] INFO: Generated 10 positions files
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: Number of calculated swarms is 10
[lightdock3_setup] INFO: Preparing environment
[lightdock3_setup] INFO: Done.
[lightdock3_setup] INFO: LightDock setup OK
```

* If ANM is enabled (it is in this example), we should convert the ANM NumPy information from 3D to 1D data using the `lgd_flatten.py` script:

```bash
lgd_flatten.py lightdock_rec.nm.npy rec_nm.npy
lgd_flatten.py lightdock_lig.nm.npy lig_nm.npy
```

* Now we can test `lightdock-rust` simulating the first swarm:

```bash
time ../../target/release/lightdock-rust setup.json init/initial_positions_0.dat 100 dfire
```
 
 Output should be similar to this:
 
 ```bash
Reading starting positions from "init/initial_positions_0.dat"
Swarm ID 0
Writing to swarm dir "swarm_0"
Reading receptor input structure: lightdock_1czy_protein.pdb
Reading ligand input structure: lightdock_1czy_peptide.pdb
Loading DFIRE scoring function
Creating GSO with 200 glowworms
Starting optimization (100 steps)

real	0m1,558s
user	0m1,292s
sys	0m0,252s
 ```
 
We recommend to use `ant_thony.py` for parallelizing this execution. Create a new `execution.sh` file with the following content:

```bash
#!/bin/bash

# Edit only the number of cores to use for this simulation
NUM_CORES=4

# LightDock setup
lightdock3_setup.py 1czy_protein.pdb 1czy_peptide.pdb --noxt --noh -anm -rst restraints.list -spr 10

# Convert ANM data
lgd_flatten.py lightdock_rec.nm.npy rec_nm.npy
lgd_flatten.py lightdock_lig.nm.npy lig_nm.npy

# Calculate number of swarms
s=`ls -d swarm_* | wc -l`
swarms=$((s-1))

# Copy lightdock-rust binary
cp ../../target/release/lightdock-rust .

# Create a task.list file for ant_thony
for i in `seq 0 $swarms`;do echo "./lightdock-rust setup.json init/initial_positions_${i}.dat 100 dfire;" >> task.list; done

# Let ant_thony run
time ant_thony.py --cores ${NUM_CORES} task.list

# Clean task.list
rm -rf task.list

```

Save it and then execute it (make sure you change the `NUM_CORES` variable according to your number of CPU cores available in your machine:

```bash
chmod u+x execution.sh
./execution.sh
```

After this, the docking simulation of the `1CZY` protein-peptide complex using the `A.PHE.467` as residue restraint should finish successfully.

```bash
$ find . -name gso_100.out | wc -l
10
```

There is a script to quickly perform the analysis and generating the top 10 predicted poses. Simply execute:

```bash
$ ./analysis.sh
```

