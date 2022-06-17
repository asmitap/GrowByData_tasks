#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import pandas as pd
from config import apiKey, ingredients
from urllib.parse import urlparse, parse_qs

#search_query = 'apple'
to_list = []

def add_to_dict(i, j,search_query, types):
    dict = {}
    dict["search_query"] = search_query
    dict["id"] = i["id"]
    dict["missedIngredientCount"] = i["missedIngredientCount"]
    dict["type"] = types
    dict["aisle"] = j["aisle"]
    dict["usedIngredientCount"] = i["usedIngredientCount"]
    dict["title"] = i["title"]
    dict["name"] = j["name"]
    dict["unit"] = j["unit"]
    dict["amount"] = j["amount"]
    #print(dict)
    to_list.append(dict)

def main():
    for ingredient in ingredients:
        #print(i)
        url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient}&apiKey={apiKey}"
        response = requests.get(url)
        data = json.loads(response.text)
        #print(data)
        parsed_url = urlparse(url)
        search_query = parse_qs(parsed_url.query)['ingredients'][0]
        for i in data:
            #print(i)
            if(i["missedIngredientCount"]):
                types = "missed_ingredient"
                for j in i["missedIngredients"]:
                    add_to_dict(i, j,search_query, types)
            if(i["usedIngredientCount"]):
                types = "used_ingredient"
                for j in i["usedIngredients"]:
                    add_to_dict(i, j, search_query, types)

    datas = to_list   
    df = pd.DataFrame (datas, columns = ['id','search_query', 'missedIngredientCount','type', 'aisle','usedIngredientCount','title', 'name','unit','amount'])
    print(df)
    #df.to_csv("task3_final.csv", index=False)

if __name__ == "__main__":
    main()


# In[ ]:




