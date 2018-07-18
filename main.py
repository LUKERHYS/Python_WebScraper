# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.golfclubs4cash.co.uk/drivers'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse teh html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# take out the <div> of product-item-title and get its value
name_box = soup.find('h2', attrs={'class': 'product-item-title'})
price_box = soup.find('span', attrs={'class': 'price'})
#description_box = soup.find('div', attrs={'id': 'ds_div'})

# strip() is used to remove starting and tailing
name = name_box.text.strip()
#price_str = price_box.string()
price = price_box
#description = description_box.text.strip()

print(name)
print(price)
#print(description)
