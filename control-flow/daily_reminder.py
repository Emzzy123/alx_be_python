task = input("Enter a task description?: ")
priority = input("Enter the task's priority (hight, medium, low): ").lower()
time_bound = input("Is the task time bound (yes or no): ").lower()

match priority:
  case 'high':
    if time_bound == 'yes':
      print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
      print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
  case 'medium':
    if time_bound == 'yes':
      print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
      print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
  case 'low':
    if time_bound == 'yes':
      print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
      print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
