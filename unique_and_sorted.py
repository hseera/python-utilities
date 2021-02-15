# -*- coding: utf-8 -*-
'''
Sort and save unique values to a new file. Ignore rows that do not have a value.

Sample values in a file might look like this
02/02/2018 23:15:12, 1234567889
02/02/2018 23:15:13, 1234568889
02/02/2018 23:15:18, 1234568889
02/02/2018 23:15:19, 
02/02/2018 23:15:25, 1234545889
02/02/2018 23:17:12, 1234512889
02/02/2018 23:18:10,
02/02/2018 23:19:12, 123456889
'''



FILE_TO_READ = "./sample_files/unique_and_sorted.csv" #replace with your file name
FILE_TO_WRITE = "./sample_files/file_to_write.csv"


def unique_and_sorted(FILE_TO_READ, FILE_TO_WRITE):
    count_list =[]
    with open(FILE_TO_READ,'r') as fread, open(FILE_TO_WRITE,'w') as fwrite:
        for line in fread: #split the row and add the values into the list
            str = line.split(',')
            if (str[1] != "\n"):
                count_list.append(int(str[1]))
        count_list = list(set(count_list)) #save the value into a new list and sort it
        count_list.sort()
        for item in count_list:
            fwrite.write('%s\n' %item)
    fread.close()
    fwrite.close()
        
def main():
    unique_and_sorted(FILE_TO_READ, FILE_TO_WRITE)
    
if __name__ == "__main__":
    main()

