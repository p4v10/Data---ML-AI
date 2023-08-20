from flask import Flask

# setup flask app
app = Flask(__name__)

# configure with database
db_uri = 'mysql+pymysql://root:password@localhost/rss_articles'
app.config['SQLALCHEMY_DATABASE_URI'] db_uri
