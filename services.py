from utils import say_hello
from rules import is_workday


def run_service():
    print("Service is running...")

    if is_workday():
        print("Today is a workday.")
        say_hello()
    else:
        print("Today is not a workday.")