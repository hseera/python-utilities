# -*- coding: utf-8 -*-

import random
import string


#Below files are used to generate the name. Replace them with your own list of name
MALE_FIRST_NAME ='./sample_files/male_name.csv'
FEMALE_FIRST_NAME ='./sample_files/female_name.csv'
LAST_NAME ='./sample_files/last_name.csv'
MIDDLE_NAME='./sample_files/middle_name.csv'

FILE_TO_WRITE = './sample_files/names.csv'

def get_name(name_type, gender, count):
    try:  
        if (gender =='M' and name_type == 0): # Male with firstname only
            get_first_name(gender,count)
        elif (gender =='F' and name_type == 0): # Female with firstname only
            get_first_name(gender,count)
        elif (gender =='M' and name_type == 1): # Male with first & last name
            get_first_last_name(gender,count)
        elif (gender =='F' and name_type == 1): # Female with first & last name
            get_first_last_name(gender,count)
        elif (gender =='M' and name_type == 2): # Male with fullname
            get_full_name(gender,count)
        elif (gender =='F' and name_type == 2): # Female with fullname
            get_full_name(gender,count)
        elif (gender =='M' and name_type == 3): # Male fullname with abbreviated middlename
            get_abbr_name(gender,count)
        elif (gender =='F' and name_type == 3): # Female fullname with abbreviated middlename
            get_abbr_name(gender,count)
        else:
            print("Sorry the given combination does not exist")
    except Exception as e:
        print(e)


#Generate list of Firstname only equal to the count defined and save them to a file        
def get_first_name(gender,count):
    firstname_list = []
    if gender == 'M':
        for i in range(0,count):
            random_firstname = random.choice(open(MALE_FIRST_NAME).readlines()).strip()
            firstname_list.append(random_firstname)
    if gender =='F':
        for i in range(0,count):
            random_firstname = random.choice(open(FEMALE_FIRST_NAME).readlines()).strip()
            firstname_list.append(random_firstname)
    with open(FILE_TO_WRITE, "w") as outfile:
        outfile.writelines("\n".join(firstname_list))

#Generate list of names( first & lastname) equal to the count defined and save them to a file        
def get_first_last_name(gender,count):
    first_last_name_list = []
    if gender == 'M':
        for i in range(0,count):
            random_firstname = random.choice(open(MALE_FIRST_NAME).readlines()).strip()
            random_lastname = random.choice(open(LAST_NAME).readlines()).strip()
            first_last_name = " ".join([random_firstname, random_lastname])
            first_last_name_list.append(first_last_name)
    if gender =='F':
        for i in range(0,count):
            random_firstname = random.choice(open(FEMALE_FIRST_NAME).readlines()).strip()
            random_lastname = random.choice(open(LAST_NAME).readlines()).strip()
            first_last_name = " ".join([random_firstname, random_lastname])
            first_last_name_list.append(first_last_name)
    with open(FILE_TO_WRITE, "w") as outfile:
        outfile.writelines("\n".join(first_last_name_list))

#Generate list of Fullname only equal to the count defined and save them to a file 
def get_full_name(gender,count):
    full_name_list = []
    if gender == 'M':
        for i in range(0,count):
            random_firstname = random.choice(open(MALE_FIRST_NAME).readlines()).strip()
            random_lastname = random.choice(open(LAST_NAME).readlines()).strip()
            m_name = random.choice(open(MIDDLE_NAME).readlines()).strip()
            middle_name=m_name.split(",")
            full_name = " ".join([random_firstname,middle_name[1], random_lastname])
            #print(middle_name)
            #print(first_last_name)
            full_name_list.append(full_name)
    if gender =='F':
        for i in range(0,count):
            random_firstname = random.choice(open(FEMALE_FIRST_NAME).readlines()).strip()
            random_lastname = random.choice(open(LAST_NAME).readlines()).strip()
            m_name = random.choice(open(MIDDLE_NAME).readlines()).strip()
            middle_name=m_name.split(",")
            full_name = " ".join([random_firstname,middle_name[0], random_lastname])
            full_name_list.append(full_name)
    with open(FILE_TO_WRITE, "w") as outfile:
        outfile.writelines("\n".join(full_name_list))

#Generate list of Fullnames with abbreviated middle name equal to the count defined and save them to a file 
def get_abbr_name(gender,count):
    abbr_name_list = []
    if gender == 'M':
        for i in range(0,count):
            random_firstname = random.choice(open(MALE_FIRST_NAME).readlines()).strip()
            random_lastname = random.choice(open(LAST_NAME).readlines()).strip()
            middle_name=random.choice(string.ascii_uppercase)+"."
            abbr_name = " ".join([random_firstname,middle_name, random_lastname])
            abbr_name_list.append(abbr_name)
    if gender =='F':
        for i in range(0,count):
            random_firstname = random.choice(open(FEMALE_FIRST_NAME).readlines())
            random_lastname = random.choice(open(LAST_NAME).readlines())
            middle_name=random.choice(string.ascii_uppercase)+"."
            abbr_name = " ".join([random_firstname,middle_name, random_lastname])
            abbr_name_list.append(abbr_name)
    with open(FILE_TO_WRITE, "w") as outfile:
        outfile.writelines("\n".join(abbr_name_list))


def main():
    '''
    TYPE options:
        Firstname Only = 0
        First & Lastname = 1
        Fullname = 2
        Fullname with abbreviated middlename = 3
    '''
    TYPE = [0,1,2,3]
    '''
    GENDER options:
        Male = M
        Female = F
    '''
    GENDER = ['M','F']
    
    COUNT = 10  #How many names needs to be generated
    
    get_name(TYPE[1],GENDER[0], COUNT)

if __name__ == "__main__":
    main()

