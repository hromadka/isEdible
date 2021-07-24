MIN_LENGTH = 4

fout = open('lookup-pg.csv', 'w', errors='ignore')

input_file = open('lookup.csv', encoding='utf-8', errors='ignore')
data = input_file.readlines() 
input_file.close()

for phrase in data:  # iterate on each element of the list
    fout.write(phrase)
    # element is a list
    word = phrase.rstrip('\n').split(' ')
    for w in word:
        if len(w) > MIN_LENGTH:
            fout.write(w + '\n')
      

fout.close()