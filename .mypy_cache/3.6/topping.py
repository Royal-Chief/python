toppings = ['pepperoni','sausage','peppers']
for topping in toppings:
    if topping == 'peppers':
        print("Sorry, we are out of peppers.")
    else:
        print("Adding " + topping + ".")

print("Finished making your pizza")


available_toppings = ['pepperoni','sausage','peppers','mushrooms','olives']

requested_toppings = ['pepperoni','pineapple']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we dont have " + requested_topping + ".")

print("\nFinished you pizza")