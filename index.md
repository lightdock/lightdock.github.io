---
title: "LightDock"
layout: splash
permalink: /
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/code.png
  actions:
    - label: "Download Latest Release"
      url: "https://github.com/brianjimenez/lightdock/releases/tag/0.7.0"
excerpt: "The flexible protein docking framework written in Python"

intro: 
  - excerpt: '*Protein-Protein, Protein-DNA and Protein-Peptide docking made easy*'

tutorials:
  - image_path: /assets/images/tutorials.jpg
    alt: "Tutorials image"
    title: "Tutorials"
    excerpt: 'How to use LightDock in different macromolecular systems.'
    url: "/tutorials/"
    btn_label: "Read More"
    btn_class: "btn--primary"

information:
  - image_path: /assets/images/swarms.png
    alt: "Information image"
    title: "How to install LightDock"
    excerpt: 'LightDock is straightforward to install as it only depends in a few Python libraries.'
    url: "https://github.com/brianjimenez/lightdock/blob/master/README.md#3-installation"
    btn_label: "Read Installation Guide"
    btn_class: "btn--primary"

---

{% include feature_row id="intro" type="center" %}

{% include feature_row id="tutorials" type="left" %}

{% include feature_row id="information" type="right" %}

