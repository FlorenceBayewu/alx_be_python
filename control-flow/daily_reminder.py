Task = input("Input a task description: ")
Priority = input("What's the task priority?(high,medium,low) " )
Time_bound = input("Is task time-bound? ")
match Priority:
    case "high":
        if Time_bound == "yes":
            reminder = f"{Task} is a high priority task that requires immediate attention"
        else:
            reminder = f"{Task} is a high priority task"
    case "medium":
        if Time_bound == "yes":
            reminder = f"{Task} is a medium priority task that requires immediate attention"
        else:
            reminder = f"{Task} is a medium priority task"
    case "low":
        if Time_bound == "yes":
            reminder = f"{Task} is a low priority task that requires immediate attention"
        else:
            reminder = f"{Task} is a low priority task"
print(f"Reminder: {reminder}")