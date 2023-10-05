import time
import random

def generate_math_problem():
    """Generate a simple addition problem."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    solution = num1 + num2
    problem = f"What is {num1} + {num2} ?"
    return problem, solution

def alarm_clock():
    """An alarm clock that requires solving a math problem to switch off."""
    print("Welcome to the Alarm Clock!")
    
    # Set the alarm time
    alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
    alarm_minute = int(input("Enter the minute for the alarm (0-59): "))
    
    # Generate a math problem
    problem, solution = generate_math_problem()
    
    print(f"\nMath problem to switch off the alarm: {problem}\n")
    
    while True:
        # Get the current time
        current_time = time.localtime()
        
        # Check if it's time for the alarm
        if (
            current_time.tm_hour == alarm_hour and
            current_time.tm_min == alarm_minute and
            current_time.tm_sec == 0
        ):
            print("\n*** Alarm! ***")
            user_solution = int(input("Solve the math problem to switch off the alarm: "))
            
            # Check if the solution is correct
            if user_solution == solution:
                print("Correct! Alarm switched off.")
                break
            else:
                print("Incorrect. Try again.")
                # Generate a new math problem
                problem, solution = generate_math_problem()
                print(f"\nNew math problem: {problem}\n")
        
        # Wait for 1 second before checking the time again
        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()
