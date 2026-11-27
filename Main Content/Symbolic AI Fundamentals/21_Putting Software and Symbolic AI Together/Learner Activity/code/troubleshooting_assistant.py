# Starter code for the Python Troubleshooting Assistant (3.6).
# Each if/elif line is a rule; each print line shows a result.

computer_on = input("Does your computer turn on? (yes/no): ").strip().lower()

if computer_on == "no":
    print("Suggestion: check the power connection.")
elif computer_on == "yes":
    internet = input("Is your internet working? (yes/no): ").strip().lower()

    if internet == "no":
        print("Suggestion: check the network connection.")
    elif internet == "yes":
        print("The computer turns on and the internet is working.")
    else:
        print("Please enter yes or no for the internet question.")
else:
    print("Please enter yes or no for the first question.")
