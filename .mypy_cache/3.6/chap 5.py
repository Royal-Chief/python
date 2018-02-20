age = int(input("Enter your age: "))
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission price is $" + str(price))

alien_color = "blue"
if alien_color == 'green':
    print("Awarded 5 points.")
elif alien_color == "red":
    print("Awarded 15 points")
elif alien_color == "yellow":
    print("Awarded 10 points")
else:
    print("You missed")
