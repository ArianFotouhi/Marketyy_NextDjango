from jose import jwt

def generate_jwt_token(user):
    from datetime import datetime, timedelta
    username = user.username if hasattr(user, 'username') else user.get_username()

    expiration_time = datetime.utcnow() + timedelta(days=1)

    # Create the JWT payload
    payload = {
        'user_name': username,
        'exp': expiration_time,
    }

    # Use Django's SECRET_KEY for JWT signing
    token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')

    return token