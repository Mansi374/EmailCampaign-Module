from main import create_app
from main.utils.db_utils import get_next_user, mark_email_sent  


app = create_app()

with app.app_context():
    user = get_next_user()
    if user:
        print(f"Next user: {user}")
        mark_email_sent(user['id'])
        print(f"Marked as sent for ID: {user['id']}")
    else:
        print("All emails have been sent already.")
