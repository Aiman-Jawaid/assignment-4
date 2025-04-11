import time

def countdown_timer():
    
    try:
        countdown_time = int(input("Enter the countdown time in seconds: "))
        
        if countdown_time <= 0:
            print("Please enter a number greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    
    while countdown_time > 0:
        minutes, seconds = divmod(countdown_time, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        print(time_str, end='\r')  
        time.sleep(1)  
        countdown_time -= 1

    print("Time's up! ⏰")


countdown_timer()
