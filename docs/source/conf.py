# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# The code of the modules can be found at the root of the repository
sys.path.insert(0, os.path.abspath('../..'))

project = 'CI Server'
copyright = '2024, Dante Astorga Castillo, Ludvig Skare, Rasmus Danielsson, Victor Stenmark, Sebastian Montén'
author = 'Dante Astorga Castillo, Ludvig Skare, Rasmus Danielsson, Victor Stenmark, Sebastian Montén'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',
              'sphinx.ext.doctest',
              'sphinx.ext.autodoc'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
