def handle_input(prompt):
    # This function keeps prompting the user until they provide valid input: 'yes', 'bye', or 'no'
    while True:
        try:
            # Get user input, remove any leading/trailing whitespace, and convert to lowercase
            value = input(prompt).strip().lower()
            #     raise ValueError

            # If input is valid, return it
            return value
        except ValueError:
            # Inform the user of invalid input and prompt again
            print("Invalid input, please try again.")


print("Welcome to sebha by Omar AlOthaman.")
count = 0  # Initialize the count variable

# Main loop to keep counting until the count reaches 33 or the user decides to quit
while count < 33:
    # Ask the user if they want to start the program
    start = handle_input("Press Enter to start the program: ")

    # if start == "yes":
    # Inner loop to handle the counting
    while count < 33:
        count += 1  # Increment the count
        print(count)  # Print the current count

        # Ask the user if they want to continue or quit
        continue_prompt = input(
            "bye to end: ").strip().lower(
            )

        # If the user types 'bye', exit the inner loop
        if continue_prompt == 'bye':
            print("See you next time.")
            break

    # If the user types 'bye', exit the outer loop as well
    if continue_prompt == 'bye':
        break

    # If the count reaches 33, ask if the user wants to restart or quit
    if count == 33:
        restart = handle_input(
            "You have finished. Do you wish to try again? Type 'yes' to restart or 'no' or any other key to quit: "
        )
        if restart == "yes":
            count = 0  # Reset the count
            continue  # Restart the outer loop
        else:
            print("Goodbye!")
            break  # Exit the outer loop if the user types 'no'
else:
    # If something goes wrong, inform the user
    print("Something went wrong, please try again.")
