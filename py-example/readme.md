<div align="center">

# Sphinx documentation from python docstring

</div>

## :tv: Demo

```sh
# Installing dependencies
pip3 install sphinx sphinx_rtd_theme

# Generating documentation
cd docs
make html
```

You can acces it through `docs/build/html/index.html`.

## :rocket: How to use it ?

**1. Generate the sphinx structure**

In a first place, you need to generate the sphinx documentation using
the command `sphinx-quickstart` inside a `docs` folder as below :

```sh
mkdir docs
cd docs
sphinx-quickstart --sep -l "fr" -r 1.0 .
```

Now your project structure should look like this

```
my_project/
├── docs/
│   ├── build/
│   ├── source/
│   ├── conf.py
│   ├── make.bat
│   └── Makefie
├── src
└── readme.md
```

**2. Edit sphinx config**

And lastly you need to copy the next script at the end of the `conf.py` file.
This script add the needed configuration to allow sphinx to generate the documentation from the docstring inside all your `.py` files.
(You don't need to change anything in the next configuration)

```py
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
print(os.path.abspath('../..'))

extensions += [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

autosummary_generate = True
```

**3. Link the doc to a toctree**

Now you need to link the documentation somewhere in your sphinx `rst` file.
The best way is to go in `source/index.rst` and add `api/library_root` as an entry of the toctree.

```css
.. autosummary::
    :toctree: api
    :recursive:

    <source_directory>
```

> **Info**
> In our case `<source_directory>` is `pyexample`

**4. Now you can generate !**

Inside the `docs` directory you can now execute `make html` !
You can acces it through `docs/build/html/index.html`.

> **Warning**
> Do not store the `build` folder in your remote storage, if you use `git` simply copy the `.gitignore` inside `py-example/docs` and paste it to your `docs` folder.