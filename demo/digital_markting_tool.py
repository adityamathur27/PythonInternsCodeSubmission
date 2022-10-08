import pandas as pd
import json
import requests
from datetime import date,timedelta

keyword=input("Enter keyword: ")
key=keyword

que_list=[]
site_list=['quora.com','reditt.com']
for site in site_list:
    keyword=keyword+" site:"+site

    #key - AIzaSyA7pM6zI2twi8fCD2W0IutObwp0YFJ2f5Y
    google_url="https://www.googleapis.com/customsearch/v1/?key=AIzaSyA7pM6zI2twi8fCD2W0IutObwp0YFJ2f5Y&cx=90d1c4236e23b4cd0"
    google_url=google_url+"&q="+keyword

    res=requests.get(google_url)
    # print("Response: "+res.text)

    json_res=json.loads(res.text)

    try:
        for item in json_res["items"]:
            title=item["title"]
            title=title.replace(" - Quora","")
            que_list.append(title)




    except Exception as e:
        pass


    keyword=key

que_Dict={"Quetions":que_list}
df=pd.DataFrame(data=que_Dict)


df.to_csv(key+"_quetions.csv")
