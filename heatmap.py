# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
 Sometimes it is hard to visualize changes that might be happening over time using line chart.
So an alternate way might be to visualize the data using heatmap.  
'''

def heatmap(FILE_TO_READ):
    try:
        df = pd.read_csv(FILE_TO_READ)
        df['Date'] = df._time.apply(lambda x: x[:10])
        df['Time'] = df._time.apply(lambda x: x[11:19])
        
        pivot = df.pivot(index='Date', columns='Time', values='Count')
        fig, ax = plt.subplots(figsize=(14,4))
        
        sns.heatmap(pivot,
                    ax=ax,
                    #annot=True, #enable annot to show the value in the box
                    linewidths=.3,
                    fmt="d",
                    square=False,
                    cmap=sns.color_palette(['green', 'orange' ,'red']),
                    cbar_kws={'pad': .02
                              }
                    )
        
        ax.xaxis.set_ticks_position('top')  # put column labels at the top and rotate by 90
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
      
        '''
        bug in seaborn where it chops the top and bottom squares. 
        Below is a workaround for it as detailed in the following link
        https://github.com/mwaskom/seaborn/issues/1773
        '''
        bottom, top = plt.ylim() # discover the values for bottom and top
        bottom += 0.5 # Add 0.5 to the bottom
        top -= 0.5 # Subtract 0.5 from the top
        plt.ylim(bottom, top) # update the ylim(bottom, top) values
        plt.show()
        plt.savefig('heatmap.png')
        
    except Exception as e:
        raise e

            
def main():
    FILE_TO_READ = "./sample_file/heatmap.csv" #data file
    heatmap(FILE_TO_READ)

if __name__ == "__main__":
    main()
