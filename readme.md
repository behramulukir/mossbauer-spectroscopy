## Description
This repository includes my work drafts at Aalto University, Probabilistic Machine Learning group. The topic was Bayesian experimental design.

In specific, this work is on Mössbauer spectroscopy, which is a spectroscopic technique that is used to observe nuclear interactions. <br>
Those interactions might be informative regarding the physical properties of a material.

Since the likelihood function was not present in the paper on which this work is based, it was not possible to use a standard Bayesian experimental design. <br>
Instead, a likelihood-free Bayesian experimental design method based on a framework called "LFIRE" is used.

## Sources

The main theoretical sources for this work were:
* C. Feng, ‘Optimal Bayesian experimental design in the presence of model error’, Massachusetts Institute of Technology, Center for Computational Engineering, 2015. [(PDF)](https://github.com/behramulukir/mossbauer-spectroscopy/blob/main/sources/Optimal%20Bayesian%20experimental%20design%20in%20the%20presence%20of%20model%20error.pdf) 
* S. Kleinegesse and M. Gutmann, ‘Efficient Bayesian Experimental Design for Implicit Models’, 10 2018. [(PDF)](https://github.com/behramulukir/mossbauer-spectroscopy/blob/main/sources/Efficient%20Bayesian%20Experimental%20Design%20for%20Implicit%20Models.pdf)
* O. Thomas, R. Dutta, J. Corander, S. Kaski, and M. U. Gutmann, ‘Likelihood-free inference by ratio estimation’, 11 2016. [(PDF)](https://github.com/behramulukir/mossbauer-spectroscopy/blob/main/sources/Likelihood-free%20inference%20by%20ratio%20estimation.pdf)

Most of the code is based on S. Kleinegesse and M. Gutmann's work and especially on the code that is published by S. Kleinegesse:
* [bedimplicit](https://github.com/stevenkleinegesse/bedimplicit)

You can check the sources folder to see all the papers used during the work.

## Tech-stack
The work is coded in Python. Jupyter notebooks were used as an experimentation tool. <br>
In this work, Python libraries such as NumPy, matplotlib, SciPy, glmnet, GPyOpt were also used.
