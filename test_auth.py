from app.auth.auth_handler import create_access_token

token = create_access_token(
    {
        "sub": "sravani"
    }
)

print(token)