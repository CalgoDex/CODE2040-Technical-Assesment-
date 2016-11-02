# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:11:59 2016
@author: cgg2126
Technical assessment for CODE2040
"""
#******************************************************************************
#Part 1 of the Techinical appplication
import requests
import ast
import dateutil.parser
import datetime

#dictionary of keys, token and github
data = { "token": "PUT YOUR TOKEN HERE",
        "github": "https://github.com/CalgoDex/CODE2040-Technical-Assesment-"}
        
r = requests.post("http://challenge.code2040.org/api/register",data)

#Checks status of response
print(r.status_code)
#******************************************************************************
#Q1 of the technical application

#Posting dictionary with token and the endpoints
#data2 = {'token':'516d682c6160ff88eac63c4512b616d3'}
post_site = requests.post('http://challenge.code2040.org/api/reverse',data)

#This part of the code will reverse the string that is received
get_Str = post_site.text
reverse = get_Str[::-1]
rev_stuff = {'token': '516d682c6160ff88eac63c4512b616d3', 'string' : reverse}

#Posting the reversed string to site
posting = requests.post("http://challenge.code2040.org/api/reverse/validate",
                        rev_stuff)
                        
#checks status of response                                 
print(posting.status_code)
#******************************************************************************
#Q2 of the technical application

#will create an object reference for the dictionary
collections = requests.post("http://challenge.code2040.org/api/haystack",
                            data)
#Transforms value referenced by collections into one string
new_collections = collections.text    

#Converts that string into a dictionary using the ast module
new_collections = ast.literal_eval(new_collections)
count = 0 #counter for indices
pos = 0 #will be the location of the needle value

#Loops over the array referenced by the key haystack and checks and sees
#if any of the elements at said index equals the value referenced by needle
for elem in new_collections['haystack']:
    if elem == new_collections['needle']:
        pos = count
    else:
        count += 1
#Dictionary containing the position at which the needle is found in haystack
dict = {'token': '516d682c6160ff88eac63c4512b616d3', 'needle': pos }        
response = requests.post('http://challenge.code2040.org/api/haystack/validate',
                         dict)
#Checks status of response                         
print(response.status_code)
#******************************************************************************
#Q3 of the technical application
#gets dictionary from server
pref_X = requests.post("http://challenge.code2040.org/api/prefix",data)

#turns entire dictionary into a string 
prefix_dict = pref_X.text

#turns string into a dictionary
prefix_dict = ast.literal_eval(prefix_dict)

no_prefix = [] #will contain words without the prefix

#iterates over the array of words and appends those that do not have the prefix
#into the no_prefix array
for elem in prefix_dict['array']:
    if not elem.startswith(prefix_dict['prefix']):
        no_prefix.append(elem)
        
not_prefix = {}        

#array containing token and value for no_prefix        
not_prefix['array'] = no_prefix
not_prefix['token'] = '516d682c6160ff88eac63c4512b616d3'

#posts response
response = requests.post("http://challenge.code2040.org/api/prefix/validate",
                         json = not_prefix)

#Checks status of response                         
print(response.status_code)
#******************************************************************************
#Q4 of the techinical application

#Gets date and interval to add from server
date_X = requests.post("http://challenge.code2040.org/api/dating",data)

#turns entire dictionary into a string
array_time = date_X.text

#converts string to a dictionary
array_time = ast.literal_eval(array_time)

#assigns value of datestamp and interval
datestamp1 = array_time['datestamp']
interval = array_time['interval']

#converts interval being added into an integer
secs = int(interval)

#parses the datestamp into an object for easy handling
date_parse = dateutil.parser.parse(datestamp1)

#adds the interval to the date
seconds = datetime.timedelta(seconds = secs)
new_date = date_parse + seconds

#gets the iso 8601 format including the +00:00 time zone portion
new_date = new_date.isoformat(sep='T')

#substitutes the '+00:00' substring with 'Z'
if '+00:00' in new_date:
    new_date = new_date.replace('+00:00','Z')

#dictionary containing token and new_date 
datestamp = {"token":"516d682c6160ff88eac63c4512b616d3",
             "datestamp": new_date}

#response sent to server to check             
response = requests.post("http://challenge.code2040.org/api/dating/validate",
                         datestamp)

#checks status of response
print(response.status_code)




















