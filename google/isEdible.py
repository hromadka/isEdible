from csv import reader
from csv import writer
from googlesearch import search
#from bs4 import BeautifulSoup
import requests
  
# read csv
fin = open('Dish-subset-TEST.csv', encoding='utf-8', errors='ignore')
Lines = fin.readlines()

# read input; write output line-by-line
with open('Dish-edible.csv', 'w') as fout:
    for line in Lines: #for line in stdin:
        query = "default"
        # note that this fails if there is a comma in the field
        x = line.rstrip('\n').split(',')

        # search term
        query = x[1]  

        url = "https://www.google.com/search?q=" + query + "&sourceid=chrome&ie=UTF-8"

        response = requests.get(url)
        txt = response.text.lower()

        result = ''
        if 'food' in txt:
            print(query, "<-- found one!")
            result = line + ",1" 
        elif 'drink' in txt:
            print(query, "<-- found one!")
            result = line + ",1"  
        elif 'recipe' in txt:  # this captures smoked pork chop
            print(query, "<-- found one!")
            result = line + ",1"
        else:
            # TODO add additional search terms 
            print(query, "<-- DO NOT EAT")
            result = line + ",0"     


        # write modified csv
        fout.write(result)

fout.close()
fin.close()


