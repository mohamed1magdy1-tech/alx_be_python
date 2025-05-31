task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base_msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_msg = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_msg = f"Reminder: '{task}' is a low priority task"
    case _:
        print("Sorry, priority level not recognized.")
        exit()

if time_bound == "yes":
    print(base_msg + " that requires immediate attention today!")
elif time_bound == "no":
    print(base_msg + ". Consider completing it when you have free time.")
else:
    print("Sorry, the time-bound input is invalid. Please enter yes or no.")

