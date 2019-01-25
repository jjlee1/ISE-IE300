import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# generate 80 samples of U(0,1)
data=np.random.rand(80)

#create Exponential QQ-plot
sorted_data=sorted(data)
stats.probplot(sorted_data, dist="expon", plot=plt)
plt.title("Exponential QQ-plot")
plt.show()


#x=np.arange(-2,5,0.001)
x=np.linspace(-2,5,1000)
y_uniform=np.zeros(len(x))
y_expon=np.zeros(len(x))


for i in range(0,len(x)):
    if x[i]>=0:
      y_expon[i]=np.exp(-x[i])
    else:
      y_expon[i]=0


for i in range(0,len(x)):
    if x[i]>=0 and x[i]<=1:
      y_uniform[i]=1
    else:
      y_uniform[i]=0

#PDF plot
plt.plot(x, y_uniform)
plt.plot(x, y_expon, 'r--')
plt.axis([-2,5,0,1.1])

plt.show()


