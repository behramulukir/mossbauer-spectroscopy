#!/usr/bin/env python3

import numpy as np
import scipy.stats as st

import simulator
import staticdesign

def mossbauer(sample_size, optimization):
    # Set these to change performance of experimental design

    # Is the process optimized or randomly selected
    optimized = str(optimization)

    # CPU cores to use
    num_cores = 1 

    # Set dimensions of design variable
    dimensions = 4

    # Number of prior samples (higher => more accurate posterior)
    sample_number = sample_size

    # Max number of utility evaluations in bayesian optimization (per core)
    iteration_number = 10

    # number of initial data points for bayesian optimization
    if num_cores > 5:
        initial_points = num_cores
    else:
        initial_points = 5

    # Sampling prior values for theta value
    mu, sigma = 0, 1
    prior_mossbauer = st.norm.rvs(mu,sigma,size=sample_number)

    # Define the domain for bayesian optimization
    domain_mossbauer = [{'name': 'var_1', 'type': 'continuous', 'domain': (-3.00, 3.00), 'dimensionality':int(dimensions)}]

    # Define the constraints for BO
    # Time cannot go backwards
    if dimensions==1:
        constraints = None
    elif dimensions>1:
        constraints = list()
        for i in range(1,dimensions):
            dic = {'name':'constr_{}'.format(i), 'constraint':'x[:,{}]-x[:,{}]'.format(i-1, i)}
            constraints.append(dic)
    else:
        raise ValueError()

    # Define the simulator model
    true_theta = 0.5
    model_mossbauer = simulator.Mossbauer(true_theta)

    BED_mossbauer = staticdesign.StaticBED(prior_mossbauer, model_mossbauer, domain=domain_mossbauer, constraints=constraints, num_cores=num_cores)
    BED_mossbauer.optimisation(init_num=initial_points, max_iter=iteration_number, is_optimized=optimization)

    # ---- SAVE MODEL ------ #
    file = './mossbauermodel_dim{}'.format(dimensions) + optimized + '_sample{}'.format(sample_number)
    BED_mossbauer.save(filename=file)
