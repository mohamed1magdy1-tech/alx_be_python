# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = "Priority level not recognized."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"
elif priority in ["high", "medium", "low"]:
    reminder += ". Consider completing it when you have free time."

print(reminder)
