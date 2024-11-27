import os

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
if os.environ.get('READTHEDOCS') == 'True':
    html_output_dir = os.environ.get('READTHEDOCS_OUTPUT', '_build/html')
    html_output = os.path.join(html_output_dir, 'html')
