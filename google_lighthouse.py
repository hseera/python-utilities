# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime

#Query pagespeed api with requested url 
def execute_pagespeed(pagespeed_base_url, params):
    response = requests.get(pagespeed_base_url, params = params) #, timeout=5.5
    if (response.status_code == 200):
        extract_metrics(response.text)
    else:
        print("Invalid Response/API Key/URL")

#extract lighthouse metrics
def extract_metrics(api_response):
    try:
        metrics = {}  
        
        response = json.loads(api_response)
        
        measuretime = datetime.now()
        metrics['measurement_date'] = measuretime.strftime('%Y-%m-%d %H:%M:%S')
        
        if (response.get('lighthouseResult') != None):
            lighthouse_result = response.get('lighthouseResult')
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
            
            #Get performance metric data
            perf_metrics = [ 'largest-contentful-paint','first-contentful-paint','interactive',
					  'speed-index','total-blocking-time','cumulative-layout-shift' ]
            
            for perf_metric in  perf_metrics:
                try:
                    metrics[perf_metric] = lighthouse_result['audits'][perf_metric]['numericValue']
                except Exception:
                    metrics[perf_metric] = 'null'
            
            #Get debug metric data
            debug_metrics = [ 'numRequests','numScripts','maxServerLatency',
					  'throughput','numTasksOver100ms','numFonts',
                      'numTasksOver500ms','numStylesheets','numTasksOver10ms', 
                      'numTasksOver50ms','mainDocumentTransferSize','numTasksOver25ms',
                      'totalTaskTime','maxRtt','numTasks',
                      'rtt','totalByteWeight']
            
            for debug_metric in  debug_metrics:
                try:
                    metrics[debug_metric] = lighthouse_result['audits']['diagnostics']['details']['items'][0][debug_metric]
                except Exception:
                    metrics[debug_metric] = 'null'
            
        display_metrics(metrics)
    
    except Exception as ex:
        print(ex)


#Print extracted lighthouse metrics for the url. Replace/Update this function to save the data in a timeseries database.
def display_metrics(metrics):
     print(metrics)
  
def main():
    #api parameters
    requested_url = 'xxxxxx'   #replace it with your url
    apikey = 'AIzaSyA5ILl...'  # replace apikey with your pagespeed api key
    pagespeed_service_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    parameters = { 'url': requested_url,
        'key': apikey ,
        'strategy': 'DESKTOP', #'strategy'-> 'DESKTOP'/'MOBILE'
        'category':['PERFORMANCE','ACCESSIBILITY','BEST_PRACTICES','SEO'],
        'locale': 'en' }
    execute_pagespeed(pagespeed_service_url, parameters)

if (__name__=="__main__"):
    main()
