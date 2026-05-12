import datetime

try:
    choice = input("1. Show today's weekday\n2. Enter a date\nChoose option (1/2): ")

    if choice == '1':
        today = datetime.date.today()
        print("Today's date: ", today)
        print("Weekday: ", today.strftime("%A"))

    elif choice == '2':
        date_input = input("Enter date (YYYY-MM-DD): ")
        date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        print("Weekday: ", date_obj.strftime("%A"))

    else:
        print("Invalid choice!")

except ValueError:
    print("Error: Invalid date format. Please use YYYY-MM-DD.")

finally:
    print("Attendance app finished")
  
