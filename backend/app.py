from flask import Flask
from models import db, User, Shoe, Order, OrderItem, Review, Category
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Welcome to the Shoe Store!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
