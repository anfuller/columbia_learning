#import your modules 
from bs4 import BeautifulSoup
import requests
import csv 

#create a file for our data
with open('books.csv','w') as f:  
  writer = csv.writer(f)
  headers = ['star_rating','title','price','in_stock_status']
  writer.writerow(headers)

  # #loop through all the pages
  # for page in range(1,51):
  #   print(page)
  #   url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'

  #   r = requests.get(url)
  #   html = r.content 
  #   soup = BeautifulSoup(html, features="html.parser")

  #   #get the text we're going to go through
  #   section = soup.find('section')
  #   row = section.find('ol', {'class':'row'})
  #   products = row.findAll('li')

  #   #loop through the products on this page
  #   for product in products:
  #     star_rating = product.find('p').get('class')
  #     star_rating = star_rating[1]
  #     title = product.find('h3')
  #     title = title.find('a').get('title')
  #     price = product.find('p', {'class': 'price_color'}).text
  #     in_stock_status = product.find('p',
  #     {'class': 'instock availability'}).text
  #     in_stock_status = in_stock_status.strip()
  #     record = (star_rating, title, price, in_stock_status)
  #     writer.writerow(record)




#comments
#importing modules  
#printing 
#quotation marks
#ethics 
#tabs and spacing 
#loops 