import logging
import os

# Ensure log directory exists
os.makedirs("logs", exist_ok=True)

# Set up logger
email_logger = logging.getLogger("email_logger")
email_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/email.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

if not email_logger.hasHandlers():
    email_logger.addHandler(file_handler)
