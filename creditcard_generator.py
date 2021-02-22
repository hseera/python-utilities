# -*- coding: utf-8 -*-

'''
Logic for credit card validation is taken from the following link
https://www.freeformatter.com/credit-card-number-generator-validator.html
https://en.wikipedia.org/wiki/Payment_card_number
'''

from random import randint
import csv

def generate_creditcard_number(credit_type, count):
    ctype = ["Master","Visa"]
    credit_card =[]
    credit_card_list =[]
    rev_card = []
    
    if credit_type not in ctype:
        return(print("Function does not support the credit card type"))
    else:
        if credit_type =="Master":
            #master card 16 digits. Only generating cards that start with 51-55
            #append 15 digits to master card list. List starts with 5 and next number is a random between 1-5
            credit_card_list.append("mastercard_numbers")
            for counter in range(count):
                credit_card.append(5)
                credit_card.append(randint(1,5))
                
                for num in range(0,13):
                    credit_card.append(randint(0,9))
                 
                rev_card = credit_card.copy()
                rev_card.reverse()   # reverse the order
                
                for i in range(0, 15, 2):  # multiple odd position digits with 2
                    rev_card[i] = rev_card[i] * 2
                
                for i in range(len(rev_card)): # if sum is >9, subtract 9
                    if (rev_card[i]) > 9:
                        rev_card[i] = (rev_card[i]) - 9
                
                total_sum = sum(rev_card)
                
                mod = total_sum % 10 #16th digit in master card is a check digit
                if mod ==0:
                    check_sum= 0
                else:
                    check_sum = 10 - mod
                    
                credit_card.append(check_sum)
                credit_card = int("".join(map(str, credit_card)))
                credit_card_list.append(credit_card) #append all the creditcards to a list
                credit_card=[]
        if credit_type == "Visa":
        #visa card can be 13-16-19 digits. This code generates 16 digit card number
            credit_card_list.append("visacard_numbers")
            for counter in range(count):
                credit_card.append(4)
                for num in range(0,14):
                    credit_card.append(randint(0,9))
                 
                rev_card = credit_card.copy()
                rev_card.reverse()   # reverse the order
                
                for i in range(0, 15, 2):  # multiple odd position digits with 2
                    rev_card[i] = rev_card[i] * 2
                
                for i in range(len(rev_card)): # if sum is >9, subtract 9
                    if (rev_card[i]) > 9:
                        rev_card[i] = (rev_card[i]) - 9
                
                total_sum = sum(rev_card)
                
                mod = total_sum % 10 #16th digit in visa is a check digit
                if mod ==0:
                    check_sum= 0
                else:
                    check_sum = 10 - mod
                    
                credit_card.append(check_sum)
                credit_card = int("".join(map(str, credit_card)))
                credit_card_list.append(credit_card) #append all the creditcards to the list
                credit_card=[]
        #print(credit_card_list)
        write_to_file(credit_card_list) # save the creditcards to a file
        credit_card_list=[]

def write_to_file(credit_card_list):
    with open('./creditcardnumber.csv', 'w') as ccn_file:
        file_writer = csv.writer(ccn_file,quoting=csv.QUOTE_ALL,delimiter='\n')
        file_writer.writerow(credit_card_list)

def main():
    ctype = ["Master","Visa"]
    generate_creditcard_number(ctype[1], 10)
    
if __name__ == "__main__":
    main()
    
