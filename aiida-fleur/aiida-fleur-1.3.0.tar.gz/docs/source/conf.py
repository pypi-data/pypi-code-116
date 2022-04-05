# -*- coding: utf-8 -*-
#
# Fleur plugin documentation build configuration file, created by
# sphinx-quickstart on Wed Dec  7 16:39:12 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import aiida_fleur
import aiida
import sys
import os
import time
# Following 3 lines avoid the need of importing load_dbenv() for compiling the
# documentation -> works also without verdi install
sys.path.append(os.path.join(os.path.split(__file__)[0],
                             os.pardir, os.pardir))
sys.path.append(os.path.join(os.path.split(__file__)[0],
                             os.pardir))
os.environ['DJANGO_SETTINGS_MODULE'] = 'rtd_settings'


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('../aiida_fleur'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser',
              'sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig',
              'sphinx.ext.intersphinx',
              'sphinx.ext.viewcode',
              'sphinx_click.ext']

todo_include_todos = True

intersphinx_mapping = {
    'aiida': ('https://aiida-core.readthedocs.io/en/latest/', None),
    'masci-tools': ('https://masci-tools.readthedocs.io/en/latest/', None),
    'ase': ('https://wiki.fysik.dtu.dk/ase/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'python': ('https://docs.python.org/3', None),
    'lxml': ('https://lxml.de/apidoc/',None),
    'h5py': ('https://docs.h5py.org/en/latest/', None)
}

nitpick_ignore = [('py:obj', 'module')]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

myst_enable_extensions = []

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AiiDA-FLEUR'
#copyright = u'2016-2019, Jens Broeder'
copyright_first_year = 2016
copyright_owners = 'FZ Jülich GmbH, Germany'

current_year = time.localtime().tm_year
copyright_year_string = current_year if current_year == copyright_first_year else '{}-{}'.format(
    copyright_first_year, current_year)
copyright = f'{copyright_year_string}, {copyright_owners}. All rights reserved'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# The full version, including alpha/beta/rc tags.

release = aiida_fleur.__version__
# The short X.Y version.
version = '.'.join(release.split('.')[:3])

author = 'The AiiDA-FLEUR team.'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

#suppress_warnings = []

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'  # 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = 'http://aiida-fleur.readthedocs.io'

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# Output file base name for HTML help builder.
htmlhelp_basename = 'aiida-fleurdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'aiida-fleur.tex', 'AiiDa-FLEUR Documentation',
     author.replace(',', r'\and'), 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# on_rtd is whether we are on readthedocs.org, this line of code grabbed
# from docs.readthedocs.org
# NOTE: it is needed to have these lines before load_dbenv()
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Following 3 lines avoid the need of importing load_dbenv() for compiling the
# documentation -> works also without verdi install
# sys.path.append( os.path.join( os.path.split(__file__)[0],
#                                           os.pardir,os.pardir) )
# sys.path.append( os.path.join( os.path.split(__file__)[0],
#                                           os.pardir))
#os.environ['DJANGO_SETTINGS_MODULE'] = 'rtd_settings'

if not on_rtd:  # only import and set the theme if we're building docs locally
    try:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    except ImportError:
        # No sphinx_rtd_theme installed
        pass
    # Load the database environment by first loading the profile and then loading the backend through the manager
    from aiida.manage.configuration import get_config, load_profile
    from aiida.manage.manager import get_manager
    config = get_config()
    load_profile(config.default_profile_name)
    get_manager().get_backend()
else:
    # Back-end settings for readthedocs online documentation.
    from aiida.manage import configuration
    configuration.IN_RT_DOC_MODE = True
    configuration.BACKEND = 'django'
    configuration.AIIDADB_PROFILE = 'default'
    #Perform reentry scan
    from reentry import manager
    manager.scan()


'''
def run_apidoc(_):
    """Runs sphinx-apidoc when building the documentation.

    Needs to be done in conf.py in order to include the APIdoc in the
    build on readthedocs.

    See also https://github.com/rtfd/readthedocs.org/issues/1139
    """
    source_dir = os.path.abspath(os.path.dirname(__file__))
    apidoc_dir = os.path.join(source_dir, 'apidoc')
    package_dir = os.path.join(source_dir, os.pardir, os.pardir, 'aiida_fleur')

    # In #1139, they suggest the route below, but for me this ended up
    # calling sphinx-build, not sphinx-apidoc
    #from sphinx.apidoc import main
    #main([None, '-e', '-o', apidoc_dir, package_dir, '--force'])

    import subprocess
    cmd_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        cmd_path = os.path.abspath(os.path.join(sys.prefix, 'bin', 'sphinx-apidoc'))

    options = [
        '-o', apidoc_dir, package_dir,
        '--private',
        '--force',
        '--no-headings',
        '--module-first',
        '--no-toc',
        '--maxdepth', '4',
    ]

    # See https://stackoverflow.com/a/30144019
    env = os.environ.copy()
    env["SPHINX_APIDOC_OPTIONS"] = 'members,special-members,private-members,undoc-members,show-inheritance'
    subprocess.check_call([cmd_path] + options, env=env)

def setup(app):
    app.connect('builder-inited', run_apidoc)
'''

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'aiida-fleur', 'AiiDA-FLEUR Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'aiida-fleur', 'AiiDA-Fleur Documentation',
     author, 'aiida-fleur', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'AiiDA-FLEUR'
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3


# Warnings to ignore when using the -n (nitpicky) option
# We should ignore any python built-in exception, for instance
with open('nitpick-exceptions', 'r') as handle:
    nitpick_ignore = [
        tuple(line.strip().split(None, 1)) for line in handle.readlines() if line.strip() and not line.startswith('#')
    ]

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'theme_overrides.css',
]
