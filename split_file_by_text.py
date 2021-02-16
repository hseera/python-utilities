# -*- coding: utf-8 -*-

import pandas as pd

'''
For each text to search in a data file, copy all the searched text data to a new file. 
'''

PATH_TO_WRITE ="./sample_files/"  #path where the split files need to be saved

FILE_TO_READ = "./sample_files/count.csv" #data file
    
SEARCH_TEXT =['test','apple','cheap','mango'] #sample search text.


def split_file_by_text(SEARCH_TEXT, FILE_TO_READ):
    try:
        file_data = []
        df = pd.read_csv(FILE_TO_READ)
        for text in SEARCH_TEXT:
            #file_data = df.loc[df['name'] == text] # use if you want to be strict with the search text
            file_data = df.loc[df['name'].str.contains(text)] # use if you want to be less strict with search text
            FILE_TO_WRITE = PATH_TO_WRITE + text + '.csv'
            with open(FILE_TO_WRITE,'w') as fwrite:
                for item in range(len(file_data)):
                    fwrite.write('%s\n' %file_data['name'].values[item])
    except Exception as e:
        raise e
             
def main():

    split_file_by_text(SEARCH_TEXT,FILE_TO_READ)

if __name__ == "__main__":
    main()
