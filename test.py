from app import app, db
from models import User, Product, Review, Order
from datetime import datetime

# Create the application context
with app.app_context():
    # Drop all tables and recreate them (optional, for testing purposes)
    db.drop_all()
    db.create_all()

    # Add sample users
    user1 = User(email="twice@gmail.com", phone="0725576890")
    user1.set_password("password1")
    user2 = User(email="once@gmail.com", phone="0104007688")
    user2.set_password("password2")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Add sample products
    product1 = Product(name="Kales", category="Vegetables", price=1200.0, rating=4.5, image="kales.jpg")
    product2 = Product(name="Spinach", category="Vegetables", price=800.0, rating=4.0, image="spinach.jpg")
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()

    # Add sample reviews
    review1 = Review(user_id=user1.id, product_id=product1.id, rating=5.0, comment="Best and high quality!")
    review2 = Review(user_id=user2.id, product_id=product2.id, rating=4.0, comment="Best quality.")
    db.session.add(review1)
    db.session.add(review2)
    db.session.commit()

    # Add sample orders
    order1 = Order(user_id=user1.id, products='[{"id": 1, "name": "Kales", "price": 200.0}]', total_price=200.0, status=0)
    order2 = Order(user_id=user2.id, products='[{"id": 2, "name": "Spinach", "price": 100.0}]', total_price=100.0, status=1)
    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

    print("Sample data added successfully!")