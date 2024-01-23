import time
import threading
import sys

def countdown_timer(seconds, stop_event):
    while seconds and not stop_event.is_set():
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        seconds -= 1

    if not stop_event.is_set():
        print("\nTime's up!")

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

    stop_event = threading.Event()

    # Start the countdown in a separate thread
    countdown_thread = threading.Thread(target=countdown_timer, args=(countdown_length, stop_event))
    countdown_thread.start()

    try:
        # Wait for user input to stop the countdown
        print("\nPress 'q' and Enter to stop the countdown:")
        user_input = input()
        if user_input.lower() == 'q':
            stop_event.set()
            countdown_thread.join()  # Wait for the countdown thread to finish

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C) to gracefully stop the countdown
        stop_event.set()
        countdown_thread.join()  # Wait for the countdown thread to finish
        print("\nCountdown stopped.")

if __name__ == "__main__":
    main()
