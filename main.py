# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:43 PM", "14:20", "tueSday"))


# Run unit tests automatically
main(module='test_module', exit=False)