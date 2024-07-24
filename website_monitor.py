import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# List of websites to monitor
websites = [
    'https://epicxplode.com',
    'https://google.com',
   'https://example.com'
]

# Email configuration
smtp_server = 'smtp.your-email-provider.com'
smtp_port = 587
email_user = 'your-email@example.com'
email_password = 'your-email-password'
email_to = 'alert-recipient@example.com'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_to, msg.as_string())
        server.close()
    except Exception as e:
        print(f"Failed to send email: {e}")

def log_result(website, status):
    with open('website_monitor_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: {website} - {status}\n")

def check_websites():
    for website in websites:
        try:
            response = requests.get(website, timeout=10)
            if response.status_code == 200:
                status = 'UP'
            else:
                status = f'DOWN (Status Code: {response.status_code})'
                send_email(f"Website Down Alert: {website}", f"The website {website} is down with status code {response.status_code}.")
        except requests.exceptions.RequestException as e:
            status = f'DOWN (Error: {e})'
            send_email(f"Website Down Alert: {website}", f"The website {website} is down with error: {e}.")
        
        log_result(website, status)
        print(f"{website} - {status}")

if __name__ == "__main__":
    check_websites()
