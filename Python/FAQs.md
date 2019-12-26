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






## References

- [Questions and Answers](https://www.tutorialspoint.com/How-to-check-version-of-python-modules)
