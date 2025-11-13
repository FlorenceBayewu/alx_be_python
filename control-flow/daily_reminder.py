task = input("Input a task description: ")
task_priority = input("What's the task priority?(high,medium,low) " )
time_bound = input("Is task time-bound? ")
match task_priority:
    case "high":
        if time_bound == "yes":
            reminder = f"{task} is a high priority task that requires immediate attention"
        else:
            reminder = f"{task} is a high priority task"
    case "medium":
        if time_bound == "yes":
            reminder = f"{task} is a medium priority task that requires immediate attention"
        else:
            reminder = f"{task} is a medium priority task"
    case "low":
        if time_bound == "yes":
            reminder = f"{task} is a low priority task that requires immediate attention"
        else:
            reminder = f"{task} is a low priority task"
print(f"Reminder: {reminder}")