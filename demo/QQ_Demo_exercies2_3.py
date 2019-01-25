import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# create data
# data = np.random.exponential(1,100)
# data = sorted(data, reverse = True)
# data = np.exp(data)
# index = np.ones(100)
# np.savetxt("QQ_Demo.txt", np.c_[index,data], fmt='%.2f', delimiter = ",")

# load data
mydata = pd.read_csv('QQ_Demo.txt', header = None)
y = np.log(mydata.ix[0:49,1]) # Row: 0-49, Column: 1
print(y)

# 4) Exponential QQ-plot
stats.probplot(y, dist = "expon", plot = plt)
plt.title ("Blah~")
plt.show()

# save it to one pdf file
# pp = PdfPages('Demo_Plot.pdf')
# pp.savefig()
# pp.close()
