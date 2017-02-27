"""Define base.individual class.

In this module the basic Individual mixing class is composed to set the basic
structure for the later in the model used Indvidual class. It Inherits from
Individual_ in that basic variables and parameters are defined.
"""

# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate Impact
# Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

#
#  Imports
#

from pycopancore.model_components import abstract
from .interface import Cell_, Individual_

#
#  Define class Individual
#


class Individual(Individual_, abstract.Individual):
    """Define properites of base.individual.

    Basic Individual mixin class that every model must use in composing their
    Individual class. Inherits from Individual_ as the interface with all
    necessary variables and parameters.
    """

    # standard methods:

    def __init__(self,
                 # *,
                 cell=None,
                 **kwargs
                 ):
        """Initialize an instance of Individual.

        Parameters
        ----------
        cell:
        kwargs:
        """
        super().__init__(**kwargs)

        assert isinstance(cell, Cell_), "cell must be an instance of Cell"
        self.cell = cell


    # setters for references:
    
    @residence.setter
    def residence(self, c):
        assert isinstance(c, Cell_)
        if self.world is not None: self.cell.residents.remove(self) 
        c.cell.add(self) 
        self.residence = c


    processes = []