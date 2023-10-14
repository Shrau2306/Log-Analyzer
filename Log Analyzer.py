import random
import time

# Step 1: Simulate Log Generation
def generate_log():
    pages = ['homepage', 'about', 'contact']
    user_id = random.randint(1, 100)
    page_visited = random.choice(pages)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp}, user_{user_id}, {page_visited}\n"
    return log_line

# Step 2: Store Logs in a file
def write_logs(num=1000):
    with open('logs.txt', 'w') as f:
        for _ in range(num):
            log_line = generate_log()
            f.write(log_line)
            time.sleep(0.01)  # simulating time delay between requests
    print(f"Generated {num} logs in logs.txt")

# Step 3: Analysis
def analyze_logs():
    with open('logs.txt', 'r') as f:
        logs = f.readlines()
    
    homepage_visits = sum(1 for log in logs if 'homepage' in log)
    about_visits = sum(1 for log in logs if 'about' in log)
    contact_visits = sum(1 for log in logs if 'contact' in log)

    print(f"Homepage was visited {homepage_visits} times.")
    print(f"About page was visited {about_visits} times.")
    print(f"Contact page was visited {contact_visits} times.")

    most_visited = max(homepage_visits, about_visits, contact_visits)

    if most_visited == homepage_visits:
        print("Homepage is the most visited page.")
    elif most_visited == about_visits:
        print("About page is the most visited page.")
    else:
        print("Contact page is the most visited page.")

# Execution
write_logs(1000)
analyze_logs()