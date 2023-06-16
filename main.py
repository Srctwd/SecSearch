import re
import time
import sys
import os
import requests

    
def get_links():
    link_list = []
    try:
        arg1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),"links.txt")
    except Exception as error:
        print(error)
        input("")
    arg2 = "results.csv"
    if len(sys.argv) > 1:
            arg1 = sys.argv[1]
            if len(sys.argv) > 2:
                arg2 = sys.argv[2]
    try:
        links = open(arg1, "r").read().splitlines()
    except Exception as error:
        print(error)
        input("")
    for i in links:
        if "http" in i:
            link_list.append(i)
        else:
            link_list.append(0)
            
    return link_list, arg1, arg2

def count_keywords():
    
    result_list = []
    key_words =  open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"keywords.txt")).read().splitlines()
    url_list, arg1, arg2 = get_links()

    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), arg2), "w+")
    for i in range(len(url_list)):
        result_list = []
        time.sleep(0.2)
        url = url_list[i]
        row = ''
        if url != 0:
            request = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) 
            text = request.text
            text = text.lower()
            for j in key_words:
                count = text.count(j)
                result_list.append(count)

        for i in range(len(result_list)):
            row = row + str(result_list[i]) + ","
        print(row[:-1])
        f.write(row[:-1]+"\n")
    f.close()
    return 


try:
    count_keywords()
except Exception as error:
    print(error)
