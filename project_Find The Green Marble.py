# Week 4,

# Project Find the green Marble

# Import random

import random

# This is Juan's collection
collection = ['red','pink','orange','red','pink','yellow']

# This is the secret Bag collection
secret_bag = ['pink','blue','green','orange','red','purple','green','blue','green','purple','yellow','red','pink','red','green','yellow']

# Keeping track of the marbles chosen

marbles_chosen =[]

# To keep track of how many tries juan has left

tries_remaining = 5

# create a loop to iterate

for x in range(6):
    if tries_remaining > 0:
        selection = random.choice(secret_bag)
        marbles_chosen.append(selection)
        tries_remaining -= 1
        if selection == 'green':
            collection.append(selection)
            secret_bag.remove(selection)
            if ('green' in collection):
                print (f'Awesome! You found a green marble. if you would like another marble, you have {tries_remaining} pick (s) left.')
                break
    else:
         print('Sorry, you out of tries. Please come back tomorrow and try again!')
print(f'Here are all the marbles that you choose: {marbles_chosen}')

