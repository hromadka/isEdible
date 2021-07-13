from googlesearch import search
from bs4 import BeautifulSoup
import requests
  
# to search
query = "pim-olas"

url = "https://www.google.com/search?q=" + query + "&sourceid=chrome&ie=UTF-8"

response = requests.get(url)
#print(response.text)

if 'food' in response.text:
    print("found one!")





