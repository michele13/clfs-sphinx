# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Cross-Compiled Linux From Scratch - Embedded'
copyright = '2005-2024, Andrew Bradford, Joe Ciccone, Jim Gifford, Maarten Lankhorst, Ryan Oliver, & Michele Bucca'
author = 'Andrew Bradford, Joe Ciccone, Jim Gifford, Maarten Lankhorst, Ryan Oliver, & Michele Bucca'


# Get the current date in YYYYMMDD format
import datetime
current_date = datetime.datetime.now().strftime("%Y%m%d")

# Set the version
version = f'GIT-{current_date}'
release = version

# --- Footer ---

rst_epilog = """
.. include:: /include/packages.txt
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 
   'sphinx.ext.duration',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_title = 'Cross-Compiled Linux From Scratch - Embedded'
html_title = 'CLFS - Embedded'
html_theme = 'furo'
html_static_path = ['_static']
