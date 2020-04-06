#List exercise 1
#Prompt user for single item and append it to list

#do same thing in loop

groc = ['milk', 'bread', 'beer']

# need = input('Enter one grocery item: ')
# groc.append(need)
# print(groc)
# print(groc[1])

# WHILE LOOP VERSION

while True:
    needs = input('Enter one grocery item you need: ')
    groc.append(needs)
    print(groc)

#print(len(groc)) <---- PRINTS NUMBER OF ITEMS IN LIST/ LIST LENGTH