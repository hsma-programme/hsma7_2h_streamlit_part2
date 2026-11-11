# HSMA-7 Module 2H: Creating a DES interface with Streamlit - Part 2

This repository contains materials for module 2H:

* `app/` - a multi-page app for running, saving and comparing scenarios.
    * `app/app.py` - main entrypoint.
    * `app/model.py` - copy of model used by app.

* `exercise/` - exercise materials.

* `slides/` - Quarto slides.
    * `slides/slides.qmd` - main slides file.
    * `slides/code/` - Python examples, kept separate to make the slides file easier to read and search.
    * `template` - templates and assets for creating the HSMA slide style.

The slides are deployed on GitHub pages via GitHub actions and can be viewed via the browser at: <https://hsma-programme.github.io/hsma7_2h_streamlit_part2>.

The example app is deployed with Streamlit Community Cloud and can be viewed at: <https://hsma-des-scenarios.streamlit.app>.

<br>

## Viewing the slides and example app locally

Activate the HSMA `des` GitHub environment. The environment file required is available in <https://github.com/hsma-chief-elf/H7_Phase_1_Artefacts>: `DES_2/environment/environment.yml`.

> **Note:** A record of the packages needed is also available in this repository under `app/requirements.txt` as it is required for deployment.

```
mamba activate des
```

To view the slides:

```
quarto preview slides/slides.qmd
```

To view the app:

```
streamlit run app/app.py
```