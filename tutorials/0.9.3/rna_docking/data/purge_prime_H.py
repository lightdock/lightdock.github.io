#!/usr/bin/env python3
import os
import argparse
from lightdock.pdbutil.PDBIO import read_atom_line

def _format_atom_name(atom_name):
    """Format ATOM name with correct padding"""
    if len(atom_name) == 4:
        return atom_name
    else:
        return " %s" % atom_name


def write_atom_line(atom, output):
    """Writes a PDB file format line to output."""
    if atom.__class__.__name__ == "HetAtom":
        atom_type = "HETATM"
    else:
        atom_type = "ATOM  "
    line = "%6s%5d %-4s%-1s%3s%2s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f%12s\n" % (
        atom_type,
        atom.number,
        _format_atom_name(atom.name),
        atom.alternative,
        atom.residue_name,
        atom.chain_id,
        atom.residue_number,
        atom.residue_insertion,
        atom.x,
        atom.y,
        atom.z,
        atom.occupancy,
        atom.b_factor,
        atom.element,
    )
    output.write(line)

def _add_RNA_tag(atom):
    """Adds R tag to RNA residues"""
    if not atom.residue_name.startswith("R"):
        atom.residue_name = "R" + atom.residue_name
    
    return atom

def _remove_RNA_tag(atom):
    """Removes R tag to RNA residues"""
    if atom.residue_name.startswith("R"):
        atom.residue_name = atom.residue_name[1:]

    return atom


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdb_file")
    parser.add_argument("output_pdb_file")
    args = parser.parse_args()

    with open(args.input_pdb_file) as ih:
        with open(args.output_pdb_file, 'w') as oh:
            
            for line in ih:
                line = line.rstrip(os.linesep)
                
                if line.startswith("ATOM  "):
                    atom = read_atom_line(line)

                    if atom.name in ("HO'3", "HO'5"):
                        continue

                    write_atom_line(atom, oh)
                else:
                    oh.write(line + os.linesep)