# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 08:43:51 2021

@author: William Hoke
"""


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

def addToInventory(inventory, addedItems):
    #Loop through the list of items to add to the player's inventory
    for item in addedItems:
        #If at least one of the item is already in the player's inventory, add one to the total
        if item in inventory.keys():
            inventory[item] += 1
        #If the item is not in the inventory, add a new listing for it.
        else:
            inventory[item] = 1
    
    #return the inventory item
    return inventory
    
    

playerInventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
playerInventory = addToInventory(playerInventory, dragonLoot)
displayInventory(playerInventory)