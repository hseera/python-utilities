# -*- coding: utf-8 -*-

from scapy.all import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import networkx as nx
from matplotlib.offsetbox import AnchoredText
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

'''
Currently the script only caters for packets that have IP layer. 
It filters out packets such as simple service discovery protocol (ssdp)/ Address Resloution Protocol (ARP) as it doesn't contain the IP information. 
'''

def convert_pcap_file(pcap_file,heatmap_status, graph_status ):
    try:
        packets = PcapReader(pcap_file) # network trace file
        
        packet_list = []
            
        for packet in packets:
            if packet.haslayer('IP'):
                src_ip = packet['IP'].src
                dst_ip = packet['IP'].dst
                length = packet['IP'].len
                packet_list.append([src_ip,dst_ip, length])
            else:
                continue
        
        df=pd.DataFrame(packet_list,columns=['src','dst','length'])
        
        res = df.pivot_table(index=['src', 'dst'],values='length' , aggfunc='sum').reset_index()
        
        pivot = res.pivot(index='src', columns='dst', values='length')       
        
        if (heatmap_status == True):
            network_traffic_heatmap(pivot, res['src'].nunique(),res['dst'].nunique())
            
        if (graph_status == True):
            network_graph(res, res['src'].nunique(),res['dst'].nunique())
        
    except Exception as e:
        print(e)


def network_traffic_heatmap(pivot_data, unique_src, unique_dst):
    try:
        
        fig, ax = plt.subplots(figsize=(14,10))
        
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
        
        anc = AnchoredText("src = {}, dst = {}".format(unique_src,unique_dst), loc="upper right", frameon=True)
        ax.add_artist(anc)
        
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
        plt.xlabel('Destination')
        plt.ylabel('Source')
        plt.show()
        fig.savefig("network-conversation-heatmap.png",bbox_inches = "tight")
        
    except Exception as e:
        print(e)


def network_graph(df, unique_src, unique_dst):
    G = nx.Graph()
    G = nx.from_pandas_edgelist(df, source='src', target='dst', edge_attr=True, create_using=nx.DiGraph())
    fig, ax = plt.subplots(figsize=(14,10))
    ax.set_title('Network Conversation Flow')
    nx.draw_networkx(G)
    anc = AnchoredText("src = {}, dst = {}".format(unique_src,unique_dst), loc="upper right", frameon=True)
    ax.add_artist(anc)
    plt.show()
    fig.savefig("network-conversation-flow.png",bbox_inches = "tight")
    
    
def main():
    PCAP_FILE = './sample.pcap' #replace it with your pcap/pcapng file
     
    GRAPH_PLOT = False #Set this to true if you want graph chart. Default is false.
    
    HEATMAP_PLOT = True #Set this to False if you don't want heat chart. Default is True.
    
    convert_pcap_file(PCAP_FILE, HEATMAP_PLOT, GRAPH_PLOT)
    
if __name__ == "__main__":
    main()