# conf.py

import os
import sphinx_rtd_theme

# Project information
project = 'Your Project Name'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
]

# HTML output
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom output directory for Read the Docs
if os.getenv('READTHEDOCS', None) == 'True':
    html_output = os.getenv('READTHEDOCS_OUTPUT', '_build/html')
else:
    html_output = '_build/html'

# Ensure the _static directory exists
if not os.path.exists('_static'):
    os.makedirs('_static')
