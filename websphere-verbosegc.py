# -*- coding: utf-8 -*-

'''
Parse websphere verbosegc log and extract data to a csv. Currently it gives you a high level information such as
- Date & Time when invocation of the garbage collection happened
- intervalms -> Interval between the present and previous garbage collection invocation
- totalms -> Total execution time of this garbage collection
- requested_bytes -> Allocation requested bytes

Useful if you want to import this metrics to your load testing tool for further analysis with other metrics.

TODO
- Extract metrics for the heap (i.e. nursery & tenured space) state before the collection and after the collection 
- Extract the Heap occupancy details after GC

Links
- https://gauravrohatgi.files.wordpress.com/2014/01/was-tuning.pdf

'''

import xml.etree.ElementTree as ET
from datetime import datetime
from time import strptime
from collections import  OrderedDict
import pandas as pd

def parse_verbosegc_data(verbosegc_xml): 
    verbosegc_list=[]   
    try:
        tree = ET.parse(verbosegc_xml) # create element tree object
        for item in tree.findall ('./af'):
            df_dict = OrderedDict()
            date_time = (item.attrib['timestamp']).split()
            date = datetime(int(date_time[3]),strptime(date_time[0],'%b').tm_mon,int(date_time[1]))
            df_dict['date'] = date.strftime("%d/%m/%Y")
            df_dict['time'] = date_time[2]
            df_dict['type'] = item.attrib['type']
            df_dict['intervalms'] = item.attrib['intervalms']
        
            for child in item:
                if 'totalms' in child.attrib:
                    df_dict['totalms'] = child.attrib['totalms']
                if 'requested_bytes' in child.attrib:
                    df_dict['requested_bytes'] = child.attrib['requested_bytes']
            
            verbosegc_list.append(df_dict)    
        
        verbosegc_data = pd.DataFrame(verbosegc_list)
        
        save_verbosegc_data(verbosegc_data)
    except Exception as e:
        print (e)
  
def save_verbosegc_data(verbosegc_data): 
    FILE_TO_WRITE="./sample_files/verbose.csv"
    verbosegc_data.to_csv(FILE_TO_WRITE, index=False)
      
def main(): 
    # parse xml file 
    parse_verbosegc_data('./sample_files/node1.txt') 
      
if __name__ == "__main__": 
    main() 