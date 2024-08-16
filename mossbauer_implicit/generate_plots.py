#!/usr/bin/env python3

import plotting
import numpy as np

# --- PLOTTING DATA: MOSSBAUER MODEL --- #

data = np.load('mossbauer_implicit/mossbauermodel_dim4.npz', allow_pickle=True)
filename = 'mossbauermodel_utility'

# UTILITY
if type(data['bo_obj']) == np.ndarray:
    obj = data['bo_obj'].tolist()
else:
    obj = data['bo_obj']
#plotting.plot_acquisition(obj, data['d_opt'], filename=filename)

# POSTERIOR
pp = data['prior_samples']
rr = data['r_obs']
plotting.plot_posterior(pp, rr, model='mossbauer', truth=0.5)

# --- PLOTTING DATA: SIR MODEL --- #

data = np.load('./sirmodel_dim1.npz')
filename = 'sirmodel_utility'

# UTILITY
if type(data['bo_obj']) == np.ndarray:
    obj = data['bo_obj'].tolist()
else:
    obj = data['bo_obj']
plotting.plot_acquisition(obj, data['d_opt'], filename=filename)

# POSTERIOR
pp = data['prior_samples']
rr = data['r_obs']
plotting.plot_posterior(pp, rr, model='sir', truth=np.array([0.15, 0.05]))
