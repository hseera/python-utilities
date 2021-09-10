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
|[33: Influxdb JMeter Plot](#33-influxdb-jmeter-plot)|[34: OSWatcher top](#34-oswatcher-top)|[35: Tornado Graph](#35-tornado-graph)||
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
Extract data that matches a text in the data file and save it to a new file.Useful when you have a single large data file containing all of the data and wish to create different data for each test run.

For example, suppose you have a single large data file with images, java, and CSS URLs. And you want to build distinct data files for CSS, JS, and pictures.
This script will assist you in doing so.

In the screenshot below, team was not part of the search text, hence no csv was created for it. The name is the file's column name. 
![Data](https://github.com/hseera/python-utilities/blob/main/images/split-file-by-text.png)

# [9: Heatmap](#9-heatmap)
There may be instances when using a line chart, it is difficult to detect slight swings in data.
This script creates a heatmap for the data when you are attempting to observe patterns over minutes/hours but for a longer period of time (i.e.30 days).
For example, there may be a specific hour of the day when there is increased load, but it is not greater than the peak load for the day.
As a result, a line chart for a longer period of time (e.g., 30 days) may hide or obscure that pattern.


The same thing can be done in Excel using a pivot table, but it will take some manual effort. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/heatmap.png)

# [10: Pivot Table](#10-pivot-table)
This script converts extensive data (two/three column data) into a summairzed pivot table format. 
Useful when you want to have a summarized view of the requests/error/response time over long period.

![Data](https://github.com/hseera/python-utilities/blob/main/images/pivot.png)

# [11: Generate ABN And ACN](#11-generate-abn-and-acn)
Generate random ABN and ACN numbers. Useful for performance/functional test scenario's that require valid ABN and/or ACN data for testing.

![Data](https://github.com/hseera/python-utilities/blob/main/images/abn-acn.png)

# [12: Network Conversation Heatmap](#12-network-conversation-heatmap)
Create a heatmap from the network conversation obtained in the trace file.
When you have a large number of conversations captured, this is really useful. 
If you are not comfortable reading/trolling the Wireshark network conversation view, this script will help you visualise the conversations. 
It also gives the option of generating a graph. However, the technology used to produce the graph will need to be tweaked somewhat to accommodate too many conversations. The current code should suffice for less than 40 conversations in a trace file. 

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
Format the data file with a monetary value. 
When you need to transmit a dollar value parameter from a file in a payload instead of a number, this is useful.
The majority of the time, it should be handled in code.
If you are passing it through a file, this script can help you save time. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/dollar.png)

# [17: File Splitter](#17-file-splitter)
Split a big file into multiple smaller size files. 
Useful when you want to have unique data for the same script running across multiple injectors. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/file-splitter.png)

# [18: Locate File](#18-locate-file)
Search for a file in a folder and all of its subfolders recursively.
Print the locations where that file can be found.
When you don't want to scroll through all the folders and files to get the file you need, this feature comes in handy. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/find-files.png)

# [19: Websphere Verbosegc](#19-websphere-verbosegc)
Save the high-level websphere verbosegc metrics to a csv file.
When you wish to import data into a load test tool for analysis and correlation with other metrics, this is useful.
Assumption is that you have other tools (e.g., apm tools, sitescope, etc.) to view this data alongside other application and system metrics. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/verbosegc.png)

# [20: Formatted Server Metrics To Excel](#20-formatted-server-metrics-to-excel)
In some cases, you will receive metrics data for all servers in an excel file in a column format.
You would prefer, however, to have metrics data for each server on a separate sheet. 
Also, the data is appropriately formatted and pivoted, making it simple to analyse and build graphs from it. 
This script will assist you in doing so. 

It accepts data in column format and stores pivoted data from each system/application to a separate sheet. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/formatted-server-metrics.png)

# [21: Merge Columns](#21-merge-columns)
This script merges multiple columns in a file to two columns. One column with the values and other the header names.
Useful when you want to do analysis (i.e. Tukey test on the data set) using python.

![Data](https://github.com/hseera/python-utilities/blob/main/images/merge-columns.png)

# [22: Arrange Files](#22-arrange-files)
This script organises files in the right folder so that they are easier to find when needed.
When you wish to have a separate folder for data, scripts, scenarios, and results, this is useful.
Also excellent for organising all of the contents in your download folder, which may contain photos, music, executables, and video files. 

![Data](https://github.com/hseera/python-utilities/blob/main/images/arrange-files.png)

# [23: Outliers](#23-outliers)
To identify outliers in a data collection, use the Tukey fence test.
When you merely want to know the outlier values, this is a great tool.
Also useful when extreme outliers distort the display and you need to eliminate them temporarily in order to study the rest of the data. 

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
There are situations when you have [OSWbb](https://docs.oracle.com/cd/E37670_01/E37355/html/ol_oswatcher_diag.html) data but don't have the OSWbba analyser to view it.
The system metrics (CPU/memory/load/task/swap) gathered by the oswtop script are extracted using this python script.
The script will extract the system metrics and save them in a CSV file after you provide it the oswtop file.
The data can then be visualised using any visualisation tool or imported into a load testing tool (if the programme allows it). 


# [35: Tornado Graph](#35-tornado-graph)
Generate response time tornado graph. This type of graph is excellent for showing points of freezing in a system, more so than standard 
scatter graphs.

![Data](https://github.com/hseera/python-utilities/blob/main/images/tornado-graph.jpg)

## Contribute

Contribution is welcomed. Pull requests are welcomed too.

## Author
[<img id="github" src="./images/github.png" width="50" a="https://github.com/hseera/">](https://github.com/hseera/)    [<img src="./images/linkedin.png" style="max-width:100%;" >](https://www.linkedin.com/in/hpseera) [<img id="twitter" src="./images/twitter.png" width="50" a="twitter.com/HarinderSeera/">](https://twitter.com/@HarinderSeera) <a href="https://twitter.com/intent/follow?screen_name=harinderseera"> <img src="https://img.shields.io/twitter/follow/harinderseera.svg?label=Follow%20@harinderseera" alt="Follow @harinderseera" /> </a>          [![GitHub followers](https://img.shields.io/github/followers/hseera.svg?style=social&label=Follow)](https://github.com/hseera?tab=followers)
