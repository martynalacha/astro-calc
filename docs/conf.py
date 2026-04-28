import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

project = 'astro-calc'
copyright = '2026, Martyna'
author = 'Martyna'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # Automatyczne generowanie dokumentacji z docstringów
    'sphinx.ext.napoleon',   # Obsługa ładnych opisów (format Google/NumPy)
    'sphinx.ext.viewcode',   # Dodaje przycisk "[source]" przy funkcjach
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
