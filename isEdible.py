
from googlesearch import search
#from bs4 import BeautifulSoup
import requests
  
# read csv
file1 = open('input4.txt', 'r')
Lines = file1.readlines()

# read input; count occurences for conditional probabilties; save test_cases for prediction step
for line in Lines: #for line in stdin:
    x = line.rstrip('\n').split(',')

# search term
query = "default"

url = "https://www.google.com/search?q=" + query + "&sourceid=chrome&ie=UTF-8"

response = requests.get(url)

if 'food' in response.text:
    print("found one!")


# write modified csv



