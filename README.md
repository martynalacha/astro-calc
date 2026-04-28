# Astro Calc 🚀

[![Tests](https://github.com/martynalacha/astro-calc/actions/workflows/test.yml/badge.svg)](https://github.com/martynalacha/astro-calc/actions/workflows/test.yml)
[![Docs](https://github.com/martynalacha/astro-calc/actions/workflows/docs.yml/badge.svg)](https://<USER>.github.io/astro-calc/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martynalacha/astro-calc/blob/main/notebooks/demo.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/martynalacha/astro-calc/main?filepath=notebooks%2Fdemo.ipynb)

A lightweight Python library for basic planetary physics calculations. Built as a showcase for modern Python packaging, CI/CD automation, and unit conversion management.

## Features

- **Dimensional Accuracy**: Uses the `Pint` library to handle physical units and prevent calculation errors.
- **Physics Calculations**:
  - Planetary weight calculation based on local gravity.
  - First cosmic velocity (orbital velocity) for celestial bodies.
- **Fully Automated**:
  - CI testing via `pytest` and GitHub Actions.
  - Automatic documentation deployment to GitHub Pages.
  - Git-coupled versioning using `setuptools_scm`.

