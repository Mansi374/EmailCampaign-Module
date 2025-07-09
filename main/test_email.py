from main.utils.email_utils import create_email_message, send_email

# Test recipient
user_email = ""  # Replace with your email for testing
domain = user_email.split('@')[-1]

# Generate and send the message
msg = create_email_message(user_email, domain)
if msg:
    send_email(msg)
else:
    print("❌ Failed to create message.")