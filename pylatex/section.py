# -*- coding: utf-8 -*-
"""
This module implements the class that deals with sections.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from .utils import dumps_list
from .base_classes import Container, Command


# TODO move base class to base_classe submodule
class SectionBase(Container):

    """A class that is the base for all section type classes.

    :param title:
    :param numbering:
    :param data:

    :type title: str
    :type numbering: bool
    :type data: list
    """

    def __init__(self, title, numbering=True, data=None):
        self.title = title
        self.numbering = numbering

        super().__init__(data)

    def dumps(self):
        """Represent the section as a string in LaTeX syntax.

        :return:
        :rtype: str
        """

        if not self.numbering:
            num = '*'
        else:
            num = ''

        section_type = self.__class__.__name__.lower()
        string = Command(section_type + num, self.title).dumps()
        string += dumps_list(self)

        super().dumps()

        return string


class Section(SectionBase):

    """A class that represents a section."""


class Subsection(SectionBase):

    """A class that represents a subsection."""


class Subsubsection(SectionBase):

    """A class that represents a subsubsection."""
