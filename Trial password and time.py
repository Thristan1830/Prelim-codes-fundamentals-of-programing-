import time
import sys
import threading

def custom_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50,
                        fill='#', print_end='\r'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write(print_end + '\n')

def countdown(seconds):
    global stop_countdown
    while seconds > 0 and not stop_countdown:
        print(f"Time left: {seconds} seconds", end="\r")
        time.sleep(1)
        seconds -= 1
    if not stop_countdown:
        print("\n⏳ Time's up! You failed to enter the password.")
        sys.exit()  

password = "python123"
stop_countdown = False
time_limit = 20


t = threading.Thread(target=countdown, args=(time_limit,))
t.start()

for attempt in range(5):
    guess = input("Enter password: ")
    if guess == password:
        stop_countdown = True  
        print("\n✅ Access granted!")
        
        
        total_tasks = 50
        for i in range(total_tasks):
            custom_progress_bar(i + 1, total_tasks, prefix='Loading:', suffix='Complete',
                                length=30)
            time.sleep(0.1)
        break
    else:
        print("❌ Wrong password")

else:
    print("\n🚫 Too many wrong tries, bro stop")
