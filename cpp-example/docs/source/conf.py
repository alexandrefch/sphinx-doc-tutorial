# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cpp-example'
copyright = '2024, Alexandre Foucher'
author = 'Alexandre Foucher'
release = '1.0'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -----------------------------------------------------------------------------

extensions += ['breathe','exhale']

breathe_projects = {"My Project": "../build/_doxygen/xml"}
breathe_default_project = "My Project"

exhale_args = {
    "containmentFolder":     "./api",
    "rootFileName":          "library_root.rst",
    "doxygenStripFromPath":  "..",
    "rootFileTitle":         "Library API",
    "createTreeView":        True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    "INPUT = ../../include"
}