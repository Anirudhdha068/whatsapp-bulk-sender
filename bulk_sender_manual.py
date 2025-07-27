import pywhatkit
import time

numbers = [
    "+911234567890",
    # Add Numbers as needed
]

message = "YOURE MASSAGE......."

for num in numbers:
    pywhatkit.sendwhatmsg_instantly(num, message, wait_time=10, tab_close=True)
    time.sleep(10)  # Wait between messages

