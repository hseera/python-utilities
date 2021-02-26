# -*- coding: utf-8 -*-
"""
This script takes an excel file with data for multiple system in a column format 
and pivots it and saves each systems data in a seperate sheet.

Useful when you have server metrics for different system in a csv/xlsx 
and you want to extract and plot graphs for each system seperately.

To understand how this scirpt works, run it with the sample file provided so you understand the output.

Note: The code is based on the sample file headers. 
For your file you will have different column names. 
Therefore this script will require minor modification to cater for your scenario.
"""
#import openpyxl
import pandas as pd

def format_data(file_to_read):
    try:
        '''
        For each unique name in the column "TARGET_NAME", extract all the data for it and generate a pivot table.
        Once pivot table is generated, save that data into the same xlsx file as a new sheet. 
        The sheet name is the TARGET_NAME.
        '''
        df = pd.read_excel(file_to_read)
        for target in df.TARGET_NAME.unique(): 
            x = df.loc[df['TARGET_NAME'] == target] #filter out all the rows for which the label column does not contain value target 
            
            res = x.pivot_table(index=['TimeStamp','METRIC_COLUMN'], values='VALUE', aggfunc='sum').reset_index()
            pivot = res.pivot(index='TimeStamp', columns='METRIC_COLUMN', values='VALUE')
            
            pivot = pivot.fillna(0) # fill all cells with NaN with value 0. Change it as you see fit for your usecase.
            
            save_data_to_xls(file_to_read, target, pivot)
            
    except Exception as e:
        print(e)

def save_data_to_xls(file_to_read, sheet_name, pivoted_data):
    try:                
        writer = pd.ExcelWriter(file_to_read, engine='openpyxl', mode='a') #engine='xlsxwriter' <-- doesn't support append mode
        pivoted_data.to_excel(writer, index=True, sheet_name=sheet_name)
        writer.bookworksheet = writer.sheets[sheet_name]
        writer.save()
        writer.close()
    except Exception as e:
        print(e)
   
def main():
    FILE_TO_READ = './sample_files/log-file-database.xlsx' #sample data file
    format_data(FILE_TO_READ)

if __name__ == "__main__":
    main()
