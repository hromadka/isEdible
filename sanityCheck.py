from csv import reader
from csv import writer
from googlesearch import search
#from bs4 import BeautifulSoup
import requests
  
# read csv
fin = open('Dish-csv.csv', 'r')

count = 0

while True:
	line = fin.readline()
	count += 1
	print(line)
	if not line:
		break

print(count)

fin.close()