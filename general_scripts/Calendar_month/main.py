import calendar

def display_calendar():

    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)

    # Check if the month is valid
    if month < 1 or month > 12:
        print("Invalid month. Please enter a month between 1 and 12.")
        return

    # Format the month and year
    formatted_month = cal.formatmonth(year, month)

    # Print the formatted month
    print(formatted_month)

# Display the calendar for a specific month and year
if __name__ == "__main__":
    # Example usage
    display_calendar()