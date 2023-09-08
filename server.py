from flask_app import app

# import users.py from folder 'flask_app/controllers'
from flask_app.controllers import users 


if __name__ == "__main__":
    app.run(debug=True)

