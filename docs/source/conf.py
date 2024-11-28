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
    html_theme_options = {
        'base_url': os.getenv('READTHEDOCS_OUTPUT', '_build/html')
    }
else:
    html_theme_options = {
        'base_url': '_build/html'
    }
