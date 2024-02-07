# Documentation
The documentation currently relies on having sphinx and sphinx_rtd_theme installed. This, however, won't
be necessary when package management is implemented.

## Generating the documentation
To generate the autodoc documentation, the following command must be run from the project root:
```bash
sphinx-apidoc -o doc/source .
```

To then generate the html files, run the command 

```bash
make html
```
from within the `doc` directory.

## Viewing the documentation
The documentation can be viewed by opening the file `doc/build/index.html` in a web browser.

## Things to consider when creating modules
1. Do not use hyphens in module names, it will most likely cause the autodoc to fail. Use underscores instead.
2. Each module must have a `__init__.py` file in the directory to be considered a package. If it 
doesn't have one, it won't be seen by the autodoc.
