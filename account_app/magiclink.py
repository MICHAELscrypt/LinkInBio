import jwt
import time

def createMagicLink(username, secret):
    encoded_jwt = jwt.encode({"user": username, "time": int(time.time())}, secret, algorithm="HS256")
    return encoded_jwt

def link():
    token = createMagicLink("admin1", "secret")
    print("http://localhost:8000/acc/autologin?t=" + token)

# minutes_of_link_active = 1

# encoded_jwt = jwt.encode({"user": "user1", "time": int(time.time())}, "secret", algorithm="HS256")
# print(encoded_jwt)

# decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])

# if int(time.time()) < minutes_of_link_active * 60 + decoded_jwt["time"]:
#     print(decoded_jwt["user"])

# print(decoded_jwt["time"])
