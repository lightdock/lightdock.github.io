---
title: "LightDock Workshop - University of Talca"
layout: splash
permalink: /workshops/talca24
classes: wide
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /workshops/talca24/images/uni_talca.jpg

feature_row:
  - image_path: /workshops/talca24/images/lightdock_theory.jpg
    alt: "LightDock Theory"
    title: "LightDock Theory"
    excerpt: "Learn the theory behind the Lightdock macromolecular docking framework."
    url: "/workshops/talca24/lightdock_theory"
    btn_label: "Learn the basics"
    btn_class: "btn--primary"
  - image_path: /workshops/talca24/images/lightdock_server.png 
    alt: "LightDock Server"
    title: "Lightdock Server"
    excerpt: "Make use of the online LightDock Server to model macromolecular interactions."
    url: "https://server.lightdock.org/"
    btn_label: "Run simulations online"
    btn_class: "btn--primary"
  - image_path: /workshops/talca24/images/help.jpg 
    alt: "Help"
    title: "Help"
    excerpt: "Your LightDock simulation turned into a magical creature instead of a macromolecular complex? 🤖 Do not panic!"
    url: "https://join.slack.com/t/lightdock/shared_invite/zt-14ezmx2hv-Opr3OgN99~5OfSWeNmUl2A"
    btn_label: "Ask in our Slack channel"
    btn_class: "btn--primary"

blind_docking:
  - image_path: /workshops/talca24/images/blind_docking.png
    alt: "Blind Docking"
    title: "Blind protein-RNA docking"
    excerpt: "A quick guide about how to setup a blind (ab initio) macromolecular docking simulation with LightDock."
    url: "/workshops/talca24/blind_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

restraints_docking:
  - image_path: /workshops/talca24/images/restraints_docking.png
    alt: "Restraints Docking"
    title: "Protein-peptide docking using residue restraints"
    excerpt: "This is a complete example on how to drive LightDock docking simulations using residue restraints."
    url: "/workshops/talca24/restraints_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

membrane_docking:
  - image_path: /workshops/talca24/images/membrane_docking.png
    alt: "Membrane Docking"
    title: "Membrane-associated protein docking"
    excerpt: "This tutorial demonstrates the use of LightDock for predicting the structure of a membrane receptor–soluble protein complex."
    url: "/workshops/talca24/membrane_docking"
    btn_label: "Read More"
    btn_class: "btn--primary"

docking_challenge:
  - image_path: /workshops/talca24/images/completo.jpg
    alt: "Docking Challenge"
    title: "Docking Challenge"
    excerpt: "Are you ready for a challenge?"
    url: "/workshops/talca24/docking_challenge"
    btn_label: "Let's go!"
    btn_class: "btn--primary"

---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

{% include feature_row id="lightdock_theory" type="left" %}

{% include feature_row id="blind_docking" type="left" %}

{% include feature_row id="restraints_docking" type="left" %}

{% include feature_row id="membrane_docking" type="left" %}

{% include feature_row id="docking_challenge" type="left" %}
