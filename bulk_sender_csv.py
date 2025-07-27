import pywhatkit
import pandas as pd
import time

# Load numbers from CSV
data = pd.read_csv("contacts.csv")

# Message to send
message = f"Hello {row['Name']}, this is Kre8IoT reaching out!"

# Loop through numbers
for index, row in data.iterrows():
    phone = row['Number']
    try:
        print(f"Sending to {phone}")
        pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)
        time.sleep(10)  # Delay between messages
    except Exception as e:
        print(f"Failed to send to {phone}: {e}")
