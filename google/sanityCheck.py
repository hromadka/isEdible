from csv import reader
from csv import writer
from googlesearch import search
#from bs4 import BeautifulSoup
import requests
  
# read csv
fin = open('Dish-csv.csv', encoding='utf-8', errors='ignore')

count = 0

while True:
	line = fin.readline()
	count += 1
	print(line)
	if not line:
		break

print(count)

fin.close()