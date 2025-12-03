# Imported modules
import http_health_check
import scheduler


def main():
    http_health_check.check_http_health()
    scheduler.schedule_health_checks()

    
if __name__ == "__main__":
    main()
