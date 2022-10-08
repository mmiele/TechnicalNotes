# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""This is the module summary. Only add one or two lines of documentation
here as it shows up in a list. Remarks are ignored here, so don't include them.
"""

# from my_other_module import *

class MyClass:
    """
    Put a one or two line summary here. It will show up in a list as well so it
    should be terse and informative.

    .. remarks::

        This is where you put the meat of your documentation. **The preceding empty line and
        indentation are critical** or your documentation won't work.

        Remember that your summary line will show as well, so the remarks section should follow
        naturally, or at least relate well to your summary line.

        In the remarks section you should be very verbose about how your class works and include
        inline code samples, see also, and other relevant examples. For example:

        * Bulleted lists!
        * Numbered lists using numbers or #
        * Most Markdown syntax works just great!

        .. code-block:: python

            # This is a code block
            my_class = MyClass(a, b, c)

            # If things don't render correctly, check the spacing around documentation blocks

        Parameters for the __init__ method need to be documented on the class construct to appear
        in the documentation. Write meaningful docstrings that help the user! If there are explicit
        values that are required, supply the ranges, list, or a link to where the user can find the
        information!

    :param name: The name of the object
    :type name: str
    :param description: An optional description
    :type description: str
    """

    def __init__(self, name, description=None):
        """
        The docstring for __init__ is  ignored by the documentation system but you still
        need to write it or build will generate PEP warnings

        :param name: The name of the object
        :type name: str
        :param description: An optional description
        :type description: str

        """

        self.name = name
        self.description = description

    def my_func(self):
        """
        This is a summary string that gives a basic description that shows in a list.
        Only use one or two lines of text.

        .. remarks::

            This is where you put the interesting part of the documentation including

            .. note::

                This is a highlighted note in a box

            and

            .. code-block:: python

                # This is a code sample
                result = my_class.my_func()

            Also a great opportunity to add links to other functions like :func:`my_other_func` and
            other classes like :class:`my_other_module.MyOtherClass`

        :return: Another class
        :rtype: my_other_module.MyOtherClass

        """

        value = self.my_other_func(3, _my_private_param = 2)

        return self._my_private_func(value)

    def my_other_func(self, my_public_param, _my_private_param = 1):
        """
        Summary string is sometimes sufficient if the function is simple

        :param my_public_param: Description of the parameter
        :type my_public_param: int
        :param _my_private_param: Private parameters (with _) are not rendered in documentation by default
        :type _my_private_param: int
        :return: A value
        :rtype: int

        """

        return my_public_param * _my_private_param

    def _my_private_func(self, my_value):
        """
        Private functions (with _) are not rendered in documentation by default
        but still need docstrings to avoid PEP warnings.

        :param my_value: Description of the parameter
        :type my_value: int
        :return: A new other object
        :rtype: my_other_module.MyOtherClass

        """

        return self._my_private_func(my_value)