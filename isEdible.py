from csv import reader
from csv import writer
#from googlesearch import search
#from bs4 import BeautifulSoup
#import requests
  
# read DISH csv
fin = open('Dish.csv', encoding='utf-8', errors='ignore')
Lines = fin.readlines()

flookup = open('lookup-csv.csv', 'r', encoding='utf-8')
Refs = flookup.readlines()
flookup.close()

#dishes = dict.fromkeys(Refs)
dishes = {}
for ref in Refs:
    r = ref.rstrip('\n').split(',')
#    print(r)
    dishes[r[0]] = "1"


# read input; write output line-by-line
with open('Dish-edible.csv', 'w') as fout:
    for line in Lines: #for line in stdin:
        query = "default"
        # note that this fails if there is a comma in the field
        x = line.rstrip('\n').split(',')

        # search term
        isEdible = 0
        if x[1] in dishes:
            print('found ' + x[1])
            isEdible = 1
        else:
            print('do not eat ' + x[1])  
 
        # write modified csv
        fout.write(isEdible)

fout.close()
fin.close()

