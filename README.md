# Python Utilities
![Language Python](https://img.shields.io/badge/%20Language-python-blue.svg) [![MIT License](http://img.shields.io/badge/License-MIT-blue.png)](LICENSE)
[![GitHub Size](https://img.shields.io/github/repo-size/hseera/python-utilities.svg)](https://github.com/hseera/python-utilities/)
[![GitHub Last Commits](https://img.shields.io/github/last-commit/hseera/python-utilities.svg)](https://github.com/hseera/python-utilities/commits/)

Different python utility scripts to help automate mundane/repetitive/specific performance testing tasks.
The readme page will continue to get updated as and when I add a new utility to the repo.

**Note:** Most of these utilities are focused around performance testing/engineering. 
However, with some modifications(/in some cases none) can be used in other fields/areas too.


|Utility Link |Utility Link|Utility Link|Utility Link|
|:-------------------------|:---------------|:------------------|:------------------|
|[1: Merge Files Column](#1-merge-files-column)|[2: Unique and Sorted](#2-unique-and-sorted)|[3: Histogram](#3-histogram)|[4: Extract Matched Data](#4-extract-matched-data)|
|[5: Swap Columns](#5-swap-columns)|[6: Randomize Data](#6-randomize-data)|[7: Unique Occurrence Count](#7-unique-occurrence-count)|[8: Split File By Text](#8-split-file-by-text)|
|[9: Heatmap](#9-heatmap)|[10: Pivot Table](#10-pivot-table)|[11: Generate ABN And ACN](#11-generate-abn-and-acn)|[12: Network Conversation Heatmap](#12-network-conversation-heatmap)|
|[13: Creditcard Generator](#13-creditcard-generator)|[14: TFN Generator](#14-tfn-generator)|[15: IRD Generator](#15-ird-generator)|[16: Dollar Format](#16-dollar-format)|
|[17: File Splitter](#17-file-splitter)|[18: Locate File](#18-locate-file)|[19: Websphere Verbosegc](#19-websphere-verbosegc)|[20: Formatted Server Metrics To Excel](#20-formatted-server-metrics-to-excel)|
|[21: Merge Columns](#21-merge-columns)|[22: Arrange Files](#22-arrange-files)|[23: Outliers](#23-outliers)|[24: Basic Statistics](#24-basic-statistics)|
|[25: Generate Name](#25-generate-name)|[26: File Detail](#26-file-detail)|[27: Port Scanner](#27-port-scanner)|[28: Google Lighthouse](#28-google-lighthouse)|
|[29: Multi Plots](#29-multi-plots)|[30: Split String in Column](#30-split-string-in-column)|[31: Remove Consumed Data](#31-remove-consumed-data)|[32: Word Cloud](#32-word-cloud)|
|[33: Influxdb JMeter Plot](#33-influxdb-jmeter-plot)|[34: OSWatcher top](#34-oswatcher-top)|||
----

# [1: Merge Files Column](#1-merge-files-column)
This script merges columns from multiple files and generates a new file.
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

# [12: Network Conversation Heatmap](#12-network-conversation-heatmap)
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

# [18: Locate File](#18-locate-file)
Recursively search for a file in a folder and all its subfolders. Print out the locations where that file is located.
Useful when you don't want to scroll through all the folders and files to locate the file you need.

![Data](https://github.com/hseera/python-utilities/blob/main/images/find-files.png)

# [19: Websphere Verbosegc](#19-websphere-verbosegc)
Save highlevel websphere verbosegc metrics into csv. Useful when you want to import the data to a load test tool for analyses & correlate with other metrics.
Assupmtion is that you do have any other means (i.e apm tools, sitescope etc) to view this data with other application & system metrics.  

![Data](https://github.com/hseera/python-utilities/blob/main/images/verbosegc.png)

# [20: Formatted Server Metrics To Excel](#20-formatted-server-metrics-to-excel)
There are situations when you get metrics data for all the servers in an excel file in a column format.   
However, you would like to have metrics data for each server in a separate sheet. 
Also properly formated & pivoted so it makes it easy to analyze the data or generate graphs out of it.
This script will help you just do that. It takes data in a column format and saves pivoted data of each system/application into a separate sheet.

![Data](https://github.com/hseera/python-utilities/blob/main/images/formatted-server-metrics.png)

# [21: Merge Columns](#21-merge-columns)
This script merges multiple columns in a file to two columns. One column with the values and other the header names.
Useful when you want to do analysis (i.e. Tukey test on the data set) using python.

![Data](https://github.com/hseera/python-utilities/blob/main/images/merge-columns.png)

# [22: Arrange Files](#22-arrange-files)
This script arranges files in the appropriate folder so it easy to find them when needed. 
Useful when you want to have seperate folder for data, scripts, scenario & result. 
Also useful when you want to arrange all the files in your download folder which might have images, music, executable, video files.

![Data](https://github.com/hseera/python-utilities/blob/main/images/arrange-files.png)

# [23: Outliers](#23-outliers)
Use Tukey fence test to identify outliers from the data set. 
Useful when you just want to know the outlier values. 
Also useful when extreme outliers distort the visualization and therefore you want to remove them temporarily to analyze the rest of the data.

![Data](https://github.com/hseera/python-utilities/blob/main/images/outliers.png)

# [24: Basic Statistics](#24-basic-statistics)
Generate basic statistics. Useful when you want to generate & compare statistics of different test runs. 
Saves time of not filling in all the formulas in excel.

![Data](https://github.com/hseera/python-utilities/blob/main/images/basic-statistics.png)

# [25: Generate Name](#25-generate-name)
Generate list of random names. Useful when you want to have alot of random names for testing purpose. Following options are available:
1. First name Only
2. First & Last name
3. Full name
4. Full name but abbreviated Middle name 

  
![Data](https://github.com/hseera/python-utilities/blob/main/images/generate-name.png)

# [26: File Detail](#26-file-detail)
Recursively list all files present in the directory (& sub directory) with File type & permission, File Size, Owner Id and Last modified date. The file detail is saved in a text file.
  
![Data](https://github.com/hseera/python-utilities/blob/main/images/file-detail.png)

# [27: Port Scanner](#27-port-scanner)
Given a list of hostname/ipaddresses, scan for open ports. Useful for system admin to identify which ports are open and which are closed.
Useful for performance engineers too.

![Data](https://github.com/hseera/python-utilities/blob/main/images/port-scanner.png)

# [28: Google Lighthouse](#28-google-lighthouse)
For a given URL, capture lighthouse performance and debug metrics. Useful for webpage performance analysis. 
You can extend the code to save the metrics to a time-series DB (i.e. influxdb) and use visualization tools such as Grafana to view the metrics.

![Data](https://github.com/hseera/python-utilities/blob/main/images/google-lighthouse.png)

# [29: Multi Plots](#29-multi-plots)
This script shows you how to create an image with multiple plots/graphs & table. Useful for generating graphs out of JMeter raw data.
Can we modified to cater for other tools like Gatling.

![Data](https://github.com/hseera/python-utilities/blob/main/images/graphs.png)

# [30: Split String in Column](#30-split-string-in-column)
This script splits strings using a delimiter in a column and saves all the resultant strings to a csv. Useful when you need to get total count.

![Data](https://github.com/hseera/python-utilities/blob/main/images/split-strings-in-column.png)

# [31: Remove Consumed Data](#31-remove-consumed-data)
This script removes consumed data from the original data set. Useful for those tests where you have a consumable data and you need to refresh the original data file with data that is still valid and usable.

![Data](https://github.com/hseera/python-utilities/blob/main/images/remove-consumed-data.png)

# [32: Word Cloud](#32-word-cloud)
Create a word cloud out of title, name etc.
![Data](https://github.com/hseera/python-utilities/blob/main/images/word-cloud.png)

# [33: Influxdb JMeter Plot](#33-influxdb-jmeter-plot)
This simple utility connects to Influxdb, downloads the JMeter response time data and plots a chart.
It demostrate how to accomplish the task. Script can be modified as per your need.
 
![Data](https://github.com/hseera/python-utilities/blob/main/images/plot.png)

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
```
Note: 
1: The script was tested on Windows OS.
2: NovatecConsulting JMeter plugin was used in JMeter to send data to Influxdb. 

Link: https://github.com/NovaTecConsulting/JMeter-InfluxDB-Writer/releases
```

### Prerequisites

What things you need to execute the script

```
1: Python 3.5
2: Influxdb, Panda & Matlab packages installed
```

### Execution
```
1: Make sure above prerequisite are met first.
2: Update the Influxdb connection detail in the script.
3: Update the Influx query accordingly. Sample query example are provided in the script.
4: Update the script with the correct timezone. By default the script timezone is set to Australia/Melbourne.
5: Run the python script
```

# [34: OSWatcher top](#34-oswatcher-top)
There are times when you have data gathered by [OSWbb](https://docs.oracle.com/cd/E37670_01/E37355/html/ol_oswatcher_diag.html) but don't have the OSWbba analyzer to view it. 
This python script extracts the system metrics (CPU/memory/load/task/swap) gathered by the oswtop script.
You pass in the oswtop file to the script and it will extract the system metrics and save them in a CSV.
Use can then use any visualization tool to visualize the data or import it into a load testing tool (if tool permits) to visualize it.

## Contribute

Contribution is welcomed. Pull requests are welcomed too.

## Author
[<img id="github" src="./images/github.png" width="50" a="https://github.com/hseera/">](https://github.com/hseera/)    [<img src="./images/linkedin.png" style="max-width:100%;" >](https://www.linkedin.com/in/hpseera) [<img id="twitter" src="./images/twitter.png" width="50" a="twitter.com/HarinderSeera/">](https://twitter.com/@HarinderSeera) <a href="https://twitter.com/intent/follow?screen_name=harinderseera"> <img src="https://img.shields.io/twitter/follow/harinderseera.svg?label=Follow%20@harinderseera" alt="Follow @harinderseera" /> </a>          [![GitHub followers](https://img.shields.io/github/followers/hseera.svg?style=social&label=Follow)](https://github.com/hseera?tab=followers)
