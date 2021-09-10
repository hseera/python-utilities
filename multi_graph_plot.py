# -*- coding: utf-8 -*-
'''
TODO:
Modify the code to display test duration for the scatterplot rather than the count of data points plot. 
'''

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

import seaborn as sns


'''
This function iterates through all the columns in the responsetime_histogram file
and generate histogram for all of them. It also plots the average response time for all.

Note: comment out the code that plots mean on the graph if not required.
'''

FILE = "./sample_files/metrics.csv" #replace with your file name

def generate_graphs(): 
    try:
        df = pd.read_csv(FILE) # read the file    
    
        fig, axes = plt.subplots(2, 2, figsize=(14, 8), sharey=False) # set 2x2 plots
        
        plt.subplots_adjust(hspace = 0.3)
        
        #generate scatterplot for elapsed time
        hist_df = df.filter(regex='elapsed_')
        ax = sns.scatterplot(ax=axes[0, 0], data=hist_df, s=2, legend=True)
        ax.set(ylim=(0,3000))
        ax.legend(fontsize='medium')
        ax.set_title('Response Time')
        ax.set_xlabel('Test Duration')
        ax.set_ylabel('Response Time (ms)')
        
        #generate response time distribuiton graph
        kwargs = dict(element='step',shrink=.8, alpha=0.6, fill=True, legend=False) 
        ax = sns.histplot(ax=axes[0, 1], data=hist_df,**kwargs)
        ax.set(xlim=(0,3000))
        ax.set_title('Response Time Distribution')
        ax.set_xlabel('Response Time (ms)')
        ax.set_ylabel('Frequency')
        
        #generate summary for the response time
        summary = np.round(hist_df.describe(percentiles=[0.25,0.5,0.75,0.90,0.95],include='all'),2)# show basic statistics as in row
        
        axes[1, 0].axis("off")
        table_result = axes[1, 0].table(cellText=summary.values,
                  rowLabels=summary.index,
                  colLabels=summary.columns,
                  cellLoc = 'right', rowLoc = 'center',
                  loc='center')
        table_result.auto_set_font_size(False)
        table_result.set_fontsize(9)
        
              
        #generate response code distribution graph
        hist_df = df.filter(regex='responsecode_')
        bar_df = pd.DataFrame(columns=['name', 'response_code', 'count'])
                
        for col in hist_df.columns:
            data = Counter(df[col])
            for key,value in data.items():
                data = {'name':col, 'response_code':key, 'count':value}
                bar_df = bar_df.append(data, ignore_index=True)

        ax = sns.barplot(ax=axes[1, 1],data=bar_df,x='count', y='response_code', hue='name', orient = 'h' )
        ax.legend_.remove()
        ax.set_title('Response Code Distribution')
        ax.set_xlabel('Count')
        ax.set_ylabel('Response Code')
        
        
        fig.tight_layout()  

        plt.savefig('graphs.png')
    except Exception as e:
        raise e



def main():
    generate_graphs()
    

if __name__ == "__main__":
    main()