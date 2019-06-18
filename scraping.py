#first part
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
a = ["http://www.datamation.com/data-center/20-big-data-companies-leading-the-way-1.html",
     "http://www.datamation.com/data-center/20-big-data-companies-leading-the-way-2.html", 
"http://www.datamation.com/data-center/20-big-data-companies-leading-the-way-3.html"]
for i in a:
    html = urlopen(i)
    bsObj = BeautifulSoup(html)
    #print(bsObj) 
    images = bsObj.findAll("strong")
    for i in images:
        print(i.text)


#second part
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
a = ["http://blog.dennybritz.com/2015/10/13/deep-learning-startups-applications-and-acquisitions-a-summary/"]
html = urlopen(a)
bsObj = BeautifulSoup(html) 
images = bsObj.findAll('a', {"class":"external"})
    #print (images.get_text())
for i in images:
    print(i.text)
    #print(bsObj)
