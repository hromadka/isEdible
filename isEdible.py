
from googlesearch import search
#from bs4 import BeautifulSoup
import requests
  
# read csv
file1 = open('Dish-subset-TEST.csv', 'r')
Lines = file1.readlines()

# read input; count occurences for conditional probabilties; save test_cases for prediction step
for line in Lines: #for line in stdin:
    query = "default"
    # note that this fails if there is a comma in the field
    x = line.rstrip('\n').split(',')

    # search term
    query = x[1]  

    url = "https://www.google.com/search?q=" + query + "&sourceid=chrome&ie=UTF-8"

    response = requests.get(url)

    if 'food' in response.text:
        print(query, "<-- found one!")
    else:
        # TODO add additional search terms 
        print(query, "<-- DO NOT EAT")


# write modified csv



