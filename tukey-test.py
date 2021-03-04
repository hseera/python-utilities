# -*- coding: utf-8 -*-

'''
This script tries to identify potential outliers from a data file. 
Useful when you want to identify the potential outlier values or you want to remove them to get a better visual for analysis purpose.

The solution is based on the tukey fence test.

https://en.wikipedia.org/wiki/Outlier
'''
import pandas as pd

def tukey_test(file, variable_name):
    try:
        outliers = []
        far_outliers = []
        k1 = 1.5 # nonnegative constant value. k = 1.5 => outlier 
        k2 = 3 # k = 3 => far out outliers. Change k values as per your requirement.
        
        df = pd.read_csv(file) # read the file
        
        #df_copy = df.copy() #create a dataframe copy. K2 Outliers values will be removed from it
        
        first_quartile = df[variable_name].quantile(0.25) #q1
        third_quartile = df[variable_name].quantile(0.75) #q3
         
        interquartile_range = third_quartile-first_quartile #irq = g3 - q1
        
        lower_inner_fence = first_quartile - k1*interquartile_range 
        upper_inner_fence = third_quartile + k1*interquartile_range
        
        print("Outlier Range (k=%s): [%s, %s]\n" %(k1, lower_inner_fence,upper_inner_fence))
        
        lower_outer_fence = first_quartile - k2*interquartile_range
        upper_outer_fence = third_quartile + k2*interquartile_range
        
        print("Outlier Range (k=%s): [%s, %s]\n" %(k2,lower_outer_fence,upper_outer_fence))
        
        for index, x in enumerate(df[variable_name]):
            if x >= upper_inner_fence or x <= lower_inner_fence:
                outliers.append(x)
            if x >= upper_outer_fence or x <= lower_outer_fence: 
                #df_copy.drop(df_copy.index[df_copy[variable_name] == x], inplace = True) #drop values that are out of range
                far_outliers.append(x)
                        
        return k1, k2, sorted(outliers), sorted(far_outliers)
    except Exception as e:
        print(e)
   

def main():
    FILE = "./sample_files/tukey_test.csv" #replace with your file name
    k1, k2, outliers, far_outliers = tukey_test(FILE, "results_001")
    print("Potential outliers not in (k=%s) range: \n%s\n" %(k1, outliers))
    print("Potential outliers not in (k=%s) range: \n%s" %(k2,far_outliers))
    
if __name__ == "__main__":
    main()
