# -*- coding: utf-8 -*-

'''
This script generates a 9 digit TFN number

https://en.wikipedia.org/wiki/Tax_file_number

To valid the data -> https://cdn.rawgit.com/steveswinsburg/tfn-validator/master/tfn-validator.html

Special TFN numbers -> https://www.ato.gov.au/Forms/PAYG-payment-summary---individual-non-business/?page=3

'''

from random import randint
import csv

TFN_NUMBERS_TO_GENERATE = 10

def generate_tfn(tfn_num_to_generate):
    tfn =[]
    tfn_list=[]
    num_weight = [1,4,3,7,5,8,6,9,10]
    i = 1
    tfn_list.append('tfn_numbers')
    while i <= tfn_num_to_generate: #How many TFN numbers to generate
        total_sum = 0
        tfn.append(randint(1,9)) # The first digit in TFN is not 0
        
        for num in range(0,7): # Append 7 random digits to TFN number
            tfn.append(randint(0,9))
        
        for num in range(0,8): # Get total sum of 8 digit based on their weight
            total_sum = total_sum + (tfn[num] * num_weight[num])
           
        quotient, remainder = divmod(total_sum, 11) #Get the 
        
        counter = 0
        '''While Remainder is not zero, continue iterating. 
        When remainder = 0, the counter value is the checksum value. And that is the last digit of the TFN number.
        '''
        while (remainder != 0):  
            counter += 1
            quotient, remainder = divmod(total_sum + counter*10, 11)
        
        if (counter > 9): #Ignore tfn number where checksum value is greater than 9
            print("This is not valid TFN Number %s" %tfn)
            tfn =[]
            continue
        else:
            tfn.append(counter)
            print("Valid TFN Number %s" %tfn)
            i= i +1
            tfn = int("".join(map(str, tfn)))
            tfn_list.append(tfn)
            tfn =[]
    write_to_file(tfn_list)
        

def write_to_file(tfn_list):
    with open('./tfn.csv', 'w') as tfn_file:
        file_writer = csv.writer(tfn_file,quoting=csv.QUOTE_ALL,delimiter='\n')
        file_writer.writerow(tfn_list)

def main():
    generate_tfn(TFN_NUMBERS_TO_GENERATE)
    
if __name__ == "__main__":
    main()
    
