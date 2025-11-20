# Import libraries
import schedule
# import time
import performance_function


def schedule_function():
    # Schedule the function to run every 60 min
    schedule.every(60).minutes.do(performance_function.performance_function)

    # Cancel job after every job comlletes
    return schedule.CancelJob


schedule_function()
