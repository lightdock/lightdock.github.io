---
title: "Tutorials"
layout: splash
permalink: /tutorials/0.9.3/
classes: wide
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/tutorials.jpg
excerpt: "How to use LightDock version [0.9.3 & 0.9.4](https://github.com/lightdock/lightdock/releases/tag/0.9.3.post1)"

feature_row:
  - image_path: /tutorials/0.9.3/images/basics.png
    alt: "LightDock Basics"
    title: "LightDock Basics"
    excerpt: "Learn the basics of the framework, as well as more advanced details."
    url: "/tutorials/0.9.3/basics"
    btn_label: "Learn the basics"
    btn_class: "btn--primary"
  - image_path: /tutorials/0.9.3/images/tree.png
    alt: "Changelog"
    title: "Previous versions"
    excerpt: "Find tutorials for previous versions of LightDock."
    url: "/tutorials/previous"
    btn_label: "Take me to the past"
    btn_class: "btn--primary"
  - image_path: /tutorials/0.9.3/images/faq.jpg 
    alt: "FAQ"
    title: "FAQ"
    excerpt: "Browse previous or frequently asked questions by other LightDock users."
    url: "/tutorials/0.9.3/faq"
    btn_label: "Browse FAQ"
    btn_class: "btn--primary"

simple_docking:
  - image_path: /tutorials/0.9.3/images/simple.png
    alt: "Simple Docking"
    title: "Simple protein-protein docking example"
    excerpt: "A quick guide about how to setup a protein docking simulation with LightDock."
    url: "/tutorials/0.9.3/simple_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"
    
membrane_docking:
  - image_path: /tutorials/0.9.3/images/membrane.png
    alt: "Membrane Docking"
    title: "Membrane-associated protein docking"
    excerpt: "This tutorial demonstrates the use of LightDock for predicting the structure of a membrane receptor–soluble protein complex."
    url: "/tutorials/0.9.3/membrane"
    btn_label: "Read More"
    btn_class: "btn--primary"

restraints_docking:
  - image_path: /tutorials/0.9.3/images/restraints.png
    alt: "Restraints Docking"
    title: "Protein-protein docking using residue restraints"
    excerpt: "This is a complete example of the LightDock docking protocol to model the 4G6M protein complex making use of residue restraints."
    url: "/tutorials/0.9.3/restraints"
    btn_label: "Read More"
    btn_class: "btn--primary"

dna_docking:
  - image_path: /tutorials/0.9.3/images/dna.png
    alt: "Protein-DNA Docking"
    title: "Protein-DNA docking using residue restraints"
    excerpt: "This is a complete example of the LightDock docking protocol to model the 1AZP protein-DNA complex making use of residue restraints and flexibility through ANM model."
    url: "/tutorials/0.9.3/dna_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

rna_docking:
  - image_path: /tutorials/0.9.3/images/rna.png
    alt: "Protein-RNA Docking"
    title: "Protein-RNA docking"
    excerpt: "This is an example of the LightDock docking protocol to model the 1A1T protein-RNA complex with flexibility through ANM model."
    url: "/tutorials/0.9.3/rna_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

sbgrid_seminar:
  - image_path: /tutorials/0.9.3/images/sbgrid_logo.png
    alt: "SBGrid Consortium"
    title: "SBGrid LightDock seminar"
    excerpt: "Watch the LightDock seminar at the SBGrid Consortium Youtube channel"
    url: "/tutorials/0.9.3/sbgrid_seminar"
    btn_label: "Watch now"
    btn_class: "btn--primary"

lightdock-rust:
  - image_path: /tutorials/0.9.3/images/rust.png
    alt: "LightDock+Rust"
    title: "Accelerating LightDock with Rust"
    excerpt: "LightDock-Rust is a new implementation of the LightDock software in the Rust programming language."
    url: "/tutorials/0.9.3/rust"
    btn_label: "Read More"
    btn_class: "btn--primary"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

{% include feature_row id="simple_docking" type="left" %}

{% include feature_row id="membrane_docking" type="left" %}

{% include feature_row id="restraints_docking" type="left" %}

{% include feature_row id="dna_docking" type="left" %}

{% include feature_row id="rna_docking" type="left" %}

{% include feature_row id="sbgrid_seminar" type="left" %}

{% include feature_row id="lightdock-rust" type="left" %}

