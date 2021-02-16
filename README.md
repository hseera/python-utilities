# Python Utilities
Different python utility scripts to help automate mundane/repetitive performance testing tasks.
The readme page will continue to get updated as and when, I add new utility to the repo.


|Utility Link |Utility Link|Utility Link|Utility Link|
|:-------------------------|:---------------|:------------------|:------------------|
|[1: Merge Columns](#1-merge-columns)|[2: Unique and Sorted](#2-unique-and-sorted)|[3: Histogram](#3-histogram)|[4: Extract Data](#4-extract-data)|
|[5: Swap Columns](#5-swap-columns)|[6: Randomize Data](#6-randomize-data)|[7: Unique Occurrence Count](#7-unique-occurrence-count)|[8: Split File By Text](#8-split-file-by-text)|
|[9: Heatmap](#9-heatmap)||||



# [1: Merge Columns](#1-merge-columns)
This script merges columns from different files together and generates a new file.
![MergeColumns](https://github.com/hseera/python-utilities/blob/main/images/merged-files.png)

# [2: Unique and Sorted](#2-unique-and-sorted)
This script extracts data from a file, removes rows with no data, sorts and saves unique data into a file.
![Unique](https://github.com/hseera/python-utilities/blob/main/images/unique-sorted.png)

# [3: Histogram](#3-histogram)
This script generates histrogram for the response time data.
![Histogram](https://github.com/hseera/python-utilities/blob/main/images/histogram.png)

# [4: Extract Data](#4-extract-data)
This script extracts response time data that matches a specific text in a column and saves into a new file.
![Data](https://github.com/hseera/python-utilities/blob/main/images/extract-data.png)

# [5: Swap Columns](#5-swap-columns)
This script swaps columns in a file. Useful when trying to rearrange columns for easy of use/readability. 
For demonstration purpose, the script rearranges JMeter result csv columns as I like them to view. However can be extended for other use too.
![Data](https://github.com/hseera/python-utilities/blob/main/images/swap-columns.png)

# [6: Randomize Data](#6-randomize-data)
This script randomizes data in a file. Useful when you want to have a random order of data in file for testing purpose.

![Data](https://github.com/hseera/python-utilities/blob/main/images/randomize-data.png)

# [7: Unique Occurrence Count](#7-unique-occurrence-count)
This script saves total number of occurrence of each unique item in a file. Useful for designing the test data distribution for testing.

![Data](https://github.com/hseera/python-utilities/blob/main/images/unique-occurrence-count.png)
 
# [8: Split File By Text](#8-split-file-by-text)
Extract data that matches a text in the data file and create a new file containing that data. 
Useful when you have one big data file with all the data and you want to create separate data for each test script. 
For example, you have one big data file that contains images, js & CSS URLs. 
And you want to create a separate data file for CSS, js & images respectively. This script will help just do that.
In the below screenshot team was not part of the search text and hence no csv created for it. name is the column name in the file. 
![Data](https://github.com/hseera/python-utilities/blob/main/images/split-file-by-text.png)

# [9: Heatmap](#9-heatmap)
There might the times when it is not easy to notice small fluctuations in data using a line chart. 
This script generates a heatmap for the data where you are trying to observe patterns over minutes/hours but for a longer duration (i.e.30 days). 
For example, there might be a specific hour of the day when you see more load but it is not higher than the peak load in a day. 
Therefore line chart for a longer duration (i.e. 30 days) might hide that pattern or it might not be easily visible.

Same can be performed in excel using pivot table but will require some manual effort.

![Data](https://github.com/hseera/python-utilities/blob/main/images/heatmap.png)
