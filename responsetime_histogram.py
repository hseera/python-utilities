# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#for testing purpose use the file responsetime_histogram.csv provided
FILE = "./sample_files/responsetime_histogram.csv" #replace with your file name

df = pd.read_csv(FILE)

x = []
x = df['elapsed_time'].dropna() #replace "elapsed_time' with the correct colume name. Add dropna() incase you have empty row values

plt.figure(figsize=(10,6))

#parameters for the histogram. Update the values when you want to plot multiple histogram together
#kwargs = dict(histtype='step', stacked=False, alpha=0.7, fill=False, bins=500)
kwargs = dict(histtype='stepfilled', stacked=False, alpha=0.7, fill=True, bins=20000)

#define historgram label
plt.xlabel('Response Time (ms)')
plt.ylabel('Frequency')

#plot histogram
plt.hist(x, **kwargs)

#highlight mean & 95th percentile value in the histogram  
plt.axvline(np.mean(x), color='r', linestyle='dashed', linewidth=1)
plt.axvline(np.percentile(x,95), color='k', linestyle='dashed', linewidth=1)


min_ylim, max_ylim = plt.ylim()
plt.text(np.mean(x)*1.03, max_ylim*0.6, 'Mean: {:.4f}'.format(np.mean(x)))
plt.text(np.percentile(x,95)*1.03, max_ylim*0.3, '95th: {:.4f}'.format(np.percentile(x,95)))
