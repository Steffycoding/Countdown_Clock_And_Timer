import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def main():
    print("Welcome to the Countdown Timer App")
    try:
        countdown_length = int(input("Enter the countdown length in seconds: "))
        if countdown_length <= 0:
            print("Please enter a positive countdown length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("\nCountdown started:")
    countdown_timer(countdown_length)

if __name__ == "__main__":
    main()

