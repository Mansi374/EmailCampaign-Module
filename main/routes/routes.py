

from flask import Blueprint
from main.utils.email_utils import create_email_message, send_email
from main.utils.db_utils import get_next_user

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return "Hello from the email campaign!"

@main_bp.route('/send-email')
def send_email_route():
    user = get_next_user()
    if not user:
        return "No users found."

    msg = create_email_message(user['email_id'], user['domain'])
    if not msg:
        return "Email creation failed (template missing)."

    success = send_email(msg)
    return "✅ Email sent." if success else "❌ Email failed."