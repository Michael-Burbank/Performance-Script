import time
import schedule
# import time
import http_health_check

def schedule_health_check():
    try:
        # Schedule the function to run every 60 min
        schedule.every(60).minutes.do(http_health_check.check_http_health)

        print("Scheduler running: Press Ctrl+C to exit.")
    
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Scheduler stopped by user.")