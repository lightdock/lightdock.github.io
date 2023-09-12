---
title: "Integrative modelling of protein interactions"
layout: splash
permalink: /workshops/embo23
classes: wide
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /workshops/embo23/images/embo23_header.jpg
excerpt: "[EMBO Practical Course](https://meetings.embo.org/event/23-biomolecular-interactions)"

feature_row:
  - image_path: /workshops/embo23/images/lightdock_theory.jpg
    alt: "LightDock Theory"
    title: "LightDock Theory"
    excerpt: "Learn the theory behind the Lightdock macromolecular docking framework."
    url: "/workshops/embo23/lightdock_theory"
    btn_label: "Learn the basics"
    btn_class: "btn--primary"
  - image_path: /workshops/embo23/images/lightdock_server.png 
    alt: "LightDock Server"
    title: "Lightdock Server"
    excerpt: "Make use of the online LightDock Server to model macromolecular interactions."
    url: "https://server.lightdock.org/"
    btn_label: "Run simulations online"
    btn_class: "btn--primary"
  - image_path: /workshops/embo23/images/faq.jpg 
    alt: "FAQ"
    title: "FAQ"
    excerpt: "Browse previous or frequently asked questions by other LightDock users."
    url: "/workshops/embo23/faq"
    btn_label: "Browse FAQ"
    btn_class: "btn--primary"

blind_docking:
  - image_path: /workshops/embo23/images/blind_docking.png
    alt: "Blind Docking"
    title: "Blind protein-protein docking"
    excerpt: "A quick guide about how to setup a blind (ab initio) macromolecular docking simulation with LightDock."
    url: "/workshops/embo23/blind_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

restraints_docking:
  - image_path: /workshops/embo23/images/restraints_docking.png
    alt: "Restraints Docking"
    title: "Protein-peptide docking using residue restraints"
    excerpt: "This is a complete example on how to drive LightDock docking simulations using residue restraints."
    url: "/workshops/embo23/restraints_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

membrane_docking:
  - image_path: /workshops/embo23/images/membrane_docking.png
    alt: "Membrane Docking"
    title: "Membrane-associated protein docking"
    excerpt: "This tutorial demonstrates the use of LightDock for predicting the structure of a membrane receptor–soluble protein complex."
    url: "/workshops/embo23/membrane_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

docking_challenge:
  - image_path: /workshops/embo23/images/docking_challenge.png
    alt: "Docking Challenge"
    title: "Docking Challenge"
    excerpt: "Are you ready to model the Turkish 🇹🇷 flag?"
    url: "/workshops/embo23/docking_challenge"
    btn_label: "Go!"
    btn_class: "btn--primary"


---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

{% include feature_row id="lightdock_theory" type="left" %}

{% include feature_row id="blind_docking" type="left" %}

{% include feature_row id="restraints_docking" type="left" %}

{% include feature_row id="membrane_docking" type="left" %}

{% include feature_row id="docking_challenge" type="left" %}
