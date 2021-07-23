import json

fout = open('recipes-de.csv', 'w')

input_file = open('recipes-de.json')
data = json.load(input_file)  # get the data list
for element in data:  # iterate on each element of the list
    # element is a dict
    name = element['Name']  # get the id
    print(name)  # print it
    fout.write(name + '\n')

fout.close()