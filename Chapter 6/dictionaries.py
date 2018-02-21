alien_0 = {'color': 'green','points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x-position': 0, 'y-postion': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x-position']))
#Move alien to the right
#Determine how far to move based on speed
if alien_0['speed'] =='slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x-position'] = alien_0['x-position'] + x_increment
print("New x-position: " + str(alien_0['x-position']))

fav_lang = {'jeff': 'python', 'jen': 'c++'}
print("Jeff's favorite programming language is " + fav_lang['jeff'].title())

person_details = {'first_name': 'frank', 'last_name': 'supancic', 'city': "kansas city", 'age': '31'}
print(person_details['first_name'].title())