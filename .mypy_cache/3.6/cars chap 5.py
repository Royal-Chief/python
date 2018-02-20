cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

topping = ['pepperoni','peppers','mushrooms']
for toppings in topping:
    if topping != 'anchovies':
        print("hold the anchovies and add " + topping)
else:
    print("you ordered anchovies")


user = input("Enter Name: ")
banned_user = ['jeff','frank','matt']
if user.lower() not in banned_user:
    print(user.title() + " you are authorized")
else:
    print(user.title() + " you are not authorized")

age = 19
if age >= 18:
    print("You are old enough")

