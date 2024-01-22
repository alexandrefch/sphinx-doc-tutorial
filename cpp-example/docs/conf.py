from cgitb import html

extensions = ["breathe"]

html_theme = "shibuya"

html_theme_options = {
    "globaltoc_expand_depth": 1,
}

breathe_projects = {"my_project": "build/doxyxml/"}
breathe_default_project = "my_project"