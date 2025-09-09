import time
Password = "python123"

while True:
    userinput = input("Enter Your Password: ")

    
    if userinput == Password :
        print("Acess Granted")  
        break
    else:
        print("Wrong Password, Please Try Again")
        time.sleep(3) 
    