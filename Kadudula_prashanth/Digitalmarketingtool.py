import requests #library for http requests in python
import pandas as pd #library to represent responses in 2D format
import json #library for data reprsentation during transmission
from datetime import date,timedelta #library for datemangement
questions_list=[]
keyword=input("enter the keyword")
keyword1=keyword
site_list=["quora.com","reditt.com"]
for l in site_list:
    keyword=keyword+"%20site:"+ l
    # Key file - AIzaSyBE6tqFBueieJAVk8f_ZTcIJuKvpQ3UPzw
    google_url="https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyBE6tqFBueieJAVk8f_ZTcIJuKvpQ3UPzw&cx=012773643409177149611:giuhxzmolrc"
    google_url=google_url + "&q=" + keyword
    #print("GOOGLE URL:"+google_url)
    response=requests.get(google_url)
    #print("responses:"+str(response.text))
    #convert response string to jason object
    json_response=json.loads(response.text)
    search_time=json_response["searchInformation"]["searchTime"]
    print("search time taken is",search_time)
    total_results=int(json_response["searchInformation"]["totalResults"])
    print("Total results are ",total_results)
    #get the start index of next page
    #next_index=json_response["queries"]["nextPage"][0]["startIndex"]
    #loop through all the responses from the google
    total_pages=round(total_results/10)
    try:
     # Loop through the responses
     for item in json_response["items"]:
       title = item["title"]
       title = title.replace(" - Quora","")
       questions_list.append(title)
       #print(title)
    except Exception as e:
        pass
    # Reset the keyword
    keyword = keyword1
# questions_list
questions_dict = {"Questions": questions_list}
df = pd.DataFrame(data=questions_dict)
#export the data to a file
df
#now export it into a csv file
df.to_csv(keyword1+"_questions.csv")


