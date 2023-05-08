import requests
import re
import time
import sys


arg1 = "links.txt"
arg2 = "results.csv"
if len(sys.argv) > 1:
        arg1 = sys.argv[1]
        if len(sys.argv) > 2:
            arg2 = sys.argv[2]
links = open(arg1, "r").read().splitlines()


def get_links():
    link_list = []
    for i in links:
        if "http" in i:
            link_list.append(i)
        else:
            link_list.append(0)
            
    return link_list

def count_keywords():
    
    result_list = []
    key_words = ["non-gaap", "adjusted earnings", "ebitda", "adjusted net income", "non-ifrs"]
    url_list = get_links()

    f = open(arg2, "w")
    for i in range(len(url_list)):
        result_list = []
        time.sleep(0.2)
        url = url_list[i]
        row = ''
        if url != 0:
            request = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) 
            text = request.text
#            text = re.sub("<[^<]+?>", "", text)
#            text = re.sub("[^a-zA-Z\d\s\u00C0-\u00FF]{2,}", "", text)
#            text = re.sub("\n+", "\n", text)
#            text = re.sub(" +", " ", text)
            text = text.lower()
            for j in key_words:
                count = text.count(j)
                result_list.append(count)

        if len(result_list) == 0:
            for i in range(len(key_words)):
                result_list = [""]
        

        for i in range(len(result_list)):
            row = row + str(result_list[i]) + ","
        print(row[:-1])
        f.write(row[:-1]+"\n")
    f.close()
    return 



count_keywords()
