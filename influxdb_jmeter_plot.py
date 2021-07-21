# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient
import pandas as pd
import matplotlib.pyplot as plt

#Default Influxdb connection detail. Update them to your connection detail.
HOST = '127.0.0.1'
PORT = 8086
USER = 'jmeter'
PASSWORD = 'jmeter'
DBNAME = 'jmeter'

'''
******************************Sample Query Examples*****************************************************
***********Script will need to be slighly modified to handle the below or your queries******************
********************************************************************************************************

FIELDS = """count("responseTime")/60"""
MEASUREMENTS = """requestRaw"""
FILTERS = """ where time > '2021-01-31T23:53:00Z' AND time <'2021-02-01T01:10:00Z' GROUP BY time(60s)"""
QUERY = """SELECT {} FROM {} {}""".format(FIELDS,MEASUREMENTS,FILTERS)

FIELDS = """mean("responseTime")"""
MEASUREMENTS = """requestRaw"""
FILTERS = """ where time > '2021-01-31T23:53:00Z' AND time <'2021-02-01T01:10:00Z' GROUP BY time(60s)"""
QUERY = """SELECT {} FROM {} {}""".format(FIELDS,MEASUREMENTS,FILTERS)

FIELDS = """sum("errorCount")/60"""
MEASUREMENTS = """requestRaw"""
FILTERS = """ where time > '2021-01-31T23:53:00Z' AND time <'2021-02-01T01:10:00Z' GROUP BY time(60s)"""
QUERY = """SELECT {} FROM {} {}""".format(FIELDS,MEASUREMENTS,FILTERS)

FIELDS = """percentile("responseTime",95)"""
MEASUREMENTS = """requestRaw"""
FILTERS = """ where time > '2021-01-31T23:53:00Z' AND time <'2021-02-01T01:10:00Z' GROUP BY time(60s)"""
QUERY = """SELECT {} FROM {} {}""".format(FIELDS,MEASUREMENTS,FILTERS)

'''

#Sample Influxdb query example. Replace with your query
FIELDS = """sum("maxActiveThreads")/60"""
MEASUREMENTS = """virtualUsers"""
FILTERS = """ where time > '2021-01-31T23:53:00Z' AND time <'2021-02-01T01:10:00Z' GROUP BY time(60s)"""
QUERY = """SELECT {} FROM {} {}""".format(FIELDS,MEASUREMENTS,FILTERS)


'''
Connect to the influxdb and get data. Parse the resultset and generate the plot.
Based on the query result, the below code will need to be slighly modified.
'''
def get_data_from_influxdb():
    try:
        client = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)
        response = client.query(QUERY)
        column_titles = ['time','sum']
        df = pd.DataFrame((response.get_points()),columns=['sum','time']).dropna()
        df_response = df.reindex(columns=column_titles) #Incase time is not first column. Setting time to be first column.
        df_response['time'] = pd.to_datetime(df_response['time'], format='%Y-%m-%d %H:%M:%S')
        df_response['time'] = df_response['time'].dt.tz_localize('utc').dt.tz_convert('Australia/Melbourne') #Set to your local time.
        plot_graph(df_response)
    except Exception as e:
        print(e)

def plot_graph(response):
    plt.figure(figsize=(10,10))
    plt.xlabel('Date/Time')
    plt.ylabel('# of Virtual Users')
    plt.plot(response['time'], response['sum'], marker='o')        
    plt.show()

def main():
    get_data_from_influxdb()
    
if __name__ == "__main__":
    main()
