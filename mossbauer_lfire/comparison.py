
import numpy as np
import scipy.stats as st

import mossbauer_model
from scipy.interpolate import make_interp_spline, BSpline

import numpy as np
from scipy.stats import gaussian_kde

# Matplotlib parameters
import matplotlib.pyplot as plt
from matplotlib import rc
# Style
plt.style.use('default')
plt.rcParams['figure.figsize'] = (16.0, 8.0)
plt.rcParams.update({'font.size': 16})
# Fonts
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = r"\usepackage{amsmath}"

# --- COMPARING RANDOM VS OPTIMIZED DESIGN SELECTION --- #

# This file is used for both generating and plotting the error in posteriors by RMSE.
# Different numbers of priors can be used for this process.
# By controlling the variables of "generate" and "is_optimized", user can control the process.

# Some possible number of prior samples
list_of_sample_size = [10, 100, 200, 300, 400]

# Is this data-generating process or plotting process
generate = False

# Is design points optimized or randomly selected
is_optimized = True

# True theta value
true_theta = 0.5

# Initializing the mossbauer model and generating the data accordingly.
if generate:
    for i in list_of_sample_size:
        mossbauer_model.mossbauer(i, is_optimized)

#Random RMSE
rmse_random = []
for i in list_of_sample_size:
    if not generate:
        data = np.load('data/mossbauermodel_dim4False_sample{}.npz'.format(i), allow_pickle=True)
        filename = 'mossbauermodel_utility'

        # POSTERIOR
        prior_samples = data['prior_samples']
        ratios = data['r_obs']

        # Get some posterior samples from ratios
        ww = np.array(ratios)
        pp = prior_samples

        ww[ww == np.inf] = 0
        ws_norm = ww / np.sum(ww)

        K = 10000
        post = list()
        for _ in range(K):
            cat = np.random.choice(range(len(ws_norm)), p=ws_norm)
            post.append(pp[cat])
        post = np.array(post)

        # define kde smoothing and grid
        smooth = 0.35
        xs = np.linspace(np.min(prior_samples),np.max(prior_samples),1000)

        # get kde on grid
        density = gaussian_kde(post)
        density.covariance_factor = lambda : smooth
        density._compute_covariance()
        resampled = density.resample(size=50)
        error_sum = 0
        for sample in resampled[0]:
            error_sum = error_sum + ((true_theta - sample) ** 2)
        rmse_random.append(error_sum/50)

#Optimized RMSE
rmse_optimized = []
for i in list_of_sample_size:
    if not generate:
        data = np.load('data/mossbauermodel_dim4True_sample{}.npz'.format(i), allow_pickle=True)
        filename = 'mossbauermodel_utility'

        # POSTERIOR
        prior_samples = data['prior_samples']
        ratios = data['r_obs']
        # Get some posterior samples from ratios

        ww = np.array(ratios)
        pp = prior_samples

        ww[ww == np.inf] = 0
        ws_norm = ww / np.sum(ww)

        K = 10000
        post = list()
        for _ in range(K):
            cat = np.random.choice(range(len(ws_norm)), p=ws_norm)
            post.append(pp[cat])
        post = np.array(post)

        # define kde smoothing and grid
        smooth = 0.35
        xs = np.linspace(np.min(prior_samples),np.max(prior_samples),1000)

        # get kde on grid
        density = gaussian_kde(post)
        density.covariance_factor = lambda : smooth
        density._compute_covariance()
        resampled = density.resample(size=100)
        error_sum = 0
        for sample in resampled[0]:
            error_sum = error_sum + ((true_theta - sample) ** 2)
        rmse_optimized.append(error_sum/100)

# Smoothing the lines of plots
xnew = np.linspace(max(list_of_sample_size), min(list_of_sample_size), 300)
spl_random = make_interp_spline(list_of_sample_size, rmse_random, k=3)
smooth_random = spl_random(xnew)
spl_optimized = make_interp_spline(list_of_sample_size, rmse_optimized, k=3)
smooth_optimized = spl_optimized(xnew)

#Plotting the lines
plt.plot(xnew, smooth_random, label = "Random design points")
plt.plot(xnew, smooth_optimized, label = "LFIRE + MI")

plt.title("Random design points or LFIRE + MI")
plt.xlabel("Number of prior samples")
plt.ylabel("RMSE")

plt.legend()
plt.show()

# Printing the RMSE values
#print(rmse_random)
#print(rmse_optimized)
