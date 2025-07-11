from main import create_app
from main.extensions import db
from main.models import User  

app = create_app()

with app.app_context():
    users = [
        User(email_id="neha@example.com", domain="tech"),
        User(email_id="palvi@example.com", domain="business"),
        User(email_id="team@example.com", domain="marketing"),
        User(email_id="testuser@example.com", domain="testing"),
    ]
    db.session.add_all(users)
    db.session.commit()
    
    # output we get when we run python insert_dummy_users.py
    print("✅ Dummy users inserted.")
