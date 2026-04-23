import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(workflow_name, repo_name ,workflow_run_id):
    # Email configuration
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    # Email message
    subject = f"GitHub Workflow Failure: {workflow_name}"
    body = f"The GitHub workflow '{workflow_name}' in the repository '{repo_name}' has failed. Please check the GitHub Actions logs for more details.\nMore info: {workflow_run_id}"

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    try: 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred while sending email: {e}")
    finally:
        server.quit()

send_email(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))