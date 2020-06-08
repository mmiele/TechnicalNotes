# FAQs




## How to check version of python modules?

When you install Python, you also get the Python package manager **pip**. You can use pip to get the versions of python modules. If you want to list all installed Python modules with their version numbers, use the following command:

```cmd
$ pip freeze
```
To individually find the version number you can grep on this output. For example, in windows, you can use **findstr** instead of grep. For example:

```cmd
pip freeze | findstr botbuilder-dialogs
```

## \__init__.py

From [What is __init__.py ?](https://pythontips.com/2013/07/28/what-is-__init__-py/).

Files name `__init__.py` are used to mark directories on disk as **Python package directories**. If you have these files:

- `mydir/classes/__init__.py`
- `midir/classes/module.py`

and if `mydir` is on your path, you can import the code in `module.py` using this statement:

- `import classes.module` or
- `from classes import module`

If you remove the `__init__.py` file, Python will no longer look for sub-modules inside that directory, so attempts to import the module will fail.

The `__init__.py` file is usually empty, but can be used to export selected portions of the package under more convenient name, hold convenience functions, etc. Given the example above, the contents of the init module can be accessed as `import classes`.

For mor information, see [Packages](http://docs.python.org/tutorial/modules.html#packages) in the official documentation.


The `__init__.py` files are required to make Python treat the
directories as containing packages; this is done to prevent
directories with a common name, such as string, from
unintentionally hiding valid modules that occur later on the
module search path. In the simplest case,`__init__.py` can just
be an empty file, but it can also execute initialization code
for the package or set the `__all__` variable, described later.

Source : http://effbot.org/pyfaq/what-is-init-py-used-for.htm


## requirements.txt





## References

- [Questions and Answers](https://www.tutorialspoint.com/How-to-check-version-of-python-modules)
- [Installing Packages from Multiple Servers from One or More Requirements File](https://stackoverflow.com/questions/29289695/installing-packages-from-multiple-servers-from-one-or-more-requirements-file)