# HSMA-7 Module 2H: Creating a DES interface with Streamlit - Part 2

This repository contains materials for module 2H:

* `app/` contains the example app.
    * It is a multi-page app that can run, store and compare multiple scenarios. The main entrypoint is `app/app.py`.
    * A copy of the model used is available under `app/model.py`.

* `exercise/` contains the exercise materials.

* `slides/` contains the Quarto slides.

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