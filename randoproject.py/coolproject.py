import time

# Ask user for duration in minutes
minutes = int(input("Enter countdown time in minutes: "))
seconds = minutes * 60

# Countdown loop
while seconds > 0:
    mins, secs = divmod(seconds, 60)
    timer_display = f"{mins:02d}:{secs:02d}"
    print(timer_display, end="\r")
    time.sleep(1)
    seconds -= 1

print("⏰ Time's up! Take a break or switch tasks.")