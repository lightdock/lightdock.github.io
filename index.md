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
  - excerpt: 'Protein-Protein, Protein-DNA and Protein-Peptide docking made easy'

tutorials:
  - image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "Tutorials image"
    title: "Tutorials"
    excerpt: 'How to use LightDock'
    url: "/tutorials/"
    btn_label: "Read More"
    btn_class: "btn--primary"

information:
  - image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "Information image"
    title: "More information"
    excerpt: 'How to install'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"

---

{% include feature_row id="intro" type="center" %}

{% include feature_row id="tutorials" type="left" %}

{% include feature_row id="information" type="right" %}

