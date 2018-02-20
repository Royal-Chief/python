players = ['charles','martinez','michael','florence','eli']
print(players[0:3])
print(players[:4])
print(players[2:])
#get first 3 items in list
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

#copying a list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('canoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)