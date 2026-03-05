import jwt
import datetime

SECRET="deepfake_secret"

def generate_token(username):

    payload={
    "username":username,
    "exp":datetime.datetime.utcnow()+datetime.timedelta(hours=24)
    }

    token=jwt.encode(payload,SECRET,algorithm="HS256")

    return token