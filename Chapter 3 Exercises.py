#I made a list of elements, and then used append to add new values to it over time
mushroom_kingdom = ["Mario", "Luigi", "Toad"] 
mushroom_kingdom.append('Peach')
mushroom_kingdom.append('Daisy')
mushroom_kingdom.append('Yoshi')

#I then created another list of values I inteded to remove from the list but would still like to interact with later
animals = ['Toad', 'Yoshi'] 

#I couldn't quite figure out why the remove method wouldn't remove "Toad" and "Yoshi" without me specifying their position
#But my guess is that they would have to appear in the mushroom_kingdom list in the same sequence as they appear in the "Animals"
#List in orde to be removed that way, but anyways I just specified their position to make the rest work
mushroom_kingdom.remove(animals[0])
mushroom_kingdom.remove(animals[1]) 
print(mushroom_kingdom)
print(f"I don't like animals so I removed {animals[0]} and {animals[1]} from the list, oops")