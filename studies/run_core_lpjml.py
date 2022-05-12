"""Dummy run script for LPJmL coupling"""

# This file is part of pycopancore.
#
# Copyright (C) 2022 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
 
import pycopancore.models._testing.lpjml.lpjml_dummy as M 

# standard runner for simulating any model:
from pycopancore.runners.runner import Runner

from pycopancore import master_data_model as D  # to be able to specify variables with physical units

import numpy as np  # which is usually needed
from numpy.random import choice, uniform  # to generate random initial conditions

import pylab as plt  # to plot stuff

# instantiate the model and have it analyse its own structure:
model = M.Model()


# TODO: initial coupling

#include config of LPJmL (maybe in own .py)    
#from pycoupler.coupler import Coupler
#from pycoupler.data import supply_inputs, preprocess_inputs
 
 
# paths
base_path = "/p/projects/open/Jannes/copan_core/lpjml_test"
config_coupled_fn = f"{base_path}/config_coupled.json"
 
# coupled simulation years
start_year = 1981
end_year = 2005
sim_years = range(start_year, end_year+1)
 
# initiate coupler after run_lpjml on LOGIN NODE 1
#coupler = Coupler(config_file=config_coupled_fn)
 
# get and process initial inputs
#inputs = supply_inputs(config_file=config_coupled_fn,
                       #historic_config_file=config_historic_fn,
                       #input_path=f"{base_path}/input",
                       #model_path=model_path,
                       #start_year=start_year, end_year=start_year)
#input_data = preprocess_inputs(inputs, grid=coupler.grid, time=start_year)

# simulation parameters:

delta_t = 1  # desired temporal resolution of the resulting output.
 
# TODO ? dt_lpjml = dt*12 #adjust temporal scales?
 
end_year = 2005
# test_dict_in = {"landuse": np.zeros((1, 64)),"fertilizer_nr": np.zeros((1, 32))}
# test_dict_out = {"cftfrac": np.zeros((1, 32)),"pft_harvestc": np.zeros((1, 32)),"pft_harvestn": np.zeros((1, 32))}


# exchange for tillage variable
# adjust reading and writing as in Jannes' test script
# fkt die output auf hohem level als argument entgegennimmt
test_dict_in = {"with_tillage": np.zeros((1, 1))}
test_dict_out = {"cftfrac": np.zeros((1, 32)), "pft_harvestc": np.zeros((1, 32))}

landuse_update_rate = 10
landuse_update_prob = 1.

t_max = 2008  # interval for which the model will be simulated
dt = 0.1  # desired temporal resolution of the resulting output.


# instantiate process taxa:
env = M.Environment(
    delta_t = delta_t, #dt should be given to environment probably
    end_year = end_year, #our starting point
    in_dict = test_dict_in,
    out_dict = test_dict_out,
    old_out_dict = test_dict_out
    
    )
met = M.Metabolism(
    landuse_update_rate = landuse_update_rate,
    landuse_update_prob = landuse_update_prob
    )
cul = M.Culture(
    )

# generate entities:

world = M.World(
    environment = env,
    metabolism = met,
    culture = cul,
    )
soc = M.SocialSystem(world = world)
cell = M.Cell(
    social_system = soc,
    lpjml_grid_cell_ids = [0],
    # landuse = test_dict_in["landuse"][0]
    with_tillage = test_dict_in["with_tillage"][0],
    )
ind = M.Individual(cell = cell)

# Run the model
#

runner = Runner(model=model)
traj = runner.run(t_0=2005, t_1=t_max, dt=dt)

# TODO: Add some further analysis such as plotting or saving
# plt.plot(traj['t'], traj[M.SocialSystem.population][socs[0]])
# plt.show()
