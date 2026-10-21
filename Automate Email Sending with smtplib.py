import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login (use app password for Gmail)
server.login("your_email@gmail.com", "your_app_password")

message = "Hello Sneha, this is a test email from Python!"
server.sendmail("your_email@gmail.com", "receiver_email@gmail.com", message)

server.quit()
print("Email sent successfully!")


# For Gmail,  need to enable App Passwords instead of your main password.
