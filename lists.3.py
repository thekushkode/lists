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
