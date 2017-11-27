"""Model class template.

NEED TO:
Copy this file, rename it to the name of your model,
then adjust or fill in code and documentation wherever marked by "NEED TO:",
finally remove these instructions.
See the model development tutorial for details.
"""
# This file is part of pycopancore.
#
# Copyright (C) 2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

# all models must use the base component
from pycopancore import base

#
# NEED TO: import all other needed model components:
#
# Model components are either provided by pycopancore
from pycopancore.model_components import SOMECOMPONENT

# Or you implement your own components
from model_components import first_component
from model_components import second_component

# entity types:

# NEED TO: compose all needed entity type implementation classes
# by mixing the above model components' mixin classes of the same name.
# Only compose those entity types and process taxons that the model needs,
# delete the templates for the unneeded ones, and add those for missing ones:

# NEED TO: list all mixin classes needed:
class World(SOMECOMPONENT.World,
            first_component.World,
            second_component.World,
            base.World):
    """World entity type."""
    pass


# NEED TO: list all mixin classes needed:
class Society(SOMECOMPONENT.Society,
              first_component.Society,
              second_component.Society,
              base.Society):
    """Society entity type."""
    pass


# NEED TO: list all mixin classes needed:
class Cell(SOMECOMPONENT.Cell,
           first_component.Cell,
           second_component.Cell,
           base.Cell):
    """Cell entity type."""
    pass


# NEED TO: list all mixin classes needed:
class Individual(SOMECOMPONENT.Individual,
                 first_component.Individual,
                 second_component.Individual,
                 base.Individual):
    """Individual entity type."""
    pass


# process taxa:

# NEED TO: do the same for process taxa:

# NEED TO: list all mixin classes needed:
class Nature(SOMECOMPONENT.Nature,
             first_component.Nature,
             second_component.Nature,
             base.Nature):
    """Nature process taxon."""
    pass


# NEED TO: list all mixin classes needed:
class Metabolism(SOMECOMPONENT.Metabolism,
                 first_component.Metabolism,
                 second_component.Metabolism,
                 base.Metabolism):
    """Metabolism process taxon."""
    pass


# NEED TO: list all mixin classes needed:
class Culture(SOMECOMPONENT.Culture,
              first_component.Culture,
              second_component.Culture,
              base.Culture):
    """Culture process taxon."""
    pass


# Model class:

# NEED TO: list all used model components:
class Model(SOMECOMPONENT.Model,
            first_component.Model,
            second_component.Model,
            base.Model):
    """Class representing the whole model."""

    name = "..."
    """Name of the model"""
    description = "..."
    """Longer description"""

    # NEED TO: list all entity types you composed above:
    entity_types = [World, Society, Cell, Individual]
    """List of entity types used in the model"""

    # NEED TO: list all entity types you composed above:
    process_taxa = [Nature, Metabolism, Culture]
    """List of process taxa used in the model"""
