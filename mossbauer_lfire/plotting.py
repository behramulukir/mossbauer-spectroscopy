#!/usr/bin/env python3

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

# Utility information
from GPyOpt.acquisitions import AcquisitionEI
from GPyOpt.util.general import normalize

# ------- POSTERIOR PLOTS ------- #

def plot_posterior(prior_samples, ratios, model, truth, filename = None):

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

    if model=='mossbauer':
        # define kde smoothing and grid
        smooth = 0.35
        xs = np.linspace(np.min(prior_samples),np.max(prior_samples),1000)

        # get kde on grid
        density = gaussian_kde(post)
        density.covariance_factor = lambda : smooth
        density._compute_covariance()
        kde = density(xs)
        
        # make plot
        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(111)
        ax.plot(xs, kde, lw=2, label='Posterior KDE')
        ax.axvline(truth, ls='--', c='r', lw=2, label=r'$theta_{\text{true}}$', alpha=0.5)
        ax.grid(True, ls='--')
        ax.tick_params(labelsize=20)
        ax.set_xlabel(r'theta', size=20)
        ax.set_ylabel(r'Posterior Density', size=20)
        ax.legend(prop={'size': 17})

        plt.tight_layout()

    else:
        raise NotImplementedError()

    if filename:
        plt.savefig('{}.pdf'.format(filename))
        plt.savefig('{}.png'.format(filename))
    else:
        plt.savefig('./mossbauermodel_dim4False_sample200.pdf')
        plt.savefig('./mossbauermodel_dim4False_sample200.png')
