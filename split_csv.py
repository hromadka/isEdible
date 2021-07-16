import pandas as pd


in_csv = 'Dish.csv'
number_lines = sum(1 for row in (open(in_csv,encoding='utf-8', errors='ignore')))
rowsize = 500000

#colnames = ['id', 'name', 'description', 'menus_appeared', 'times_appeared', 'first_appeared', 'last_appeared', 'lowest_price', 'highest_price']
# make this dynamic in case adding new cols through OpenRefine or other means
fin = open(in_csv, 'r')
header = fin.readline()
colnames = header.rstrip('\n').split(',')
fin.close()

for i in range(1,number_lines,rowsize):
    df = pd.read_csv(in_csv,
          header=None,
          nrows = rowsize,#number of rows to read at each loop
          skiprows = i)#skip rows that have been read
    out_csv = 'input' + str(i) + '.csv'
    df.to_csv(out_csv,
          index=False,
          header=colnames,
          mode='a',#append data to csv file
          chunksize=rowsize)#size of data to append for each loop

