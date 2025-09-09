import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("times up")
try:
    seconds = int(input("Enter the time in seconds for the countdown: "))
    countdown(seconds)
except ValueError:
    print("invlid input, Please enter a number.")
