import requests 
import pandas 
from bs4 import BeautifulSoup

response=requests.get("https://www.bikewale.com/best-bikes-in-india/")
#print(response)

soup=BeautifulSoup(response.content,"html.parser")
#print(soup)

items=soup.find_all('h3',class_="bikeTitle margin-bottom10")
item=[]
for i in items[0:10]:
    item.append(i.get_text())
print(item)
# # # # print(2*" ","items")

prices=soup.find_all('div',class_="text-bold")
price=[]
for i in prices[0:10]:
    price.append(i.get_text())
print(price)

reviews=soup.find_all('span',class_="font14 inline-block")
review=[]
for i in reviews[0:10]:
    review.append(i.get_text())
print(review)


Details=soup.find_all('div',class_="text-xt-light-grey font14 margin-bottom15")
Detail=[]
for i in Details[0:10]:
    Detail.append(str(i.get_text()))
print(Detail)


links=soup.find_all('a',class_="bw-ga")
link=[]
for i in links[0:10]:
    d='https://www.bikewale.com'+ i['href']
    link.append(d)
print(link)
img1=[]
images=soup.find_all('div',class_="imageWrapper")
for i in images[0:10]:
    j=i.img['src']
    img1.append(j)
#print(img1)
    

# print(df)
data={
    "items":pandas.Series(item),
    "prices":pandas.Series(price),
    "reviews":pandas.Series(review),
    "Details":pandas.Series(Detail),
    "Links":pandas.Series(link),
    "images":pandas.Series(img1),
}
print(data)
df=pandas.DataFrame(data) # 2 dimensional array rows*columns
print(df)

df.to_csv("Bikesdetails.csv")
