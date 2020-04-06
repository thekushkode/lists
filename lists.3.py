#Lists Exercise 3
#Promt unitl string is empty
#Show them the list
#Give them a chance to replace stuff in list
    #prompt for a subset of items to replace
    #if start and end the same, replace 1
    #if different, replace with a list
    #prompt until empty string


groc = []

while len(groc) < 5:
    needs1 = input('Enter one grocery item you need: ')
    if needs1 == '':
        break
    groc.append(needs1)
    print(needs1)

print(groc)

num1 = int(input('Enter start num: '))
num2 = int(input('Enter end num: '))
    
if num1 == num2:
    new_one_item = input("What is new item: ")
    groc[num1] = new_one_item
else:
    new_list = []
    while True:
        new_items = input('What are the items you want to replace them with? ')
        if new_items == '':
            break
        new_list.append(new_items)
    print(new_list)
    groc[num1 : num2] = new_list
print(groc)



# groc[new_range] = new_items
# print(groc)



# start = int(input("Enter a subset start number to begin replacing items: "))
# fin = int(input("Enter a subset end number to begin replacing items: "))
# user_input = [start:fin]
# print user_input

# changes = input("Enter a subset of items to be replaced  ex: [1:3]- ")
# change_array = changes.split(',')
# print(changes)
# print(f'These are the changes you want to make: {change_array}.')






# for i in range(len(change_array)):
#     if change_array[0] == groc[0] and change_array[i] == groc[4]:
#         groc.remove(groc[4])
#     print(groc)


# for i in changes:
#     if changes[i] == groc[0] and changes[i] == groc[4]:
#         groc.remove()





# for i in groc:
#     for x, y in range(len(changes)):
#         if x == y:
#             groc[i] = groc[x]
#         else:
#             new_groc = groc[x:y]
#             print(new_groc)




# groc2 = []

# while len(groc2) < 3:
#     needs2 = input('Enter one grocery item you need: ')
#     if needs2 == '':
#         break
#     groc2.append(needs2)
#     print(needs2)

# groc3 = groc + groc2
# print(groc3)


# index_to_replace = int(input('Enter the index of the item you want to replace: '))
# item_to_add = input('What item would you like to add: ')
# groc_fin[index_to_replace] = item_to_add

# print(groc_fin)