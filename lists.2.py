# List Exercise 2
# convert infinite grocery item propt
# only accept 3 items

# groc list var defined
groc = []

#build list
while len(groc) < 3:
    needs = input('Enter one grocery item you need: ')
    groc.append(needs)

#groc2 list var defined
groc2 = []

#build list
while len(groc2) < 3:
    needs2 = input('Enter one grocery item you need: ')
    groc2.append(needs2)

#adds lists and puts them into a new list
groc_fin = groc + groc2

#or groc_fin = groc.extend(groc2)
print(groc_fin)

#ask for index to be replaced
index_to_replace = int(input('Enter the index of the iem you want to replace: '))

#ask for item to add
item_to_add = input('What item would you like to add: ')

#adds item to final list based on user inputs
groc_fin[index_to_replace] = item_to_add

#prints new list
print(groc_fin)

#code w/o comments
# groc = []

# while len(groc) < 3:
#     needs = input('Enter one grocery item you need: ')
#     groc.append(needs)

# groc2 = []

# while len(groc2) < 3:
#     needs2 = input('Enter one grocery item you need: ')
#     groc2.append(needs2)

# groc_fin = groc + groc2
# print(groc_fin)

# index_to_replace = int(input('Enter the index of the iem you want to replace: '))
# item_to_add = input('What item would you like to add: ')
# groc_fin[index_to_replace] = item_to_add

# print(groc_fin)