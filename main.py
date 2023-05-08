import requests
import re
import time
import numpy as np
import pandas as pd

df = pd.read_csv("links.csv")


def get_links():
    link_list = []
    for i in df["Unnamed: 5"]:
        if type(i) is str and i[0:4] == "http":
            link_list.append(i)
        else:
            link_list.append(0)

    return link_list

def count_keywords():
    
    result_list = []
    key_words = ["non-gaap", "adjusted earnings", "ebitda", "adjusted net income", "non-ifrs"]
    url_list = get_links()

    for i in range(len(url_list)):
        result_list = []
        time.sleep(0.25)
        url = url_list[i]
        row = ''
        if url != 0:
            request = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) 
            text = request.text
            text = re.sub("<[^<]+?>", "", text)
            text = re.sub("[^a-zA-Z\d\s\u00C0-\u00FF]{2,}", "", text)
            text = re.sub("\n+", "\n", text)
            text = re.sub(" +", " ", text)
            text = text.lower()
            for j in key_words:
                count = text.count(j)
                result_list.append(count)

        if len(result_list) == 0:
            for i in range(len(key_words)):
                result_list = [""]
        
        f = open("planilha.csv", "a")
        for i in range(len(result_list)):
            row = row + str(result_list[i]) + ","
        print(row[:-1])
        f.write(row[:-1]+"\n")
    return 


count_keywords()
#results.to_csv("planilha.csv")









#text = open("page.txt", "r").read()
#text = re.sub("\t+", " ", text)
#with open('page.txt', 'w') as f:
#    f.write(text)
#text = re.sub("\n", "", text)
#print(text)
#print(re.sub("[^a-zA-Z0-9_ ]+", "", text))
#print(re.sub("<.*?>|<.*=|\n| ", "", r.text))
#print(re.sub("<.*=|\n|<.*?>| ", "", r.text))
#print(re.sub("</a>|</span>|</div>|</body>|</html>|<a>|<span>|<div>|<body>|<html>|<head>|</button>|<buttonname=|divclass|</p>|<p>|</li>|<li>|><|type =| |\n", "", r.text))
#print(re.sub("<.*?>|\n|<.*?=| ", "", r.text))
#print(re.sub("|<.*?=|<.*?>", "", r.text))
