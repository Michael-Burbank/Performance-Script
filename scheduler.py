# Import libraries
import schedule
import time
import http_health_check


def schedule_health_checks():
    # Schedule the function to run every 60 min
    schedule.every(60).minutes.do(http_health_check.check_http_health)
    
    while True:
        schedule.run_pending()
        time.sleep(1)



