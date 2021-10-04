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
      url: "https://github.com/lightdock/lightdock/releases/latest"
    - label: "Online server (beta)"
      url: "https://server.lightdock.org/"
excerpt: "The open-source protein docking framework written in Python ([and Rust](https://github.com/lightdock/lightdock-rust))"

intro: 
  - excerpt: '*Protein-Protein, Protein-DNA and Protein-Peptide docking made easy*'

---

![LightDock Docking](assets/images/lightdock_docking.png){: .align-center}

{% include feature_row id="intro" type="center" %}


## Installation
[![PyPi version](https://img.shields.io/pypi/v/lightdock.svg)](https://pypi.org/project/lightdock/) [![Build Status](https://travis-ci.com/lightdock/lightdock.svg?branch=master)](https://travis-ci.com/lightdock/lightdock)

LightDock is distributed as a [PyPi package](https://pypi.org/project/lightdock/)!

```
pip install lightdock
```

For members of the [SBGrid](https://sbgrid.org/) consortium, LightDock can be also installed using the [CLI client](https://sbgrid.org/software/titles/lightdock):

```bash
sbgrid-cli install lightdock
```

Alternative ways to install LightDock can be found in the official [GitHub repository](https://github.com/lightdock/lightdock/blob/master/README.md).


## Tutorials

LightDock is able to model different binary systems such as protein-protein, protein-DNA or protein-peptide complexes.

[Learn more!](/tutorials/latest){: .btn .btn--primary .btn--large}


## License

![GPLv3](/assets/images/gplv3.png){: .align-left}
LightDock is free and open-source under license [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)!


## Source code
![GitHub](/assets/images/github_logo.png){: .align-left}
Browse the source code from the [official repository](https://github.com/lightdock/lightdock).
