from flask import Flask
from main import create_app

app = create_app()
print(app.config['EMAIL_USER']) 


if __name__ == "__main__":
    app.run(debug=True)
