




groceries = ['goats', 'gator', 'shrimp', 'pork rinds']

main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''

delete_menu = '''

1. Print Items
2. Delete An Item
3. Delete Mulitple Items
4. Exit

'''

edit_menu = '''

1. Print Items
2. Edit Items (1 or More!)
3. Exit

'''

add_menu = '''
1. Print Items
2. Add Items
3. Exit

'''

print_menu = '''

1. Print List
2. Print One Index
3. Exit

'''
#THIS CODE WORKS FOR MEDIUM EXERCISES!
while True:
    menu_choice = int(input(main_menu))
    if menu_choice == '':
        break
    elif menu_choice == 1:
        print_choices = int(input(print_menu))
        if print_choices == 1:
            print(groceries)
            print_choices = int(input(print_menu))
        if print_choices == 2:
            index_to_print = int(input('What index do you want to print? '))
            print(groceries[index_to_print])
            print_choices = int(input(print_menu))
        if print_choices == 3:
            menu_choice = int(input(main_menu))
    if menu_choice == 2:
        add_choices = int(input(add_menu))
        if add_choices == 1:
            print(groceries)
            add_choices = int(input(add_menu))
        if add_choices == 2:
            added_items_list = []
            added_items = input('Enter what you want to add: ')   
            added_items_list.append(added_items)
            groceries += added_items_list
            add_choices = int(input(add_menu))
        if add_choices == 3:
            menu_choice = int(input(main_menu))
    new_items_list = []
    if menu_choice == 3:
        edit_choices = int(input(edit_menu))
        if edit_choices == 1:
            print(groceries)
            edit_choices = int(input(edit_menu))
        if edit_choices == 2:
            num1 = int(input('Enter the index number to start at: '))
            num2 = int(input('Enter the index number to end at: '))
            new_items = input('What items are you replacing with? ')
            new_items_list.append(new_items)
            groceries[num1 : num2] = new_items_list
            edit_choices = int(input(edit_menu))
        if edit_choices == 3:
            menu_choice = int(input(main_menu))
    if menu_choice == 4:
        delete_choices = int(input(delete_menu))
        if delete_choices == 1:
            print(groceries)
            delete_choices = int(input(delete_menu))
        if delete_choices == 2:
            item_to_remove = int(input('What index would you like to delete? '))
            del groceries[item_to_remove]
            delete_choices = int(input(delete_menu))
        if delete_choices == 3:
            start_index = int(input('What index do you want to start at? '))
            end_index = int(input('What index do you want to end at? '))
            del groceries[start_index : end_index]
            delete_choices = int(input(delete_menu))
        if delete_choices == 4:
            menu_choice = int(input(main_menu))
    if menu_choice == 5:
        break
print('Thank you for using the grocery list app!')

#THIS CODE WORKS FOR SMALL EXERCISES
# while True:
#     menu_choice = int(input(main_menu))
#     if menu_choice == '':
#         break
#     elif menu_choice == 1:
#         print(groceries)
#     #added_items_list =[]
#     if menu_choice == 2:
#         added_items_list = []
#         added_items = input('Enter what you want to add: ')   
#         added_items_list.append(added_items)
#         groceries += added_items_list
#         #print(groceries) <- works just dont need
#     new_items_list = []
#     if menu_choice == 3:
#         num1 = int(input('Enter the index number to start at: '))
#         num2 = int(input('Enter the index number to end at: '))
#         new_items = input('What items are you replacing with? ')
#         new_items_list.append(new_items)
#         groceries[num1 : num2] = new_items_list
#     remove_items_list = []
#     if menu_choice == 4:
#         item_to_remove = int(input('What index would you like to delete? '))
#         del groceries[item_to_remove]
#     if menu_choice == 5:
#         break
# print('Thank you for using the grocery list app!')