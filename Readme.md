# Flask E-Commerce Backend

This is a Flask-based backend for an e-commerce application. It provides user authentication, product management, order processing, and review functionalities. Additionally, it includes a "Forgot Password" feature that allows users to reset their passwords via email.

## Features

- User registration and authentication
- Password reset functionality
- Product management (CRUD operations)
- Review management (CRUD operations)
- Order management (CRUD operations)
- Email notifications for password reset

## Technologies Used

- Flask
- SQLAlchemy
- Flask-Mail
- ItsDangerous
- SQLite (for database)

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/Alex-gikungu/Twiga_backend.git
cd Twiga_backend
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add the following variables:

```plaintext
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_email_password
SECRET_KEY=your_secret_key
```

### Initialize the Database

Run the following command to create the SQLite database:

```bash
flask shell
```

Then, in the Flask shell:

```python
from models import db
db.create_all()
exit()
```

## Usage

### Run the Application

To start the Flask application, run:

```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## API Endpoints

### User Routes

#### Get All Users
```
GET /users
```

#### Get User by ID
```
GET /users/<id>
```

#### Create User
```
POST /users
```
Request Body:
```json
{ "email": "user@example.com", "phone": "1234567890", "password": "your_password" }
```

#### Delete User
```
DELETE /users/<id>
```

#### Login User
```
POST /login
```
Request Body:
```json
{ "email": "user@example.com", "password": "your_password" }
```

### Forgot Password

#### Request Password Reset
```
POST /forgot_password
```
Request Body:
```json
{ "email": "user@example.com" }
```

#### Reset Password
```
POST /reset_password/<token>
```
Request Body:
```json
{ "password": "new_password" }
```

### Product Routes

#### Get All Products
```
GET /products
```

#### Get Product by ID
```
GET /products/<id>
```

#### Create Product
```
POST /products
```
Request Body:
```json
{ "name": "Product Name", "category": "Category", "price": 100.0, "rating": 4.5, "image": "image_url" }
```

#### Delete Product
```
DELETE /products/<id>
```

### Review Routes

#### Get All Reviews
```
GET /reviews
```

#### Get Review by ID
```
GET /reviews/<id>
```

#### Create Review
```
POST /reviews
```
Request Body:
```json
{ "user_id": 1, "product_id": 1, "rating": 5, "comment": "Great product!" }
```

#### Delete Review
```
DELETE /reviews/<id>
```

### Order Routes

#### Get All Orders
```
GET /orders
```

#### Get Order by ID
```
GET /orders/<id>
```

#### Create Order
```
POST /orders
```
Request Body:
```json
{ "user_id": 1, "products": "product_ids", "total_price": 100.0 }
```

#### Delete Order
```
DELETE /orders/<id>
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation
- SQLAlchemy documentation
- Flask-Mail documentation
- ItsDangerous documentation
