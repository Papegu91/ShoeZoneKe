from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
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
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
 
    if not username or not email or not password:
        return jsonify({'message': 'Missing username, email, or password'}), 400
 
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
 
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400
 
    hashed_password = generate_password_hash(password)
 
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
 
    return jsonify({'message': 'User registered successfully'}), 201
 
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
 
    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400
 
    user = User.query.filter_by(username=username).first()
 
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid username or password'}), 401
 
    # Here you can implement JWT token creation and return it in the response
    # For simplicity, let's just return a success message for now
    return jsonify({'message': 'Login successful'}), 200
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
