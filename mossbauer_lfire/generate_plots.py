#!/usr/bin/env python3

import plotting
import numpy as np

# --- PLOTTING DATA: MOSSBAUER MODEL --- #

data = np.load('data/mossbauermodel_dim4False_sample200.npz', allow_pickle=True)
filename = 'mossbauermodel_utility'

# POSTERIOR
pp = data['prior_samples']
rr = data['r_obs']
plotting.plot_posterior(pp, rr, model='mossbauer', truth=0.5)