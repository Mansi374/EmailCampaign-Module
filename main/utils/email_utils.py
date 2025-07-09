import os
import random
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
from main.logger import email_logger as logger



load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
def read_templates():
    base_path=os.path.join(os.path.dirname(__file__),'..','email_templates')
    try:
        with open(os.path.join(base_path,'template1.txt'),'r') as f1,\
        open(os.path.join(base_path,'template2.txt'),'r') as f2:
            return f1.read(),f2.read()
    except FileNotFoundError as e:
        print("File is missing {e}")
        return None,None

def choose_template(domain=None):
    template1,template2=read_templates()
    if not template1 or not template2 :
        return None

    if domain:
        if ".edu" in domain:
            return template1
        if ".com" in domain:
            return template2
        else:
            return random.choice([template1,template2])

def personalize_template(template, user_email, domain):
    return template.format(user_email=user_email, domain=domain)

def create_email_message(user_email, domain):
    template = choose_template(domain)
    if not template:
        return None

    body = personalize_template(template, user_email, domain)

    msg = EmailMessage()
    msg['Subject'] = "Special Update from Our Team"
    msg['From'] = EMAIL_USER
    msg['To'] = user_email
    msg.set_content(body)

    html_body = f"""
    <html>
      <body>
        <p>Hello <b>{user_email}</b>,<br>
           Here’s your update from <i>{domain}</i>.<br><br>
           Stay tuned for more!
        </p>
      </body>
    </html>
    """
    msg.add_alternative(html_body, subtype='html')
    print(msg.as_string())

    return msg

def send_email(message: EmailMessage):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(message)
        success_msg = f" Email sent successfully to {message['To']}"
        print(success_msg)
        logger.info(success_msg)
        return True
    except smtplib.SMTPAuthenticationError as e:
        error_msg = f"Authentication failed: {e}"
    except smtplib.SMTPRecipientsRefused as e:
        error_msg = f" Invalid recipient address: {e}"
    except smtplib.SMTPException as e:
        error_msg = f" SMTP error while sending to {message['To']}: {e}"
    except Exception as e:
        error_msg = f" General error while sending to {message['To']}: {e}"

    print(error_msg)
    logger.error(error_msg)
    print("Email sent.")
    return False
