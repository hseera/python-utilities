import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as dt


'''
Data csv file looks something like this when opened in text editor:

"log_time","elapsed_time"
"09/09/2021 04:32:32",21
"09/09/2021 04:32:32",35
"09/09/2021 04:33:32",350
"09/09/2021 04:33:33",8000
"09/09/2021 04:34:35",35

'''

def tornado_graph (FILE_TO_READ):
    try:
        df = pd.read_csv(FILE_TO_READ, sep=",")
        df['end_time'] = pd.to_datetime(df['log_time'].str[11:19],format='%H:%M:%S') #extract the time
        df['latency'] = round(df['elapsed_time']/1000) #Comment this if the elapsed_time is in sec. If in milliseconds convert to seconds
        df['start_time'] = df['end_time'] - pd.to_timedelta(df['latency'], unit='s') # get the request start time 
        df = (df.sort_values(by=['start_time'])).reset_index(drop=True)
        
        fig = plt.fig(figsize=(14,8))
        fmt = dt.DateFormatter('%H:%M:%S')
        plt.gca().xaxis.set_major_formatter(fmt)
        for x1, x2, y in zip(df['start_time'],df['end_time'],df['latency']):
            if y > 0.0:
                plt.plot([x1,x2],[y,y], color='red')
                '''
                Can have extra check to change color of the graph based on latency range
                
                if (y < 100.0):
                    plt.plot([x1,x2],[y,y], color='black')
                if (y >=100.0 and y < 200.0):
                    plt.plot([x1,x2],[y,y], color='green')
                if (y >=200.0 and y < 300.0):
                    plt.plot([x1,x2],[y,y], color='purple')
                '''
                
        #plt.plot_date('end_time', 'latency', data = df, xdate=True, ydate=False) <--Scatter plot
        
        plt.grid()
        plt.xlabel("Time")
        plt.ylabel("Response Time (sec)")
        fig.tight_layout()
    
    except Exception as e:
        print(e)

def main():
    FILE_TO_READ ="./response_time.csv"
    tornado_graph(FILE_TO_READ)
    

if __name__ == "__main__":
    main()