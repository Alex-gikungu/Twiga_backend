# routes.py
from flask import request, jsonify
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from models import db, User,Order,Review,Product

# Configure Flask-Mail
mail = Mail()
s = URLSafeTimedSerializer('your_secret_key')  # Replace with a secret key

# Initialize mail in your app context
def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Replace with your email
    app.config['MAIL_PASSWORD'] = 'your_email_password'  # Replace with your email password
    app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'  # Replace with your email
    mail.init_app(app)

# User routes
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'email': user.email, 'phone': user.phone} for user in users])

def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'email': user.email, 'phone': user.phone})

def create_user():
    data = request.get_json()
    user = User(email=data['email'], phone=data['phone'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'email': user.email, 'phone': user.phone}), 201

def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User  deleted successfully'})

# Login route
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401

# Forgot Password route
def forgot_password():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({'message': 'Email not found'}), 404

    # Generate a password reset token
    token = s.dumps(email, salt='password-reset-salt')
    reset_link = f'http://127.0.0.1:5000/reset_password/{token}'

    # Send the email
    msg = Message('Password Reset Request', recipients=[email])
    msg.body = f'Click the link to reset your password: {reset_link}'
    mail.send(msg)

    return jsonify({'message': 'Password reset link sent!'}), 200

# Reset Password route
def reset_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)  # Token expires in 1 hour
    except Exception as e:
        return jsonify({'message': 'Invalid or expired token'}), 400

    data = request.get_json()
    new_password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({'message': 'User  not found'}), 404

    user.set_password(new_password)
    db.session.commit()

    return jsonify({'message': 'Password has been reset successfully!'}), 200

# Product routes
def get_products():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price, 'rating': product.rating, 'image': product.image} for product in products])

def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price, 'rating': product.rating, 'image': product.image})

def create_product():
    data = request.get_json()
    product = Product(name=data['name'], category=data['category'], price=data['price'], rating=data.get('rating', 0.0), image=data.get('image'))
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price, 'rating': product.rating, 'image': product.image}), 201

def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

# Review routes
def get_reviews():
    reviews = Review.query.all()
    return jsonify([{'id': review.id, 'user_id': review.user_id, 'product_id': review.product_id, 'rating': review.rating, 'comment': review.comment, 'date_created': review.date_created} for review in reviews])

def get_review(id):
    review = Review.query.get_or_404(id)
    return jsonify({'id': review.id, 'user_id': review.user_id, 'product_id': review.product_id, 'rating': review.rating, 'comment': review.comment, 'date_created': review.date_created})

def create_review():
    data = request.get_json()
    review = Review(user_id=data['user_id'], product_id=data['product_id'], rating=data['rating'], comment=data.get('comment'))
    db.session.add(review)
    db.session.commit()
    return jsonify({'id': review.id, 'user_id': review.user_id, 'product_id': review.product_id, 'rating': review.rating, 'comment': review.comment, 'date_created': review.date_created}), 201

def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'})

# Order routes
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': order.id, 'user_id': order.user_id, 'products': order.products, 'total_price': order.total_price, 'status': order.status, 'date_created': order.date_created} for order in orders])

def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify({'id': order.id, 'user_id': order.user_id, 'products': order.products, 'total_price': order.total_price, 'status': order.status, 'date_created': order.date_created})

def create_order():
    data = request.get_json()
    order = Order(user_id=data['user_id'], products=data['products'], total_price=data['total_price'])
    db.session.add(order)
    db.session.commit()
    return jsonify({'id': order.id, 'user_id': order.user_id, 'products': order.products, 'total_price': order.total_price, 'status': order.status, 'date_created': order.date_created}), 201

def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'})

# Register routes in the main app
def register_routes(app):
    app.add_url_rule('/users', 'get_users', get_users, methods=['GET'])
    app.add_url_rule('/users/<int:id>', 'get_user', get_user, methods=['GET'])
    app.add_url_rule('/users', 'create_user', create_user, methods=['POST'])
    app.add_url_rule('/users/<int:id>', 'delete_user', delete_user, methods=['DELETE'])
    app.add_url_rule('/login', 'login_user', login_user, methods=['POST'])
    app.add_url_rule('/forgot_password', 'forgot_password', forgot_password, methods=['POST'])
    app.add_url_rule('/reset_password/<token>', 'reset_password', reset_password, methods=['POST'])
    app.add_url_rule('/products', 'get_products', get_products, methods=['GET'])
    app.add_url_rule('/products/<int:id>', 'get_product', get_product, methods=['GET'])
    app.add_url_rule('/products', 'create_product', create_product, methods=['POST'])
    app.add_url_rule('/products/<int:id>', 'delete_product', delete_product, methods=['DELETE'])
    app.add_url_rule('/reviews', 'get_reviews', get_reviews, methods=['GET'])
    app.add_url_rule('/reviews/<int:id>', 'get_review', get_review, methods=['GET'])
    app.add_url_rule('/reviews', 'create_review', create_review, methods=['POST'])
    app.add_url_rule('/reviews/<int:id>', 'delete_review', delete_review, methods=['DELETE'])
    app.add_url_rule('/orders', 'get_orders', get_orders, methods=['GET'])
    app.add_url_rule('/orders/<int:id>', 'get_order', get_order, methods=['GET'])
    app.add_url_rule('/orders', 'create_order', create_order, methods=['POST'])
    app.add_url_rule('/orders/<int:id>', 'delete_order', delete_order, methods=['DELETE'])
