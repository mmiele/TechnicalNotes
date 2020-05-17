# Python examples
This folder contains various examples to play with the Python language.
> NOTE
> Nothing fancy. But to get the job done.

On a separate topic: in order to create sub-folders in GitHub, you must have at least a file in the parent folder, such as this [README.md](README.md) file. It took me a while to get it. For more information, see [Creating folders inside a GitHub repository without using Git](https://stackoverflow.com/questions/18773598/creating-folders-inside-a-github-repository-without-using-git).

## Building the documentation

1. In the terminal window, navigate to the directory that contains the code directory, in this case `C:\Users\v-mimiel\aWork\GitHub\TechnicalNotes\Python\examples`.
1. Enter the command `sphinx-quickstart`.
    1. Assure to create a **source** folder by answering `y` to the question *Separate source and build directories (y/n) [n]: y*.
    1. Also enter the name of the code directory:
        *Root path for the documentation [.]: examples*
1. Modify the `config.py` file to contains the following lines:
    1. `import os`
    1. `import sys`
    1. `sys.path.insert(0, os.path.abspath('.'))`
    1. `extensions = ['sphinx.ext.autodoc', 'docfx_yaml.extension']`
1. Execute the command `sphinx-apidoc -o source .` to generate the `.rst` files.
1. Execute the command  `sphinx-build source build` to generate the documentation in the `build` folder.
1. Execute the command: `"C:\Program Files\docfx\docfx.exe" init -q`. This creates a new `docfx_project` folder.
1. Copy the YAML files previously generated via Sphinx in `_build/docfx_yaml` into the `docfx_project/api folder`.
1. Navigate to the `docfx_project` directory.
1. Build the site (on line docs) and serve by running this command:
`"C:\Program Files\docfx\docfx.exe" --serve`.
1. In your browser, navigate to http://localhost:8080 to see the online docs.

## References

- [From Sphinx to DocFX - Generating Python API Documentation with DocFx ](http://blog.travelmarx.com/2020/02/from-sphinx-to-docfx-generating-python-api-documentation.html)
- [Python Documentation using Sphinx ](https://www.patricksoftwareblog.com/python-documentation-using-sphinx/)