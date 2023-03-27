# Ask a user their name and age and tell them some things about themself

user_name = input("What is your name? ")
user_age = input("How old are you? ")
user_age_int = int(user_age)

print("Hello there " + user_name)

user_age_x10 = user_age_int * 10
print("Your age times ten is " + str(user_age_x10))

if (user_age_x10 >= 180):
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")