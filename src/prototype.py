proto_user = {
    "role": "user",
    "features": ["read"]}
proto_admin = {
    "role": "admin",
    "features": ["read", "write", "delete"]}

def create_user(role: str, name: str) -> dict:
    if role == "user":
        return proto_user.copy()
    elif role == "admin":
        return proto_admin.copy()
    else:
        raise ValueError("Unknown role")
