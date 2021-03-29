# -*- coding: utf-8 -*-
"""
For a given list of hostname/ip address in a file, scan for open ports and save the result to a file.

Note: 
To speed up the scanning process, this script will need to be modified to use threads.
Currently it scans port in a sequential order. This can take time if the port range is large as well as number of hosts to scan is large too.
"""

import socket
import pandas as pd

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOSTNAME_TO_READ = './sample_files/hostname.csv' #host file containing the hostname to scan for open ports
PORT_INFO_TO_WRITE = './sample_files/ports.csv' # file to save port information

data = []
PORT_NUMBER_START = 130 # port scan start value
PORT_NUMBER_END = 140 # port scan end value

#For port for each target
def scan_target_port(target):
    try:
        for port_number in range(PORT_NUMBER_START, PORT_NUMBER_END):
            if scan_port(target, port_number):
                data.append([port_number, 1, target]) # 1 indicates that port is open
            else:
                data.append([port_number, 0, target]) # 0 indicates that port is closed
    except Exception as ex:
        raise ex


#Return True if port is open else False
def scan_port(target, port):
    try:
        s.connect((target, port))
        return True
    except:
        return False

#convert the list into a pivot table and save the result to a file
def generate_pivot_table(data):
    try:
        df = pd.DataFrame(data,columns=['port', 'value', 'hostname'])
        pivot = df.pivot(index='port', columns='hostname', values='value')
        pivot.to_csv(PORT_INFO_TO_WRITE, index=True)
        #print(pivot)
    except Exception as ex:
        raise ex

def main():
    df = pd.read_csv(HOSTNAME_TO_READ)
    for ind in df.index:
        #print(df['target_name'][ind])
        scan_target_port(df['target_name'][ind])
    generate_pivot_table(data)

if __name__ == "__main__":
    main()