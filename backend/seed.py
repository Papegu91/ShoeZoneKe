from datetime import datetime
from app import app, db
from models import User, Shoe, Order, OrderItem, Review, Category

def seed_data():
    with app.app_context():
        db.drop_all()  # Drop all tables
        db.create_all()  # Create all tables

        # Create Users
        users = [
            User(username='user1', email='user1@example.com', password_hash='password1'),
            User(username='user2', email='user2@example.com', password_hash='password2'),
            User(username='user3', email='user3@example.com', password_hash='password3'),
            User(username='user4', email='user4@example.com', password_hash='password4'),
            User(username='user5', email='user5@example.com', password_hash='password5')
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()

        # Create Shoes
        shoes = [
            Shoe(name='Air Max', brand='Nike', description='Comfortable running shoes', price=120.00, stock=50, image_url='url1'),
            Shoe(name='Superstar', brand='Adidas', description='Classic casual shoes', price=90.00, stock=30, image_url='url2'),
            Shoe(name='Classic Leather', brand='Reebok', description='Timeless style', price=80.00, stock=20, image_url='url3'),
            Shoe(name='Gel-Kayano', brand='ASICS', description='Supportive running shoes', price=140.00, stock=25, image_url='url4'),
            Shoe(name='Blazer', brand='Nike', description='Retro basketball shoes', price=100.00, stock=40, image_url='url5')
        ]
        db.session.bulk_save_objects(shoes)
        db.session.commit()

        # Create Categories
        categories = [
            Category(name='Running'),
            Category(name='Casual'),
            Category(name='Basketball'),
            Category(name='Retro'),
            Category(name='Support')
        ]
        db.session.bulk_save_objects(categories)
        db.session.commit()

        # Associate Shoes with Categories
        shoes[0].categories.append(categories[0])  # Air Max -> Running
        shoes[1].categories.append(categories[1])  # Superstar -> Casual
        shoes[2].categories.append(categories[1])  # Classic Leather -> Casual
        shoes[3].categories.append(categories[0])  # Gel-Kayano -> Running
        shoes[4].categories.append(categories[2])  # Blazer -> Basketball
        db.session.commit()

        # Create Orders
        orders = [
            Order(user_id=1, status='Completed'),
            Order(user_id=2, status='Pending'),
            Order(user_id=3, status='Shipped'),
            Order(user_id=4, status='Cancelled'),
            Order(user_id=5, status='Completed')
        ]
        db.session.bulk_save_objects(orders)
        db.session.commit()

        # Create OrderItems
        order_items = [
            OrderItem(order_id=1, shoe_id=1, quantity=2, price_at_purchase=120.00),
            OrderItem(order_id=2, shoe_id=2, quantity=1, price_at_purchase=90.00),
            OrderItem(order_id=3, shoe_id=3, quantity=3, price_at_purchase=80.00),
            OrderItem(order_id=4, shoe_id=4, quantity=1, price_at_purchase=140.00),
            OrderItem(order_id=5, shoe_id=5, quantity=4, price_at_purchase=100.00)
        ]
        db.session.bulk_save_objects(order_items)
        db.session.commit()

        # Create Reviews
        reviews = [
            Review(user_id=1, shoe_id=1, rating=5, comment='Great shoes!', created_at=datetime.utcnow()),
            Review(user_id=2, shoe_id=2, rating=4, comment='Very comfortable.', created_at=datetime.utcnow()),
            Review(user_id=3, shoe_id=3, rating=3, comment='Okay, not the best.', created_at=datetime.utcnow()),
            Review(user_id=4, shoe_id=4, rating=5, comment='Perfect for running.', created_at=datetime.utcnow()),
            Review(user_id=5, shoe_id=5, rating=4, comment='Nice design.', created_at=datetime.utcnow())
        ]
        db.session.bulk_save_objects(reviews)
        db.session.commit()

        print("Database has been seeded with sample data.")

if __name__ == '__main__':
    seed_data()
