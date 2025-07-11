from flask import Blueprint, current_app, render_template, flash, redirect, url_for
import smtplib
from email.message import EmailMessage
from main.utils.db_utils import get_next_user, mark_email_sent

email_bp = Blueprint("email_bp", __name__)

@email_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")  


@email_bp.route("/send-email", methods=["POST"])
def send_email():
    user = get_next_user()
    if not user:
        flash("⚠️ No users left to send email!", "error")
        return redirect(url_for("email_bp.index"))

    try:
        msg = EmailMessage()
        msg['Subject'] = f'Hello {user["email_id"]}!'
        msg['From'] = current_app.config['EMAIL_USER']
        msg['To'] = user["email_id"]
        msg.set_content(f"Hi there!\n\nThis is an automated email for {user['domain']} domain.")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(
                current_app.config['EMAIL_USER'],
                current_app.config['EMAIL_PASS']
            )
            smtp.send_message(msg)

        mark_email_sent(user['id'])  # Mark email_sent = 1
        flash(f"✅ Email sent to {user['email_id']} and marked as sent!", "success")

    except Exception as e:
        flash(f"❌ Failed to send email to {user['email_id']}: {str(e)}", "error")

    return redirect(url_for("email_bp.index"))