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
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Ensure the _static directory exists
if not os.path.exists('_static'):
    os.makedirs('_static')

# Set the correct output directory for Read the Docs
if os.getenv('READTHEDOCS') == 'True':
    html_output = os.path.join(os.getenv('READTHEDOCS_OUTPUT', 'html'))
else:
    html_output = '_build/html'

# Specify the output directory for Sphinx
html_output = os.getenv('READTHEDOCS_OUTPUT', html_output)
