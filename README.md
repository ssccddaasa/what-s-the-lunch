# What's the Lunch

## Overview
"What's the Lunch" is a web application designed for managing lunch orders. It allows users to register, log in, view meals from various restaurants, and place orders. Restaurants can register, log in, manage their profiles, and add/update meals. The application is built using Flask, SQLAlchemy, Flask-WTF, and Flask-Login.

## Features
- User and Restaurant registration and login
- User and Restaurant profile management
- Restaurant meal management (add, update, delete)
- Ordering meals by users
- Image upload for user and restaurant profiles, as well as meals
- Flash messages for user feedback
- CSRF protection on forms
- Password hashing with Bcrypt

## Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login
- MySQL database


## Usage

### User Registration
1. Navigate to the registration page for users (`/reg`).
2. Fill out the form and submit.

### Restaurant Registration
1. Navigate to the registration page for restaurants (`/reg2`).
2. Fill out the form and submit.

### User Login
1. Navigate to the login page for users (`/log`).
2. Fill out the form and submit.

### Restaurant Login
1. Navigate to the login page for restaurants (`/log2`).
2. Fill out the form and submit.

### Add a Meal (Restaurant)
1. After logging in as a restaurant, navigate to the add meal page (`/add`).
2. Fill out the form and submit.

### Order a Meal (User)
1. After logging in as a user, navigate to the meal order page (`/ord/<meal_id>`).
2. Fill out the form and submit.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Flask documentation
- WTForms documentation
- SQLAlchemy documentation



## Setup

### Clone the Repository
```bash
git clone https://github.com/ssccddaasa/what-s-the-lunch.git
cd what-s-the-lunch
