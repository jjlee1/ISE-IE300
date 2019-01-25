import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import pareto

# #Quantile function of the Pareto random variable
def pareto_RV(alpha):
 	p = np.random.uniform(0,1)
 	x = ((1.0 - p)**(-1.0/alpha))
 	return x
#
 # alpha is a Pareto Index, s is a number of samples to generate
def pareto_RVs(alpha,s):
 	z = np.zeros(s)
 	for i in range(s):
 		z[i] = pareto_RV(alpha)
 	return z

z = pareto_RVs(1.5,100)

#z = pareto.rvs(1.5, size=100)
#r = norm.rvs(size=100)

stats.probplot(z, dist="expon", plot=plt)
plt.title("Exponential QQ-plot")
plt.show()

stats.probplot(z, dist="norm", plot=plt)
plt.title("Normal QQ-plot")
plt.show()

# stats.probplot(r, dist="norm", plot=plt)
# plt.title("Normal QQ-plot2")
# plt.show()
