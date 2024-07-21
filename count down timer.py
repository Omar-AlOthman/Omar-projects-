import time 
print ("Welcome to the count down timer.")
def get_countdown_seconds():
    while True:
        try:
            count_amount = int(input("Seconds of countdown = ")) 
            return count_amount  # Return the valid input
        except ValueError:
            print("Wrong input, please enter a valid integer in should be a number.")

   

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)  # Wait for one second
        seconds -= 1
    print("Time is up!!")

count_amount = get_countdown_seconds()
countdown(count_amount)
