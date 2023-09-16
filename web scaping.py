#importing libraryes
import requests
from bs4 import  BeautifulSoup
#add  url from web page
url="https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
#now we send request to server
response=requests.get(url)
#now checq our request is comnfirm or not

#print(response)

#when it is 200 then it is ok else not
#now creat a veriable for store our code
soup=BeautifulSoup(response.text,"html.parser")
#find command only works for first element
price=(soup.find('h4',attrs={"class":"pull-right price"}))
#print price using text or string

#print(price.text)

title=soup.find("a",attrs={"class":"title"})

#print(title.text)

description=soup.find("p",attrs={"class":"description"})

#print(description.text)

#lets find full details of one artical
full=soup.find('div',attrs={"class":"col-sm-4 col-lg-4 col-md-4"})

#print(full.text)

#find all code uses for all element
all_price=soup.findAll('h4',attrs={"class","pull-right price"})

#print(len(all_price))

#there are length of our price

#now we checq our prices

#print(all_price)

#so with prices we get tag also so now we get only pricese

#for i in all_price:
    #print(i.text)

#now if I want to find any particular value

#print(all_price[4].text)

#find all with description

all_description = soup.findAll('p',attrs={"class","description"})

#print(all_description)

# now simlarly we want only values

#for i in all_description:
    #print(i.text)

#for particular value

#print(all_description[4].text)

#now find all with title

all_title=soup.findAll("a",attrs={"class","title"})

#print(all_title)

#step 2 for loop

#for i in all_title:
    #print(i.text)

#last step

#print(all_title[4].text)

#for full box element in one shot
all_full=soup.findAll('div',attrs={"class","col-sm-4 col-lg-4 col-md-4"})
#print(all_full)
#for function
#for i in all_full:
    #print(i.text)
#now cheq

#print(all_full[1].text)

#find all with string it give only value whic we write on code

string1=soup.find_all(string="Galaxy Tab")

#print(string1)

#for find values whic we want more text if it have on web first import re library then

import re
string2=soup.find_all(string=re.compile("Idea"))

#print(string2)

#create dataframe
import pandas as pd
names=[]
for i in all_title:
    names.append(i.text)
#print(names)

#step 2 price
cost=[]
for i in all_price:
    cost.append(i.text)
#print(cost)

#step3
details=[]
for i in all_description:
    details.append(i.text)
#print(details)

#step4
reaction=[]
all_reviews=soup.findAll("p",attrs={"class","pull-right"})
for i in all_reviews:
    reaction.append(i.text)
#print(reaction)

#step 5 create data frame
df=pd.DataFrame({"product":names,"price":cost,"details":details,"reviews":reaction})
#print(df)

#dataframe to csv

df.to_csv("tablets.csv")

#creat table
#import libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://ticker.finology.in/"
rr=requests.get(url)
#print(rr)
soup2=BeautifulSoup(rr.text,"html.parser")
table=soup2.find("table",attrs={"class","table table-sm table-hover screenertable"})
hh=table.findAll("th")
header=[]
for i in hh:
    header.append(i.text)
#print(header)
aa=pd.DataFrame(columns=header)
#print(aa)
rows=table.findAll("tr")
for i in rows[1:]:
    data=i.find_all("td")
    row=[tr.text.strip() for tr in data]
    l=len(aa)
    aa.loc[l]=row
#print(aa)