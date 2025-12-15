from rules.calendar import is_workday
from utils.logger import say_hello
from config.settings import APP_NAME, ENV, ENABLE_HELLO


def run_service():
    print(f"{APP_NAME} is running in {ENV} mode.")

    if is_workday():
        print("Today is a workday.")

        if ENABLE_HELLO:
            say_hello()
    else:
        print("Today is not a workday.")