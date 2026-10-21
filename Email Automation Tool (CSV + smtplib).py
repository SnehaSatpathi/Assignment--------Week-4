# Email Automation Tool
import smtplib
import pandas as pd

# Load student data from CSV
students = pd.read_csv("students.csv")  # columns: Name, Email

# Setup SMTP
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")

# Send personalized emails
for index, row in students.iterrows():
    name = row["Name"]
    email = row["Email"]
    subject = "Course Update"
    message = f"Subject: {subject}\n\nHello {name},\nThis is a personalized update email."
    server.sendmail("your_email@gmail.com", email, message)
    print(f"Email sent to {name} ({email})")

server.quit()


# For Gmail,  must use App Passwords instead of your main password.
