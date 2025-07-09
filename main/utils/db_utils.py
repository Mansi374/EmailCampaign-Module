import os
from dotenv import load_dotenv
load_dotenv()

def get_next_user():
    return {
        'email_id':  os.getenv("TEST_EMAIL"),
        'domain': 'tech'
    }
