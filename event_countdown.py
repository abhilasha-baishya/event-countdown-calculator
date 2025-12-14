from datetime import datetime
import time

def countdown(event_name, event_datetime):
    while True:
        now = datetime.now()
        remaining_time = event_datetime - now

        if remaining_time.total_seconds() <= 0:
            print(f"\n🎉 The event '{event_name}' has arrived!")
            break

        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(
            f"\rTime left for '{event_name}': "
            f"{days} days {hours} hours {minutes} minutes {seconds} seconds",
            end=""
        )

        time.sleep(1)

def main():
    print("Countdown to Any Future Event Calculator\n")

    event_name = input("Enter event name: ")

    date_input = input("Enter event date and time (YYYY-MM-DD HH:MM:SS): ")

    try:
        event_datetime = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")

        if event_datetime <= datetime.now():
            print("Please enter a future date and time.")
        else:
            countdown(event_name, event_datetime)

    except ValueError:
        print("Invalid date format. Please follow YYYY-MM-DD HH:MM:SS")

if __name__ == "__main__":
    main()
