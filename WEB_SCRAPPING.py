
import csv
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


url='https://www.luluhypermarket.com/en-kw/'




def get_url(search_term):
    template = 'https://www.luluhypermarket.com/en-kw/search/?text={}%3Arelevance'
    search_term=search_term.replace(' ','+')
    return template.format(search_term)


url =get_url('mobile phones')
print(url)


driver.get(url)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

soup = BeautifulSoup(driver.page_source,'html.parser')

results = soup.find_all('input',{'data-list-name': 'Search Results'})

#print(len(results))


#item = results[39]



#print(item)



'''soup.find_all("a", class_="sister")
print("category0 = "+item.get("data-category0"))
print("category1 = "+item.get("data-category1"))
print("category2 = "+item.get("data-category2"))
print("category3 = "+item.get("data-category3"))
print("category4 = "+item.get("data-category4"))
print("category5 = "+item.get("data-category5"))
print("category6 = "+item.get("data-category6"))
print("category7 = "+item.get("data-category7"))
print("category8 = "+item.get("data-category8"))
print("product name = "+item.get("data-name"))
print("price ="+item.get("data-price"))'''


def extract_record(item):
    category0 = item.get("data-category0")
    category1 = item.get("data-category1")
    category2 = item.get("data-category2")
    category3 = item.get("data-category3")
    category4 = item.get("data-category4")
    category5 = item.get("data-category5")
    category6 = item.get("data-category6")
    category7 = item.get("data-category7")
    category8 = item.get("data-category8")
    product_name = item.get("data-name")
    product_name1=  re.sub('<>', '', product_name)
    price = item.get("data-price")

    result =(category0,category1,category2,category3,category4,category5,category6,category7,category8,product_name1,price)
    return result

records =[]
results = soup.find_all('input',{'data-list-name': 'Search Results'})

for item in results:
    records.append(extract_record(item))
    


for row in records:
    print(row[9]+"--"+row[10])


