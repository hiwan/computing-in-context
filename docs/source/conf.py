import os
import sphinx_rtd_theme

project = 'Your Project Name'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

if not os.path.exists('_static'):
    os.makedirs('_static')

if os.getenv('READTHEDOCS', None) == 'True':
    html_output = os.path.join(os.getenv('READTHEDOCS_OUTPUT', ''), 'html')
else:
    html_output = '_build/html'
    