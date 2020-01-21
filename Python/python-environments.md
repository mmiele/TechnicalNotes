# Python environments in Visual Studio code

An **environment** in Python is the **context** in which a program runs. An environment consists of an interpreter and any number of installed packages. The Python extension for VS Code provides helpful integration features for working with different environments.

> **Note**. If you're looking to get started with Python in Visual Studio Code, see [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial).

A **context** includes one of the following environments:

- global
- virtual
- [conda](https://www.anaconda.com/)

An environment consists of:

- an interpreter
- a library (typically the Python Standard Library)
- a set of installed packages

> **Note**.
> An environment determine which language constructs and syntax are valid, what operating-system functionality you can access, and which packages you can use.


## Select and activate an environment

By default, the Python extension looks for and uses the first **Python interpreter** it finds in the system path. If it doesn't find an interpreter, it issues a warning.
To select a specific environment, use the **Python: Select Interpreter** command from the **Command Palette `(Ctrl+Shift+P)`**.

![select-environment](../Media/Python/select-environment.PNG)

You can switch environments at any time; switching environments helps you test different parts of your project with different interpreters or library versions as needed.
The Python: Select Interpreter command displays a list of available global environments, conda environments, and virtual environments. 

Selecting an interpreter from the list adds an entry for `python.pythonPath` with the path to the interpreter inside your **Workspace Settings**. Because the path is part of the workspace settings, the same environment should already be selected whenever you open that workspace. If you'd like to set up a default interpreter for your applications, you can instead add an entry for `python.pythonPath` manually inside your **User Settings**. To do so, open the **Command Palette `(Ctrl+Shift+P)`** and enter **Preferences: Open User Settings**. Then set `python.pythonPath`, which is in the **Python extension** section of *User Settings*, with the appropriate interpreter.

The Python extension uses the selected environment for running Python code. Activate a **New Terminal** from, switch to the directory where the Python file is, the run the command `python filename.py`. 

When you have a .py file open in the editor, and open a terminal, VS Code automatically activated the selected environment.

**Note**. To prevent automatic activation of a selected environment, add `"python.terminal.activateEnvironment": false` to your `settings.json` file. It can be placed anywhere as a sibling to the existing settings.

To edit the `settings.json` file, perform these steps:

1. Open the **Command Palette** by entering `(Ctrl+Shift+P)` on your keyboard.
1. In the input box, enter **Python: Select Interpreter** command from the **Command Palette `(Ctrl+Shift+P)` **Preferences: Open Default Settings (JSON)**.
1. Add the settings:

    ```json
    {
        "python.terminal.activateEnvironment": false
    }
    ```

## References

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments#_global-virtual-and-conda-environments)
- [How to create and manage Python environments in Visual Studio](https://docs.microsoft.com/en-us/visualstudio/python/managing-python-environments-in-visual-studio?view=vs-2019)

