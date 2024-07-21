
import time 
print ("Welcome to the count down timer.")
def get_countdown_seconds():
    while True:
        try:
            time_input = input("Enter the countdown time (minutes:seconds) = ")
            minutes, seconds = map(int,time_input.split(":"))
            total_seconds = minutes * 60 + seconds 
            return total_seconds  # Return the valid input
        except ValueError:
            print("Wrong input, please enter a valid integer in should be a number.")

   

def countdown(seconds):
    while seconds > 0:
        minutes , sec = divmod(seconds,60)
        time_str = f"{minutes:02}:{sec:02}"
        print (time_str)
        time.sleep(1)  # Wait for one second
        seconds -= 1
    print("Time is up!!")
    
count_amount = get_countdown_seconds()
countdown(count_amount)
