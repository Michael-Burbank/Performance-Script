# main.py
# MVC pattern: Model-View-Controller
# Main python controller for the project

# Imported modules
import http_health_check
import scheduler



def main():
        http_health_check.check_http_health()
        scheduler.schedule_health_check()


if __name__ == "__main__":
    main()
