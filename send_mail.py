import subprocess
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



result = subprocess.run(['./check_servers.sh'], capture_output=True, text=True, shell=True)
sender_email = "fec.report.card@gmail.com"
# receiver_email = "tech3@fecdirect.net"
# receiver_email = "palashp@fecdirect.net"
# receiver_email = "offersi@inboxopsteam.com"
receiver_email = ["rahulkum@fecdirect.net"]
# receiver_email_cc = "tech3@fecdirect.net"
password = "rqoeirngqumuwsdt"
message = MIMEMultipart("alternative")
message["Subject"] = f"status "
message["From"] = f"Server Status Report <fec.report.card@gmail.com>"
text = """\ Report """
# Turn these into plain/html MIMEText objects

text = result.stdout
part1 = MIMEText(text, "plain")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
# Create secure connection with server and send email
context1 = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context1) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Mail sent")
