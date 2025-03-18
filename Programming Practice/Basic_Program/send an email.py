import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "gakadhane@gmail.com"
password = "Garun0d@ysakal"

# List of recipients
recipients = ["gkadhane@gmail.com"]

# Email subject and body
subject = "Important Update"
body = "Hello,\n\nThis is a test email sent using Python.\n\nBest regards,\nYour Name"

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Login to your email account

        # Send email to each recipient
        for recipient in recipients:
            message["To"] = recipient
            server.sendmail(sender_email, recipient, message.as_string())
            print(f"Email sent to {recipient}")
except Exception as e:
    print(f"An error occurred: {e}")
