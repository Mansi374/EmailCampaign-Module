from main.extensions import db
from main.models import User
import logging

def get_next_user():
    try:
        user = User.query.filter_by(email_sent=False).first()
        if user:
            logging.info(f"Next user to email: {user.email_id}")
            return {'id': user.id, 'email_id': user.email_id, 'domain': user.domain}
        else:
            logging.info("All emails sent!")
            return None
    except Exception as e:
        logging.error(f"Error fetching user: {e}")
        return None


def mark_email_sent(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            user.email_sent = True
            db.session.commit()
            logging.info(f"Marked email_sent=True for user: {user.email_id}")
            return True
        else:
            logging.warning(f"No user found with ID: {user_id}")
            return False
    except Exception as e:
        logging.error(f"Failed to update email_sent for user_id={user_id}: {e}")
        return False
