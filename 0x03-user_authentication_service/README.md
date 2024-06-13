# Authentication Service

This project implements a Flask-based authentication service with features for user registration, login, logout, password reset, and profile management.

## Technologies Used
- Python
- Flask
- bcrypt

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Slonjoh/alx-backend-user-data.git
   cd 0x03-user_authentication_service
   ```

## Install dependencies
pip install -r requirements.txt

## Configuration
- Set environment variables for database connection and any other configuration needed.

## Usage
1. Register a New User
	- Endpoint: `POST /users`
	- Example:
	```bash
	curl -X POST http://localhost:5000/users -d 'email=user@example.com' -d 'password=myPassword'
```
2. Log In
	- Endpoint: `POST /sessions`
	- Example:
	```bash
	curl -X POST http://localhost:5000/sessions -d 'email=user@example.com' -d 'password=myPassword'
```
3. Log Out
	- Endpoint: `DELETE /sessions`
	- Example:
	```bash
	curl -X DELETE http://localhost:5000/sessions -b 'session_id=<session_id>'
```
4. Get User Profile
	- Endpoint: `GET /profile`
	- Example:
	```bash
	curl -X GET http://localhost:5000/profile -b 'session_id=<session_id>'
```
5. Request Password Reset
	- Endpoint: `POST /reset_password`
	- Example:
	```bash
	curl -X POST http://localhost:5000/reset_password -d 'email=user@example.com'
```
6. Update Password After Reset
	- Endpoint: `PUT /reset_password`
	- Example:
	```bash
	curl -X PUT http://localhost:5000/reset_password -d 'email=user@example.com' -d 'reset_token=<reset_token>' -d 'new_password=myNewPassword'
```

## API Endpoints
- POST /users
	- Register a new user.
	- Example: `curl -X POST http://localhost:5000/users -d 'email=user@example.com' -d 'password=myPassword'`

- POST /sessions
	- Log in with email and password.
	- Example: `curl -X POST http://localhost:5000/sessions -d 'email=user@example.com' -d 'password=myPassword'`

- DELETE /sessions
	- Log out the current user.
	- Example: `curl -X DELETE http://localhost:5000/sessions -b 'session_id=<session_id>'`

- GET /profile
	- Get the profile of the currently logged-in user.
	- Example: `curl -X GET http://localhost:5000/profile -b 'session_id=<session_id>'`

- POST /`reset_password`
	- Request a password reset by email.
	- Example: `curl -X POST http://localhost:5000/reset_password -d 'email=user@example.com'`

- PUT /`reset_password`
	- Update password after receiving a reset token.
	- Example: `curl -X PUT http://localhost:5000/reset_password -d 'email=user@example.com' -d 'reset_token=<reset_token>' -d 'new_password=myNewPassword'`
