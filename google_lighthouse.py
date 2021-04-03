# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime

#extract lighthouse metrics
def extract_metrics(pagespeed_response):
    try:
        metrics = {}  
        fullresults = json.loads(pagespeed_response)
        measuretime = datetime.now()
        metrics['measurement_date'] = measuretime.strftime('%Y-%m-%d %H:%M:%S')
        if (fullresults.get('lighthouseResult') != None):
            lighthouse_result = fullresults.get('lighthouseResult')
            metrics['requestedUrl'] = lighthouse_result['requestedUrl']
            
            metrics['device'] = lighthouse_result['configSettings']['emulatedFormFactor']
            
            if  lighthouse_result['configSettings']['emulatedFormFactor'] == 'desktop':
                metrics['device'] = 'D'
            elif lighthouse_result['configSettings']['emulatedFormFactor'] == 'mobile':
                metrics['device'] = 'M'
            else:
                metrics['device'] = 'D' # if the strategy option is "" or not present, It defaults to desktop
            
            metrics['locale'] = lighthouse_result['configSettings']['locale']
            
            categories = ['performance', 'accessibility','best-practices','seo']
            for category in categories:
                try:
                    metrics[category] = lighthouse_result['categories'][category]['score']*100
                except Exception:
                    metrics[category] = 'null'
            
            metrics['largest-contentful-paint'] = lighthouse_result['audits']['largest-contentful-paint']['numericValue']
            metrics['first-contentful-paint'] = lighthouse_result['audits']['first-contentful-paint']['numericValue']
            metrics['interactive'] = lighthouse_result['audits']['interactive']['numericValue']
            metrics['speed-index'] = lighthouse_result['audits']['speed-index']['numericValue']
            metrics['total-blocking-time'] = lighthouse_result['audits']['total-blocking-time']['numericValue']
            metrics['cumulative-layout-shift'] = lighthouse_result['audits']['cumulative-layout-shift']['numericValue']
            metrics['numRequests'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numRequests']
            metrics['numScripts'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numScripts']
            metrics['maxServerLatency'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['maxServerLatency']
            metrics['throughput'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['throughput']
            metrics['numTasksOver100ms'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numTasksOver100ms']
            metrics['numFonts'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numFonts']
            metrics['numTasksOver500ms'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numTasksOver500ms']
            metrics['numStylesheets'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numStylesheets']
            metrics['numTasksOver10ms'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numTasksOver10ms']
            metrics['numTasksOver50ms'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numTasksOver50ms']
            metrics['mainDocumentTransferSize'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['mainDocumentTransferSize']
            metrics['numTasksOver25ms'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numTasksOver25ms']
            metrics['totalTaskTime'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['totalTaskTime']
            metrics['maxRtt'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['maxRtt']
            metrics['numTasks'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['numTasks']
            metrics['rtt'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['rtt']
            metrics['totalByteWeight'] = lighthouse_result['audits']['diagnostics']['details']['items'][0]['totalByteWeight']
        display_metrics(metrics)
    except Exception as ex:
        print(ex)


#Shown captured metrics for the url. Replace/Update this function to save the data to a timeseries database.
def display_metrics(metrics):
     print(metrics)

#Invoke pagespeed api 
def execute_pagespeed(pagespeed_url, params ):
    response = requests.get(pagespeed_url, params = params) #, timeout=5.5
    if (response.status_code==200):
        extract_metrics(response.text)
    else:
        print("Invalid Response OR Invalid Key")
  
def main():
    #api parameters
    requested_url='https://www.bbc.co.uk/'   #replace the requested url with your url
    apikey='AIzaSyA5ILlS...'  # replace apikey with your pagespeed api key
    pagespeed_service_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    parameters = { 'url': requested_url,
        'key': apikey ,
        'strategy': 'DESKTOP', #'strategy'-> 'DESKTOP'/'MOBILE'
        'category':['PERFORMANCE','ACCESSIBILITY','BEST_PRACTICES','SEO'],
        'locale': 'en' }
    execute_pagespeed(pagespeed_service_url, parameters)

if (__name__=="__main__"):
    main()
