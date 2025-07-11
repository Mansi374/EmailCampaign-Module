from main.utils.email_utils import create_email_message, send_email

user_email = ""  
domain = user_email.split('@')[-1]

msg = create_email_message(user_email, domain)
if msg:
    send_email(msg)
else:
    print("❌ Failed to create message.")