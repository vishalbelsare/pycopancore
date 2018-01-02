"""
Cell entity type mixing class template.

TODO: adjust, uncomment or fill in code and documentation wherever marked by
the "TODO" flag.
"""
# This file is part of pycopancore.
#
# Copyright (C) 2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>

from .. import interface as I

class Cell (I.Cell):
    """Cell entity type mixin implementation class."""

    def __init__(self,
                 # *,  # TODO: uncomment when adding named args after this
                 **kwargs):
        """Initialize an instance of Cell."""
        super().__init__(**kwargs)  # must be the first line
        # TODO: add custom code here
        pass


    # TODO: uncomment neccessary standard methods
    # def deactivate(self):
    #     """Deactivate a cell."""
    #     # TODO: add custom code here
    #     pass
    #     super().deactivate()  # must be the last line

    # def reactivate(self):
    #     """Reactivate a cell."""
    #     super().reactivate()  # must be the first line
    #     # TODO: add custom code here
    #     pass

    # TODO: add process-related methods if needed
    
    # TODO: instantiate and list process objects here
    processes = []  
