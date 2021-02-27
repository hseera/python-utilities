# Python Utilities
Different python utility scripts to help automate mundane/repetitive/specific performance testing tasks.
The readme page will continue to get updated as and when I add a new utility to the repo.

**Note:** Most of these utilities are focused on performance testing/engineering. 
However, with slight modification(/in some cases none) can be used in other fields/areas too.


|Utility Link |Utility Link|Utility Link|Utility Link|
|:-------------------------|:---------------|:------------------|:------------------|
|[1: Merge Columns](#1-merge-columns)|[2: Unique and Sorted](#2-unique-and-sorted)|[3: Histogram](#3-histogram)|[4: Extract Matched Data](#4-extract-matched-data)|
|[5: Swap Columns](#5-swap-columns)|[6: Randomize Data](#6-randomize-data)|[7: Unique Occurrence Count](#7-unique-occurrence-count)|[8: Split File By Text](#8-split-file-by-text)|
|[9: Heatmap](#9-heatmap)|[10: Pivot Table](#10-pivot-table)|[11: Generate ABN And ACN](#11-generate-abn-and-acn)|[12: Network Conversation Flow](#12-network-conversation-flow)|
|[13: Creditcard Generator](#13-creditcard-generator)|[14: TFN Generator](#14-tfn-generator)|[15: IRD Generator](#15-ird-generator)|[16: Dollar Format](#16-dollar-format)|
|[17: File Splitter](#17-file-splitter)|[18 Locate File](#18-locate-file)|[19 Websphere Verbosegc](#19-websphere-verbosegc)|[20 Formatted Server Metrics To Excel](#20-formatted-server-metrics-to-excel)|


# [1: Merge Columns](#1-merge-columns)
This script merges columns from different files together and generates a new file.
![MergeColumns](https://github.com/hseera/python-utilities/blob/main/images/merged-files.png)

# [2: Unique and Sorted](#2-unique-and-sorted)
This script extracts data from a file, removes rows with no data, sorts and saves unique data into a file.
![Unique](https://github.com/hseera/python-utilities/blob/main/images/unique-sorted.png)

# [3: Histogram](#3-histogram)
This script generates response time distribution graph (histrogram) from the JMeter result CSV.
Can be extended for others tools too.

![Histogram](https://github.com/hseera/python-utilities/blob/main/images/histogram.png)

# [4: Extract Matched Data](#4-extract-matched-data)
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

# [10: Pivot Table](#10-pivot-table)
This script converts extensive data (two/three column data) into a summairzed pivot table format. 
Useful when you want to have a summarized view of the requests/error/response time over long period.

![Data](https://github.com/hseera/python-utilities/blob/main/images/pivot.png)

# [11: Generate ABN And ACN](#11-generate-abn-and-acn)
Generate random ABN and ACN numbers. Useful for performance/functional test scenario's that require valid ABN and/or ACN data for testing.

![Data](https://github.com/hseera/python-utilities/blob/main/images/abn-acn.png)

# [12: Network Conversation Flow](#12-network-conversation-flow)
Convert network conversation captured in the trace file into a heatmap. Useful when you have a lot of conversations captured. 
This script makes it easy to visualize the conversations, if you are not comfortable reading/trolling the Wireshark network conversation view.
It also has an option to generate a graph too. However, the code to generate the graph will require a little modification to cater to too many conversations. 
For less than 40 conversations in a trace file, the current code should suffice.

![Data](https://github.com/hseera/python-utilities/blob/main/images/network-conversation-heatmap.png)
![Data](https://github.com/hseera/python-utilities/blob/main/images/graph.png)

# [13: Creditcard Generator](#13-creditcard-generator)
Generate Mastercard/Visa creditcard numbers. Useful when dummy creditcard numbers are needed for **Testing purpose ONLY**. 
They are useless without the valid owner name, an expiration date and a valid CVV code. Therefore they **CAN NOT** be used for **REAL** transactions.

![Data](https://github.com/hseera/python-utilities/blob/main/images/creditcards.png)

# [14: TFN Generator](#14-tfn-generator)
Generate a list of valid Australian Tax File Numbers (TFN). It is useful when you need TFN numbers for testing purposes.

![Data](https://github.com/hseera/python-utilities/blob/main/images/tfn.png)

# [15: IRD Generator](#15-ird-generator)
Generate a list of valid New Zealand Inland Revenue Department Numbers (IRD). It is useful when you need IRD numbers for testing purposes.

![Data](https://github.com/hseera/python-utilities/blob/main/images/ird.png)

# [16: Dollar Format](#16-dollar-format)
Format data file with the dollar value. Useful when you need to pass dollar value parameter from a file in a payload instead of a number.
Most of the time it should be handled in a code. Incase you are passing it through a file then this script can reduce the effort.

![Data](https://github.com/hseera/python-utilities/blob/main/images/dollar.png)

# [17: File Splitter](#17-file-splitter)
Split a big file into multiple smaller size files. 
Useful when you want to have unique data for the same script running across multiple injectors. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/file-splitter.png)

# [18 Locate File](#18-locate-file)
Recursively search for a file in a folder and all its subfolders. Print out the locations where that file is located.
Useful when you don't want to scroll through all the folders and files to locate the file you need.

![Data](https://github.com/hseera/python-utilities/blob/main/images/find-files.png)

# [19 Websphere Verbosegc](#19-websphere-verbosegc)
Save highlevel websphere verbosegc metrics into csv. Useful when you want to import the data to a load test tool for analyses & correlate with other metrics.
Assupmtion is that you do have any other means (i.e apm tools, sitescope etc) to view this data with other application & system metrics.  

![Data](https://github.com/hseera/python-utilities/blob/main/images/verbosegc.png)

# [20 Formatted Server Metrics To Excel](#20-formatted-server-metrics-to-excel)
There are situations when you get metrics data for all the servers in an excel file in a column format.   
However, you would like to have metrics data for each server in a separate sheet. 
Also properly formated & pivoted so it makes it easy to analyze the data or generate graphs out of it.
This script will help you just do that. It takes data in a column format and saves pivoted data of each system/application into a separate sheet.

![Data](https://github.com/hseera/python-utilities/blob/main/images/formatted-server-metrics.png)


## Contribute

Please do contribute! Issues and pull requests are welcome.

## Author
[<img id="github" src="./images/github.png" width="50" a="https://github.com/hseera/">](https://github.com/hseera/)    [<img src="./images/linkedin.png" style="max-width:100%;" >](https://www.linkedin.com/in/hpseera) [<img id="twitter" src="./images/twitter.png" width="50" a="twitter.com/HarinderSeera/">](https://twitter.com/@HarinderSeera) <a href="https://twitter.com/intent/follow?screen_name=harinderseera"> <img src="https://img.shields.io/twitter/follow/harinderseera.svg?label=Follow%20@harinderseera" alt="Follow @harinderseera" />
