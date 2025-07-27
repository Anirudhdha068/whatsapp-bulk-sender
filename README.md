# 📲 WhatsApp Bulk Message Sender Using CSV & Python

This project allows you to send **WhatsApp messages in bulk** using either a `.csv` file **or manual input**—without saving contacts, making a group, or using a broadcast list.

✅ Simple UI  
✅ No contacts needed  
✅ CSV & manual mode  
✅ Uses WhatsApp Web  
✅ 100% free and open-source  

---

## 🚨 Disclaimer

> ⚠️ This tool is for **educational and personal use only**.  
> **Do NOT use for spam or unsolicited marketing**—doing so may violate WhatsApp's terms and result in a ban.

---

## 🔧 Features

- 📁 CSV and manual number support
- ✍️ Personalized or static messages
- 🧑‍💻 No contact saving needed
- 🌐 Sends via WhatsApp Web
- 🕒 Adjustable delay for safe operation
- 🪟 Works on Windows, Mac, and Linux

---

## 📁 CSV File Format (For `bulk_sender_csv.py`)

Use a `contacts.csv` file like this:

```csv
Name,Number
Ravi,+919876543210
Sneha,+911234567890
Amit,+919898989898

````

✅ Make sure the column is named exactly `Number`<br>
✅ Include international code like `+91` for India

---

## 🛠️ Requirements

* Python 3.7 or higher
* Google Chrome (set as your default browser)
* Logged into WhatsApp Web in browser

---

## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/whatsapp-bulk-sender.git
cd whatsapp-bulk-sender
```

2. Install required Python packages:

```bash
pip install pywhatkit pandas
```

---

## 🚀 How to Run

### ✅ Method 1: Using CSV File

This will send a fixed message to all numbers listed in `contacts.csv`.

🔗 [Click here to view code → `bulk_sender_csv.py`](./bulk_sender_csv.py)

```bash
python bulk_sender_csv.py
```

---

### ✅ Method 2: Without CSV (Manual Entry)

This version allows you to **manually enter phone numbers** without needing a CSV file.

🔗 [Click here to view code → `bulk_sender_manual.py`](./bulk_sender_manual.py)

```bash
python bulk_sender_manual.py
```

---

## 🧠 Customization Tips

* Change the message content inside the script easily.
* Add personalization using a `Name` column in CSV.
* Increase `time.sleep()` if messages are being blocked.
* Use `sendwhats_image()` to send images or documents.

---

## ❓ FAQ

**Q: Does it save contacts to phone?**<br>
A: No. It sends directly without saving anything.

**Q: Can I send attachments?**<br>
A: Yes. `pywhatkit` supports sending images with `sendwhats_image()`.

**Q: Does the tab auto-close after sending?**<br>
A: Yes, if `tab_close=True` is set.

---

## 👨‍💻 Developed by

**Anirudhdha Poriya**<br>
📧 [anirudhdha068@gmail.com](mailto:anirudhdha068@gmail.com)

---

⭐ If you find this helpful, please give a **GitHub star** to support the project!


