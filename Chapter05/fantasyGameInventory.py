# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:06:49 2021

@author: William
"""
# DisplayInvetory function, takes a dictionary as "'item': count" pairs
def displayInventory(player_inventory):
    print('Inventory:')
    
    #item accumulator
    total_items = 0
    
    #loop through each dictionary entry and display the amount of each item followed by the item
    for item, item_amount in player_inventory.items():
        print(str(item_amount) + ' ' + item)
        total_items += item_amount
    
    #Display the total number of items    
    print('Total number of items: ' + str(total_items) )
    
#test inventory    
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
 
#call the function
displayInventory(inventory)