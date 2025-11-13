task = input("Enter your task: ")
priority = input("Priority (high/medium/low): " ).lower
time_bound = input("Is it time-bound?(yes/no) ").lower
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"{task} is a high priority task that requires immediate attention today"
        else:
            reminder = "High priority task,not time-bound"
    case "medium":
        if time_bound == "yes":
            reminder = f"{task} is a medium priority task that requires immediate attention today"
        else:
            reminder = f"{task} is a medium priority task,consider completing today"
    case "low":
        if time_bound == "yes":
            reminder = f"{task} is a low priority task that requires immediate attention today"
        else:
            reminder = f"{task} is a low priority task"
    case _:
        if time_bound == "yes":
            reminder = f"{task} is an unknown priority task that requires immediate attention today"
        else:
            reminder = f"{task} is an unknown priority task"
print(f"Reminder: {reminder}")