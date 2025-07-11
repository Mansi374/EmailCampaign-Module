from main import create_app
from main.extensions import db
from main.models import User

app = create_app()

with app.app_context():
    users = User.query.all()
    for u in users:
        print(f"{u.id} | {u.email_id} | {u.domain} | email_sent: {u.email_sent}")
