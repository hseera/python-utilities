# -*- coding: utf-8 -*-

from scapy.all import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap


'''
Currently the script doesn't cater for simple service discovery protocol (ssdp). 
Therefore make sure ssdp is filtered out before generating the heatmap.

'''

def convert_trace_file(FILE):
    try:
        packets = PcapReader(FILE) # network trace file
        
        packet_list = []
            
        for packet in packets:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            length = packet['IP'].len
            packet_list.append([src_ip,dst_ip, length])
        
        df=pd.DataFrame(packet_list,columns=['src','dst','length'])
        
        res = df.pivot_table(index=['src', 'dst'],values='length' , aggfunc='sum').reset_index()
        
        pivot = res.pivot(index='src', columns='dst', values='length')
        
        network_traffic_heatmap(pivot)
        
    except Exception as e:
        print(e)


def network_traffic_heatmap(pivot_data):
    try:
        
        fig, ax = plt.subplots(figsize=(14,6))
        
        sns.heatmap(pivot_data,
                    ax=ax,
                    #annot=True, #enable annot to show the value in the box. However I suggest you don't do it without modifying the code.
                    linewidths=.2,
                    fmt="d",
                    square=False,
                    cmap=LinearSegmentedColormap.from_list('gr',["g", "y", "r"], N=256),
                    cbar_kws={'pad': .02
                              }
                    )
        
        ax.set_title('Network Conversation Flow & Bytes Transferred')
        
        ax.set_facecolor('lightgrey')
          
        '''
        bug in seaborn where it chops the top and bottom squares. 
        Below is a workaround for it as detailed in the following link
        https://github.com/mwaskom/seaborn/issues/1773
        '''
        bottom, top = plt.ylim() # discover the values for bottom and top
        bottom += 0.5 # Add 0.5 to the bottom
        top -= 0.5 # Subtract 0.5 from the top
        plt.ylim(bottom, top) # update the ylim(bottom, top) values
        plt.xlabel('Destination IPs')
        plt.ylabel('Source IPs')
        plt.show()
        fig.savefig("network-conversation-heatmap.png",bbox_inches = "tight")
        
    except Exception as e:
        print(e)

    

def main():
    FILE =  './sample.pcapng'
    convert_trace_file(FILE)
    
if __name__ == "__main__":
    main()