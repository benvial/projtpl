"""This module define a model"""


class Person:
    """Short summary.

    Parameters
    ----------
    name : type
        Description of parameter `name`.
    age : type
        Description of parameter `age`.

    Attributes
    ----------
    name
    age

    """

    def __init__(self, name, age):
        """Short summary.

        Parameters
        ----------
        name : type
            Description of parameter `name`.
        age : type
            Description of parameter `age`.

        Returns
        -------
        type
            Description of returned object.

        """
        self.name = name
        self.age = age

    def myfunc(self):
        """Short summary.

        Parameters
        ----------


        Returns
        -------
        type
            Description of returned object.

        """
        print("Hi, my name is {}".format(self.name))
