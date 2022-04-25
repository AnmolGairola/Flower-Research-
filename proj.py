import webbrowser 
import os
import requests
from bs4 import BeautifulSoup
import re

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

print(0)
url = "https://www.all-my-favourite-flower-names.com/list-of-flower-names.html"
response = requests.get(url)
print(1)

if response.ok:
    print(2)
    soup = BeautifulSoup(response.text, "lxml")
    title = soup.find_all("b")
    #print(str(title[0].get_text()))
    
    num = 0
    limit = 10
    
    for i in title:
        num += 1
        txt = i.text.strip()
        if(len(txt) > 3 and txt.endswith(".")):
            print(txt)
            webbrowser.open('http://www.google.com/search?q=' + txt)
            
        if(num > limit):
            break

else:
    print("response not ok")

print(3)
#python (code name).py