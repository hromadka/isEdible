from csv import reader
from csv import writer
#from googlesearch import search
#from bs4 import BeautifulSoup
#import requests

MIN_LENGTH = 4

# read DISH csv
NAME_CORRECTED = 2
fin = open('Dish-csv.csv', encoding='utf-8', errors='ignore')
Lines = fin.readlines()

flookup = open('lookup-pg-csv.csv', 'r', encoding='utf-8')
Refs = flookup.readlines()
flookup.close()

#dishes = dict.fromkeys(Refs)
dishes = {}
for ref in Refs:
    r = ref.rstrip('\n').split(',')
#    print(r)
    dishes[r[0]] = "1"  # dummy value just in case


# read input; write output line-by-line
counter = 0
fout = open('Dish-edible.csv', 'w')
for line in Lines: #for line in stdin:
    counter += 1  # for debugging, can delete
    query = "default"
    # note that this fails if there is a comma in the field!
    x = line.rstrip('\n').split(',')

    # search term
    isEdible = 0
    if x[NAME_CORRECTED] in dishes:
        print('found ' + x[NAME_CORRECTED])
        isEdible = 1
        #fout.write("1\n")
    else:
        # now try just keywords
        words = x[NAME_CORRECTED].split(" ")
        for word in words:
            w = word.strip().strip('"')
            if len(w) > MIN_LENGTH:
                if w in dishes:
                    print('found ' + x[NAME_CORRECTED])
                    isEdible = 1
                    #fout.write("1\n") 
            if isEdible:
                continue                   

    if not isEdible:
        print('do not eat ' + x[NAME_CORRECTED])
#        fout.write("0\n")  
    # write modified csv
    if counter == 1:
        fout.write("isEdible\n")
    else:
        fout.write(str(isEdible)+"\n")

 #   if counter > 100:
 #       break


fout.close()
fin.close()
print(counter)

