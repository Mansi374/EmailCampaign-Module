from flask import Blueprint, current_app, render_template, flash, redirect, url_for
import smtplib
from email.message import EmailMessage

email_bp = Blueprint("email", __name__)

@email_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # ✅ render HTML template

@email_bp.route("/send-email", methods=["POST"])
def send_email():
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Test Email from Flask'
        msg['From'] = current_app.config['EMAIL_USER']
        msg['To'] = "jisko bejna uski id daldo" # ✅ your test email
        msg.set_content("Hello from Janvi's Flask app!")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(
                current_app.config['EMAIL_USER'],
                current_app.config['EMAIL_PASS']
            )
            smtp.send_message(msg)

        flash("✅ Email sent successfully!", "success")  # ✅ green success message
    except Exception as e:
        flash(f"❌ Failed to send email: {str(e)}", "error")  # ✅ red error message

    return redirect(url_for("email.index"))  # reload page with message
