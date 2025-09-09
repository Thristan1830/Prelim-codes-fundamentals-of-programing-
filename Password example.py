password = "secret"

for attempt in range(5):
    guess = input("Enter password")
    if guess == password:
        print("Access granted!")
        break
    else:
        print("wrong password")

else:
    print("too many Wrong tries bro stop")