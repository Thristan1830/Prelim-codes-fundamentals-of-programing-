import time
import sys
import getpass

# Colors for terminal text (ANSI escape codes)
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def custom_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50,
                        fill='█', print_end='\r'):
    percent = f"{100 * (iteration / float(total)):.{decimals}f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write(print_end + '\n')

# Simulate loading
print(YELLOW + "Initializing secure system..." + RESET)
total_tasks = 50
delay = 0.05

for i in range(total_tasks):
    custom_progress_bar(i + 1, total_tasks, prefix='Loading:', suffix='Complete', length=30)
    time.sleep(delay)

# Password system
password = "secret"
max_attempts = 5

print(YELLOW + "\nSystem Ready. Authentication Required." + RESET)

for attempt in range(max_attempts):
    guess = getpass.getpass(f"Attempt {attempt + 1}/{max_attempts} - Enter password: ")
    
    if guess == password:
        print(GREEN + "✅ Access Granted! Welcome back." + RESET)
        break
    else:
        print(RED + "❌ Wrong password." + RESET)
        time.sleep(0.5)  # small pause for realism
else:
    print(RED + "\n🚫 Access Denied! Too many wrong attempts." + RESET)
    print(YELLOW + "System shutting down..." + RESET)
