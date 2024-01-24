<div align="center">

# Sphinx documentation from c/c++ doxygen doc

</div>

## :tv: Demo

```sh
# Installing dependencies
pip3 install sphinx shibuya breathe exhale
sudo apt-get install doxygen

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
This script add the needed configuration to allow sphinx to generate the documentation from doxygen documentation inside `.h`,`.c`,`.cpp`,`.hpp`... (You don't need to change anything in the next configuration)

```py
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
```

**3. Link the doc to a toctree**

Now you need to link the documentation somewhere in your sphinx `rst` file.
The best way is to go in `source/index.rst` and add `api/library_root` as an entry of the toctree.

```css
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/library_root
```

**4. Now you can generate !**

Inside the `docs` directory you can now execute `make html` !
You can acces it through `docs/build/html/index.html`.