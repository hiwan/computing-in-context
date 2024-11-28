# conf.py

import os
import sphinx_rtd_theme

# Project information
project = 'Your Project Name'
copyright = '2024, Your Name'
author = 'Your Name'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
]

# HTML output configuration
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Ensure the _static directory exists
if not os.path.exists('_static'):
    os.makedirs('_static')