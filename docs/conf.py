"""Configure Sphinx configuration."""
from __future__ import annotations

import os
import sys
from typing import Any
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))

source_suffix = ".md"
master_doc = "index"

project = "django-greeking"
year = datetime.now().year
copyright = f"{year} palewire"

exclude_patterns = ["_build"]

html_theme = "palewire"
html_sidebars: dict[Any, Any] = {}
html_theme_options: dict[Any, Any] = {
    "canonical_url": f"https://palewi.re/docs/{project}/",
    "nosidebar": True,
}

pygments_style = "sphinx"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
