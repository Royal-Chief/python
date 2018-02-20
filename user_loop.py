user_names = ['jeff','john','frank','joe','admin']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello Admin, would you like a status report?")
        else:
            print("Hello " + user_name.title() + " thank you for logging in.")
else:
    print("No user.")
"\n"


current_users = ['jHAwK201','jeffm201','jtmullins12','konabean13','fatboj10']
new_users = ['justynmichelle','Jhawk201','golfer77','summer18','fatboj10']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Username " + new_user + " is already taken. Choose another name")
    else:
        print("Username " + new_user + " is available.")

