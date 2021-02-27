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
            date = datetime(int(date_time[3]),strptime(date_time[0],'%b').tm_mon,int(date_time[1])) #converting month (i.e. 'Feb') to month number using strptime
            df_dict['date'] = date.strftime("%d/%m/%Y")
            df_dict['time'] = date_time[2]
            df_dict['type'] = item.attrib['type']
            df_dict['intervalms'] = item.attrib['intervalms']
            nursery_counter = False
            tenured_counter = False
            for child in item:
                if 'totalms' in child.attrib:
                    df_dict['totalms'] = child.attrib['totalms']
                if 'requested_bytes' in child.attrib:
                    df_dict['requested_bytes'] = child.attrib['requested_bytes']
                    
                if ('freebytes' in child.attrib and 'nursery' in child.tag  and nursery_counter == False):
                    before = 'beforegc_'+ child.tag + '_freebytes'
                    df_dict[before] = child.attrib['freebytes']
                    nursery_counter = True
                elif ('freebytes' in child.attrib and 'nursery' in child.tag and nursery_counter == True):
                    after = 'aftergc_'+ child.tag + '_freebytes'
                    df_dict[after] = child.attrib['freebytes']
                    nursery_counter = False
                    
                if ('freebytes' in child.attrib and 'tenured' in child.tag  and tenured_counter == False):
                    before = 'beforegc_'+ child.tag + '_freebytes'
                    df_dict[before] = child.attrib['freebytes']
                    tenured_counter = True
                elif ('freebytes' in child.attrib and  'tenured' in child.tag and tenured_counter == True):
                    after = 'aftergc_'+ child.tag + '_freebytes'
                    df_dict[after] = child.attrib['freebytes']
                    tenured_counter = False
                            
                if ('gc' in child.tag):
                    df_dict['gc_intervalms'] = child.attrib['intervalms']
            
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