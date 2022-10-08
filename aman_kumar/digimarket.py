import requests 
import pandas as pd
import json

from datetime import date,timedelta

keyword = input("enter a keyword: ")
keyword1 = keyword
#keyword = keyword + "site:quora.com site:reditt.com"

site_list = ["quora.com","reditt.com","microsoft.com"]
for site in site_list:
    keyword = ""
    keyword = keyword + " site:"+ site
    print(keyword)
    #search on google using google API's and key
    #key file = AIzaSyA1JxtcWdYjtL9LRwgX7vhLw7pFoh3MWF0
    #google_url = "http://www.googleapis.com/customsearch/v1/?key=AIzaSyA1JxtcWdYjtL9LRwgX7vhLw7pFoh3MWF0&cx=43157bd8f39827832"
    google_url = "https://www.googleapis.com/customsearch/v1/?key=AIzaSyB0fpT6tagI4kgfy15h28awDRjk6kE2hXk&cx=012773643409177149611:giuhxzmolrc"
    google_url = google_url + "&q=" +keyword
    print("google Url: " + google_url)
    response = requests.get(google_url)
    print("Response: " + str(response.text))

    #convert response string into json object
    json_response = json.loads(response.text)
    #total_result = json_response ["searchInformation"]["total_result"]
    #print("total results are ", total_result)
    #Reset the keyword
    keyword = keyword1