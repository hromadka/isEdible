from googlesearch import search
#from bs4 import BeautifulSoup
import requests
  
# read csv


# search term
query = "pim-olas"

url = "https://www.google.com/search?q=" + query + "&sourceid=chrome&ie=UTF-8"

response = requests.get(url)

if 'food' in response.text:
    print("found one!")





