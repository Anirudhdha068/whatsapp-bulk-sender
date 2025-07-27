import pywhatkit
import time

numbers = [
    "+911234567890",
    # Add Numbers as needed
]

message = "Hello! This is a bulk message test from Kre8IoT."

for num in numbers:
    pywhatkit.sendwhatmsg_instantly(num, message, wait_time=10, tab_close=True)
    time.sleep(10)  # Wait between messages

