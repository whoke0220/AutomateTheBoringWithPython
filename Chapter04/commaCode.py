#This program takes a list and adds commas between each value with "and"
#inserted before the last value


def AddComas(items):
    if len(items) == 0:
        print('Item list is empty.')
    else:
        for i in range(len(items)):
            if i == len(items) - 1:
                print('and ' + items[i])
            else:
                print(items[i] + ', ', end='')


listItems = []
AddComas(listItems)
