import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time

# Email configuration
email_user = 'your_email@example.com'
email_password = 'your_email_password'
email_subject = 'Happy Birthday!'

# SMTP server configuration for Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Load the birthday data
birthday_data = pd.read_csv('birthdays.csv')

def send_birthday_email(name, email):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = email_subject

    body = f"Dear {name},\n\nWishing you a very Happy Birthday! Have a wonderful day filled with love and joy.\n\nBest regards,\n[Your Name]"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, email, text)
        server.quit()
        print(f"Email sent to {name} at {email}")
    except Exception as e:
        print(f"Failed to send email to {name} at {email}: {e}")

def check_and_send_birthday_emails():
    today = datetime.now().strftime('%m-%d')
    for index, row in birthday_data.iterrows():
        birthdate = datetime.strptime(row['Birthdate'], '%Y-%m-%d').strftime('%m-%d')
        if birthdate == today:
            send_birthday_email(row['Name'], row['Email'])

if __name__ == "__main__":
    while True:
        now = datetime.now()
        if now.hour == 8 and now.minute == 0:
            check_and_send_birthday_emails()
            time.sleep(60)  # Wait for a minute to avoid duplicate emails
        time.sleep(30)  # Check every 30 seconds
