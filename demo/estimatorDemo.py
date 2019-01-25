import pandas as pd
import numpy as np
mydata = pd.read_csv('Demo2.txt', header = None,  sep='\t', thousands=',')
R_array = np.array([130,140])

# Estimator 1
for i in range(len(R_array)):
    t = R_array[i]
    excess_data = mydata[1][mydata[1] > t] - t
    #print(excess_data)
    pi_1 = excess_data.sum()/mydata.shape[0]
    print ("R = " + str(t) + " and Pi_1 = " + str(pi_1))

# Estimator 3
n = mydata.shape[0]
k = 2
data = mydata[1]
log_data = np.log(mydata[1])
#print(log_data.shape)

for i in range(len(R_array)):
    R = R_array[i]
    x_n_minus_k = data[k]
    log_x_n_minus_k = log_data[k] # (k + 1)th largest observation
    log_data_k = log_data.iloc[0:(k-1)]
    #print(log_data_k)
    gamma_hat_k_n = log_data_k.mean() -  log_x_n_minus_k
    pi_3 = R/(1.0/gamma_hat_k_n - 1.0) * (k/float(n))*(R/float(x_n_minus_k)) ** (-1/(gamma_hat_k_n))
    print(pi_3)
