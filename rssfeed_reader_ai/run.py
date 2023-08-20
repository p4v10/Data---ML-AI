from app import app
from db import db

# this will ensure that all the tables that we create are actually going to be created in the MySQL database
with app.app_context():
    db.create_all()

# run the app
app.run()