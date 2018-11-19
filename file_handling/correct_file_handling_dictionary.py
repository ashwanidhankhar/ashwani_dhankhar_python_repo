


for row in csv_reader:
    if row[0] not in animal_dictionary.keys():
        animal_dictionary[row[0]] = int(row[2])
    else:
        animal_dictionary[row[0]]=animal_dictionary[row[0]]+int(row[2])

        
for #same to print all in list
